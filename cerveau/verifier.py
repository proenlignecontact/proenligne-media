"""Vérifie un plan de semaine AVANT programmation : règles de contenu, mix éditorial, vocabulaire, rotation, ressemblance.

usage : python3 cerveau/verifier.py suivi/plan/<lundi>.json [--briefs <dossier des briefs vidéo>] [--relecture]
sortie : « plan OK » (code 0) ou la liste des problèmes (code 1).
  --briefs     : contrôle aussi les textes des briefs vidéo (règles n°1-2-3, phrases complètes)
  --relecture  : exige une relecture validée et à jour (cerveau/relecture.py controler) — obligatoire avant programmation
  --sans-medias : ne vérifie pas la présence des médias (étape « avant rendu » : les URL Postiz n'existent pas encore).
                  Sans cette option, un créneau sans média est refusé — c'est l'état exigé juste avant programmation.

Règles mécaniques appliquées à CHAQUE élément textuel (textes, accroche, titres, premier commentaire, briefs visuels et vidéo) :
  n°1 « fiche Google » · n°2 aucun prix · n°3 aucune statistique ni résultat client (cerveau/regles_texte.py).
La compréhension (sens, contradictions) est jugée par la relecture, pas ici.

Format du plan : {"creneaux": [ {
   "date": "2026-11-16", "creneau_nominal": "13:00|19:00", "heure": "13:15"  (heure réelle, à ±45 min du nominal),
   "creneau": "visuel|video", "intention": "utile|preuve|offre",
   (le créneau « texte » de 06:30 est supprimé depuis la semaine du 16/11/2026 : il est refusé)
   "metier": …, "angle": …, "format": …, "ton": …, "symptome": … ou null, "accroche": …, "slug": …,
   "textes": {canal: texte} — canaux attendus :
        visuel : instagram (+ linkedin le mardi et le jeudi)
        video  : tiktok, instagram, youtube, facebook
   "premier_commentaire": … (≤ 300 car., un COMPLÉMENT d'information, jamais une question ni un prix — la question va dans le texte),
   "youtube_title", "tiktok_title" (vidéo),
   "media": {…}  — visuel : "carrousel": [urls media.glidy.uk…] (3 à 5) ou "postiz": url ; vidéo : "postiz_vertical", "postiz_horizontal" ;
                   texte : "postiz": url de l'image (facultatif mais recommandé)
   "ab": "A"|"B" (facultatif, TikTok)
} ] }

Mix éditorial sur la semaine (14 créneaux) : utile ≥ 9 (≈ 70 %), preuve 2 à 4, offre ≤ 2.
TikTok : la légende invite à s'abonner (« Abonnez-vous… »), décision du 11/11/2026.
Variante B (A/B TikTok) : entrée distincte avec "ab": "B", même slug que sa vidéo A, creneau_nominal "12:30", textes {"tiktok": …} seulement.
"""
import datetime as dt, glob, itertools, json, os, re, sys, unicodedata
from collections import Counter

ICI = os.path.dirname(os.path.abspath(__file__))
import importlib.util as _ilu  # noqa: E402
_sp = _ilu.spec_from_file_location('pub_video', os.path.join(ICI, '..', 'outils', 'pub-video.py'))
PUBVIDEO = _ilu.module_from_spec(_sp); _sp.loader.exec_module(PUBVIDEO)
sys.path.insert(0, ICI)
import regles_texte  # noqa: E402
METIERS = {'plombier', 'electricien', 'chauffagiste', 'serrurier', 'paysagiste', 'macon', 'coiffeur', 'estheticienne', 'autoecole', 'boulangerie', 'garage', 'general'}
ANGLES = {'peur-de-perdre', 'gain-de-temps', 'preuve'}
TONS = {'question', 'constat', 'scene', 'avant-apres', 'contre-intuitif', 'pendant-que', 'replique'}
INTENTIONS = {'utile', 'preuve', 'offre'}
FORMATS = {'texte': {'conseil', 'test', 'constat', 'idee-recue', 'preuve'}, 'visuel': {'avant-apres', 'conseil', 'question'}, 'video': {'recherche', 'fiche', 'avis', 'journee', 'libre'}}
CANAUX = {'visuel': {'instagram'}, 'video': {'tiktok', 'instagram', 'youtube', 'facebook'}}
HEURES = {'visuel': '13:00', 'video': '19:00'}
JOURS_LINKEDIN = {1, 3}   # mardi et jeudi (décision du 11/11/2026 : LinkedIn allégé)
UTILE_MIN, PREUVE_MIN, PREUVE_MAX, OFFRE_MAX, TON_MAX = 9, 2, 4, 2, 4
TOLERANCE_MIN = 45
LIMITES = {'x': 280, 'tiktok': 2000, 'instagram': 2200, 'linkedin': 3000}
PRIX = regles_texte.PRIX
MAX_EXPLICATION_IDENTIQUE = 4   # la phrase « Votre fiche Google, c'est ce qui s'affiche… » ne peut pas être copiée telle quelle plus de 4 fois par semaine
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
    if typ == 'visuel' and dt.date.fromisoformat(date).weekday() in JOURS_LINKEDIN:
        c.add('linkedin')
    return c


