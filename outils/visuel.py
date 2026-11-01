"""Visuels Proenligne : 3 gabarits + carrousel. Format 1080 × 1350 (4:5), accepté par Instagram, Facebook et LinkedIn.

usage : python3 outils/visuel.py <brief.json> <sortie.png>            → une image (gabarit selon "gabarit")
        python3 outils/visuel.py <brief.json> <dossier/> --carrousel   → dossier/01.png … 0N.png (3 à 5 slides)

brief.json (champs communs) :
  "gabarit": "avant-apres" | "conseil" | "question"     (défaut : avant-apres)
  "surtitre": ≤ 60 car.  "titre": ≤ 60 car.  "mot": morceau exact de "titre" surligné en vert
  "cta": "offre" | "question" | "aucun"    offre = bouton « Essayez gratuitement » ; question = une question en bas ; aucun = rien
  "question": texte de la question si cta = question (≤ 90)
  Règles : surtitre + titre contiennent « Google » ; aucun prix nulle part.

Gabarit avant-apres : "carte": {"enseigne": FICTIF (métier + Weber/Martin/Durand/Bernard/Petit), "metier", "avant" ≤ 34, "apres" ≤ 34}
Gabarit conseil     : "points": 2 à 3 phrases courtes (≤ 70 car.) — une astuce concrète, chaque point commence par un verbe
Gabarit question    : "reponses": 2 à 3 propositions (≤ 40 car.) — un test / sondage ; la bonne est marquée par "bonne": index

Carrousel ("slides", 3 à 5) : la 1re slide = le brief ci-dessus (accroche), les suivantes :
  {"type": "point", "numero": "1", "titre": ≤ 40, "texte": ≤ 120}   une idée par slide
  {"type": "fin", "titre": ≤ 40, "texte": ≤ 120}                     dernière : question ou conclusion (jamais de prix)
"""
import base64, html, json, os, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(ICI, 'assets')
PRIX = re.compile(r'€|\bmois\b|centime|euro', re.I)
GABARITS = ('avant-apres', 'conseil', 'question')


def b64(nom):
    return base64.b64encode(open(os.path.join(A, nom), 'rb').read()).decode()


def verifier(b):
    err = []
    g = b.get('gabarit', 'avant-apres')
    if g not in GABARITS: err.append(f'gabarit inconnu « {g} »')
    for k, n in (('surtitre', 60), ('titre', 60), ('question', 90)):
        if len(b.get(k, '') or '') > n: err.append(f'{k} > {n} caractères')
    if b.get('mot') and b['mot'] not in b.get('titre', ''): err.append('"mot" doit être un morceau exact de "titre"')
    if 'google' not in (b.get('surtitre', '') + ' ' + b.get('titre', '')).lower():
        err.append('le surtitre ou le titre doit dire « fiche Google » (règle n°1)')
    if PRIX.search(json.dumps(b, ensure_ascii=False)): err.append('aucun prix ne doit apparaître (règle : essai gratuit, sans prix)')
    if b.get('cta', 'offre') not in ('offre', 'question', 'aucun'): err.append('cta inconnu')
    if b.get('cta') == 'question' and not b.get('question'): err.append('cta question sans "question"')
    if g == 'avant-apres':
        c = b.get('carte') or {}
        for k in ('enseigne', 'metier', 'avant', 'apres'):
            if not c.get(k): err.append(f'carte.{k} manquant')
        for k in ('avant', 'apres'):
            if len(c.get(k, '')) > 34: err.append(f'carte.{k} > 34 caractères')
    if g == 'conseil':
        pts = b.get('points') or []
        if not 2 <= len(pts) <= 3: err.append('conseil : 2 à 3 points')
        if any(len(p) > 70 for p in pts): err.append('un point > 70 caractères')
    if g == 'question':
        r = b.get('reponses') or []
        if not 2 <= len(r) <= 3: err.append('question : 2 à 3 réponses')
        if any(len(x) > 40 for x in r): err.append('une réponse > 40 caractères')
    for i, s in enumerate(b.get('slides') or [], 2):
        if s.get('type') not in ('point', 'fin'): err.append(f'slide {i} : type inconnu')
        if len(s.get('titre', '')) > 40 or len(s.get('texte', '')) > 120: err.append(f'slide {i} : titre > 40 ou texte > 120')
    if b.get('slides') and not 2 <= len(b['slides']) <= 4: err.append('carrousel : 3 à 5 slides au total')
    return err


