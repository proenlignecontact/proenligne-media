"""Relecture « lecteur humain » de TOUS les éléments textuels d'une semaine, par un agent indépendant — INCRÉMENTALE.

Pourquoi : le vérificateur contrôle des règles mécaniques (prix, « fiche Google », longueurs…). Il ne sait pas si une phrase
a du sens pour quelqu'un qui la lit froidement, ni si deux éléments d'un même créneau se contredisent.
Cette relecture est faite par un agent qui n'a pas écrit les textes, à partir de cerveau/relecture-consigne.md.

Principe (pour que la boucle converge au lieu de tout relire à chaque passe) :
  - chaque élément a une CLÉ stable (ref | source | champ) et une EMPREINTE de son texte (h) ;
  - un verdict « ok » est enregistré dans le REGISTRE suivi/relecture/<lundi>-valides.json, avec l'empreinte du texte relu ;
  - un élément dont le texte n'a pas changé depuis son « ok » reste validé ; seuls les éléments nouveaux, modifiés
    ou refusés sont renvoyés au relecteur ;
  - les éléments d'un même post (même ref) qu'un élément à relire sont joints en contexte (relus ensemble, mais seuls
    les éléments à relire ont besoin d'un verdict).

usage :
  python3 cerveau/relecture.py extraire <lundi> [--briefs <dossier>] [--tout]
      → écrit suivi/relecture/<lundi>-textes.json : {"empreinte", "elements": [{"id", "cle", "h", "ref", "source", "champ", "texte", "a_relire"}]}
        Par défaut n'y figurent que les éléments à relire + leurs voisins de même ref (a_relire = false, verdict facultatif).
        --tout : tous les éléments, tous à relire (première passe, ou remise à zéro du registre avec --raz).
  python3 cerveau/relecture.py enregistrer <lundi> [--briefs <dossier>]
      → lit suivi/relecture/<lundi>.json écrit par le relecteur :
        {"empreinte": "<copiée du fichier -textes>", "verdicts": [{"id", "verdict": "ok"|"refuse", "motif", "proposition"}]}
        Ajoute au registre chaque « ok » dont le texte correspond encore à l'empreinte relue ; affiche les refus et les
        éléments encore sans verdict. Archive le fichier de verdicts dans suivi/relecture/archives/.
  python3 cerveau/relecture.py controler <lundi> [--briefs <dossier>]
      → liste ce qui manque : éléments sans « ok » à jour dans le registre (nouveaux, modifiés, refusés). Code 0 = tout validé.
  python3 cerveau/relecture.py etat <lundi> [--briefs <dossier>]
      → compte validés / à relire, par ref.

Boucle type : extraire → agent relecteur → enregistrer → corriger les refus à la source → extraire (ne renvoie que
le reste) → agent relecteur → enregistrer … jusqu'à « relecture OK » au controler. Chaque passe est plus petite que la précédente.
"""
import datetime as dt, glob, hashlib, json, os, shutil, sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
import regles_texte  # noqa: E402

REP = os.path.join(ICI, '..', 'suivi', 'relecture')


def _h(texte):
    return hashlib.sha256(texte.encode('utf-8')).hexdigest()[:12]


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
    vus = {}
    for e in out:
        base = f"{e['ref']}|{e['source']}|{e['champ']}"
        n = vus.get(base, 0) + 1
        vus[base] = n
        e['cle'] = base if n == 1 else f'{base}#{n}'
        e['h'] = _h(e['texte'])
        e['id'] = 'e' + hashlib.sha1(e['cle'].encode('utf-8')).hexdigest()[:6]
    emp = hashlib.sha256('\n'.join(e['texte'] for e in out).encode('utf-8')).hexdigest()[:16]
    return emp, out


def _registre_path(lundi):
    return os.path.join(REP, f'{lundi}-valides.json')


def registre(lundi):
    p = _registre_path(lundi)
    if os.path.exists(p):
        return json.load(open(p, encoding='utf-8'))
    return {'lundi': lundi, 'valides': {}}


