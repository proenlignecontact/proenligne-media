"""Pubs vidéo 9:16 Proenligne avec les 3 skills « pub-swipe-proenligne », « pub-cinetique-proenligne » et
« pub-plan-sequence-proenligne » (SEULS skills autorisés pour la vidéo), rendues en MP4 sans intervention, avec voix off et
bruitages ElevenLabs calés sur les scènes (musique facultative).

Les skills s'exportent normalement à la main ; ce script fait le rendu image par image (Chromium + ffmpeg) et le mixage audio.
Le moteur d'animation n'est jamais réécrit : reference/ est copié et seuls des TEXTES fixes sont corrigés pour les règles du
dépôt (n°1 « fiche Google », n°2 aucun prix sauf l'écran final, n°3 aucune statistique client, n°5 aucun deux-points) :
écran final « 14,99 € / mois · 30 jours offerts » + « Lien en bio → » (phrase variable `offre_ligne`), « Exemple · ville »,
concurrent du swipe à la même note, preuve client coupée, heures « 21h00 », chaque « fiche » → « fiche Google ». Au rendu, tout le texte
réellement affiché est relevé image par image et passé dans cerveau/regles_texte.py : un seul problème = rendu refusé.

AUDIO (comme le décrit references/audio-elevenlabs.md des skills) : la voix commande le tempo. Le script entier est dit
D'UNE TRAITE (bien plus naturel que phrase par phrase) : connecteur ElevenLabs, voix « Marcel - French touch »
kENkNtk0xyzG09WW40xE, modèle eleven_v4, 1 prise, avec des balises de jeu ([warmly], [pause], [excited]…). La prise est
redécoupée aux pauses entre les phrases ; chaque scène dure le temps de ses phrases, arrondi au temps (120 BPM), avec
`nat` = durée d'auteur, et la chorégraphie s'étire. Bruitages : banque fixe outils/assets/sfx/*.mp3, placés sur les gestes.
Musique : banque outils/assets/musique/ambiance-<0|1|2>.mp3, en fond très bas (≈ 17 LU sous la voix, baissée encore
pendant qu'elle parle) ; "musique": false la retire. Le terminal ne peut pas joindre ElevenLabs : les fichiers passent
par l'action GitHub « Téléchargement audio » (commande `telecharger`).

usage :
  installer                                   prépare /home/claude/pub-video-work (une fois par session)
  tirage <lundi> --metiers m1,…,m7 [--par-jour 2] [--sortie <fichier>]
                                              moteur / angle / ville / ambiance des vidéos, en rotation (écrit
                                              suivi/plan/<lundi>-videos.json, ou --sortie ; --par-jour 2 = 2 vidéos par jour ;
                                              --eviter <fichier de tirage> = ne pas répéter moteur + angle à moins de 3 jours)
  valider <brief.json> …                      contrôle les briefs → « briefs OK »
  prise <brief.json> [--variante A|B]         donne l'id (prise-A / prise-B), la voix, le modèle et le TEXTE EXACT à envoyer
                                              à mcp__ElevenLabs__creative_generate_speech (une prise par variante)
  noter <brief.json> <id> <url> <duree>       enregistre la prise générée (content_url signée + duration_secs)
  telecharger <brief.json> …                  fait télécharger par l'action GitHub tous les fichiers notés et absents
                                              (medias/audio/<slug>/<id>.mp3), attend, tire le dépôt, vérifie
  caler <brief.json> [--variante A|B]         affiche le calage (durées des scènes, départs des voix, total)
  rendre <brief.json> <sortie.mp4> [--variante A|B] [--fps 30] [--muet]
                                              rend la vidéo avec sa bande-son ; écrit <sortie>-planche.png (À REGARDER)

Brief vidéo (suivi/briefs/<lundi>/<slug>.json ; slug = celui du créneau 19:00 du plan) :
  {
    "slug": "plombier-swipe-lorient",
    "moteur": "swipe" | "cinetique" | "plan-sequence",
    "angle": "Plus de clients" | "Face au concurrent" | "Du temps libre" | "Plus d'appels",
    "metier": "plombier", "ville": "Lorient",
    "valeur": "37",              (cinétique : grosse valeur jaune, ≤ 5 car., ≤ 18 angle concurrent, heure « 22h47 »)
    "entreprise": "",            (plan-séquence et swipe ; vide = « Votre entreprise »)
    "lieu": "",                  (plan-séquence, angle temps)
    "accroches": ["A", "B"],     (cinétique / plan-séquence : affichée ET dite à la 1re image ; swipe : dite seulement,
                                  le titre à l'écran est fixe. *mots* = mis en avant à l'écran)
    "accroches_dites": ["…"],    (facultatif : ce que la voix dit à la place de l'accroche affichée, quand celle-ci ne se dit
                                  pas seule, ex. cinétique « Plus de clients » où la valeur jaune « 23 » précède la phrase)
    "voix": [                    (les autres lignes de voix, dans l'ordre ; l'accroche est la 1re ligne, automatiquement)
      {"scene": "Probleme", "texte": "Une fiche Google qui dort, on la passe sans réfléchir."},
      {"scene": "Bascule",  "texte": "Pro en ligne la fait vivre chaque semaine."},
      {"scene": "Bascule",  "texte": "Et cette fois, on vous appelle.", "ancre": 3.0},
      {"scene": "Offre",    "texte": "Essayez Pro en ligne gratuitement, sans engagement."}
    ],                           (champ facultatif "ton" par ligne : balise de jeu en anglais, ex. "curious", "softly",
                                  "excited", "warmly", "pause" ; défauts warmly / pause / excited / warmly ; "ton_accroche")
    "offre_ligne": "Votre métier, *pas votre fiche.*",  (facultatif, ≤ 40 car. : la grande phrase de l'écran final ;
                                  à varier d'une vidéo à l'autre ; vide = phrase par défaut de l'angle)
    "musique": true,             (musique de banque de l'ambiance en fond très bas ; false = voix + bruitages seuls)
    "ambiance": 0 | 1 | 2,
    "audio_src": {}              (rempli par `noter`)
  }
Voix : écrite pour l'oreille (français parlé, « on » plutôt que « les clients », phrases qui s'enchaînent), vouvoiement,
phrases courtes (≈ 6-7 mots, ≤ 10 en Bascule), « Pro en ligne » en trois mots, « fiche Google » en entier,
aucun prix, aucun résultat chiffré, aucun « : ». Durée totale visée 15-18 s, plafond 20 s.
"""
import glob, json, math, os, re, shutil, subprocess, sys, time

ICI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(ICI)
sys.path.insert(0, os.path.join(REPO, 'cerveau'))
sys.path.insert(0, ICI)
import regles_texte  # noqa: E402