def minutes(h):
    a, b = h.split(':'); return int(a) * 60 + int(b)


def verifier(plan, medias=True):
    cr = plan['creneaux'] if isinstance(plan, dict) else plan
    pb = []
    fiches = [json.load(open(f, encoding='utf-8')) for f in glob.glob(os.path.join(ICI, 'productions', '*.json'))]
    for c in cr:
        typ = c.get('creneau')
        nominal = c.get('creneau_nominal') or HEURES.get(typ)
        ref = f"{c.get('date')} {nominal}"
        if typ == 'texte':
            pb.append(f'{ref} : créneau texte de 06:30 supprimé depuis la semaine du 16/11/2026 (X et Facebook texte sans audience)'); continue
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
        pb += regles_texte.phrase_complete(acc, f'{ref} accroche')
        for _, champ, t in regles_texte.textes_du_plan({'creneaux': [c]}):
            pb += regles_texte.problemes(t, f'{ref} {champ}')
        v = c.get('visuel') or {}
        if v:
            if v.get('gabarit') == 'question' and not v.get('titre', '').rstrip().endswith('?'):
                pb.append(f'{ref} visuel : gabarit question, le titre doit être une question (finir par « ? »)')
            if 'bonne' in v:
                pb.append(f'{ref} visuel : « bonne » interdit — un test ne coche aucune réponse, un quiz révèle la réponse sur une slide suivante')
            for _, champ_v, t_v in regles_texte.textes_du_plan({'creneaux': [dict(c, textes={}, accroche='', premier_commentaire='', youtube_title='', tiktok_title='')]}):
                pb += regles_texte.fiche_seule(t_v, f'{ref} {champ_v}')
            if 'google' not in (v.get('surtitre', '') + v.get('titre', '')).lower():
                pb.append(f'{ref} visuel : « Google » absent du surtitre + titre')
        pc = c.get('premier_commentaire') or ''
        if not pc: pb.append(f'{ref} : premier_commentaire manquant')
        elif len(pc) > 300: pb.append(f'{ref} : premier_commentaire > 300 caractères')
        elif PRIX.search(pc): pb.append(f'{ref} : prix dans le premier commentaire')
        elif '?' in pc: pb.append(f'{ref} : premier_commentaire en question — c\'est un complément d\'information (la question va dans le texte)')
        textes = c.get('textes', {})
        attendus = {'tiktok'} if variante_b else canaux_attendus(typ, c['date'])
        if set(textes) != attendus:
            pb.append(f'{ref} : canaux {sorted(textes)} au lieu de {sorted(attendus)}')
        for canal, t in textes.items():
            t = t or ''
            if 'fiche google' not in t.lower(): pb.append(f'{ref} {canal} : « fiche Google » absent')
            if 'google' not in t.split('\n')[0].lower(): pb.append(f'{ref} {canal} : première ligne sans « Google »')
            if PRIX.search(t): pb.append(f'{ref} {canal} : prix, « mois » ou « centime » dans le texte')
            if c.get('intention') == 'offre' and not ('gratuit' in t.lower() or '30 jours' in t.lower()): pb.append(f'{ref} {canal} : intention offre sans « gratuitement »')
            if c.get('intention') == 'utile' and canal not in ('x', 'tiktok') and '?' not in t:
                pb.append(f'{ref} {canal} : contenu utile sans question dans le texte')
            if canal == 'tiktok' and not re.search(r'abonnez-vous', t, re.I):
                pb.append(f'{ref} tiktok : la légende doit inviter à s\'abonner (« Abonnez-vous … »)')
            if t.count('✅') > 3: pb.append(f'{ref} {canal} : plus de 3 ✅')
            if canal in LIMITES and len(t) > LIMITES[canal]: pb.append(f'{ref} {canal} : {len(t)} caractères (> {LIMITES[canal]})')
            if re.search(r"\b(la|votre|sa|cette) fiche\b(?! google)", t, re.I) and t.lower().count('fiche google') < 2:
                pb.append(f'{ref} {canal} : « la fiche » seule sans rappel « fiche Google » suffisant')
            if canal == 'linkedin':
                if len(re.findall(r'#\w+', t)) > 5: pb.append(f'{ref} linkedin : plus de 5 hashtags')
                if re.search(r'https?://|www\.|lien en bio', t, re.I): pb.append(f'{ref} linkedin : lien externe ou « lien en bio »')
                if 'google' not in t[:220].lower(): pb.append(f'{ref} linkedin : « Google » absent des ~200 premiers caractères')
                if len(t) < 500: pb.append(f'{ref} linkedin : texte trop court ({len(t)} < 500), viser 700 à 1 300')
                for autre in ('facebook', 'instagram'):
                    if autre in textes and t.strip() == (textes[autre] or '').strip(): pb.append(f'{ref} linkedin : copie exacte du texte {autre}')
            if canal != 'linkedin' and re.search(r'lien en bio', t, re.I) and canal in ('facebook', 'youtube', 'x'):
                pb.append(f'{ref} {canal} : « lien en bio » n\'a pas de sens sur ce canal')
        if typ == 'video':
            yt, tt = c.get('youtube_title', ''), c.get('tiktok_title', '')
            if not variante_b and (not (2 <= len(yt) <= 100) or 'google' not in yt.lower()): pb.append(f'{ref} : youtube_title manquant, > 100 caractères ou sans « Google »')
            if not tt or len(tt) > 90: pb.append(f'{ref} : tiktok_title manquant ou > 90 caractères')
            if PRIX.search(yt + tt): pb.append(f'{ref} : prix dans un titre')
        m = c.get('media') or {}
        if medias and typ == 'video' and not (m.get('postiz_vertical') or m.get('vertical')): pb.append(f'{ref} : vidéo verticale manquante')
        if medias and typ == 'visuel':
            car = m.get('carrousel')
            if car is not None and not 3 <= len(car) <= 5: pb.append(f'{ref} : carrousel de {len(car)} images (3 à 5 attendues)')
            if not car and not m.get('postiz'): pb.append(f'{ref} : média manquant (carrousel ou image)')
        for f in fiches:
            if f['id'].startswith(f"{c['date']}_{nominal.replace(':', '')}"):
                continue
            r = ressemblance(acc, f.get('accroche', ''))
            if r >= SEUIL_RESSEMBLANCE:
                pb.append(f'{ref} : accroche trop proche ({r:.0%}) de la fiche {f["id"]}')
    # phrase d'explication copiée-collée
    expl = Counter()
    for c in cr:
        for t in (c.get('textes') or {}).values():
            for ph in re.split(r'(?<=[.!?])\s+|\n', t or ''):
                if "c'est ce qui s'affiche" in ph.lower() or "c’est ce qui s’affiche" in ph.lower():
                    expl[re.sub(r'«[^»]*»', '«…»', ph.strip().lower())] += 1
                    break
    for ph, n in expl.items():
        if n > MAX_EXPLICATION_IDENTIQUE:
            pb.append(f'explication « fiche Google » copiée {n} fois à l\'identique (max {MAX_EXPLICATION_IDENTIQUE}) : varier la formulation — « {ph[:70]}… »')
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
    if len(grille) >= 10:
        cr = grille
        nb_metiers = len({c['metier'] for c in cr if c.get('metier') != 'general'})
        if nb_metiers < 6: pb.append(f'seulement {nb_metiers} métiers différents sur la semaine (minimum 6)')
        it = Counter(c.get('intention') for c in cr)
        if it['utile'] < UTILE_MIN: pb.append(f'mix éditorial : {it["utile"]} contenus utiles sur {len(cr)} (minimum {UTILE_MIN}, ≈ 70 %)')
        if it['offre'] > OFFRE_MAX: pb.append(f'mix éditorial : {it["offre"]} contenus « offre » (maximum {OFFRE_MAX})')
        if not PREUVE_MIN <= it['preuve'] <= PREUVE_MAX: pb.append(f'mix éditorial : {it["preuve"]} contenus « preuve » ({PREUVE_MIN} à {PREUVE_MAX} attendus)')
        tons = Counter(c.get('ton') for c in cr)
        for t, n in tons.items():
            if n > TON_MAX: pb.append(f'ton « {t} » utilisé {n} fois (maximum {TON_MAX} par semaine)')
        ab = [c for c in cr if c.get('creneau') == 'video' and c.get('ab')]
        if len(ab) < 2: pb.append('A/B : au moins 2 vidéos de la semaine doivent porter une variante B (champ "ab")')
    doubl = [k for k, n in Counter((c.get('date'), c.get('creneau_nominal', c.get('heure'))) for c in cr).items() if n > 1]
    if doubl: pb.append(f'créneaux en double dans le plan : {doubl}')
    return pb


