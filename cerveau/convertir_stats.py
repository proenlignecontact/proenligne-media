"""Convertit un relevé brut de l'API de stats (cerveau/stats/brut/AAAA-MM-JJ.json) au format du second-brain.

usage : python3 cerveau/convertir_stats.py [<relevé brut>]   (défaut : le plus récent)
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


def convertir(chemin):
    brut = json.load(open(chemin, encoding='utf-8'))
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
        posts.append(m)
    comptes = {canal(c['platform']): {x['metric']: x.get('sum') for x in (c.get('stats') or {}).get('metrics') or []}
               for c in brut.get('channels', [])}
    out = {'releve_le': brut.get('generatedAt'), 'source': os.path.basename(chemin), 'posts': posts,
           'indisponibles': indispo, 'comptes': comptes}
    dest = os.path.join(ICI, 'stats', os.path.basename(chemin))
    json.dump(out, open(dest, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    return dest, out


if __name__ == '__main__':
    src = sys.argv[1] if len(sys.argv) > 1 else sorted(glob.glob(os.path.join(ICI, 'stats', 'brut', '*.json')))[-1]
    dest, out = convertir(src)
    print(f'{dest} : {len(out["posts"])} posts avec stats, {len(out["indisponibles"])} sans')
    for i in out['indisponibles']:
        print(f'  sans stats : {i["canal"]} {i["postiz_id"]} — {i["raison"]}')