CSS = """
@font-face{font-family:B;src:url(data:font/woff2;base64,__B__) format('woff2');font-weight:200 800}
@font-face{font-family:F;src:url(data:font/woff2;base64,__F__) format('woff2');font-weight:300 900}
*{box-sizing:border-box;margin:0}
body{width:1080px;height:1350px;background:#f6f7f4;color:#16201b;font-family:F;position:relative;overflow:hidden}
.halo{position:absolute;left:190px;top:640px;width:700px;height:900px;border-radius:350px;background:#e7f0ea}
.wrap{position:relative;padding:80px 80px 0}
.marque{display:flex;align-items:center;gap:16px;font-size:30px;font-weight:600}
.marque img{width:44px;height:44px}
.sur{margin-top:36px;font-size:38px;color:#3b4740;line-height:1.2}
h1{font-family:B;font-weight:700;font-size:84px;line-height:1.02;letter-spacing:-2px;margin-top:22px}
h1.petit{font-size:72px}
mark{background:linear-gradient(transparent 62%,#cfe3d6 62%);color:#1f6b4a;padding:0 4px}
.cta{display:flex;align-items:center;gap:24px;margin-top:44px;flex-wrap:wrap}
.btn{background:#1f6b4a;color:#fff;font-weight:700;font-size:32px;padding:20px 30px;border-radius:14px}
.mention{font-size:28px;color:#3b4740}
.q{font-family:B;font-weight:600;font-size:40px;color:#1f6b4a;margin-top:44px;line-height:1.15}
.carte{position:absolute;left:150px;right:150px;bottom:110px;background:#fff;border-radius:32px;padding:40px 44px;
  box-shadow:0 30px 60px rgba(22,32,27,.10);border:3px solid #1f6b4a}
.lab{font-size:22px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#1f6b4a;margin-bottom:10px}
.ent{font-family:B;font-weight:700;font-size:40px}
.met{font-size:26px;color:#5b665f;margin-top:6px}
.met b{color:#f2b63c}
.ligne{display:flex;align-items:center;gap:18px;font-size:30px;margin-top:26px;padding:18px 22px;border-radius:16px}
.avant{background:#fdf4e0;color:#7a5a12;text-decoration:line-through;text-decoration-color:#c99422}
.apres{background:#e7f0ea;color:#1f6b4a;font-weight:600}
.pt{width:16px;height:16px;border-radius:50%;flex:none}
.avant .pt{background:#f2b63c} .apres .pt{background:#1f6b4a}
.badge{position:absolute;top:-26px;right:40px;background:#1f6b4a;color:#fff;font-weight:700;font-size:24px;padding:12px 20px;border-radius:30px}
.points{position:absolute;left:110px;right:110px;bottom:120px}
.point{display:flex;gap:26px;align-items:flex-start;background:#fff;border-radius:24px;padding:30px 34px;margin-top:22px;
  box-shadow:0 20px 40px rgba(22,32,27,.08);font-size:34px;line-height:1.25}
.num{font-family:B;font-weight:800;font-size:40px;color:#1f6b4a;min-width:52px}
.rep{display:flex;align-items:center;gap:22px;background:#fff;border:3px solid #e2e7e3;border-radius:22px;padding:28px 34px;margin-top:22px;font-size:34px}
.rep.bonne{border-color:#1f6b4a;background:#e7f0ea;font-weight:700}
.case{width:40px;height:40px;border-radius:12px;border:3px solid #9aa89f;flex:none}
.rep.bonne .case{background:#1f6b4a;border-color:#1f6b4a}
.slidenum{position:absolute;top:84px;right:80px;font-size:28px;color:#5b665f;font-weight:600}
.big{font-family:B;font-weight:800;font-size:200px;color:#cfe3d6;position:absolute;left:80px;top:300px;line-height:1}
h2{font-family:B;font-weight:700;font-size:76px;line-height:1.05;letter-spacing:-1.5px;margin-top:300px;position:relative}
.texte{font-size:40px;line-height:1.3;margin-top:40px;color:#3b4740;position:relative}
.fin h2{margin-top:260px;color:#1f6b4a}
.suivez{position:absolute;left:80px;bottom:110px;font-size:30px;color:#3b4740}
"""


def entete(b):
    t = html.escape(b['titre'])
    if b.get('mot'):
        m = html.escape(b['mot']); t = t.replace(m, f'<mark>{m}</mark>', 1)
    cta = b.get('cta', 'offre')
    if cta == 'offre':
        bas = '<div class="cta"><span class="btn">Essayez gratuitement</span><span class="mention">Sans engagement</span></div>'
    elif cta == 'question':
        bas = f'<p class="q">{html.escape(b["question"])}</p>'
    else:
        bas = ''
    petit = ' class="petit"' if len(b['titre']) > 48 else ''
    return f'''<div class="wrap"><div class="marque"><img src="data:image/svg+xml;base64,{b64('logo.svg')}">Proenligne</div>
<p class="sur">{html.escape(b['surtitre'])}</p><h1{petit}>{t}</h1>{bas}</div>'''


