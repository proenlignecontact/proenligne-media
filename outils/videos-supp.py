"""Vidéos supplémentaires de la semaine : 2 par jour, vers 10:00 et 16:30 (heure de Paris), sur les 6 réseaux Postiz
(TikTok, Instagram, Facebook, YouTube, X, LinkedIn page, LinkedIn compris le week-end), en plus de la grille habituelle
(06:30 image, 13:00 carrousel, 19:00 vidéo). Utilisé par la tâche « Vidéos supplémentaires Proenligne »
(consigne : suivi/consignes/videos-supplementaires.md).

usage :
  python3 outils/videos-supp.py creneaux <lundi>
      les 14 créneaux de la semaine (date, heure de Paris légèrement variée, UTC), en JSON
  python3 outils/videos-supp.py verifier <plan.json> [--briefs <dossier>]
      contrôle les textes de publication (règles n°1-2-3-5, « fiche Google », longueurs X / LinkedIn / titres)
      et, avec --briefs, les briefs vidéo (outils/pub-video.py valider). Doit répondre « plan supp OK ».
  python3 outils/videos-supp.py postiz <plan.json> <slug>
      écrit /tmp/videos-supp-<slug>.json : le tableau socialPost à passer TEL QUEL à
      mcp__postiz__integrationSchedulePostTool (6 réseaux, premier commentaire, réglages des règles éditoriales).
      Le plan doit porter media.postiz_vertical (URL media.glidy.uk renvoyée par uploadFromUrlTool).

Plan (suivi/plan/<lundi>-supp.json) : une liste, une entrée par vidéo :
  {"slug", "utc", "heure_paris", "intention": "utile|preuve|offre", "tiktok_title" (≤ 90), "youtube_title" (≤ 100, avec
   « fiche Google »), "textes": {"tiktok", "instagram", "facebook", "youtube", "x" (≤ 280), "linkedin" (700 à 1 300)},
   "premier_commentaire", "media": {"postiz_vertical": "…"}}
Le brief vidéo de chaque entrée est suivi/briefs/<lundi>-supp/<slug>.json (format de outils/pub-video.py).
"""
import datetime as dt, glob, html, json, os, re, subprocess, sys, zoneinfo

ICI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(ICI)
sys.path.insert(0, os.path.join(REPO, 'cerveau'))
import regles_texte  # noqa: E402

CANAUX = {'tiktok': 'cmvsaqnzu0001pj8d4gk1ojzz', 'facebook': 'cmvs9p6ky0001mq8gkj2c0a82', 'instagram': 'cmvs9xsx80003mq8gnh6baz7n',
          'x': 'cmvsbfk2y0001nr8eba2fo36u', 'youtube': 'cmvsbyqw20001jv87195lx18q', 'linkedin': 'cmvxyqbk4001vkb7zbrwvu9pt'}
PARIS = zoneinfo.ZoneInfo('Europe/Paris')
# décalages (minutes) appliqués à 10:00 et 16:30 selon le jour : jamais deux jours à la même minute, jamais à ±45 min d'un autre créneau
DECALAGES = [(15, 0), (0, 15), (-15, -15), (30, -30), (-30, 30), (15, -15), (0, 0)]


