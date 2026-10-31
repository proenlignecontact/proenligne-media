"""Croise les fiches de production et les relevés de stats, et écrit un rapport.

usage : python3 cerveau/analyse.py [--sortie cerveau/analyses/AAAA-MM-JJ.md] [--min 5] [--delai 48]

- Fiches : cerveau/productions/*.json
- Stats  : cerveau/stats/*.json (le relevé le plus récent de chaque post l'emporte)
- Une publication est « mesurée » si son relevé date d'au moins --delai heures après sa publication
  et donne une audience connue (vues, ou portée en secours). Une audience de 0 est une mesure, pas une inconnue.
- Les verdicts sont NORMALISÉS PAR CANAL : l'engagement d'une publication est rapporté à la médiane de son canal
  (indice 1,0 = dans la moyenne du canal), car un taux TikTok ne se compare pas à un taux Instagram.
- Une valeur de dimension n'est classée que si elle a au moins --min publications mesurées.
- X et Facebook texte ne renvoient pas de stats par post : ils se pilotent au niveau du compte (section « Comptes »).
"""
import argparse, datetime as dt, glob, json, os, statistics
from collections import defaultdict
from zoneinfo import ZoneInfo

ICI = os.path.dirname(os.path.abspath(__file__))
PARIS = ZoneInfo('Europe/Paris')
DIMS = ['canal', 'creneau', 'angle', 'format', 'metier', 'ton', 'symptome', 'jour_semaine']
ENGAGE = ['likes', 'commentaires', 'partages', 'enregistrements']


def charger_fiches():
    return [json.load(open(f, encoding='utf-8')) for f in sorted(glob.glob(os.path.join(ICI, 'productions', '*.json')))]


def charger_stats():
    """postiz_id -> (date du relevé, mesures) ; le relevé le plus récent gagne. Renvoie aussi les relevés de comptes."""
    dernier, comptes = {}, []
    for f in sorted(glob.glob(os.path.join(ICI, 'stats', '*.json'))):
        r = json.load(open(f, encoding='utf-8'))
        quand = dt.datetime.fromisoformat(r['releve_le'].replace('Z', '+00:00'))
        for p in r.get('posts', []):
            pid = p.get('postiz_id')
            if pid and (pid not in dernier or quand > dernier[pid][0]):
                dernier[pid] = (quand, p)
        if r.get('comptes'):
            comptes.append((quand, r['comptes']))
    return dernier, sorted(comptes)


def lignes(fiches, stats, delai_h):
    out, non_mesurees, sans_stats = [], 0, defaultdict(int)
    for f in fiches:
        pub = dt.datetime.fromisoformat(f"{f['date_paris']}T{f['heure_paris']}").replace(tzinfo=PARIS)
        for p in f.get('publications', []):
            s = stats.get(p.get('postiz_id'))
            if not s or (s[0] - pub).total_seconds() < delai_h * 3600:
                non_mesurees += 1; continue
            m = s[1]
            audience = m.get('vues') if m.get('vues') is not None else m.get('portee')
            if audience is None:
                sans_stats[p['canal']] += 1; continue
            eng = sum(m.get(k) or 0 for k in ENGAGE)
            ligne = {d: f.get(d) for d in DIMS if d != 'canal'}
            ligne.update(canal=p['canal'], audience=audience, taux=(eng / audience) if audience else 0.0,
                         clics=m.get('clics'), id=f['id'], accroche=f.get('accroche', ''))
            out.append(ligne)
    # indice normalisé par canal
    med = {}
    for canal in {r['canal'] for r in out}:
        t = [r['taux'] for r in out if r['canal'] == canal]
        med[canal] = statistics.median(t) if t else 0
    for r in out:
        r['indice'] = (r['taux'] / med[r['canal']]) if med[r['canal']] else (1.0 if r['taux'] == 0 else 2.0)
    return out, non_mesurees, sans_stats, med


def tableau(rows, dim, mini):
    g = defaultdict(list)
    for r in rows:
        if r.get(dim) is not None:
            g[r[dim]].append(r)
    res = [(val, len(rs), statistics.median(r['audience'] for r in rs), statistics.mean(r['taux'] for r in rs),
            statistics.mean(r['indice'] for r in rs)) for val, rs in g.items()]
    res.sort(key=lambda x: (x[1] >= mini, x[4]), reverse=True)
    return res


