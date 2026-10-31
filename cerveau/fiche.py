"""Écrit les fiches de production d'un plan programmé, sans jamais créer de doublon.

usage : python3 cerveau/fiche.py suivi/plan/<lundi>.json suivi/plan/<lundi>-ids.json [--source tache-hebdo]

<lundi>-ids.json : les postiz_id renvoyés par Postiz, par créneau et par canal :
  {"2026-11-09_0630": {"x": "cmv…", "facebook": "cmv…"}, "2026-11-09_1300": {"instagram": "…", "facebook": "…"}, …}

Pour chaque créneau du plan qui a des ids :
- s'il existe déjà une fiche cerveau/productions/<date>_<HHMM>_*.json, elle est COMPLÉTÉE (ids, textes) et non dupliquée ;
- sinon la fiche est créée selon le schéma de cerveau/README.md.
Un créneau sans id dans le fichier est ignoré (non programmé).
"""
import datetime as dt, glob, json, os, re, sys

ICI = os.path.dirname(os.path.abspath(__file__))
JOURS = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche']
TYPE_MEDIA = {'texte': 'aucun', 'visuel': 'image', 'video': 'video'}


def media_de(c):
    fichiers, postiz = [], []
    for v in (c.get('media') or {}).values():
        if not isinstance(v, str):
            continue
        if 'media.glidy.uk' in v:
            postiz.append(v)
        elif 'medias/' in v:
            fichiers.append(v.split('/main/')[-1] if '/main/' in v else v)
    return {'type': TYPE_MEDIA[c['creneau']], 'fichiers': fichiers, 'postiz': postiz}


def ecrire(plan, ids, source):
    cr = plan['creneaux'] if isinstance(plan, dict) else plan
    faits = []
    for c in cr:
        cle = f"{c['date']}_{c['heure'].replace(':', '')}"
        pid = ids.get(cle)
        if not pid:
            continue
        exist = glob.glob(os.path.join(ICI, 'productions', cle + '_*.json'))
        if exist:
            chemin = exist[0]
            f = json.load(open(chemin, encoding='utf-8'))
            if len(exist) > 1:
                print(f'ATTENTION : {len(exist)} fiches pour {cle}, la première est complétée : {os.path.basename(chemin)}')
        else:
            chemin = os.path.join(ICI, 'productions', f"{cle}_{c['slug']}.json")
            f = {'id': f"{cle}_{c['slug']}", 'date_paris': c['date'], 'heure_paris': c['heure'],
                 'jour_semaine': JOURS[dt.date.fromisoformat(c['date']).weekday()], 'creneau': c['creneau'],
                 'metier': c['metier'], 'angle': c['angle'], 'format': c['format'], 'ton': c['ton'],
                 'symptome': c.get('symptome'), 'offre': 'essai', 'accroche': c['accroche'],
                 'promesse': 'photo lundi, publication jeudi, réponse à chaque avis',
                 'hashtags': sorted(set(re.findall(r'#\w+', ' '.join(c['textes'].values())))),
                 'media': media_de(c), 'publications': [], 'source': source, 'notes': c.get('notes', '')}
        deja = {p['canal']: p for p in f['publications']}
        for canal, texte in c['textes'].items():
            if canal in pid:
                deja[canal] = {'canal': canal, 'postiz_id': pid[canal], 'caracteres': len(texte), 'texte': texte}
        f['publications'] = list(deja.values())
        json.dump(f, open(chemin, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        faits.append(('complétée' if exist else 'créée', os.path.basename(chemin)))
    return faits


if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if not x.startswith('--')]
    if len(a) != 2:
        raise SystemExit(__doc__)
    source = sys.argv[sys.argv.index('--source') + 1] if '--source' in sys.argv else 'tache-hebdo'
    for etat, nom in ecrire(json.load(open(a[0], encoding='utf-8')), json.load(open(a[1], encoding='utf-8')), source):
        print(etat, nom)