WORK = os.environ.get('PUB_VIDEO_WORK', '/home/claude/pub-video-work')
SKILLS = {
    'swipe': {'nom': 'pub-swipe-proenligne', 'piece': 'SWPiece', 'bg': '#e7f0ea',
              'fichiers': ['animations-v3.jsx', 'tweaks-panel.jsx', 'p4-kit.jsx', 'sw-kit.jsx', 'sw-angles.jsx', 'audio-sync.jsx', 'PubSwipeVideo.jsx']},
    'cinetique': {'nom': 'pub-cinetique-proenligne', 'piece': 'P4Piece', 'bg': '#16201b',
                  'fichiers': ['animations-v3.jsx', 'tweaks-panel.jsx', 'p4-kit.jsx', 'p4-angles.jsx', 'audio-sync.jsx', 'Pub4AnglesVideo.jsx']},
    'plan-sequence': {'nom': 'pub-plan-sequence-proenligne', 'piece': 'PSPiece', 'bg': '#f6f7f4',
                      'fichiers': ['animations-v3.jsx', 'tweaks-panel.jsx', 'p4-kit.jsx', 'ps-kit.jsx', 'ps-angles.jsx', 'audio-sync.jsx', 'PubPlanSequenceVideo.jsx']},
}
MOTEURS = ['swipe', 'cinetique', 'plan-sequence']
RACINES = ['/mnt/skills/organization', '/mnt/skills/user', '/mnt/skills/private', '/mnt/skills/plugins', '/mnt/skills/public',
           os.path.expanduser('~/.claude/skills')]
ANGLES = ['Plus de clients', 'Face au concurrent', 'Du temps libre', "Plus d'appels"]
NAT = [('Accroche', 3.0), ('Probleme', 4.0), ('Bascule', 5.0), ('Offre', 3.0)]
SANS_SOIREES = {'boulangerie', 'boulanger', 'restaurant'}
# commerces à boutique : leurs clients viennent sur place (itinéraires), ils n'appellent pas → jamais l'angle « Plus d'appels »
SANS_APPELS = {'boulangerie', 'boulanger', 'fleuriste', 'restaurant', 'fromager', 'fromagerie', 'pressing', 'caviste', 'épicerie',
               'primeur', 'boutique', 'pâtisserie', 'pâtissier', 'boucherie', 'boucher', 'librairie', 'opticien'}
# combinaisons écartées après l'audit du 4/11/2026 : compteurs « 34 contre 6 » (promesse chiffrée) et 1re image coupée
COMBOS_EXCLUS = {('cinetique', 'Plus de clients'), ('plan-sequence', "Plus d'appels")}
PRIX_AUTORISES = {'14,99 €', '/ mois · 30 jours offerts'}   # seuls textes à prix permis, sur l'écran final de la vidéo
VOIX_ID, VOIX_NOM, VOIX_MODELE = 'kENkNtk0xyzG09WW40xE', 'Marcel - French touch', 'eleven_v4'
TONS = {'Accroche': 'warmly', 'Probleme': 'pause', 'Bascule': 'excited', 'Offre': 'warmly'}  # balises de jeu par défaut (eleven_v4)
BPM = 120
BEAT = 60 / BPM
LEAD, GAP, TAIL = 0.15, 0.25, 0.35
PLAFOND = 20.0
GAINS = {'voix': 1.0, 'sfx': 0.5}
MUSIQUE_LUFS, VOIX_LUFS = -33, -16   # musique de fond très basse : ~17 LU sous la voix, et encore baissée pendant qu'elle parle
SFX_DIR = os.path.join(ICI, 'assets', 'sfx')
MUSIQUE_DIR = os.path.join(ICI, 'assets', 'musique')

# Gestes de chaque pub en temps d'auteur (0-15 s) → bruitage de la banque (et gain relatif)
SFX_COMMUNS = {'swipe': [(11.5, 'feuille')], 'cinetique': [(2.85, 'transition'), (6.85, 'transition'), (11.85, 'feuille')],
               'plan-sequence': [(3.0, 'camera'), (7.0, 'camera'), (11.55, 'feuille')]}
SFX_ANGLES = {
    'swipe': {
        'Plus de clients': [(1.1, 'swipe'), (2.4, 'tampon'), (2.5, 'swipe'), (7.4, 'blip'), (7.9, 'blip'), (8.4, 'blip'), (10.0, 'swipe'), (10.1, 'appel')],
        'Face au concurrent': [(0.2, 'tic'), (1.1, 'tic'), (2.0, 'tic'), (2.75, 'tap'), (2.9, 'chute'), (7.4, 'blip'), (7.9, 'blip'), (8.4, 'blip'),
                               (8.7, 'tic'), (9.3, 'tic'), (9.9, 'tap'), (10.2, 'chute')],
        'Du temps libre': [(1.3, 'swipe'), (3.0, 'chute'), (4.0, 'swipe'), (4.3, 'chute'), (5.8, 'swipe'), (6.2, 'chute'), (7.6, 'rafale'), (9.0, 'blip')],
        "Plus d'appels": [(0.9, 'swipe'), (1.8, 'swipe'), (4.0, 'tap'), (7.6, 'blip'), (8.1, 'blip'), (8.6, 'blip'), (9.4, 'tap'), (9.9, 'appel'), (10.5, 'appel')],
    },
    'cinetique': {
        'Plus de clients': [(7.8, 'blip'), (8.3, 'blip'), (8.8, 'blip')],
        'Face au concurrent': [(7.8, 'blip'), (8.3, 'blip'), (10.2, 'tampon')],
        'Du temps libre': [(7.4, 'rafale'), (9.4, 'blip')],
        "Plus d'appels": [(7.8, 'blip'), (8.3, 'blip'), (10.0, 'appel'), (10.6, 'appel')],
    },
    'plan-sequence': {
        'Plus de clients': [(7.8, 'blip'), (8.3, 'blip'), (8.8, 'blip'), (10.4, 'tampon')],
        'Face au concurrent': [(7.8, 'blip'), (8.3, 'blip'), (8.8, 'blip'), (10.8, 'tampon')],
        'Du temps libre': [(7.4, 'rafale'), (9.6, 'blip')],
        "Plus d'appels": [(7.8, 'blip'), (8.3, 'blip'), (10.0, 'appel'), (10.3, 'appel'), (10.6, 'appel')],
    },
}

