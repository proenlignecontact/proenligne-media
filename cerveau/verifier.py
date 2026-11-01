"""Vérifie un plan de semaine AVANT programmation : règles de contenu, vocabulaire, rotation, ressemblance.

usage : python3 cerveau/verifier.py suivi/plan/<lundi>.json
sortie : « plan OK » (code 0) ou la liste des problèmes (code 1).

Format du plan : {"creneaux": [ { "date": "2026-11-09", "heure": "06:30", "creneau": "texte|visuel|video",
   "metier": …, "angle": …, "format": …, "ton": …, "symptome": … ou null, "accroche": …, "slug": …,
   "textes": {"x": …, "facebook": …} | {"instagram": …, "facebook": …, "linkedin": … (lundi-vendredi seulement)} | {"tiktok": …, "instagram": …, "youtube": …},
   "youtube_title": … (vidéo), "tiktok_title": … (vidéo), "media": {…} } ] }
"""
import datetime as dt, glob, itertools, json, os, re, sys, unicodedata
from collections import Counter

ICI = os.path.dirname(os.path.abspath(__file__))
METIERS = {'plombier', 'electricien', 'chauffagiste', 'serrurier', 'paysagiste', 'macon', 'coiffeur', 'estheticienne', 'autoecole', 'boulangerie', 'garage', 'general'}
ANGLES = {'peur-de-perdre', 'gain-de-temps', 'preuve'}
TONS = {'question', 'constat', 'scene', 'avant-apres', 'contre-intuitif', 'pendant-que', 'replique'}
FORMATS = {'texte': {'conseil', 'test', 'constat', 'idee-recue', 'preuve'}, 'visuel': {'avant-apres'}, 'video': {'recherche', 'fiche', 'avis', 'journee', 'libre'}}
CANAUX = {'texte': {'x', 'facebook'}, 'visuel': {'instagram', 'facebook'}, 'video': {'tiktok', 'instagram', 'youtube'}}
HEURES = {'texte': '06:30', 'visuel': '13:00', 'video': '19:00'}
LIMITES = {'x': 280, 'tiktok': 2000, 'instagram': 2200, 'linkedin': 3000}


def canaux_attendus(typ, date):
    """LinkedIn s'ajoute au créneau visuel du lundi au vendredi uniquement."""
    c = set(CANAUX[typ])
    if typ == 'visuel' and dt.date.fromisoformat(date).weekday() < 5:
        c.add('linkedin')
    return c
PRIX = re.compile(r'€|\bmois\b|centime|euro', re.I)
SEUIL_RESSEMBLANCE = 0.4


def mots(txt):
    t = unicodedata.normalize('NFD', txt.lower())
    t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    return {w for w in re.findall(r'[a-z]+', t) if len(w) > 3 and w not in {'votre', 'vous', 'fiche', 'google', 'maps', 'dans', 'pour', 'avec', 'sans', 'cherche', 'quand'}}


def ressemblance(a, b):
    A, B = mots(a), mots(b)
    return len(A & B) / max(1, len(A | B))


