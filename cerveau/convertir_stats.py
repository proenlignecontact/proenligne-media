"""Convertit un relevé brut de l'API de stats (cerveau/stats/brut/AAAA-MM-JJ.json) au format du second-brain.

usage : python3 cerveau/convertir_stats.py [<relevé brut>]   (défaut : le plus récent)
        python3 cerveau/convertir_stats.py --tout           (reconvertit tous les relevés bruts)
sortie : cerveau/stats/AAAA-MM-JJ.json (même date que le brut), résumé affiché.

Correspondance des métriques (valeur « sum » de chaque métrique, noms comparés sans casse) :
  vues            ← Views, Plays, Impressions, Video views
  portee          ← Reach, Unique impressions, Members reached (LinkedIn)
  likes           ← Likes, Reactions
  commentaires    ← Comments
  partages        ← Shares, Reposts, Retweets
  enregistrements ← Saves, Favorites, Bookmarks
  clics           ← Clicks, Link clicks
  engagement_total← Engagement (indicateur global de la plateforme, gardé à part)
Plateforme Postiz « linkedin-page » → canal « linkedin » (idem pour les fiches de production).

COMMENTAIRES DE LA MAISON (décision du 11/11/2026) : chaque post part avec un premier commentaire écrit par
Proenligne, que les plateformes comptent comme un commentaire. Ils sont retirés ici, pour que les stats ne
mesurent que les commentaires venus de l'extérieur :
  commentaires        = commentaires venus de l'extérieur (brut − commentaires de la maison, jamais < 0)
  commentaires_bruts  = valeur renvoyée par la plateforme
  commentaires_maison = nombre retiré
Par défaut on retire 1 (le premier commentaire) à chaque post, sauf si sa fiche de production a un
premier_commentaire vide. Les autres commentaires écrits par Maxime (réponses, relances) se déclarent dans
cerveau/commentaires-maison.json : {"<postiz_id>": <nombre de commentaires en plus>} ; ils sont retirés aussi.
Facebook ne donne qu'un « engagement_total » qui inclut le premier commentaire : on retire 1 de la même façon.
Les commentaires au niveau du compte (section « comptes ») restent bruts : ils comprennent les nôtres.
Les posts sans stats (available = false) sont listés dans « indisponibles » avec la raison donnée par l'API.
"""
import glob, json, os, sys

ICI = os.path.dirname(os.path.abspath(__file__))
CORRESP = {
    'views': 'vues', 'plays': 'vues', 'impressions': 'vues', 'video views': 'vues',
    'reach': 'portee', 'unique impressions': 'portee', 'members reached': 'portee',
    'likes': 'likes', 'reactions': 'likes',
    'comments': 'commentaires',
    'shares': 'partages', 'reposts': 'partages', 'retweets': 'partages',
    'saves': 'enregistrements', 'favorites': 'enregistrements', 'bookmarks': 'enregistrements',
    'clicks': 'clics', 'link clicks': 'clics', 'clicks count': 'clics',
    'engagement': 'engagement_total',
}


PLATEFORMES = {'linkedin-page': 'linkedin', 'linkedin': 'linkedin', 'instagram-standalone': 'instagram', 'tiktok-business': 'tiktok'}


def canal(p):
    return PLATEFORMES.get(p, p)


def commentaires_maison():
    """postiz_id -> nombre de commentaires écrits par Proenligne (premier commentaire + déclarés à la main)."""
    sans_pc = set()
    for f in glob.glob(os.path.join(ICI, 'productions', '*.json')):
        fi = json.load(open(f, encoding='utf-8'))
        if not (fi.get('premier_commentaire') or '').strip():
            sans_pc |= {p.get('postiz_id') for p in fi.get('publications', [])}
    extra_f = os.path.join(ICI, 'commentaires-maison.json')
    extra = json.load(open(extra_f, encoding='utf-8')) if os.path.exists(extra_f) else {}
    return lambda pid: (0 if pid in sans_pc else 1) + int(extra.get(pid, 0))


def convertir(chemin):
    brut = json.load(open(chemin, encoding='utf-8'))
    maison = commentaires_maison()
    posts, indispo = [], []
    for p in brut.get('posts', []):
        s = p.get('stats') or {}
        if not s.get('available'):
            indispo.append({'postiz_id': p['id'], 'canal': canal(p['platform']), 'raison': s.get('reason')})
            continue
        m = {'postiz_id': p['id'], 'canal': canal(p['platform'])}
        for met in s.get('metrics', []):
            cle = CORRESP.get(str(met.get('metric', '')).strip().lower())
            if cle and met.get('sum') is not None and cle not in m:
                m[cle] = met['sum']
        n = maison(p['id'])
        if m.get('commentaires') is not None:
            m['commentaires_bruts'] = m['commentaires']
            m['commentaires'] = max(0, m['commentaires'] - n)
            m['commentaires_maison'] = m['commentaires_bruts'] - m['commentaires']
        elif m.get('engagement_total') is not None and m['canal'] == 'facebook':
            m['engagement_total_brut'] = m['engagement_total']
            m['engagement_total'] = max(0, m['engagement_total'] - n)
        posts.append(m)
    comptes = {canal(c['platform']): {x['metric']: x.get('sum') for x in (c.get('stats') or {}).get('metrics') or []}
               for c in brut.get('channels', [])}
    out = {'releve_le': brut.get('generatedAt'), 'source': os.path.basename(chemin), 'posts': posts,
           'indisponibles': indispo, 'comptes': comptes}
    dest = os.path.join(ICI, 'stats', os.path.basename(chemin))
    json.dump(out, open(dest, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return dest, out


if __name__ == '__main__':
    if '--tout' in sys.argv:   # reconvertit tout l'historique (après un changement de règle de conversion)
        for src in sorted(glob.glob(os.path.join(ICI, 'stats', 'brut', '*.json'))):
            dest, out = convertir(src)
            ext = sum(p.get('commentaires') or 0 for p in out['posts'])
            print(f'{os.path.basename(dest)} : {len(out["posts"])} posts, {ext} commentaires venus de l\'extérieur')
        sys.exit(0)
    src = sys.argv[1] if len(sys.argv) > 1 else sorted(glob.glob(os.path.join(ICI, 'stats', 'brut', '*.json')))[-1]
    dest, out = convertir(src)
    ext = sum(p.get('commentaires') or 0 for p in out['posts'])
    retires = sum(p.get('commentaires_maison') or 0 for p in out['posts'])
    print(f'{dest} : {len(out["posts"])} posts avec stats, {len(out["indisponibles"])} sans · '
          f'commentaires venus de l\'extérieur {ext} (commentaires de la maison retirés {retires})')
    for i in out['indisponibles']:
        print(f'  sans stats : {i["canal"]} {i["postiz_id"]} — {i["raison"]}')
