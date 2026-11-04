"""Pubs vidéo 9:16 de 15 s avec les skills « pub-cinetique-proenligne » et « pub-plan-sequence-proenligne », rendues en MP4
sans intervention (les skills d'origine s'exportent à la main depuis un panneau Réglages ; ce script fait le rendu image par
image avec Chromium et ffmpeg, et ajoute la bande-son originale de outils/son_pub.py).

Le moteur d'animation des skills n'est jamais réécrit : le dossier reference/ est copié, puis seuls des TEXTES fixes sont
corrigés pour respecter les règles du dépôt (n°1 « fiche Google », n°2 aucun prix, n°3 aucune statistique client,
n°5 aucun deux-points) : scène Offre « Essai gratuit, sans engagement » à la place du prix, preuve client toujours coupée,
« Dernière photo il y a 2 ans », heures écrites « 21h00 », « votre fiche » → « votre fiche Google ». Au rendu, TOUT le texte
réellement affiché est relevé image par image et passé dans cerveau/regles_texte.py : un seul problème = rendu refusé.

usage :
  python3 outils/pub-video.py installer
      prépare /home/claude/pub-video-work (react, esbuild, playwright, copies adaptées des 2 skills). Une fois par session.
  python3 outils/pub-video.py tirage <lundi> --metiers m1,m2,…,m7
      propose pour les 7 vidéos 19:00 de la semaine (lundi → dimanche) le moteur, l'angle, la ville et l'ambiance sonore,
      en rotation et sans répéter la semaine précédente (suivi/historique-pubs.json). Écrit suivi/plan/<lundi>-videos.json.
  python3 outils/pub-video.py valider <brief.json> [<brief.json> …]
      contrôle les briefs (champs, longueurs, règles de texte). Doit répondre « briefs OK ».
  python3 outils/pub-video.py rendre <brief.json> <sortie.mp4> [--variante A|B] [--ambiance 0|1|2] [--muet] [--fps 30]
      rend la vidéo, écrit à côté <sortie>-planche.png (6 images : 0 / 2,5 / 4,5 / 8,5 / 11 / 14 s) À REGARDER avant usage.

Format d'un brief vidéo (suivi/briefs/<lundi>/<slug>.json ; le slug est celui du créneau 19:00 du plan) :
  {
    "slug": "plombier-classement-lorient",
    "moteur": "cinetique" | "plan-sequence",
    "angle": "Plus de clients" | "Face au concurrent" | "Du temps libre" | "Plus d'appels",
    "metier": "plombier",               (minuscules ; au féminin si l'usage le veut : coiffeuse, esthéticienne)
    "ville": "Lorient",
    "valeur": "37",                     (cinétique seulement : la grosse valeur jaune de la 1re image, ≤ 5 caractères,
                                         ≤ 18 pour l'angle concurrent ; heure écrite « 23h14 », jamais « 23:14 »)
    "entreprise": "",                   (plan-séquence seulement ; vide = « Votre entreprise »)
    "lieu": "",                         (plan-séquence, angle temps ; vide = déduit du métier)
    "accroches": ["accroche A", "accroche B"],   (A = vidéo du créneau, B = variante A/B ; *mots* = mis en avant)
    "ambiance": 0 | 1 | 2
  }
Accroche : une vraie phrase, vouvoiement, contient « Google » (de préférence « fiche Google »), aucun « : », aucun prix,
aucun résultat chiffré. Longueur ≤ 60 caractères (≤ 26 pour plan-séquence + « Plus de clients », qui s'affiche en très gros).
"""
import glob, json, os, re, shutil, subprocess, sys, tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(ICI)
sys.path.insert(0, os.path.join(REPO, 'cerveau'))
sys.path.insert(0, ICI)
import regles_texte  # noqa: E402

