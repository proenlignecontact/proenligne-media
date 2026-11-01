"""Vérifie un plan de semaine AVANT programmation : règles de contenu, mix éditorial, vocabulaire, rotation, ressemblance.

usage : python3 cerveau/verifier.py suivi/plan/<lundi>.json
sortie : « plan OK » (code 0) ou la liste des problèmes (code 1).

Format du plan : {"creneaux": [ {
   "date": "2026-11-09", "creneau_nominal": "06:30|13:00|19:00", "heure": "06:50"  (heure réelle, à ±45 min du nominal),
   "creneau": "texte|visuel|video", "intention": "utile|preuve|offre",
   "metier": …, "angle": …, "format": …, "ton": …, "symptome": … ou null, "accroche": …, "slug": …,
   "textes": {canal: texte} — canaux attendus :
        texte  : x, facebook
        visuel : instagram, facebook (+ linkedin du lundi au vendredi)
        video  : tiktok, instagram, youtube, facebook
   "premier_commentaire": … (≤ 300 car., une question ou un complément, sans prix),
   "youtube_title", "tiktok_title" (vidéo),
   "media": {…}  — visuel : "carrousel": [urls media.glidy.uk…] (3 à 5) ou "postiz": url ; vidéo : "postiz_vertical", "postiz_horizontal" ;
                   texte : "postiz": url de l'image (facultatif mais recommandé)
   "ab": "A"|"B" (facultatif, TikTok)
} ] }

Mix éditorial sur la semaine (21 créneaux) : utile ≥ 13 (≈ 70 %), preuve 2 à 5, offre ≤ 3.
Variante B (A/B TikTok) : entrée distincte avec "ab": "B", même slug que sa vidéo A, creneau_nominal "12:30", textes {"tiktok": …} seulement.
"""
import datetime as dt, glob, itertools, json, os, re, sys, unicodedata
from collections import Counter

ICI = os.path.dirname(os.path.abspath(__file__))
METIERS = {'plombier', 'electricien', 'chauffagiste', 'serrurier', 'paysagiste', 'macon', 'coiffeur', 'estheticienne', 'autoecole', 'boulangerie', 'garage', 'general'}
ANGLES = {'peur-de-perdre', 'gain-de-temps', 'preuve'}
TONS = {'question', 'constat', 'scene', 'avant-apres', 'contre-intuitif', 'pendant-que', 'replique'}
INTENTIONS = {'utile', 'preuve', 'offre'}
FORMATS = {'texte': {'conseil', 'test', 'constat', 'idee-recue', 'preuve'}, 'visuel': {'avant-apres', 'conseil', 'question'}, 'video': {'recherche', 'fiche', 'avis', 'journee', 'libre'}}
CANAUX = {'texte': {'x', 'facebook'}, 'visuel': {'instagram', 'facebook'}, 'video': {'tiktok', 'instagram', 'youtube', 'facebook'}}
HEURES = {'texte': '06:30', 'visuel': '13:00', 'video': '19:00'}
TOLERANCE_MIN = 45
LIMITES = {'x': 280, 'tiktok': 2000, 'instagram': 2200, 'linkedin': 3000}
PRIX = re.compile(r'€|\bmois\b|centime|euro', re.I)
SEUIL_RESSEMBLANCE = 0.4
STOP = {'votre', 'vous', 'fiche', 'google', 'maps', 'dans', 'pour', 'avec', 'sans', 'cherche', 'quand', 'cette', 'leur', 'leurs', 'elle', 'vos'}


def mots(txt):
    t = unicodedata.normalize('NFD', txt.lower())
    t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    return {w for w in re.findall(r'[a-z]+', t) if len(w) > 3 and w not in STOP}


def ressemblance(a, b):
    A, B = mots(a), mots(b)
    return len(A & B) / max(1, len(A | B))


def debut(txt, n=5):
    return ' '.join(re.findall(r'\w+', unicodedata.normalize('NFD', txt.lower()))[:n])


def canaux_attendus(typ, date):
    c = set(CANAUX[typ])
    if typ == 'visuel' and dt.date.fromisoformat(date).weekday() < 5:
        c.add('linkedin')
    return c


def minutes(h):
    a, b = h.split(':'); return int(a) * 60 + int(b)