def verdict(n, indice, mini):
    if n < mini: return 'à explorer (trop peu de données)'
    if indice >= 1.2: return '**à renforcer**'
    if indice <= 0.8: return 'à réduire'
    return 'dans la moyenne'


def section_comptes(comptes):
    if not comptes:
        return ['_Aucun relevé de compte._']
    L = ['| plateforme | métrique | relevé précédent | dernier relevé | évolution |', '|---|---|---|---|---|']
    quand, dernier = comptes[-1]
    prec = comptes[-2][1] if len(comptes) > 1 else {}
    for plat, mets in dernier.items():
        for k, v in (mets or {}).items():
            p = (prec.get(plat) or {}).get(k)
            evo = '' if p is None or v is None else f'{v - p:+}'
            L.append(f'| {plat} | {k} | {"" if p is None else p} | {"" if v is None else v} | {evo} |')
    L.append(f'\n_Dernier relevé : {quand:%Y-%m-%d}. X et Facebook texte ne donnent pas de stats par post : juger ces canaux sur ces chiffres de compte (abonnés, impressions)._')
    return L


def rapport(fiches, rows, non_mesurees, sans_stats, med, comptes, mini):
    aujourd = dt.date.today().isoformat()
    L = [f'# Analyse du {aujourd}', '',
         f'- Fiches de production : {len(fiches)}',
         f'- Publications mesurées : {len(rows)} · trop récentes ou sans relevé : {non_mesurees} · sans stats par post : '
         + (', '.join(f'{k} {v}' for k, v in sans_stats.items()) or '0'),
         f'- Seuil de fiabilité : {mini} publications mesurées par valeur ; verdicts normalisés par canal (indice 1,0 = médiane du canal)', '']
    total = len(rows)
    if total < 30:
        L += [f'**Phase de démarrage ({total} < 30 publications mesurées) : exploration à 50 / 50**, pas de pondération 70 / 30.', '']
    L += ['## Comptes', ''] + section_comptes(comptes) + ['']
    if not rows:
        L += ['**Pas encore de statistiques par post exploitables.** Continuer la rotation équilibrée prévue par les règles éditoriales.']
        return '\n'.join(L)
    L += ['## Médianes par canal', '', '| canal | publications | engagement médian |', '|---|---|---|']
    for canal, m in sorted(med.items()):
        L.append(f'| {canal} | {sum(1 for r in rows if r["canal"] == canal)} | {m:.2%} |')
    L.append('')
    for dim in DIMS:
        t = tableau(rows, dim, mini)
        if not t:
            continue
        L += [f'## {dim}', '', '| valeur | posts | audience médiane | engagement | indice | verdict |', '|---|---|---|---|---|---|']
        for val, n, aud, taux, ind in t:
            L.append(f'| {val} | {n} | {aud:.0f} | {taux:.2%} | {ind:.2f} | {verdict(n, ind, mini)} |')
        L.append('')
    top = sorted(rows, key=lambda r: r['indice'], reverse=True)[:5]
    L += ['## Meilleures publications (indice canal)', '']
    L += [f'- ×{r["indice"]:.2f} · {r["taux"]:.2%} · {r["audience"]:.0f} vues · {r["canal"]} · {r["metier"]} · « {r["accroche"][:80]} »' for r in top]
    flop = sorted(rows, key=lambda r: r['indice'])[:3]
    L += ['', '## Moins bonnes publications', '']
    L += [f'- ×{r["indice"]:.2f} · {r["taux"]:.2%} · {r["audience"]:.0f} vues · {r["canal"]} · {r["metier"]} · « {r["accroche"][:80]} »' for r in flop]
    return '\n'.join(L)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--sortie')
    ap.add_argument('--min', type=int, default=5)
    ap.add_argument('--delai', type=int, default=48)
    a = ap.parse_args()
    fiches = charger_fiches()
    stats, comptes = charger_stats()
    rows, nm, ss, med = lignes(fiches, stats, a.delai)
    txt = rapport(fiches, rows, nm, ss, med, comptes, a.min)
    if a.sortie:
        os.makedirs(os.path.dirname(os.path.abspath(a.sortie)), exist_ok=True)
        open(a.sortie, 'w', encoding='utf-8').write(txt + '\n')
    print(txt)