def creneaux(lundi):
    j0 = dt.date.fromisoformat(lundi)
    out = []
    for i in range(7):
        d = j0 + dt.timedelta(days=i)
        for (h, m), dec in zip(((10, 0), (16, 30)), DECALAGES[i]):
            loc = dt.datetime(d.year, d.month, d.day, h, m, tzinfo=PARIS) + dt.timedelta(minutes=dec)
            out.append({'date': d.isoformat(), 'creneau_nominal': f'{h:02d}:{m:02d}', 'heure_paris': loc.strftime('%Y-%m-%d %H:%M'),
                        'utc': loc.astimezone(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:00')})
    return out


def verifier(plan_f, briefs=None):
    P = json.load(open(plan_f, encoding='utf-8'))
    pb = []
    for p in P:
        s = p.get('slug', '?')
        for k in ('tiktok', 'instagram', 'facebook', 'youtube', 'x', 'linkedin'):
            t = (p.get('textes') or {}).get(k, '')
            if not t: pb.append(f'{s} texte {k} manquant'); continue
            pb += regles_texte.problemes(t, f'{s} {k}') + regles_texte.fiche_seule(t, f'{s} {k}')
            if not re.search(r'fiches? google', t, re.I): pb.append(f'{s} {k} : « fiche Google » absent')
        x, li = p['textes'].get('x', ''), p['textes'].get('linkedin', '')
        if len(x) > 280: pb.append(f'{s} x : {len(x)} caractères (max 280)')
        if not 700 <= len(li) <= 1300: pb.append(f'{s} linkedin : {len(li)} caractères (700 à 1 300)')
        if li.count('#') > 5: pb.append(f'{s} linkedin : plus de 5 hashtags')
        if 'http' in li or 'lien en bio' in li.lower(): pb.append(f'{s} linkedin : lien interdit')
        for k, n in (('tiktok_title', 90), ('youtube_title', 100)):
            t = p.get(k, '')
            if not t or len(t) > n: pb.append(f'{s} {k} : vide ou > {n} caractères')
            pb += regles_texte.problemes(t, f'{s} {k}') + regles_texte.fiche_seule(t, f'{s} {k}')
        if not re.search(r'fiches? google', p.get('youtube_title', ''), re.I): pb.append(f'{s} youtube_title : « fiche Google » absent')
        c = p.get('premier_commentaire', '')
        if not c or len(c) > 300: pb.append(f'{s} premier_commentaire vide ou > 300 caractères')
        pb += regles_texte.problemes(c, f'{s} commentaire') + regles_texte.fiche_seule(c, f'{s} commentaire')
        if p.get('intention') != 'offre' and '✅' in json.dumps(p, ensure_ascii=False): pb.append(f'{s} : ✅ réservés aux posts offre')
    if briefs:
        r = subprocess.run([sys.executable, os.path.join(ICI, 'pub-video.py'), 'valider'] + sorted(glob.glob(os.path.join(briefs, '*.json'))),
                           capture_output=True, text=True)
        if 'briefs OK' not in r.stdout: pb += r.stdout.strip().splitlines()
        slugs = {os.path.basename(f)[:-5] for f in glob.glob(os.path.join(briefs, '*.json'))}
        pb += [f'{p["slug"]} : brief absent de {briefs}' for p in P if p['slug'] not in slugs]
    print('\n'.join(pb) if pb else 'plan supp OK')
    return 1 if pb else 0


def h(t):
    return ''.join('<p>' + html.escape(l, quote=False) + '</p>' if l else '<p></p>' for l in t.split('\n'))


def postiz(plan_f, slug):
    p = next(x for x in json.load(open(plan_f, encoding='utf-8')) if x['slug'] == slug)
    m = (p.get('media') or {}).get('postiz_vertical')
    if not m: raise SystemExit(f'{slug} : media.postiz_vertical manquant (importer la vidéo avec uploadFromUrlTool)')
    reglages = {
        'tiktok': [('content_posting_method', 'UPLOAD'), ('privacy_level', 'PUBLIC_TO_EVERYONE'), ('duet', False), ('stitch', False), ('comment', True),
                   ('autoAddMusic', 'no'), ('brand_content_toggle', False), ('brand_organic_toggle', False), ('video_made_with_ai', False),
                   ('title', p['tiktok_title'])],
        'facebook': [('post_type', 'post')], 'instagram': [('post_type', 'post')],
        'x': [('post_type', 'post'), ('who_can_reply_post', 'everyone')],
        'youtube': [('title', p['youtube_title']), ('type', 'public'), ('selfDeclaredMadeForKids', 'no')],
        'linkedin': [('post_as_images_carousel', False)]}
    S = [{'integrationId': iid, 'isPremium': False, 'date': p['utc'], 'shortLink': False, 'type': 'schedule',
          'postsAndComments': [{'content': h(p['textes'][c]), 'attachments': [m]}, {'content': h(p['premier_commentaire']), 'attachments': []}],
          'settings': [{'key': k, 'value': v} for k, v in reglages[c]]} for c, iid in CANAUX.items()]
    f = f'/tmp/videos-supp-{slug}.json'
    json.dump(S, open(f, 'w', encoding='utf-8'), ensure_ascii=False)
    print(f)


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a: raise SystemExit(__doc__)
    if a[0] == 'creneaux':
        print(json.dumps(creneaux(a[1]), ensure_ascii=False, indent=1))
    elif a[0] == 'verifier':
        sys.exit(verifier(a[1], a[a.index('--briefs') + 1] if '--briefs' in a else None))
    elif a[0] == 'postiz':
        postiz(a[1], a[2])
    else:
        raise SystemExit(__doc__)