def verifier_briefs(dossier):
    """Briefs vidéo (pub-work/briefs ou suivi/briefs/<lundi>) : mêmes règles de texte, et les titres sont de vraies phrases."""
    pb, noms = [], Counter()
    for f in sorted(glob.glob(os.path.join(dossier, '*.json'))):
        b = json.load(open(f, encoding='utf-8'))
        slug = b.get('slug') or os.path.basename(f)
        for champ, t in regles_texte.textes_du_brief(b):
            pb += regles_texte.problemes(t, f'brief {slug} {champ}')
        for i, a in enumerate(b.get('accroches') or []):
            pb += regles_texte.phrase_complete(a, f'brief {slug} accroche {"ABC"[i] if i < 3 else i}')
            if 'google' not in a.lower(): pb.append(f'brief {slug} accroche {"ABC"[i] if i < 3 else i} : sans « Google »')
        if b.get('moteur'):  # pubs cinétiques / plan-séquence (outils/pub-video.py) : pas de « suite », contrôles du script
            pb += [f'brief {x}' for x in PUBVIDEO.probs_brief(b, slug)]
        else:
            pb += regles_texte.phrase_complete(b.get('suite', ''), f'brief {slug} suite')
        for champ, t in regles_texte.textes_du_brief(b):
            pb += regles_texte.fiche_seule(t, f'brief {slug} {champ}')
        if b.get('angle') == 'preuve': pb.append(f'brief {slug} : angle « preuve » retiré (règle n°3) — utiliser peur de perdre ou gain de temps')
        for n in re.findall(r'\b(Weber|Martin|Durand|Bernard|Petit)\b', json.dumps(b, ensure_ascii=False)):
            noms[n] += 1
    if noms and max(noms.values()) > 3:
        pb.append(f'briefs vidéo : nom fictif trop répété {dict(noms)} (max 3 par semaine, alterner Weber / Martin / Durand / Bernard / Petit)')
    return pb


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    plan = json.load(open(sys.argv[1], encoding='utf-8'))
    pb = verifier(plan, medias='--sans-medias' not in sys.argv)
    briefs = sys.argv[sys.argv.index('--briefs') + 1] if '--briefs' in sys.argv else None
    if briefs:
        pb += verifier_briefs(briefs)
    if '--relecture' in sys.argv:
        import relecture
        lundi = plan.get('lundi') if isinstance(plan, dict) else None
        lundi = lundi or os.path.basename(sys.argv[1]).split('.')[0]
        pb += ['relecture — ' + x for x in relecture.controler(lundi, briefs)]
    if pb:
        print('\n'.join('ATTENTION : ' + p for p in pb)); sys.exit(1)
    print('plan OK' + (' (briefs vidéo contrôlés)' if briefs else '') + (' + relecture validée' if '--relecture' in sys.argv else '') + (' — médias non vérifiés' if '--sans-medias' in sys.argv else ''))