def sauver_registre(lundi, reg):
    os.makedirs(REP, exist_ok=True)
    json.dump(reg, open(_registre_path(lundi), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


def a_relire(lundi, briefs_dir=None):
    """(empreinte, tous les éléments, ensemble des clés à relire)."""
    emp, els = elements(lundi, briefs_dir)
    val = registre(lundi)['valides']
    restants = {e['cle'] for e in els if val.get(e['cle'], {}).get('h') != e['h']}
    return emp, els, restants


def extraire(lundi, briefs_dir=None, tout=False, raz=False):
    if raz:
        sauver_registre(lundi, {'lundi': lundi, 'valides': {}})
    emp, els, restants = a_relire(lundi, briefs_dir)
    if tout:
        restants = {e['cle'] for e in els}
    refs = {e['ref'] for e in els if e['cle'] in restants}
    sel = []
    for e in els:
        if e['ref'] in refs or e['cle'] in restants:
            sel.append(dict(e, a_relire=e['cle'] in restants))
    os.makedirs(REP, exist_ok=True)
    p = os.path.join(REP, f'{lundi}-textes.json')
    json.dump({'lundi': lundi, 'empreinte': emp, 'nb': len(sel), 'nb_a_relire': len(restants),
               'consigne': 'Un verdict pour chaque élément a_relire=true (les autres sont du contexte déjà validé : '
                           'verdict facultatif, mais à refuser s\'ils contredisent un élément relu).',
               'elements': sel}, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'{len(restants)} élément(s) à relire sur {len(els)} (+{len(sel) - len(restants)} de contexte, {len(refs)} post(s)) → {os.path.relpath(p)} (empreinte {emp})')
    return p


def enregistrer(lundi, briefs_dir=None):
    emp, els, restants = a_relire(lundi, briefs_dir)
    par_id = {e['id']: e for e in els}
    p = os.path.join(REP, f'{lundi}.json')
    if not os.path.exists(p):
        print(f'ATTENTION : {os.path.relpath(p)} absent'); return 1
    r = json.load(open(p, encoding='utf-8'))
    textes = os.path.join(REP, f'{lundi}-textes.json')
    relus = {}
    if os.path.exists(textes):
        relus = {e['id']: e for e in json.load(open(textes, encoding='utf-8'))['elements']}
    reg = registre(lundi)
    ok, refus, perimes, inconnus = 0, [], 0, 0
    quand = dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')
    for v in r.get('verdicts', []):
        e = par_id.get(v.get('id'))
        if not e:
            inconnus += 1; continue
        relu = relus.get(e['id'])
        if relu and relu['h'] != e['h']:
            perimes += 1; continue  # le texte a changé depuis l'extraction : ce verdict ne compte pas
        if v.get('verdict') == 'ok':
            reg['valides'][e['cle']] = {'h': e['h'], 'quand': quand}
            ok += 1
        else:
            reg['valides'].pop(e['cle'], None)
            refus.append(f'{e["id"]} {e["ref"]} {e["source"]} {e["champ"]} : REFUSÉ — {v.get("motif", "?")} → « {v.get("proposition", "")} »')
    sauver_registre(lundi, reg)
    os.makedirs(os.path.join(REP, 'archives'), exist_ok=True)
    stamp = dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    shutil.move(p, os.path.join(REP, 'archives', f'{lundi}-verdicts-{stamp}.json'))
    _, _, restants = a_relire(lundi, briefs_dir)
    print(f'{ok} ok enregistré(s), {len(refus)} refus, {perimes} verdict(s) périmé(s), {inconnus} id inconnu(s) ; reste {len(restants)} élément(s) à relire')
    for x in refus: print('REFUS : ' + x)
    sans = [e['id'] for e in els if e['cle'] in restants and not any(e['id'] == v.get('id') for v in r.get('verdicts', []))]
    if sans: print(f'SANS VERDICT : {len(sans)} élément(s) : {", ".join(sans[:8])}{"…" if len(sans) > 8 else ""}')
    return 0 if not restants else 1


def controler(lundi, briefs_dir=None):
    """Retourne la liste des problèmes (vide = tous les éléments ont un « ok » à jour dans le registre)."""
    emp, els, restants = a_relire(lundi, briefs_dir)
    if not os.path.exists(_registre_path(lundi)):
        return [f'relecture absente : {os.path.relpath(_registre_path(lundi))} (lancer « relecture.py extraire --tout » puis le relecteur, puis « enregistrer »)']
    pb = []
    for e in els:
        if e['cle'] in restants:
            pb.append(f'{e["id"]} {e["ref"]} {e["source"]} {e["champ"]} : à relire (nouveau, modifié ou refusé) — « {e["texte"][:70]} »')
    return pb


def etat(lundi, briefs_dir=None):
    emp, els, restants = a_relire(lundi, briefs_dir)
    print(f'{len(els) - len(restants)} validé(s) / {len(restants)} à relire sur {len(els)} (empreinte {emp})')
    par_ref = {}
    for e in els:
        par_ref.setdefault(e['ref'], [0, 0])[0 if e['cle'] in restants else 1] += 1
    for ref, (r, v) in sorted(par_ref.items()):
        if r: print(f'  {ref} : {r} à relire, {v} validé(s)')


if __name__ == '__main__':
    cmds = ('extraire', 'controler', 'enregistrer', 'etat')
    if len(sys.argv) < 3 or sys.argv[1] not in cmds:
        raise SystemExit(__doc__)
    briefs = sys.argv[sys.argv.index('--briefs') + 1] if '--briefs' in sys.argv else None
    cmd, lundi = sys.argv[1], sys.argv[2]
    if cmd == 'extraire':
        extraire(lundi, briefs, tout='--tout' in sys.argv, raz='--raz' in sys.argv)
    elif cmd == 'enregistrer':
        sys.exit(enregistrer(lundi, briefs))
    elif cmd == 'etat':
        etat(lundi, briefs)
    else:
        pb = controler(lundi, briefs)
        if pb:
            print('\n'.join('ATTENTION : ' + x for x in pb)); sys.exit(1)
        print('relecture OK')