WORK = os.environ.get('PUB_VIDEO_WORK', '/home/claude/pub-video-work')
SKILLS = {
    'cinetique': {'nom': 'pub-cinetique-proenligne', 'piece': 'P4Piece', 'bg': '#16201b',
                  'fichiers': ['animations-v3.jsx', 'tweaks-panel.jsx', 'p4-kit.jsx', 'p4-angles.jsx', 'Pub4AnglesVideo.jsx']},
    'plan-sequence': {'nom': 'pub-plan-sequence-proenligne', 'piece': 'PSPiece', 'bg': '#f6f7f4',
                      'fichiers': ['animations-v3.jsx', 'tweaks-panel.jsx', 'p4-kit.jsx', 'ps-kit.jsx', 'ps-angles.jsx', 'PubPlanSequenceVideo.jsx']},
}
RACINES = ['/mnt/skills/plugins', '/mnt/skills/user', '/mnt/skills/public', '/mnt/skills/examples', os.path.expanduser('~/.claude/skills')]
ANGLES = ['Plus de clients', 'Face au concurrent', 'Du temps libre', "Plus d'appels"]
SCENES = [{'name': 'Accroche', 'dur': 3}, {'name': 'Probleme', 'dur': 4}, {'name': 'Bascule', 'dur': 5}, {'name': 'Offre', 'dur': 3}]
SANS_SOIREES = {'boulangerie', 'boulanger', 'restaurant'}  # « Du temps libre » peu crédible : autre angle
PLANCHE_T = [0, 2.5, 4.5, 8.5, 11, 14]

# Textes fixes des skills corrigés pour les règles du dépôt (le moteur n'est pas touché)
REMPLACEMENTS = [
    ("'14,99 €'", "'Essai gratuit'"), ('>14,99 €<', '>Essai gratuit<'),
    ('/ mois, sans engagement', 'sans engagement'),
    ('Dernière photo : il y a 2 ans', 'Dernière photo il y a 2 ans'),
    ('Nouvelle photo : lundi', 'Nouvelle photo lundi'),
    ('Publication : jeudi', 'Publication jeudi'),
    ('dernière photo : 2021', 'dernière photo en 2021'),
    ('Publications ce mois', 'Publications récentes'),
    ("Cas client O'propre, Rennes : ×3 appels par mois.", ''),
    ("Cas client O\\'propre, Rennes : ×3 appels par mois.", ''),
    ('À fiche égale,', 'À fiche Google aussi vivante,'),
    ('votre fiche Google *réclame :*', 'votre fiche Google *vous réclame tout ça.*'),
]
TEXTES_DECOR = ('p4-angles.jsx', 'ps-angles.jsx', 'p4-kit.jsx', 'ps-kit.jsx')  # fichiers dont les textes s'affichent
DEPENDANCES = 'react@18.3.1 react-dom@18.3.1 esbuild@0.23.1'


def trouver_skill(nom):
    for r in RACINES:
        p = os.path.join(r, nom, 'reference')
        if os.path.isdir(p):
            return p
    hits = glob.glob(f'/mnt/skills/**/{nom}/reference', recursive=True)
    if hits:
        return hits[0]
    raise SystemExit(f'skill {nom} introuvable (cherché dans {", ".join(RACINES)})')


def adapter_textes(js, nom):
    for a, b in REMPLACEMENTS:
        js = js.replace(a, b)
    js = re.sub(r"(['>])(\d{1,2}):(\d{2})(['<])", r'\1\2h\3\4', js)                                  # '21:00' → '21h00'
    if nom in TEXTES_DECOR:
        js = re.sub(r"\b([Ff]iches?)\b(?! Google)", r'\1 Google', js)   # visuels : toujours « fiche Google »
    return js


def controler_decor(js, nom):
    """Textes fixes restants (chaînes et texte JSX) passés dans les règles : rien ne doit rester."""
    pb = []
    for m in re.finditer(r"'((?:[^'\\\n]|\\.)*)'|\"((?:[^\"\\\n]|\\.)*)\"|>([^<>{}\n]+)<", js):
        t = next(g for g in m.groups() if g is not None)
        if not re.search(r'[A-Za-zÀ-ÿ]{3,} [A-Za-zÀ-ÿ]', t):
            continue  # code (styles, clés), pas du texte affiché
        pb += regles_texte.problemes(t, f'{nom} « {t[:50]} »') + regles_texte.fiche_seule(t, f'{nom} « {t[:50]} »')
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
    print(f'prêt : {WORK} (cinétique ← {trouver_skill(SKILLS["cinetique"]["nom"])}, plan-séquence ← {trouver_skill(SKILLS["plan-sequence"]["nom"])})')


