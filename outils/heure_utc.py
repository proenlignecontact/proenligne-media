"""Convertit une heure de Paris en UTC (heure d'été et d'hiver gérées automatiquement).

usage : python3 outils/heure_utc.py 2026-11-02 06:30            → 2026-11-02T05:30:00Z
        python3 outils/heure_utc.py 2026-11-02                   → la grille des 14 créneaux de la semaine qui commence ce lundi
        python3 outils/heure_utc.py 2026-11-02 --varier          → la même grille avec des heures réelles tirées à ± 45 min
                                                                    (tirage reproductible pour une semaine donnée), au format JSON :
                                                                    [{"date", "creneau_nominal", "heure", "utc", "type", "canaux"}, …]
Les heures réelles servent à apprendre quels horaires marchent ; le créneau nominal reste la référence des fiches.
"""
import datetime as dt, json, random, sys
from zoneinfo import ZoneInfo

PARIS = ZoneInfo('Europe/Paris')
# Grille depuis la semaine du 16/11/2026 (décision du 11/11) : le créneau 06:30 (X + Facebook) est supprimé,
# le carrousel de 13:00 ne part plus sur Facebook, et sur LinkedIn seulement le mardi et le jeudi.
GRILLE = [('13:00', 'visuel', 'instagram (+ linkedin mardi et jeudi)'), ('19:00', 'video', 'tiktok + instagram + youtube + facebook')]


def utc(date, heure):
    h, m = map(int, heure.split(':'))
    d = dt.datetime.fromisoformat(date).replace(hour=h, minute=m, tzinfo=PARIS)
    return d.astimezone(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[2] != '--varier':
        print(utc(sys.argv[1], sys.argv[2]))
    elif len(sys.argv) in (2, 3) and (len(sys.argv) == 2 or sys.argv[2] == '--varier'):
        lundi = dt.date.fromisoformat(sys.argv[1])
        varier = len(sys.argv) == 3
        rng = random.Random(sys.argv[1])
        out = []
        for i in range(7):
            j = (lundi + dt.timedelta(days=i)).isoformat()
            for heure, typ, canaux in GRILLE:
                h, m = map(int, heure.split(':'))
                if varier:
                    delta = rng.choice([-30, -15, 0, 15, 30, 45])
                    t = dt.datetime(2000, 1, 1, h, m) + dt.timedelta(minutes=delta)
                    reelle = t.strftime('%H:%M')
                else:
                    reelle = heure
                if varier:
                    out.append({'date': j, 'creneau_nominal': heure, 'heure': reelle, 'utc': utc(j, reelle), 'type': typ, 'canaux': canaux})
                else:
                    print(f'{j} {heure} Paris → {utc(j, heure)}  {typ:6} {canaux}')
        if varier:
            print(json.dumps(out, ensure_ascii=False, indent=1))
    else:
        raise SystemExit(__doc__)
