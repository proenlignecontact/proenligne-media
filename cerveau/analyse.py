"""Croise les fiches de production et les relevés de stats, et écrit un rapport.

usage : python3 cerveau/analyse.py [--sortie cerveau/analyses/AAAA-MM-JJ.md] [--min 5] [--delai 48]

- Fiches : cerveau/productions/*.json
- Stats  : cerveau/stats/*.json (le relevé le plus récent de chaque post l'emporte)
- Un post n'est « mesuré » que si son relevé date d'au moins --delai heures après sa publication.
- Une valeur de dimension n'est classée que si elle a au moins --min posts mesurés.
"""
import argparse, datetime as dt, glob, json, os, statistics
from collections import defaultdict
from zoneinfo import ZoneInfo

ICI = os.path.dirname(os.path.abspath(__file__))
PARIS = ZoneInfo('Europe/Paris')
DIMS = ['creneau', 'metier', 'angle', 'format', 'ton', 'symptome', 'offre', 'jour_semaine', 'heure_paris', 'canal']
ENGAGE = ['likes', 'commentaires', 'partages', 'enregistrements']


def charger_fiches():
    fiches = []
    for f in sorted(glob.glob(os.path.join(ICI, 'productions', '*.json'))):
        fiches.append(json.load(open(f, encoding='utf-8')))
    return fiches


def charger_stats():
    """postiz_id -> (date du relevé, mesures) ; le relevé le plus récent gagne."""
    dernier = {}
    for f in sorted(glob.glob(os.path.join(ICI, 'stats', '*.json'))):
        r = json.load(open(f, encoding='utf-8'))
        quand = dt.datetime.fromisoformat(r['releve_le'].replace('Z', '+00:00'))
        for p in r.get('posts', []):
            pid = p.get('postiz_id')
            if pid and (pid not in dernier or quand > dernier[pid][0]):
                dernier[pid] = (quand, p)
    return dernier


def lignes(fiches, stats, delai_h):
    """Une ligne par publication mesurée (fiche × canal)."""
    out, non_mesurees = [], 0
    for f in fiches:
        pub = dt.datetime.fromisoformat(f"{f['date_paris']}T{f['heure_paris']}").replace(tzinfo=PARIS)
        for p in f.get('publications', []):
            s = stats.get(p.get('postiz_id'))
            if not s or (s[0] - pub).total_seconds() < delai_h * 3600 or not s[1].get('vues'):
                non_mesurees += 1
                continue
            m = s[1]
            eng = sum(m.get(k) or 0 for k in ENGAGE)
            ligne = {d: f.get(d) for d in DIMS if d != 'canal'}
            ligne.update(canal=p['canal'], vues=m['vues'], taux=eng / m['vues'], clics=m.get('clics'),
                         id=f['id'], accroche=f.get('accroche', ''))
            out.append(ligne)
    return out, non_mesurees


def tableau(rows, dim, mini):
    g = defaultdict(list)
    for r in rows:
        if r.get(dim) is not None:
            g[r[dim]].append(r)
    res = []
    for val, rs in g.items():
        res.append((val, len(rs), statistics.median(r['vues'] for r in rs), statistics.mean(r['taux'] for r in rs)))
    res.sort(key=lambda x: (x[1] >= mini, x[3]), reverse=True)
    return res


def rapport(fiches, rows, non_mesurees, mini):
    aujourd = dt.date.today().isoformat()
    L = [f'# Analyse du {aujourd}', '',
         f'- Fiches de production : {len(fiches)}',
         f'- Publications mesurées : {len(rows)} (non mesurées ou trop récentes : {non_mesurees})',
         f'- Seuil de fiabilité : {mini} publications mesurées par valeur', '']
    if not rows:
        L += ['**Pas encore de statistiques exploitables.** Continuer la rotation équilibrée prévue par les règles éditoriales.']
        return '\n'.join(L)
    taux_med = statistics.median(r['taux'] for r in rows)
    L += [f'Taux d\'engagement médian toutes publications : **{taux_med:.2%}** · vues médianes : **{statistics.median(r["vues"] for r in rows):.0f}**', '']
    for dim in DIMS:
        t = tableau(rows, dim, mini)
        if not t:
            continue
        L += [f'## {dim}', '', '| valeur | posts | vues médianes | engagement | verdict |', '|---|---|---|---|---|']
        for val, n, vues, taux in t:
            if n < mini:
                v = 'à explorer (trop peu de données)'
            elif taux >= taux_med * 1.2:
                v = '**à renforcer**'
            elif taux <= taux_med * 0.8:
                v = 'à réduire'
            else:
                v = 'dans la moyenne'
            L.append(f'| {val} | {n} | {vues:.0f} | {taux:.2%} | {v} |')
        L.append('')
    top = sorted(rows, key=lambda r: r['taux'], reverse=True)[:5]
    L += ['## Meilleures publications', '']
    L += [f'- {r["taux"]:.2%} · {r["vues"]} vues · {r["canal"]} · {r["metier"]} · « {r["accroche"][:80]} »' for r in top]
    flop = sorted(rows, key=lambda r: r['taux'])[:3]
    L += ['', '## Moins bonnes publications', '']
    L += [f'- {r["taux"]:.2%} · {r["vues"]} vues · {r["canal"]} · {r["metier"]} · « {r["accroche"][:80]} »' for r in flop]
    return '\n'.join(L)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--sortie')
    ap.add_argument('--min', type=int, default=5)
    ap.add_argument('--delai', type=int, default=48)
    a = ap.parse_args()
    fiches = charger_fiches()
    rows, nm = lignes(fiches, charger_stats(), a.delai)
    txt = rapport(fiches, rows, nm, a.min)
    if a.sortie:
        os.makedirs(os.path.dirname(os.path.abspath(a.sortie)), exist_ok=True)
        open(a.sortie, 'w', encoding='utf-8').write(txt + '\n')
    print(txt)