def corps(b):
    g = b.get('gabarit', 'avant-apres')
    if g == 'avant-apres':
        c = {k: html.escape(v) for k, v in b['carte'].items()}
        return f'''<div class="carte"><span class="badge">Fiche Google à jour</span><div class="lab">Votre fiche Google</div>
<div class="ent">{c['enseigne']}</div><div class="met"><b>★★★★★</b> · {c['metier']}</div>
<div class="ligne avant"><span class="pt"></span>{c['avant']}</div><div class="ligne apres"><span class="pt"></span>{c['apres']}</div></div>'''
    if g == 'conseil':
        return '<div class="points">' + ''.join(f'<div class="point"><span class="num">{i}</span><span>{html.escape(p)}</span></div>'
                                              for i, p in enumerate(b['points'], 1)) + '</div>'
    bonne = b.get('bonne')
    return '<div class="points">' + ''.join(f'<div class="rep{" bonne" if i == bonne else ""}"><span class="case"></span>{html.escape(r)}</div>'
                                          for i, r in enumerate(b['reponses'])) + '</div>'


def doc(inner):
    return f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS.replace("__B__", b64("bricolage-grotesque-latin.woff2")).replace("__F__", b64("figtree-latin.woff2"))}</style></head><body><div class="halo"></div>{inner}</body></html>'


def page(b):
    return doc(entete(b) + corps(b))


def page_slide(s, i, n):
    cls = 'fin' if s['type'] == 'fin' else ''
    num = f'<div class="big">{html.escape(str(s.get("numero", i - 1)))}</div>' if s['type'] == 'point' else ''
    return doc(f'''<div class="wrap {cls}"><div class="marque"><img src="data:image/svg+xml;base64,{b64('logo.svg')}">Proenligne</div>
<div class="slidenum">{i} / {n}</div>{num}<h2>{html.escape(s['titre'])}</h2><p class="texte">{html.escape(s['texte'])}</p></div>
<div class="suivez">{'Votre fiche Google, animée chaque semaine · Essayez gratuitement' if s['type'] == 'fin' else 'Proenligne · fiche Google'}</div>''')


def capture(htmls, sorties):
    from playwright.sync_api import sync_playwright
    pb = []
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page(viewport={'width': 1080, 'height': 1350})
        for h, out in zip(htmls, sorties):
            pg.set_content(h); pg.wait_for_timeout(250)
            deb = pg.evaluate("""() => [...document.querySelectorAll('h1,h2,.sur,.ligne,.btn,.ent,.point,.rep,.q,.texte')]
                .filter(e => e.scrollWidth > e.clientWidth + 1 || e.getBoundingClientRect().right > 1080 || e.getBoundingClientRect().bottom > 1350).length""")
            chev = pg.evaluate("""() => { const w = document.querySelector('.wrap'); const c = document.querySelector('.carte, .points');
                if (!w || !c) return false; return w.getBoundingClientRect().bottom > c.getBoundingClientRect().top - 30; }""")
            pg.screenshot(path=out)
            if deb or chev: pb.append(f'{os.path.basename(out)} : texte trop long (débordement={deb}, chevauchement={chev})')
        br.close()
    return pb


if __name__ == '__main__':
    if len(sys.argv) < 3: raise SystemExit(__doc__)
    b = json.load(open(sys.argv[1], encoding='utf-8'))
    e = verifier(b)
    if e: raise SystemExit('refusé : ' + ' ; '.join(e))
    if '--carrousel' in sys.argv:
        d = sys.argv[2]; os.makedirs(d, exist_ok=True)
        slides = b.get('slides') or []
        n = 1 + len(slides)
        htmls = [page(b)] + [page_slide(s, i, n) for i, s in enumerate(slides, 2)]
        outs = [os.path.join(d, f'{i:02d}.png') for i in range(1, n + 1)]
    else:
        os.makedirs(os.path.dirname(os.path.abspath(sys.argv[2])) or '.', exist_ok=True)
        htmls, outs = [page(b)], [sys.argv[2]]
    pb = capture(htmls, outs)
    if pb: raise SystemExit('ATTENTION : ' + ' ; '.join(pb))
    print('visuel OK :', ', '.join(outs))