def verifier(plan):
    cr = plan['creneaux'] if isinstance(plan, dict) else plan
    pb = []
    fiches = [json.load(open(f, encoding='utf-8')) for f in glob.glob(os.path.join(ICI, 'productions', '*.json'))]
    for c in cr:
        ref = f"{c.get('date')} {c.get('heure')}"
        typ = c.get('creneau')
        if typ not in CANAUX:
            pb.append(f'{ref} : creneau inconnu « {typ} »'); continue
        if c.get('heure') != HEURES[typ]:
            pb.append(f'{ref} : heure {c.get("heure")} au lieu de {HEURES[typ]} pour un créneau {typ}')
        if c.get('metier') not in METIERS: pb.append(f'{ref} : métier inconnu « {c.get("metier")} »')
        if c.get('angle') not in ANGLES: pb.append(f'{ref} : angle inconnu « {c.get("angle")} »')
        if c.get('ton') not in TONS: pb.append(f'{ref} : ton inconnu « {c.get("ton")} »')
        if c.get('format') not in FORMATS[typ]: pb.append(f'{ref} : format « {c.get("format")} » invalide pour {typ}')
        if c.get('offre', 'essai') != 'essai': pb.append(f'{ref} : offre « {c.get("offre")} » — seule « essai » est autorisée')
        acc = c.get('accroche', '')
        if 'google' not in acc.lower(): pb.append(f'{ref} : accroche sans « Google »')
        if PRIX.search(acc): pb.append(f'{ref} : prix ou « mois » dans l\'accroche')
        textes = c.get('textes', {})
        attendus = canaux_attendus(typ, c['date'])
        if set(textes) != attendus:
            pb.append(f'{ref} : canaux {sorted(textes)} au lieu de {sorted(attendus)}')
        for canal, t in textes.items():
            t = t or ''
            if 'fiche google' not in t.lower(): pb.append(f'{ref} {canal} : « fiche Google » absent')
            if 'google' not in t.split('\n')[0].lower(): pb.append(f'{ref} {canal} : première ligne sans « Google »')
            if PRIX.search(t): pb.append(f'{ref} {canal} : prix, « mois » ou « centime » dans le texte')
            if 'gratuit' not in t.lower(): pb.append(f'{ref} {canal} : appel à l\'action « gratuitement » absent')
            if canal in LIMITES and len(t) > LIMITES[canal]: pb.append(f'{ref} {canal} : {len(t)} caractères (> {LIMITES[canal]})')
            if canal == 'linkedin':
                if len(re.findall(r'#\w+', t)) > 5: pb.append(f'{ref} linkedin : plus de 5 hashtags')
                if re.search(r'https?://|www\.|lien en bio', t, re.I): pb.append(f'{ref} linkedin : lien externe ou « lien en bio »')
                if 'google' not in t[:220].lower(): pb.append(f'{ref} linkedin : « Google » absent des ~200 premiers caractères (avant « voir plus »)')
                if t.count('✅') > 3: pb.append(f'{ref} linkedin : plus de 3 ✅')
                if len(t) < 500: pb.append(f'{ref} linkedin : texte trop court ({len(t)} < 500), viser 700 à 1 300 caractères')
                if 'facebook' in textes and t.strip() == (textes['facebook'] or '').strip(): pb.append(f'{ref} linkedin : copie exacte du texte Facebook')
            if re.search(r"\b(la|votre|sa|cette) fiche\b(?! google)", t, re.I) and t.lower().count('fiche google') < 2:
                pb.append(f'{ref} {canal} : « la fiche » seule sans rappel « fiche Google » suffisant')
        if typ == 'video':
            yt, tt = c.get('youtube_title', ''), c.get('tiktok_title', '')
            if not (2 <= len(yt) <= 100) or 'google' not in yt.lower(): pb.append(f'{ref} : youtube_title manquant, > 100 caractères ou sans « Google »')
            if not tt or len(tt) > 90: pb.append(f'{ref} : tiktok_title manquant ou > 90 caractères')
            if PRIX.search(yt + tt): pb.append(f'{ref} : prix dans un titre')
        if typ != 'texte' and not c.get('media'): pb.append(f'{ref} : média manquant')
        # ressemblance avec les fiches existantes (hors le créneau lui-même)
        for f in fiches:
            if f['id'].startswith(f"{c['date']}_{c['heure'].replace(':', '')}"):
                continue
            r = ressemblance(acc, f.get('accroche', ''))
            if r >= SEUIL_RESSEMBLANCE:
                pb.append(f'{ref} : accroche trop proche ({r:.0%}) de la fiche {f["id"]}')
    # ressemblance à l'intérieur du plan
    for a, b in itertools.combinations(cr, 2):
        r = ressemblance(a.get('accroche', ''), b.get('accroche', ''))
        if r >= SEUIL_RESSEMBLANCE:
            pb.append(f'{a["date"]} {a["heure"]} et {b["date"]} {b["heure"]} : accroches trop proches ({r:.0%})')
    # rotation
    seq = sorted(cr, key=lambda c: (c.get('date', ''), c.get('heure', '')))
    for a, b in zip(seq, seq[1:]):
        if a.get('metier') == b.get('metier') and a['metier'] != 'general':
            pb.append(f'{a["date"]} {a["heure"]} → {b["date"]} {b["heure"]} : même métier deux créneaux de suite ({a["metier"]})')
    textes = [c for c in seq if c.get('creneau') == 'texte']
    for a, b in zip(textes, textes[1:]):
        if a.get('format') == b.get('format'):
            pb.append(f'{a["date"]} et {b["date"]} 06:30 : même format texte deux jours de suite ({a["format"]})')
    nb_metiers = len({c['metier'] for c in cr if c.get('metier') != 'general'})
    if len(cr) >= 15 and nb_metiers < 6:
        pb.append(f'seulement {nb_metiers} métiers différents sur la semaine (minimum 6)')
    doubl = [k for k, n in Counter((c.get('date'), c.get('heure')) for c in cr).items() if n > 1]
    if doubl: pb.append(f'créneaux en double dans le plan : {doubl}')
    return pb


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    pb = verifier(json.load(open(sys.argv[1], encoding='utf-8')))
    if pb:
        print('\n'.join('ATTENTION : ' + p for p in pb)); sys.exit(1)
    print('plan OK')