REMPLACEMENTS = [
    ('/ mois, sans engagement', '/ mois · 30 jours offerts'),          # prix affiché sur l'écran final (décision du 4/11/2026)
    ('Essayer gratuitement →', 'Lien en bio →'),                       # fin pensée pour les publications non sponsorisées
    ('En direct · {tw.ville}, ce matin', 'Exemple · {tw.ville}, un matin'),   # pas de fausse donnée « en direct »
    ("sub={'4,8 · '", "sub={'4,2 · '"),                                # le concurrent a la même note : la note n'est pas l'argument
    ('text={line} size={132}', 'text={window.PUB_OFFRE_LIGNE || line} size={132}'),  # phrase de l'Offre variable par vidéo
    ('Dernière photo : il y a 2 ans', 'Dernière photo il y a 2 ans'),
    ('Après dix heures de chantier.', 'Après une longue journée de travail.'),   # cinétique « Du temps libre » : vaut pour tous les métiers (salon, boutique…)
    ("Vos appels aujourd'hui : {calls}", "Appels aujourd'hui · {calls}"),   # règle n°5 (swipe « Plus d'appels »)
    ('Nouvelle photo : lundi', 'Nouvelle photo lundi'),
    ('Publication : jeudi', 'Publication jeudi'),
    ('dernière photo : 2021', 'dernière photo en 2021'),
    ('Dernière photo : 2021', 'Dernière photo en 2021'),
    (">Cas client O'propre, Rennes : ×3 appels par mois<", '><'),
    ('Publications ce mois', 'Publications récentes'),
    ("Cas client O'propre, Rennes : ×3 appels par mois.", ''),
    ("Cas client O\\'propre, Rennes : ×3 appels par mois.", ''),
    ('À fiche égale,', 'À fiche Google aussi vivante,'),
    ('votre fiche Google *réclame :*', 'votre fiche Google *vous réclame tout ça.*'),
    ('Les clients du coin *vous trouvent, vous.*', 'Les clients du coin *voient votre travail.*'),   # pas de promesse invérifiable
]
TEXTES_DECOR = ('p4-angles.jsx', 'ps-angles.jsx', 'sw-angles.jsx', 'p4-kit.jsx', 'ps-kit.jsx', 'sw-kit.jsx')
DEPENDANCES = 'react@18.3.1 react-dom@18.3.1 esbuild@0.23.1'


def trouver_skill(nom):
    for r in RACINES:
        p = os.path.join(r, nom, 'reference')
        if os.path.isdir(p):
            return p
    hits = glob.glob(f'/mnt/skills/**/{nom}/reference', recursive=True) + \
        glob.glob(os.path.expanduser(f'~/.claude/skills/**/{nom}/reference'), recursive=True)
    if hits:
        return hits[0]
    raise SystemExit(f'skill {nom} introuvable (cherché dans {", ".join(RACINES)})')


def adapter_textes(js, nom):
    for a, b in REMPLACEMENTS:
        js = js.replace(a, b)
    js = re.sub(r"(['>\"])(\d{1,2}):(\d{2})(?=['<\"\s·])", r'\1\2h\3', js)   # '21:00', >23:02 · … → 21h00, 23h02
    if nom in TEXTES_DECOR:
        js = re.sub(r"\b([Ff]iches?)\b(?!\*? Google)", r'\1 Google', js)
    return js


def controler_decor(js, nom):
    pb = []
    for m in re.finditer(r"'((?:[^'\\\n]|\\.)*)'|\"((?:[^\"\\\n]|\\.)*)\"|>([^<>{}\n]+)<", js):
        t = next(g for g in m.groups() if g is not None)
        if not re.search(r'[A-Za-zÀ-ÿ]{3,} [A-Za-zÀ-ÿ]', t):
            continue
        pb += problemes_ecran(t, f'{nom} « {t[:50]} »') + regles_texte.fiche_seule(t, f'{nom} « {t[:50]} »')
    return pb


def problemes_ecran(t, ou):
    """Règles de texte, sauf le prix de l'écran final (PRIX_AUTORISES), seul endroit où il est permis."""
    pb = regles_texte.problemes(t, ou)
    if t.strip() in PRIX_AUTORISES:
        pb = [x for x in pb if 'règle n°2' not in x]
    return pb


def installer():
    os.makedirs(WORK, exist_ok=True)
    if not os.path.exists(os.path.join(WORK, 'node_modules', 'esbuild')):
        subprocess.run('npm init -y >/dev/null && npm i --silent ' + DEPENDANCES, shell=True, cwd=WORK, check=True)
    try:
        import playwright  # noqa: F401
    except ImportError:
        subprocess.run([sys.executable, '-m', 'pip', 'install', '--quiet', 'playwright', 'pillow', '--break-system-packages'], check=True)
    r = subprocess.run([sys.executable, '-c', 'from playwright.sync_api import sync_playwright\nwith sync_playwright() as p: p.chromium.launch().close()'],
                       capture_output=True)
    if r.returncode:
        subprocess.run([sys.executable, '-m', 'playwright', 'install', 'chromium'], check=True)
    if not shutil.which('ffmpeg'):
        raise SystemExit("ffmpeg manquant (apt-get install -y ffmpeg)")
    esb = os.path.join(WORK, 'node_modules', '.bin', 'esbuild')
    for moteur, s in SKILLS.items():
        src = trouver_skill(s['nom'])
        dst = os.path.join(WORK, moteur)
        os.makedirs(dst, exist_ok=True)
        for f in s['fichiers']:
            js = adapter_textes(open(os.path.join(src, f), encoding='utf-8').read(), f)
            if f in TEXTES_DECOR:
                reste = controler_decor(js, f)
                if reste:
                    raise SystemExit('textes du skill à adapter (ajouter un remplacement dans REMPLACEMENTS) :\n' + '\n'.join(reste))
            tmp = os.path.join(dst, f)
            open(tmp, 'w', encoding='utf-8').write(js)
            subprocess.run([esb, tmp, '--loader:.jsx=jsx', '--outfile=' + tmp[:-4] + '.js', '--log-level=error'], check=True)
    for f in ('react.production.min.js', 'react-dom.production.min.js'):
        pkg = 'react' if f.startswith('react.') else 'react-dom'
        shutil.copy(os.path.join(WORK, 'node_modules', pkg, 'umd', f), os.path.join(WORK, f))
    for f in ('bricolage-grotesque-latin.woff2', 'figtree-latin.woff2'):
        shutil.copy(os.path.join(ICI, 'assets', f), os.path.join(WORK, f))
    manque = sorted(({s for t in SFX_ANGLES.values() for l in t.values() for _, s in l} | {s for l in SFX_COMMUNS.values() for _, s in l})
                    - {os.path.basename(f)[:-4] for f in glob.glob(os.path.join(SFX_DIR, '*.mp3'))})
    print(f'prêt : {WORK} (' + ', '.join(f'{m} ← {trouver_skill(SKILLS[m]["nom"])}' for m in MOTEURS) + ')')
    if manque:
        print('ATTENTION bruitages absents de outils/assets/sfx : ' + ', '.join(manque))