# ---------------------------------------------------------------- tirage
def tirage(lundi, metiers):
    import datetime as dt
    hist = []
    p = os.path.join(REPO, 'suivi', 'historique-pubs.json')
    if os.path.exists(p):
        hist = [h for h in json.load(open(p, encoding='utf-8')) if h.get('moteur')]
    hist.sort(key=lambda h: h.get('date', ''))
    villes = json.load(open(os.path.join(REPO, 'suivi', 'villes-pubs.json'), encoding='utf-8'))['villes']

    def recence(cle, valeurs):  # valeur la moins récemment utilisée d'abord
        dern = {v: -1 for v in valeurs}
        for i, h in enumerate(hist):
            if h.get(cle) in dern: dern[h[cle]] = i
        return sorted(valeurs, key=lambda v: (dern[v], valeurs.index(v)))

    moteur = 'plan-sequence' if (hist and hist[-1]['moteur'] == 'cinetique') else 'cinetique'
    ordre_angles = recence('angle', ANGLES)
    ordre_villes = recence('ville', villes)
    dern_amb = hist[-1].get('ambiance') if hist else None
    out, angles_sem = [], []
    j0 = dt.date.fromisoformat(lundi)
    for i, metier in enumerate(metiers):
        cands = [a for a in ordre_angles + ordre_angles if a not in angles_sem[-1:]]
        if metier.lower() in SANS_SOIREES:
            cands = [a for a in cands if a != 'Du temps libre']
        compte = {a: angles_sem.count(a) for a in ANGLES}
        angle = min(cands, key=lambda a: (compte[a], cands.index(a)))
        angles_sem.append(angle)
        amb = (i + (0 if dern_amb is None else dern_amb + 1)) % 3
        out.append({'date': (j0 + dt.timedelta(days=i)).isoformat(), 'moteur': moteur, 'angle': angle,
                    'metier': metier.lower(), 'ville': ordre_villes[i % len(ordre_villes)], 'ambiance': amb})
        moteur = 'cinetique' if moteur == 'plan-sequence' else 'plan-sequence'
    f = os.path.join(REPO, 'suivi', 'plan', f'{lundi}-videos.json')
    json.dump(out, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for o in out:
        print(f"{o['date']}  {o['moteur']:<13} {o['angle']:<19} {o['metier']:<14} {o['ville']:<14} ambiance {o['ambiance']}")
    print(f'→ {os.path.relpath(f, REPO)}')
    return out


# ---------------------------------------------------------------- validation
def probs_brief(b, nom=''):
    pb, ou = [], (b.get('slug') or nom)
    m = b.get('moteur')
    if m not in SKILLS: pb.append(f'{ou} : moteur « {m} » inconnu (cinetique | plan-sequence)')
    if b.get('angle') not in ANGLES: pb.append(f'{ou} : angle « {b.get("angle")} » inconnu ({" | ".join(ANGLES)})')
    for k in ('slug', 'metier', 'ville'):
        if not (b.get(k) or '').strip(): pb.append(f'{ou} : champ {k} vide')
    acc = b.get('accroches') or []
    if not acc: pb.append(f'{ou} : aucune accroche')
    lim = 26 if (m == 'plan-sequence' and b.get('angle') == 'Plus de clients') else 60
    for i, a in enumerate(acc):
        lab = f'{ou} accroche {"ABC"[i] if i < 3 else i}'
        nu = a.replace('*', '')
        if len(nu) > lim: pb.append(f'{lab} : {len(nu)} caractères (max {lim})')
        if 'google' not in nu.lower(): pb.append(f'{lab} : sans « Google »')
        if a.count('*') % 2: pb.append(f'{lab} : astérisques * non appariés')
        pb += regles_texte.problemes(nu, lab)
        pb += regles_texte.phrase_complete(nu, lab)
        pb += regles_texte.fiche_seule(nu, lab)
    if m == 'cinetique':
        v = (b.get('valeur') or '').strip()
        lv = 18 if b.get('angle') == 'Face au concurrent' else 5
        if len(v) > lv: pb.append(f'{ou} valeur : « {v} » trop long (max {lv})')
        pb += regles_texte.problemes(v, f'{ou} valeur')
    if m == 'plan-sequence':
        if len(b.get('metier', '') + b.get('ville', '')) > 28: pb.append(f'{ou} : métier + ville > 28 caractères')
        if len(b.get('entreprise') or '') > 24: pb.append(f'{ou} entreprise : > 24 caractères')
    for k in ('entreprise', 'lieu', 'ville', 'metier'):
        pb += regles_texte.problemes(b.get(k) or '', f'{ou} {k}') + regles_texte.fiche_seule(b.get(k) or '', f'{ou} {k}')
    if b.get('ambiance') not in (0, 1, 2, None): pb.append(f'{ou} ambiance : 0, 1 ou 2')
    return pb


def valider(fichiers):
    pb = []
    for f in fichiers:
        pb += probs_brief(json.load(open(f, encoding='utf-8')), os.path.basename(f))
    print('\n'.join(pb) if pb else 'briefs OK')
    return 1 if pb else 0


# ---------------------------------------------------------------- rendu
PAGE = """<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:"Bricolage Grotesque";src:url(bricolage-grotesque-latin.woff2) format("woff2");font-weight:200 800}
@font-face{font-family:"Figtree";src:url(figtree-latin.woff2) format("woff2");font-weight:300 900}
html,body{margin:0;background:%(bg)s}#root{position:relative;width:1080px;height:1920px;overflow:hidden;background:%(bg)s}
</style>
<script src="react.production.min.js"></script><script src="react-dom.production.min.js"></script>
<script>window.TWEAK_DEFAULTS=%(tw)s;window.OM_SCENES=%(scenes)s;window.OM_PLAYBACK='{"mode":"loop"}';</script>
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
      var cs = getComputedStyle(n), r = n.getBoundingClientRect(), o = parseFloat(cs.opacity);
      var vis = cs.visibility !== 'hidden' && r.width > 0 && r.height > 0;
      for (var p = n; p && vis; p = p.parentElement){ var c = getComputedStyle(p); if (c.visibility==='hidden' || parseFloat(c.opacity) < 0.05) vis = false; }
      var t = n.innerText || n.textContent; if (/^fiches?$/i.test((t||'').trim())) { var q = n.parentElement; for (var u = 0; u < 3 && q && q.innerText.trim().split(/\\s+/).length < 3; u++) q = q.parentElement; if (q) t = q.innerText; } if (vis && t && t.trim()) out.push({t:t.replace(/\\s+/g,' ').trim(), l:r.left, r:r.right}); } }
    return out; };
  window.__ok = true;
})();
</script></body></html>"""


def sons_pour(angle):
    base = [['apparition', 'Accroche', 0.05], ['balayage', 'Probleme', 0.0], ['balayage', 'Bascule', 0.0], ['pop', 'Bascule', 0.9],
            ['pop', 'Bascule', 1.4], ['victoire', 'Offre', 0.3], ['clic', 'Offre', 1.6]]
    if angle == "Plus d'appels":
        base += [['notif', 'Bascule', 3.0], ['notif', 'Bascule', 3.3], ['notif', 'Bascule', 3.6]]
    elif angle == 'Face au concurrent':
        base += [['alerte', 'Probleme', 1.2], ['notif', 'Bascule', 3.2]]
    elif angle == 'Du temps libre':
        base += [['frappe', 'Probleme', 0.6, 2.2], ['pop', 'Bascule', 2.4]]
    else:
        base += [['alerte', 'Probleme', 1.6], ['notif', 'Bascule', 3.4]]
    return base


def rendre(brief_f, sortie, variante='A', ambiance=None, muet=False, fps=30):
    from playwright.sync_api import sync_playwright
    from PIL import Image
    b = json.load(open(brief_f, encoding='utf-8'))
    pb = probs_brief(b, os.path.basename(brief_f))
    if pb:
        raise SystemExit('brief refusé :\n' + '\n'.join(pb))
    m = SKILLS[b['moteur']]
    if not os.path.exists(os.path.join(WORK, b['moteur'], 'p4-kit.js')):
        raise SystemExit('lancer d\'abord : python3 outils/pub-video.py installer')
    acc = b['accroches'][1 if variante == 'B' and len(b['accroches']) > 1 else 0]
    tw = {'angle': b['angle'], 'metier': b['metier'], 'ville': b['ville'], 'accroche': acc, 'preuve': False, 'motionEditor': False}
    if b['moteur'] == 'cinetique':
        tw['valeur'] = b.get('valeur', '')
    else:
        tw.update(entreprise=b.get('entreprise', ''), lieu=b.get('lieu', ''))
    scripts = '\n'.join(f'<script src="{b["moteur"]}/{f[:-4]}.js"></script>' for f in m['fichiers'])
    page = os.path.join(WORK, f'page-{os.getpid()}.html')
    open(page, 'w', encoding='utf-8').write(PAGE % {'bg': m['bg'], 'tw': json.dumps(tw, ensure_ascii=False),
                                                     'scenes': json.dumps(json.dumps(SCENES)), 'scripts': scripts, 'piece': m['piece']})
    sortie = os.path.abspath(sortie)
    os.makedirs(os.path.dirname(sortie), exist_ok=True)
    n = int(15 * fps)
    textes, deborde, planche = {}, set(), []
    erreurs = []
    ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', str(fps), '-i', '-',
                           '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-r', str(fps),
                           '-movflags', '+faststart', sortie], stdin=subprocess.PIPE)
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
        cibles = {round(t * fps) for t in PLANCHE_T}
        for i in range(n):
            t = i / fps
            pg.evaluate(f'window.__setT({t})')
            img = pg.screenshot(type='png', clip={'x': 0, 'y': 0, 'width': 1080, 'height': 1920})
            ff.stdin.write(img)
            if i % max(1, fps // 4) == 0 or i in cibles:
                for e in pg.evaluate('window.__textes()'):
                    textes.setdefault(e['t'], round(t, 2))
                    if t < 2.9 and (e['l'] < -2 or e['r'] > 1082): deborde.add(e['t'])
            if i in cibles:
                tmp = os.path.join(WORK, f'f{os.getpid()}-{i}.png'); open(tmp, 'wb').write(img); planche.append(tmp)
        br.close()
    ff.stdin.close(); ff.wait()
    os.remove(page)
    if ff.returncode:
        raise SystemExit('ffmpeg a échoué')
    # planche de contrôle 3 × 2
    pl = Image.new('RGB', (3 * 360 + 40, 2 * 640 + 30), '#888888')
    for k, f in enumerate(sorted(planche, key=lambda x: int(x.rsplit('-', 1)[1][:-4]))):
        pl.paste(Image.open(f).convert('RGB').resize((360, 640)), (10 + (k % 3) * 370, 10 + (k // 3) * 650)); os.remove(f)
    pl_f = sortie[:-4] + '-planche.png'
    pl.save(pl_f)
    # contrôle de tout le texte affiché
    pb = []
    for t, at in textes.items():
        pb += regles_texte.problemes(t, f'à l\'écran vers {at} s « {t[:60]} »')
        pb += regles_texte.fiche_seule(t, f'à l\'écran vers {at} s « {t[:60]} »')
    mots_acc = set(re.findall(r"[\w'’?]+", acc.replace('*', '')))
    pb += [f'accroche qui déborde de l\'image « {t[:60]} »' for t in deborde if t in mots_acc or t in acc.replace('*', '')]
    if not muet:
        sys.path.insert(0, ICI)
        os.environ['PUB_AMBIANCE'] = str(ambiance if ambiance is not None else b.get('ambiance', 0))
        import importlib, son_pub
        importlib.reload(son_pub)
        pa, _ = son_pub.bande_son(sons_pour(b['angle']), SCENES, [sortie])
        pb += pa
    rapport = {'video': sortie, 'planche': pl_f, 'variante': variante, 'accroche': acc, 'textes_affiches': sorted(textes), 'problemes': pb}
    json.dump(rapport, open(sortie[:-4] + '-rapport.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    if pb:
        print('RENDU REFUSÉ (vidéo à ne pas publier) :\n' + '\n'.join(pb))
        return 1
    print(f'vidéo OK : {sortie}\nplanche à regarder : {pl_f}\n{len(textes)} textes affichés contrôlés (règles n°1-2-3-5)')
    return 0


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a: raise SystemExit(__doc__)
    def opt(k, d=None):
        return a[a.index(k) + 1] if k in a else d
    if a[0] == 'installer':
        installer()
    elif a[0] == 'tirage':
        tirage(a[1], [x.strip() for x in opt('--metiers', '').split(',') if x.strip()])
    elif a[0] == 'valider':
        sys.exit(valider([x for x in a[1:] if x.endswith('.json')]))
    elif a[0] == 'rendre':
        amb = opt('--ambiance')
        sys.exit(rendre(a[1], a[2], opt('--variante', 'A'), None if amb is None else int(amb), '--muet' in a, int(opt('--fps', 30))))
    else:
        raise SystemExit(__doc__)