def verifier(plan):
    cr = plan['creneaux'] if isinstance(plan, dict) else plan
    pb = []
    fiches = [json.load(open(f, encoding='utf-8')) for f in glob.glob(os.path.join(ICI, 'productions', '*.json'))]
    for c in cr:
        typ = c.get('creneau')
        nominal = c.get('creneau_nominal') or HEURES.get(typ)
        ref = f"{c.get('date')} {nominal}"
        if typ not in CANAUX:
            pb.append(f'{ref} : creneau inconnu « {typ} »'); continue
        variante_b = c.get('ab') == 'B'
        attendu_h = '12:30' if variante_b else HEURES[typ]
        if variante_b and typ != 'video': pb.append(f'{ref} : une variante B est forcément une vidéo')
        if nominal != attendu_h:
            pb.append(f'{ref} : creneau_nominal {nominal} au lieu de {attendu_h} pour {"une variante B" if variante_b else "un créneau " + typ}')
        try:
            if abs(minutes(c.get('heure', nominal)) - minutes(attendu_h)) > TOLERANCE_MIN:
                pb.append(f'{ref} : heure réelle {c.get("heure")} à plus de {TOLERANCE_MIN} min du créneau')
        except Exception:
            pb.append(f'{ref} : heure illisible « {c.get("heure")} »')
        if c.get('intention') not in INTENTIONS: pb.append(f'{ref} : intention manquante ou inconnue (utile | preuve | offre)')
        if c.get('metier') not in METIERS: pb.append(f'{ref} : métier inconnu « {c.get("metier")} »')
        if c.get('angle') not in ANGLES: pb.append(f'{ref} : angle inconnu « {c.get("angle")} »')
        if c.get('ton') not in TONS: pb.append(f'{ref} : ton inconnu « {c.get("ton")} »')
        if c.get('format') not in FORMATS[typ]: pb.append(f'{ref} : format « {c.get("format")} » invalide pour {typ}')
        if c.get('offre', 'essai') != 'essai': pb.append(f'{ref} : offre « {c.get("offre")} » — seule « essai » est autorisée')
        acc = c.get('accroche', '')
        if 'google' not in acc.lower(): pb.append(f'{ref} : accroche sans « Google »')
        if PRIX.search(acc): pb.append(f'{ref} : prix ou « mois » dans l\'accroche')
        pc = c.get('premier_commentaire') or ''
        if not pc: pb.append(f'{ref} : premier_commentaire manquant')
        elif len(pc) > 300: pb.append(f'{ref} : premier_commentaire > 300 caractères')
        elif PRIX.search(pc): pb.append(f'{ref} : prix dans le premier commentaire')
        textes = c.get('textes', {})
        attendus = {'tiktok'} if variante_b else canaux_attendus(typ, c['date'])
        if set(textes) != attendus:
            pb.append(f'{ref} : canaux {sorted(textes)} au lieu de {sorted(attendus)}')
        for canal, t in textes.items():
            t = t or ''
            if 'fiche google' not in t.lower(): pb.append(f'{ref} {canal} : « fiche Google » absent')
            if 'google' not in t.split('\n')[0].lower(): pb.append(f'{ref} {canal} : première ligne sans « Google »')
            if PRIX.search(t): pb.append(f'{ref} {canal} : prix, « mois » ou « centime » dans le texte')
            if c.get('intention') == 'offre' and 'gratuit' not in t.lower(): pb.append(f'{ref} {canal} : intention offre sans « gratuitement »')
            if c.get('intention') == 'utile' and canal != 'x' and '?' not in t and '?' not in pc:
                pb.append(f'{ref} {canal} : contenu utile sans question (ni dans le texte ni dans le premier commentaire)')
            if t.count('✅') > 3: pb.append(f'{ref} {canal} : plus de 3 ✅')
            if canal in LIMITES and len(t) > LIMITES[canal]: pb.append(f'{ref} {canal} : {len(t)} caractères (> {LIMITES[canal]})')
            if re.search(r"\b(la|votre|sa|cette) fiche\b(?! google)", t, re.I) and t.lower().count('fiche google') < 2:
                pb.append(f'{ref} {canal} : « la fiche » seule sans rappel « fiche Google » suffisant')
            if canal == 'linkedin':
                if len(re.findall(r'#\w+', t)) > 5: pb.append(f'{ref} linkedin : plus de 5 hashtags')
                if re.search(r'https?://|www\.|lien en bio', t, re.I): pb.append(f'{ref} linkedin : lien externe ou « lien en bio »')
                if 'google' not in t[:220].lower(): pb.append(f'{ref} linkedin : « Google » absent des ~200 premiers caractères')
                if len(t) < 500: pb.append(f'{ref} linkedin : texte trop court ({len(t)} < 500), viser 700 à 1 300')
                if 'facebook' in textes and t.strip() == (textes['facebook'] or '').strip(): pb.append(f'{ref} linkedin : copie exacte du texte Facebook')
            if canal != 'linkedin' and re.search(r'lien en bio', t, re.I) and canal in ('facebook', 'youtube', 'x'):
                pb.append(f'{ref} {canal} : « lien en bio » n\'a pas de sens sur ce canal')
        if typ == 'video':
            yt, tt = c.get('youtube_title', ''), c.get('tiktok_title', '')
            if not variante_b and (not (2 <= len(yt) <= 100) or 'google' not in yt.lower()): pb.append(f'{ref} : youtube_title manquant, > 100 caractères ou sans « Google »')
            if not tt or len(tt) > 90: pb.append(f'{ref} : tiktok_title manquant ou > 90 caractères')
            if PRIX.search(yt + tt): pb.append(f'{ref} : prix dans un titre')
        m = c.get('media') or {}
        if typ == 'video' and not (m.get('postiz_vertical') or m.get('vertical')): pb.append(f'{ref} : vidéo verticale manquante')
        if typ == 'visuel':
            car = m.get('carrousel')
            if car is not None and not 3 <= len(car) <= 5: pb.append(f'{ref} : carrousel de {len(car)} images (3 à 5 attendues)')
            if not car and not m.get('postiz'): pb.append(f'{ref} : média manquant (carrousel ou image)')
        for f in fiches:
            if f['id'].startswith(f"{c['date']}_{nominal.replace(':', '')}"):
                continue
            r = ressemblance(acc, f.get('accroche', ''))
            if r >= SEUIL_RESSEMBLANCE:
                pb.append(f'{ref} : accroche trop proche ({r:.0%}) de la fiche {f["id"]}')
    # ressemblance et structures à l'intérieur du plan
    for a, b in itertools.combinations(cr, 2):
        if a.get('slug') == b.get('slug') and {a.get('ab'), b.get('ab')} == {'A', 'B'}:
            continue
        ra, rb = f"{a['date']} {a.get('creneau_nominal', a.get('heure'))}", f"{b['date']} {b.get('creneau_nominal', b.get('heure'))}"
        r = ressemblance(a.get('accroche', ''), b.get('accroche', ''))
        if r >= SEUIL_RESSEMBLANCE: pb.append(f'{ra} et {rb} : accroches trop proches ({r:.0%})')
        if debut(a.get('accroche', '')) and debut(a.get('accroche', '')) == debut(b.get('accroche', '')):
            pb.append(f'{ra} et {rb} : même début d\'accroche (« {debut(a["accroche"])} … »)')
        for canal in set(a.get('textes', {})) & set(b.get('textes', {})):
            if debut(a['textes'][canal] or '', 6) == debut(b['textes'][canal] or '', 6):
                pb.append(f'{ra} et {rb} ({canal}) : même début de texte')
    # rotation
    seq = sorted([c for c in cr if c.get('ab') != 'B'], key=lambda c: (c.get('date', ''), c.get('creneau_nominal', c.get('heure', ''))))
    for a, b in zip(seq, seq[1:]):
        if a.get('metier') == b.get('metier') and a['metier'] != 'general':
            pb.append(f'{a["date"]} → {b["date"]} : même métier deux créneaux de suite ({a["metier"]})')
        if a.get('ton') == b.get('ton'):
            pb.append(f'{a["date"]} → {b["date"]} : même ton deux créneaux de suite ({a["ton"]})')
    textes = [c for c in seq if c.get('creneau') == 'texte']
    for a, b in zip(textes, textes[1:]):
        if a.get('format') == b.get('format'): pb.append(f'{a["date"]} et {b["date"]} 06:30 : même format texte deux jours de suite')
    visuels = [c for c in seq if c.get('creneau') == 'visuel']
    for a, b in zip(visuels, visuels[1:]):
        if a.get('format') == b.get('format'): pb.append(f'{a["date"]} et {b["date"]} 13:00 : même gabarit visuel deux jours de suite')
    grille = [c for c in cr if c.get('ab') != 'B']
    if len(grille) >= 15:
        cr = grille
        nb_metiers = len({c['metier'] for c in cr if c.get('metier') != 'general'})
        if nb_metiers < 6: pb.append(f'seulement {nb_metiers} métiers différents sur la semaine (minimum 6)')
        it = Counter(c.get('intention') for c in cr)
        if it['utile'] < 13: pb.append(f'mix éditorial : {it["utile"]} contenus utiles sur {len(cr)} (minimum 13, ≈ 70 %)')
        if it['offre'] > 3: pb.append(f'mix éditorial : {it["offre"]} contenus « offre » (maximum 3)')
        if not 2 <= it['preuve'] <= 5: pb.append(f'mix éditorial : {it["preuve"]} contenus « preuve » (2 à 5 attendus)')
        tons = Counter(c.get('ton') for c in cr)
        for t, n in tons.items():
            if n > 5: pb.append(f'ton « {t} » utilisé {n} fois (maximum 5 par semaine)')
        ab = [c for c in cr if c.get('creneau') == 'video' and c.get('ab')]
        if len(ab) < 2: pb.append('A/B : au moins 2 vidéos de la semaine doivent porter une variante B (champ "ab")')
    doubl = [k for k, n in Counter((c.get('date'), c.get('creneau_nominal', c.get('heure'))) for c in cr).items() if n > 1]
    if doubl: pb.append(f'créneaux en double dans le plan : {doubl}')
    return pb


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    pb = verifier(json.load(open(sys.argv[1], encoding='utf-8')))
    if pb:
        print('\n'.join('ATTENTION : ' + p for p in pb)); sys.exit(1)
    print('plan OK')