# ---------------------------------------------------------------- tirage
def tirage(lundi, metiers, par_jour=1, sortie=None, eviter=None):
    import datetime as dt
    hist = []
    p = os.path.join(REPO, 'suivi', 'historique-pubs.json')
    if os.path.exists(p):
        hist = [h for h in json.load(open(p, encoding='utf-8')) if h.get('moteur') in MOTEURS]
    hist.sort(key=lambda h: h.get('date', ''))
    villes = json.load(open(os.path.join(REPO, 'suivi', 'villes-pubs.json'), encoding='utf-8'))['villes']

    def recence(cle, valeurs):
        dern = {v: -1 for v in valeurs}
        for i, h in enumerate(hist):
            if h.get(cle) in dern: dern[h[cle]] = i
        return sorted(valeurs, key=lambda v: (dern[v], valeurs.index(v)))

    ordre_moteurs = recence('moteur', MOTEURS)
    ordre_angles = recence('angle', ANGLES)
    ordre_villes = recence('ville', villes)
    dern_amb = hist[-1].get('ambiance') if hist else None
    out, angles_sem = [], []
    j0 = dt.date.fromisoformat(lundi)
    autres = [e for e in hist if e.get('date')] + (json.load(open(eviter, encoding='utf-8')) if eviter and os.path.exists(eviter) else [])
    for i, metier in enumerate(metiers):
        moteur = ordre_moteurs[i % 3]
        d = j0 + dt.timedelta(days=i // par_jour)
        def permis(a, strict=True):
            if (moteur, a) in COMBOS_EXCLUS: return False
            if metier.lower() in SANS_SOIREES and a == 'Du temps libre': return False
            if metier.lower() in SANS_APPELS and a == "Plus d'appels": return False
            if strict:
                for e in autres + out:
                    if e.get('moteur') == moteur and e.get('angle') == a and abs((dt.date.fromisoformat(e['date'][:10]) - d).days) <= 2:
                        return False
            return True
        cands = [a for a in ordre_angles + ordre_angles if a not in angles_sem[-1:] and permis(a)] or \
                [a for a in ordre_angles if permis(a, False)] or list(ANGLES)
        compte = {a: angles_sem.count(a) for a in ANGLES}
        angle = min(cands, key=lambda a: (compte[a], cands.index(a)))
        angles_sem.append(angle)
        amb = (i + (0 if dern_amb is None else dern_amb + 1)) % 3
        out.append({'date': d.isoformat(), 'moteur': moteur, 'angle': angle,
                    'metier': metier.lower(), 'ville': ordre_villes[i % len(ordre_villes)], 'ambiance': amb})
    f = sortie or os.path.join(REPO, 'suivi', 'plan', f'{lundi}-videos.json')
    json.dump(out, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for o in out:
        print(f"{o['date']}  {o['moteur']:<13} {o['angle']:<19} {o['metier']:<14} {o['ville']:<14} ambiance {o['ambiance']}")
    print(f'→ {os.path.relpath(f, REPO)}')
    return out


# ---------------------------------------------------------------- validation
def lignes_voix(b, variante='A'):
    """[(id, scene, texte, ancre, ton)] : l'accroche de la variante, puis les lignes de "voix"."""
    acc = b.get('accroches') or ['']
    i = 1 if variante == 'B' and len(acc) > 1 else 0
    dites = b.get('accroches_dites') or []
    dite = dites[i] if i < len(dites) and dites[i] else acc[i].replace('*', '')
    out = [(f'vo-accroche-{"AB"[i]}', 'Accroche', dite, 0.0, b.get('ton_accroche') or TONS['Accroche'])]
    vu = set()
    for k, l in enumerate(b.get('voix') or [], 1):
        sc = l.get('scene')
        ton = l.get('ton') or (TONS.get(sc) if sc not in vu else '')
        vu.add(sc)
        out.append((f'vo-{k}', sc, l.get('texte', ''), float(l.get('ancre', 0) or 0), ton))
    return out


def id_prise(variante='A'):
    return f'prise-{variante}'


def texte_prise(b, variante='A'):
    """Le script complet, dit d'une traite (plus naturel que ligne par ligne), avec les balises de jeu eleven_v4."""
    return ' '.join((f'[{ton}] ' if ton else '') + t.strip() for _, _, t, _, ton in lignes_voix(b, variante))


def silences(f):
    r = subprocess.run(['ffmpeg', '-hide_banner', '-i', f, '-af', 'silencedetect=noise=-35dB:d=0.18', '-f', 'null', '-'],
                       capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r'silence_start: ([0-9.]+)', r)]
    en = [float(x) for x in re.findall(r'silence_end: ([0-9.]+)', r)]
    return list(zip(st, en + [duree_fichier(f)] * (len(st) - len(en))))


def decouper(b, variante='A'):
    """Redécoupe la prise unique en phrases, aux silences les plus proches des fins de phrase attendues.
    Renvoie [(id, scene, texte, ancre, debut_dans_fichier, duree)]."""
    f = os.path.join(dossier_audio(b), id_prise(variante) + '.mp3')
    if not os.path.exists(f):
        raise SystemExit(f'{os.path.relpath(f, REPO)} absent : générer la prise, `noter`, puis `telecharger`')
    lignes = lignes_voix(b, variante)
    total = duree_fichier(f)
    sil = silences(f)
    debut = sil[0][1] if sil and sil[0][0] < 0.05 else 0.0
    fin = sil[-1][0] if sil and sil[-1][1] >= total - 0.05 else total
    internes = [s for s in sil if s[0] > debut + 0.2 and s[1] < fin - 0.2]
    poids = [max(1, len(re.sub(r'\W', '', l[2]))) for l in lignes]
    cumul, attendus = 0, []
    for w in poids[:-1]:
        cumul += w; attendus.append(debut + (fin - debut) * cumul / sum(poids))
    n = len(attendus)
    if len(internes) < n:
        raise SystemExit(f'{b["slug"]} {id_prise(variante)} : {len(internes)} pauses pour {n + 1} phrases — prise inexploitable, la régénérer')
    # choix monotone : pour chaque fin de phrase, la pause la plus proche (les longues pauses sont favorisées)
    choix, j0 = [], 0
    for i, t in enumerate(attendus):
        reste = n - i - 1
        cands = range(j0, len(internes) - reste)
        j = min(cands, key=lambda j: abs((internes[j][0] + internes[j][1]) / 2 - t) - 0.6 * (internes[j][1] - internes[j][0]))
        choix.append(internes[j]); j0 = j + 1
    bornes = [debut] + [x for s in choix for x in s] + [fin]
    out = []
    for k, l in enumerate(lignes):
        a, z = max(0.0, bornes[2 * k] - 0.04), min(total, bornes[2 * k + 1] + 0.08)
        out.append(l[:4] + (round(a, 3), round(z - a, 3)))
    for (id_, sc, t, *_), (*_, d) in zip(lignes, out):
        att = len(re.findall(r"[\w'’]+", t)) / 2.6
        if not (0.35 * att <= d <= 2.6 * att + 0.6):
            raise SystemExit(f'{b["slug"]} : découpage douteux de « {t} » ({d:.2f} s pour ~{att:.1f} s attendues) — régénérer la prise')
    return out


def probs_brief(b, nom=''):
    pb, ou = [], (b.get('slug') or nom)
    m = b.get('moteur')
    if m not in SKILLS: pb.append(f'{ou} : moteur « {m} » inconnu ({" | ".join(MOTEURS)}) — seuls ces 3 skills sont autorisés')
    if b.get('angle') not in ANGLES: pb.append(f'{ou} : angle « {b.get("angle")} » inconnu ({" | ".join(ANGLES)})')
    for k in ('slug', 'metier', 'ville'):
        if not (b.get(k) or '').strip(): pb.append(f'{ou} : champ {k} vide')
    acc = b.get('accroches') or []
    if not acc: pb.append(f'{ou} : aucune accroche')
    lim = 90 if m == 'swipe' else (26 if (m == 'plan-sequence' and b.get('angle') == 'Plus de clients') else 60)
    for i, a in enumerate(acc):
        lab = f'{ou} accroche {"ABC"[i] if i < 3 else i}'
        nu = a.replace('*', '')
        if len(nu) > lim: pb.append(f'{lab} : {len(nu)} caractères (max {lim})')
        if 'google' not in nu.lower(): pb.append(f'{lab} : sans « Google »')
        if a.count('*') % 2: pb.append(f'{lab} : astérisques * non appariés')
        pb += regles_texte.problemes(nu, lab) + regles_texte.phrase_complete(nu, lab) + regles_texte.fiche_seule(nu, lab)
    if m == 'cinetique':
        v = (b.get('valeur') or '').strip()
        lv = 18 if b.get('angle') == 'Face au concurrent' else 5
        if len(v) > lv: pb.append(f'{ou} valeur : « {v} » trop long (max {lv})')
        pb += regles_texte.problemes(v, f'{ou} valeur')
    if m in ('plan-sequence', 'swipe'):
        if m == 'plan-sequence' and len(b.get('metier', '') + b.get('ville', '')) > 28: pb.append(f'{ou} : métier + ville > 28 caractères')
        if len(b.get('entreprise') or '') > 24: pb.append(f'{ou} entreprise : > 24 caractères')
    for k in ('entreprise', 'lieu', 'ville', 'metier'):
        pb += regles_texte.problemes(b.get(k) or '', f'{ou} {k}') + regles_texte.fiche_seule(b.get(k) or '', f'{ou} {k}')
    if b.get('ambiance') not in (0, 1, 2, None): pb.append(f'{ou} ambiance : 0, 1 ou 2')
    if (m, b.get('angle')) in COMBOS_EXCLUS: pb.append(f'{ou} : combinaison {m} + « {b.get("angle")} » écartée (audit du 4/11)')
    if b.get('angle') == "Plus d'appels" and (b.get('metier') or '').lower() in SANS_APPELS:
        pb.append(f'{ou} : « Plus d\'appels » interdit pour un commerce à boutique (ses clients viennent sur place)')
    ol = b.get('offre_ligne') or ''
    if ol:
        if len(ol.replace('*', '')) > 40: pb.append(f'{ou} offre_ligne : > 40 caractères')
        pb += regles_texte.problemes(ol.replace('*', ''), f'{ou} offre_ligne') + regles_texte.fiche_seule(ol, f'{ou} offre_ligne')
    # métier et ville dans l'accroche (affichée quand elle est libre, et dite)
    def racine(x):
        import unicodedata
        x = unicodedata.normalize('NFD', x.lower()); x = ''.join(c for c in x if unicodedata.category(c) != 'Mn')
        return x[:5]
    def contient(t, mot):
        import unicodedata
        t = unicodedata.normalize('NFD', t.lower()); t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
        return racine(mot) in t
    met, vil = b.get('metier') or '', b.get('ville') or ''
    dites = b.get('accroches_dites') or []
    for i, a in enumerate(acc):
        lab = f'{ou} accroche {"ABC"[i] if i < 3 else i}'
        dite = (dites[i] if i < len(dites) and dites[i] else a).replace('*', '')
        if not (contient(dite, met) and contient(dite, vil)): pb.append(f'{lab} (dite) : doit nommer le métier et la ville')
        affichee_libre = not (m == 'swipe' or (m == 'plan-sequence' and b.get('angle') == 'Plus de clients'))
        if affichee_libre and not (contient(a, met) and contient(a, vil)): pb.append(f'{lab} (affichée) : doit nommer le métier et la ville')
    # voix
    voix = b.get('voix') or []
    scenes = [l.get('scene') for l in voix]
    for s in ('Probleme', 'Bascule', 'Offre'):
        if s not in scenes: pb.append(f'{ou} voix : aucune ligne pour la scène {s}')
    if any(s not in ('Probleme', 'Bascule', 'Offre') for s in scenes): pb.append(f'{ou} voix : scène inconnue (Probleme | Bascule | Offre ; l\'accroche est dite automatiquement)')
    if scenes != sorted(scenes, key=lambda s: ['Probleme', 'Bascule', 'Offre'].index(s) if s in ('Probleme', 'Bascule', 'Offre') else 9):
        pb.append(f'{ou} voix : lignes dans le désordre des scènes')
    if scenes.count('Bascule') > 2: pb.append(f'{ou} voix : au plus 2 lignes en Bascule')
    for i, d in enumerate(b.get('accroches_dites') or []):
        if d:
            lab = f'{ou} accroche dite {"ABC"[i] if i < 3 else i}'
            pb += regles_texte.problemes(d, lab) + regles_texte.fiche_seule(d, lab)
            if 'google' not in d.lower(): pb.append(f'{lab} : sans « Google »')
    mots = 0
    for k, l in enumerate(voix, 1):
        t, lab = l.get('texte', ''), f'{ou} voix {k}'
        n = len(re.findall(r"[\w'’]+", t)); mots += n
        lim_m = 10 if l.get('scene') == 'Bascule' else 9
        if n > lim_m: pb.append(f'{lab} : {n} mots (max {lim_m}, sinon la pub dépasse 20 s)')
        if re.search(r'proenligne', t, re.I): pb.append(f'{lab} : écrire « Pro en ligne » en trois mots (prononciation)')
        pb += regles_texte.problemes(t, lab) + regles_texte.fiche_seule(t, lab)
    offres = [l.get('texte', '').lower() for l in voix if l.get('scene') == 'Offre']
    if offres and not ('bio' in offres[-1] and re.search(r'trente jours|30 jours', offres[-1])):
        pb.append(f'{ou} voix Offre : doit dire « trente jours offerts » et « lien en bio »')
    if mots + len(re.findall(r"[\w'’]+", (acc[0] if acc else '').replace('*', ''))) > 42:
        pb.append(f'{ou} voix : trop de mots au total (≈ 2,4 mots par seconde, plafond 20 s)')
    return pb


def valider(fichiers):
    pb = []
    for f in fichiers:
        pb += probs_brief(json.load(open(f, encoding='utf-8')), os.path.basename(f))
    print('\n'.join(pb) if pb else 'briefs OK')
    return 1 if pb else 0


# ---------------------------------------------------------------- audio : fichiers, calage
def dossier_audio(b):
    return os.path.join(REPO, 'medias', 'audio', b['slug'])


def duree_fichier(f):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', f], capture_output=True, text=True)
    return float(r.stdout.strip())


def duree_ligne(b, id_):
    f = os.path.join(dossier_audio(b), id_ + '.mp3')
    if os.path.exists(f):
        return duree_fichier(f)
    src = (b.get('audio_src') or {}).get(id_)
    if src and src.get('duree'):
        return float(src['duree'])
    raise SystemExit(f'{b["slug"]} : ligne {id_} ni téléchargée ni notée (générer puis `noter`)')


def caler(b, variante='A'):
    """Durées des scènes (dur / nat), départ de chaque voix et de chaque bruitage, en temps de lecture."""
    segs = decouper(b, variante)
    src = os.path.join(dossier_audio(b), id_prise(variante) + '.mp3')
    par_scene = {s: [l for l in segs if l[1] == s] for s, _ in NAT}
    scenes, start, voix = [], 0.0, []
    for s, nat in NAT:
        ls = par_scene[s]
        d = [l[5] for l in ls]
        besoin = LEAD + sum(d) + GAP * max(0, len(d) - 1) + TAIL
        dur = math.ceil(max(besoin, 0.85 * nat) / BEAT - 1e-9) * BEAT
        # ancres : une ligne ne démarre pas avant son ancre convertie
        t = start + LEAD
        for (id_, _, texte, ancre, ss, _), di in zip(ls, d):
            t = max(t, start + ancre * dur / nat)
            voix.append({'id': id_, 'texte': texte, 'at': round(t, 3), 'fin': round(t + di, 3), 'scene': s, 'src': src, 'ss': ss, 'dur': di})
            t += di + GAP
        fin_voix = max([v['fin'] for v in voix if v['scene'] == s] or [start])
        while fin_voix > start + dur - 0.3:
            dur += BEAT
        scenes.append({'name': s, 'dur': round(dur, 3), 'nat': nat, 'start': round(start, 3)})
        start += dur
    total = round(start, 3)

    def lecture(t_aut):
        acc = 0.0
        for sc in scenes:
            if t_aut < acc + sc['nat'] or sc is scenes[-1]:
                return sc['start'] + (t_aut - acc) * sc['dur'] / sc['nat']
            acc += sc['nat']
    sfx = [{'id': n, 'at': round(max(0.0, lecture(t)), 3)} for t, n in sorted(SFX_COMMUNS[b['moteur']] + SFX_ANGLES[b['moteur']][b['angle']])]
    return {'scenes': scenes, 'total': total, 'voix': voix, 'sfx': sfx}


def noter(brief_f, id_, url, duree):
    b = json.load(open(brief_f, encoding='utf-8'))
    b.setdefault('audio_src', {})[id_] = {'url': url, 'duree': float(duree)}
    json.dump(b, open(brief_f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'{b["slug"]} {id_} noté ({float(duree):.2f} s)')


def telecharger(fichiers, attente=420):
    demandes = []
    for f in fichiers:
        b = json.load(open(f, encoding='utf-8'))
        for id_, s in (b.get('audio_src') or {}).items():
            dest = os.path.relpath(os.path.join(dossier_audio(b), id_ + '.mp3'), REPO)
            if not os.path.exists(os.path.join(REPO, dest)):
                demandes.append({'url': s['url'], 'dest': dest})
    if not demandes:
        print('rien à télécharger'); return 0
    g = lambda *a: subprocess.run(['git', '-C', REPO] + list(a), capture_output=True, text=True)
    stamp = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    json.dump({'demande': stamp, 'fichiers': demandes}, open(os.path.join(REPO, 'suivi', 'audio-a-telecharger.json'), 'w', encoding='utf-8'), indent=1)
    g('add', 'suivi/audio-a-telecharger.json') ; g('-c', 'user.name=Claude', '-c', 'user.email=noreply@anthropic.com', 'commit', '-qm', f'Audio ElevenLabs à télécharger ({len(demandes)} fichiers)')
    for _ in range(3):
        if g('push', '-q', 'origin', 'HEAD:main').returncode == 0: break
        g('pull', '-q', '--rebase', 'origin', 'main')
    print(f'{len(demandes)} fichiers demandés à l\'action GitHub…', flush=True)
    t0 = time.time()
    while time.time() - t0 < attente:
        time.sleep(15)
        g('pull', '-q', '--rebase', 'origin', 'main')
        p = os.path.join(REPO, 'suivi', 'audio-telecharge.json')
        if os.path.exists(p):
            r = json.load(open(p, encoding='utf-8'))
            if r.get('demande') == stamp:
                for e in r.get('echecs', []): print('ÉCHEC ' + e)
                manque = [d['dest'] for d in demandes if not os.path.exists(os.path.join(REPO, d['dest']))]
                print(f"{len(r.get('telecharges', []))} fichiers téléchargés" + (f', {len(manque)} manquants' if manque else ''))
                return 1 if manque else 0
    print(f'action GitHub non terminée après {attente} s (voir https://github.com/proenlignecontact/proenligne-media/actions)')
    return 1


# ---------------------------------------------------------------- mixage
def mixer(plan, b, sortie_m4a, musique):
    entrees, filtres, voix, sfx, nb = [], [], [], [], [0]
    total = plan['total']

    def entree(f, at, gain, lab, ss=None, dur=None):
        k = nb[0]; nb[0] += 1; ms = int(round(at * 1000))
        entrees.extend((['-ss', str(ss), '-t', str(dur)] if ss is not None else []) + ['-i', f])
        fondu = f',afade=t=in:d=0.02,afade=t=out:st={max(0, dur - 0.06):.3f}:d=0.06' if ss is not None else ''
        filtres.append(f'[{k}:a]aresample=48000,aformat=channel_layouts=stereo{fondu},adelay={ms}|{ms},volume={gain}[{lab}{k}]')
        return f'[{lab}{k}]'
    for v in plan['voix']:
        voix.append(entree(v['src'], v['at'], GAINS['voix'], 'v', v['ss'], v['dur']))
    for s in plan['sfx']:
        sfx.append(entree(os.path.join(SFX_DIR, s['id'] + '.mp3'), s['at'], GAINS['sfx'] * (0.8 if s['id'] in ('tic', 'blip') else 1), 's'))
    filtres.append(f'{"".join(voix)}amix=inputs={len(voix)}:normalize=0,apad,atrim=0:{total},loudnorm=I={VOIX_LUFS}:TP=-3:LRA=11,aresample=48000[vox]')
    filtres.append(f'{"".join(sfx)}amix=inputs={len(sfx)}:normalize=0,apad,atrim=0:{total}[sfx]')
    bus = ['[voxa]', '[sfx]']
    if musique:
        k = nb[0]; nb[0] += 1; entrees.extend(['-stream_loop', '-1', '-i', musique])
        filtres.append('[vox]asplit=2[voxa][voxk]')
        filtres.append(f'[{k}:a]aresample=48000,aformat=channel_layouts=stereo,atrim=0:{total},loudnorm=I={MUSIQUE_LUFS}:TP=-9:LRA=7,aresample=48000,'
                       f'afade=t=in:d=0.3,afade=t=out:st={max(0, total - 1.0)}:d=1.0[mus]')
        filtres.append('[mus][voxk]sidechaincompress=threshold=0.02:ratio=6:attack=30:release=500:makeup=1[musd]')
        bus.append('[musd]')
    else:
        filtres.append('[vox]anull[voxa]')
    filtres.append(f'{"".join(bus)}amix=inputs={len(bus)}:normalize=0,atrim=0:{total},afade=t=out:st={max(0, total - 0.3)}:d=0.3,'
                   f'loudnorm=I=-14:TP=-1.5:LRA=11,aresample=48000[out]')
    r = subprocess.run(['ffmpeg', '-y', '-loglevel', 'error'] + entrees + ['-filter_complex', ';'.join(filtres), '-map', '[out]',
                        '-c:a', 'aac', '-b:a', '192k', '-t', str(total), sortie_m4a], capture_output=True, text=True)
    if r.returncode:
        raise SystemExit('mixage ffmpeg : ' + r.stderr[-800:])


def mesure(f):
    r = subprocess.run(['ffmpeg', '-hide_banner', '-i', f, '-af', 'loudnorm=print_format=json', '-f', 'null', '-'], capture_output=True, text=True).stderr
    m = json.loads(r[r.rindex('{'):r.rindex('}') + 1])
    return float(m['input_i']), float(m['input_tp'])


# ---------------------------------------------------------------- rendu
PAGE = """<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:"Bricolage Grotesque";src:url(bricolage-grotesque-latin.woff2) format("woff2");font-weight:200 800}
@font-face{font-family:"Figtree";src:url(figtree-latin.woff2) format("woff2");font-weight:300 900}
html,body{margin:0;background:%(bg)s}#root{position:relative;width:1080px;height:1920px;overflow:hidden;background:%(bg)s}
</style>
<script src="react.production.min.js"></script><script src="react-dom.production.min.js"></script>
<script>window.TWEAK_DEFAULTS=%(tw)s;window.OM_SCENES=%(scenes)s;window.OM_PLAYBACK='{"mode":"loop"}';window.PUB_AUDIO='{}';window.PUB_OFFRE_LIGNE=%(offre)s;</script>
%(scripts)s
</head><body><div id="root"></div><script>
(function(){
  var d = ccDerive(JSON.parse(window.OM_SCENES)); var tw = window.TWEAK_DEFAULTS; var setT = null;
  function H(){ var s = React.useState(0); setT = s[1];
    return React.createElement(TimelineContext.Provider, {value:{time:s[0],duration:d.total,playing:false}},
      React.createElement(CompositionClock, {derived:d, cues:d.table}, React.createElement(window.%(piece)s, {tw:tw}))); }
  var root = ReactDOM.createRoot(document.getElementById('root'));
  ReactDOM.flushSync(function(){ root.render(React.createElement(H)); });
  window.__setT = function(t){ ReactDOM.flushSync(function(){ setT(t); }); };
  window.__textes = function(){ var out = [], w = document.createTreeWalker(document.getElementById('root'), NodeFilter.SHOW_ELEMENT);
    var n; while((n = w.nextNode())){ if (!n.children.length || [].some.call(n.childNodes, function(c){return c.nodeType===3 && c.textContent.trim();})) {
      var cs = getComputedStyle(n), r = n.getBoundingClientRect();
      var vis = cs.visibility !== 'hidden' && r.width > 0 && r.height > 0;
      for (var p = n; p && vis; p = p.parentElement){ var c = getComputedStyle(p); if (c.visibility==='hidden' || parseFloat(c.opacity) < 0.05) vis = false; }
      var t = n.innerText || n.textContent; if (/^fiches?$/i.test((t||'').trim())) { var q = n.parentElement; for (var u = 0; u < 3 && q && q.innerText.trim().split(/\\s+/).length < 3; u++) q = q.parentElement; if (q) t = q.innerText; } if (vis && t && t.trim()) out.push({t:t.replace(/\\s+/g,' ').trim(), l:r.left, r:r.right}); } }
    return out; };
  window.__ok = true;
})();
</script></body></html>"""


def rendre(brief_f, sortie, variante='A', muet=False, fps=30):
    from playwright.sync_api import sync_playwright
    from PIL import Image
    b = json.load(open(brief_f, encoding='utf-8'))
    pb = probs_brief(b, os.path.basename(brief_f))
    if pb:
        raise SystemExit('brief refusé :\n' + '\n'.join(pb))
    m = SKILLS[b['moteur']]
    if not os.path.exists(os.path.join(WORK, b['moteur'], 'p4-kit.js')):
        raise SystemExit('lancer d\'abord : python3 outils/pub-video.py installer')
    if muet:
        plan = {'scenes': [{'name': s, 'dur': n, 'nat': n, 'start': sum(x for _, x in NAT[:i])} for i, (s, n) in enumerate(NAT)], 'total': 15.0, 'voix': [], 'sfx': []}
    else:
        plan = caler(b, variante)
    if plan['total'] > PLAFOND + 0.01:
        raise SystemExit(f'durée {plan["total"]} s > {PLAFOND} s : raccourcir la ligne de voix la plus longue et la régénérer')
    acc = b['accroches'][1 if variante == 'B' and len(b['accroches']) > 1 else 0]
    tw = {'angle': b['angle'], 'metier': b['metier'], 'ville': b['ville'], 'preuve': False, 'motionEditor': False}
    if b['moteur'] == 'cinetique':
        tw.update(valeur=b.get('valeur', ''), accroche=acc)
    elif b['moteur'] == 'plan-sequence':
        tw.update(entreprise=b.get('entreprise', ''), lieu=b.get('lieu', ''), accroche=acc)
    else:
        tw.update(entreprise=b.get('entreprise', ''))
    scenes_js = [{'name': s['name'], 'dur': s['dur'], 'nat': s['nat']} for s in plan['scenes']]
    scripts = '\n'.join(f'<script src="{b["moteur"]}/{f[:-4]}.js"></script>' for f in m['fichiers'])
    page = os.path.join(WORK, f'page-{os.getpid()}.html')
    open(page, 'w', encoding='utf-8').write(PAGE % {'bg': m['bg'], 'tw': json.dumps(tw, ensure_ascii=False),
                                                     'scenes': json.dumps(json.dumps(scenes_js)), 'scripts': scripts, 'piece': m['piece'],
                                                     'offre': json.dumps(b.get('offre_ligne') or '', ensure_ascii=False)})
    sortie = os.path.abspath(sortie)
    os.makedirs(os.path.dirname(sortie), exist_ok=True)
    total = plan['total']
    n = int(math.ceil(total * fps))
    sc = {s['name']: s for s in plan['scenes']}
    planche_t = [0, sc['Accroche']['dur'] - 0.4, sc['Probleme']['start'] + sc['Probleme']['dur'] * 0.6, sc['Bascule']['start'] + 0.6 * sc['Bascule']['dur'] * 0.5,
                 sc['Bascule']['start'] + sc['Bascule']['dur'] * 0.85, total - 0.4]
    cibles = {min(n - 1, round(t * fps)) for t in planche_t}
    textes, deborde, planche, erreurs = {}, set(), [], []
    video = sortie[:-4] + '.video.mp4'
    ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', str(fps), '-i', '-',
                           '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', str(fps),
                           '-movflags', '+faststart', video], stdin=subprocess.PIPE)
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page(viewport={'width': 1080, 'height': 1920})
        pg.on('pageerror', lambda e: erreurs.append(str(e)))
        pg.goto('file://' + page)
        pg.wait_for_function('window.__ok === true', timeout=30000)
        pg.evaluate('Promise.all([document.fonts.load("700 80px \\"Bricolage Grotesque\\""), document.fonts.load("600 40px Figtree"), document.fonts.load("800 40px Figtree")])')
        pg.evaluate('document.fonts.ready')
        pg.evaluate('window.__setT(0.001)')
        if erreurs:
            raise SystemExit('erreur JavaScript : ' + erreurs[0])
        for i in range(n):
            t = i / fps
            pg.evaluate(f'window.__setT({t})')
            img = pg.screenshot(type='png', clip={'x': 0, 'y': 0, 'width': 1080, 'height': 1920})
            ff.stdin.write(img)
            if i % max(1, fps // 4) == 0 or i in cibles:
                for e in pg.evaluate('window.__textes()'):
                    textes.setdefault(e['t'], round(t, 2))
                    if t < sc['Accroche']['dur'] - 0.1 and (e['l'] < -2 or e['r'] > 1082): deborde.add(e['t'])
            if i in cibles:
                tmp = os.path.join(WORK, f'f{os.getpid()}-{i}.png'); open(tmp, 'wb').write(img); planche.append(tmp)
        br.close()
    ff.stdin.close(); ff.wait()
    os.remove(page)
    if ff.returncode:
        raise SystemExit('ffmpeg a échoué')
    pl = Image.new('RGB', (3 * 360 + 40, 2 * 640 + 30), '#888888')
    for k, f in enumerate(sorted(planche, key=lambda x: int(x.rsplit('-', 1)[1][:-4]))):
        pl.paste(Image.open(f).convert('RGB').resize((360, 640)), (10 + (k % 3) * 370, 10 + (k // 3) * 650)); os.remove(f)
    pl_f = sortie[:-4] + '-planche.png'
    pl.save(pl_f)
    pb = []
    for t, at in textes.items():
        pb += problemes_ecran(t, f'à l\'écran vers {at} s « {t[:60]} »') + regles_texte.fiche_seule(t, f'à l\'écran vers {at} s « {t[:60]} »')
    acc_nu = acc.replace('*', '')
    mots_acc = set(re.findall(r"[\w'’?]+", acc_nu))
    pb += [f'accroche qui déborde de l\'image « {t[:60]} »' for t in deborde if t in mots_acc or t in acc_nu]
    if muet:
        os.replace(video, sortie)
    else:
        musique = None
        if b.get('musique', True):
            musique = os.path.join(MUSIQUE_DIR, f'ambiance-{b.get("ambiance", 0)}.mp3')
            if not os.path.exists(musique):
                pb.append(f'musique de banque absente ({os.path.relpath(musique, REPO)}) : rendu sans musique'); musique = None
        m4a = sortie[:-4] + '.son.m4a'
        mixer(plan, b, m4a, musique)
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', video, '-i', m4a, '-map', '0:v:0', '-map', '1:a:0', '-c:v', 'copy', '-c:a', 'copy',
                        '-shortest', '-movflags', '+faststart', sortie], check=True)
        os.remove(video); os.remove(m4a)
        lu, tp = mesure(sortie)
        if abs(lu + 14) > 1.5: pb.append(f'niveau sonore {lu:.1f} LUFS (cible -14)')
        if tp > -0.9: pb.append(f'crête {tp:.1f} dB (max -1)')
    rapport = {'video': sortie, 'planche': pl_f, 'variante': variante, 'accroche': acc, 'duree': total, 'calage': plan,
               'textes_affiches': sorted(textes), 'problemes': pb}
    json.dump(rapport, open(sortie[:-4] + '-rapport.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    if pb:
        print('RENDU REFUSÉ (vidéo à ne pas publier) :\n' + '\n'.join(pb))
        return 1
    print(f'vidéo OK : {sortie} ({total:.1f} s, ' + ('muette' if muet else 'voix + bruitages' + (' + musique de fond' if b.get('musique', True) else '')) + ')')
    print(f'planche à regarder : {pl_f}\n{len(textes)} textes affichés contrôlés (règles n°1-2-3-5)')
    return 0


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a: raise SystemExit(__doc__)
    def opt(k, d=None):
        return a[a.index(k) + 1] if k in a else d
    c = a[0]
    if c == 'installer':
        installer()
    elif c == 'tirage':
        tirage(a[1], [x.strip() for x in opt('--metiers', '').split(',') if x.strip()], int(opt('--par-jour', 1)), opt('--sortie'), opt('--eviter'))
    elif c == 'valider':
        sys.exit(valider([x for x in a[1:] if x.endswith('.json')]))
    elif c in ('prise', 'lignes'):
        b = json.load(open(a[1], encoding='utf-8')); v = opt('--variante', 'A'); id_ = id_prise(v)
        etat = 'déjà téléchargée' if os.path.exists(os.path.join(dossier_audio(b), id_ + '.mp3')) else ('déjà notée' if id_ in (b.get('audio_src') or {}) else 'à générer')
        print(f'id : {id_} ({etat})\nvoice_id : {VOIX_ID} ({VOIX_NOM})\nmodel_id : {VOIX_MODELE}\ngenerations_count : 1\nprompt :')
        print(texte_prise(b, v))
    elif c == 'noter':
        noter(a[1], a[2], a[3], a[4])
    elif c == 'telecharger':
        sys.exit(telecharger([x for x in a[1:] if x.endswith('.json')]))
    elif c == 'caler':
        p = caler(json.load(open(a[1], encoding='utf-8')), opt('--variante', 'A'))
        print('scènes : ' + ' · '.join(f"{s['name']} {s['dur']} s" for s in p['scenes']) + f"  → total {p['total']} s")
        for v in p['voix']: print(f"  {v['at']:6.2f} → {v['fin']:6.2f}  {v['id']:<14} {v['texte']}")
    elif c == 'rendre':
        sys.exit(rendre(a[1], a[2], opt('--variante', 'A'), '--muet' in a, int(opt('--fps', 30))))
    else:
        raise SystemExit(__doc__)
