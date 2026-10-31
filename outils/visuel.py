"""Visuel fixe Proenligne pour le créneau de 13h (Instagram + Facebook).

usage : python3 outils/visuel.py <brief.json> <sortie.png>

brief.json :
{
  "surtitre": "Un soir de fuite, on cherche sur Google.",  # ≤ 60 car., phrase d'amorce
  "titre": "On appelle la fiche Google la plus vivante.", # ≤ 60 car. ; surtitre + titre doivent contenir « Google »
  "mot": "la plus vivante",                              # morceau exact de "titre", surligné en vert
  "carte": {                                           # mini-fiche avant / après
    "enseigne": "Plomberie Weber",                     # FICTIF : métier + un nom de noms_fictifs du skill (Weber, Martin, Durand, Bernard, Petit)
    "metier": "Plombier",
    "avant": "Dernière photo : il y a 2 ans",          # ≤ 34 car., ligne ambre (le problème)
    "apres": "Nouvelle photo publiée lundi"            # ≤ 34 car., ligne verte (Proenligne)
  },
  "offre": "essai"                                     # essai | audit | unEuro | annuel
}
Format : 1080 × 1350 (4:5), accepté par Instagram et Facebook.
"""
import base64, html, json, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))
A = os.path.join(ICI, 'assets')

OFFRES = {
    'essai': ('Essayez dès 14,99 €/mois', 'Sans engagement'),
    'audit': ('Audit gratuit de votre fiche', 'Puis dès 14,99 €/mois'),
    'unEuro': ('Premier mois à 1 €', 'Puis 14,99 €/mois'),
    'annuel': ('99,99 € par an', 'Soit 8,33 €/mois'),
}
LIMITES = {'surtitre': 60, 'titre': 60}


def b64(nom):
    return base64.b64encode(open(os.path.join(A, nom), 'rb').read()).decode()


def verifier(b):
    err = []
    for k, n in LIMITES.items():
        if len(b.get(k, '')) > n:
            err.append(f'{k} > {n} caractères')
    if b.get('mot') and b['mot'] not in b['titre']:
        err.append('"mot" doit être un morceau exact de "titre"')
    for k in ('avant', 'apres'):
        if len(b['carte'].get(k, '')) > 34:
            err.append(f'carte.{k} > 34 caractères')
    if b.get('offre', 'essai') not in OFFRES:
        err.append('offre inconnue')
    if 'google' not in (b.get('surtitre', '') + ' ' + b.get('titre', '')).lower():
        err.append('le surtitre ou le titre doit dire « fiche Google » (règle n°1)')
    return err


def page(b):
    t = html.escape(b['titre'])
    if b.get('mot'):
        m = html.escape(b['mot'])
        t = t.replace(m, f'<mark>{m}</mark>', 1)
    bouton, mention = OFFRES[b.get('offre', 'essai')]
    c = {k: html.escape(v) for k, v in b['carte'].items()}
    logo = b64('logo.svg')
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:B;src:url(data:font/woff2;base64,{b64('bricolage-grotesque-latin.woff2')}) format('woff2');font-weight:200 800}}
@font-face{{font-family:F;src:url(data:font/woff2;base64,{b64('figtree-latin.woff2')}) format('woff2');font-weight:300 900}}
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;height:1350px;background:#f6f7f4;color:#16201b;font-family:F;position:relative;overflow:hidden}}
.halo{{position:absolute;left:190px;top:640px;width:700px;height:900px;border-radius:350px;background:#e7f0ea}}
.wrap{{position:relative;padding:80px 80px 0}}
.marque{{display:flex;align-items:center;gap:16px;font-size:30px;font-weight:600}}
.marque img{{width:44px;height:44px}}
.sur{{margin-top:36px;font-size:38px;color:#3b4740;line-height:1.2}}
h1{{font-family:B;font-weight:700;font-size:84px;line-height:1.02;letter-spacing:-2px;margin-top:22px}}
mark{{background:linear-gradient(transparent 62%,#cfe3d6 62%);color:#1f6b4a;padding:0 4px}}
.cta{{display:flex;align-items:center;gap:24px;margin-top:44px}}
.btn{{background:#1f6b4a;color:#fff;font-weight:700;font-size:32px;padding:20px 30px;border-radius:14px}}
.mention{{font-size:28px;color:#3b4740}}
.carte{{position:absolute;left:150px;right:150px;bottom:110px;background:#fff;border-radius:32px;padding:40px 44px;
  box-shadow:0 30px 60px rgba(22,32,27,.10);border:3px solid #1f6b4a}}
.lab{{font-size:22px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#1f6b4a;margin-bottom:10px}}
.ent{{font-family:B;font-weight:700;font-size:40px}}
.met{{font-size:26px;color:#5b665f;margin-top:6px}}
.met b{{color:#f2b63c}}
.ligne{{display:flex;align-items:center;gap:18px;font-size:30px;margin-top:26px;padding:18px 22px;border-radius:16px}}
.avant{{background:#fdf4e0;color:#7a5a12;text-decoration:line-through;text-decoration-color:#c99422}}
.apres{{background:#e7f0ea;color:#1f6b4a;font-weight:600}}
.pt{{width:16px;height:16px;border-radius:50%;flex:none}}
.avant .pt{{background:#f2b63c}} .apres .pt{{background:#1f6b4a}}
.badge{{position:absolute;top:-26px;right:40px;background:#1f6b4a;color:#fff;font-weight:700;font-size:24px;padding:12px 20px;border-radius:30px}}
</style></head><body><div class="halo"></div><div class="wrap">
<div class="marque"><img src="data:image/svg+xml;base64,{logo}">Proenligne</div>
<p class="sur">{html.escape(b['surtitre'])}</p>
<h1>{t}</h1>
<div class="cta"><span class="btn">{html.escape(bouton)}</span><span class="mention">{html.escape(mention)}</span></div>
</div>
<div class="carte"><span class="badge">Fiche Google à jour</span>
<div class="lab">Votre fiche Google</div>
<div class="ent">{c['enseigne']}</div><div class="met"><b>★★★★★</b> · {c['metier']}</div>
<div class="ligne avant"><span class="pt"></span>{c['avant']}</div>
<div class="ligne apres"><span class="pt"></span>{c['apres']}</div>
</div></body></html>"""


def rendre(b, sortie):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page(viewport={'width': 1080, 'height': 1350})
        pg.set_content(page(b))
        pg.wait_for_timeout(300)
        deborde = pg.evaluate("""() => [...document.querySelectorAll('h1,.sur,.ligne,.btn,.ent')]
            .filter(e => e.scrollWidth > e.clientWidth + 1 || e.getBoundingClientRect().right > 1080).length""")
        h1bas = pg.evaluate("document.querySelector('.cta').getBoundingClientRect().bottom")
        cartehaut = pg.evaluate("document.querySelector('.carte').getBoundingClientRect().top")
        pg.screenshot(path=sortie)
        br.close()
    if deborde or h1bas > cartehaut - 40:
        raise SystemExit(f'ATTENTION : texte trop long (débordement={deborde}, titre chevauche la carte={h1bas > cartehaut - 40})')


if __name__ == '__main__':
    b = json.load(open(sys.argv[1], encoding='utf-8'))
    e = verifier(b)
    if e:
        raise SystemExit('refusé : ' + ' ; '.join(e))
    os.makedirs(os.path.dirname(os.path.abspath(sys.argv[2])), exist_ok=True)
    rendre(b, sys.argv[2])
    print('visuel OK :', sys.argv[2])
