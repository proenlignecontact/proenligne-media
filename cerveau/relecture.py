"""Relecture « lecteur humain » de TOUS les éléments textuels d'une semaine, par un agent indépendant.

Pourquoi : le vérificateur contrôle des règles mécaniques (prix, « fiche Google », longueurs…). Il ne sait pas si une phrase
a du sens pour quelqu'un qui la lit froidement (« Nouveauté tue sur votre fiche Google, clients partis »), ni si deux
éléments d'un même créneau se contredisent (le texte dit « 3 choses », le visuel coche une seule bonne réponse).
Cette relecture est faite par un agent qui n'a pas écrit les textes, à partir de cerveau/relecture-consigne.md.

usage :
  python3 cerveau/relecture.py extraire <lundi> [--briefs <dossier des briefs vidéo>]
      → écrit suivi/relecture/<lundi>-textes.json : {"empreinte", "elements": [{"id", "ref", "source", "champ", "texte"}]}
        source = plan (textes, accroche, titres, premier commentaire, brief visuel) | brief:<slug> (brief vidéo)
  python3 cerveau/relecture.py controler <lundi> [--briefs <dossier>]
      → lit suivi/relecture/<lundi>.json écrit par le relecteur :
        {"empreinte": "<copiée du fichier -textes>", "verdicts": [{"id", "verdict": "ok"|"refuse", "motif", "proposition"}]}
        Refusé si : fichier absent, empreinte différente (les textes ont changé depuis), un id sans verdict, ou un verdict « refuse ».
        Code 0 = relecture complète et sans refus.
"""
import glob, hashlib, json, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import regles_texte  # noqa: E402

REP = os.path.join(ICI, '..', 'suivi', 'relecture')


def elements(lundi, briefs_dir=None):
    plan = json.load(open(os.path.join(ICI, '..', 'suivi', 'plan', f'{lundi}.json'), encoding='utf-8'))
    out = []
    for ref, champ, texte in regles_texte.textes_du_plan(plan):
        if texte: out.append({'ref': ref, 'source': 'plan', 'champ': champ, 'texte': texte})
    if briefs_dir:
        for f in sorted(glob.glob(os.path.join(briefs_dir, '*.json'))):
            b = json.load(open(f, encoding='utf-8'))
            slug = b.get('slug') or os.path.basename(f)[:-5]
            ref = next((c.get('date', '') + ' 19:00' for c in plan['creneaux'] if c.get('slug') == slug and c.get('ab') != 'B'), '')
            for champ, texte in regles_texte.textes_du_brief(b):
                if texte: out.append({'ref': ref, 'source': f'brief:{slug}', 'champ': champ, 'texte': texte})
    for i, e in enumerate(out, 1):
        e['id'] = f'e{i:03d}'
    emp = hashlib.sha256('\n'.join(e['texte'] for e in out).encode('utf-8')).hexdigest()[:16]
    return emp, out


def extraire(lundi, briefs_dir=None):
    emp, els = elements(lundi, briefs_dir)
    os.makedirs(REP, exist_ok=True)
    p = os.path.join(REP, f'{lundi}-textes.json')
    json.dump({'lundi': lundi, 'empreinte': emp, 'nb': len(els), 'elements': els}, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'{len(els)} éléments à relire → {os.path.relpath(p)} (empreinte {emp})')
    return p


def controler(lundi, briefs_dir=None):
    """Retourne la liste des problèmes (vide = relecture complète et validée)."""
    emp, els = elements(lundi, briefs_dir)
    p = os.path.join(REP, f'{lundi}.json')
    if not os.path.exists(p):
        return [f'relecture absente : {os.path.relpath(p)} (lancer « relecture.py extraire » puis le relecteur)']
    r = json.load(open(p, encoding='utf-8'))
    pb = []
    if r.get('empreinte') != emp:
        pb.append(f'relecture périmée : les textes ont changé depuis (empreinte {r.get("empreinte")} ≠ {emp}) — réextraire et relire')
    verdicts = {v.get('id'): v for v in r.get('verdicts', [])}
    manquants = [e['id'] for e in els if e['id'] not in verdicts]
    if manquants: pb.append(f'{len(manquants)} élément(s) sans verdict : {", ".join(manquants[:8])}{"…" if len(manquants) > 8 else ""}')
    for e in els:
        v = verdicts.get(e['id'])
        if v and v.get('verdict') != 'ok':
            pb.append(f'{e["id"]} {e["ref"]} {e["source"]} {e["champ"]} : REFUSÉ — {v.get("motif", "?")} → « {v.get("proposition", "")} »')
    return pb


if __name__ == '__main__':
    if len(sys.argv) < 3 or sys.argv[1] not in ('extraire', 'controler'):
        raise SystemExit(__doc__)
    briefs = sys.argv[sys.argv.index('--briefs') + 1] if '--briefs' in sys.argv else None
    if sys.argv[1] == 'extraire':
        extraire(sys.argv[2], briefs)
    else:
        pb = controler(sys.argv[2], briefs)
        if pb:
            print('\n'.join('ATTENTION : ' + x for x in pb)); sys.exit(1)
        print('relecture OK')
