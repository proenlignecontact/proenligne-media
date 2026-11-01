"""Convertit une heure de Paris en UTC (heure d'été et d'hiver gérées automatiquement).

usage : python3 outils/heure_utc.py 2026-11-02 06:30     → 2026-11-02T05:30:00Z
        python3 outils/heure_utc.py 2026-11-02            → la grille des 21 créneaux de la semaine qui commence ce lundi (54 posts : LinkedIn en plus à 13:00 du lundi au vendredi)
"""
import datetime as dt, sys
from zoneinfo import ZoneInfo

PARIS = ZoneInfo('Europe/Paris')
GRILLE = [('06:30', 'texte', 'x + facebook'), ('13:00', 'visuel', 'instagram + facebook (+ linkedin lun-ven)'), ('19:00', 'video', 'tiktok + instagram + youtube')]


def utc(date, heure):
    h, m = map(int, heure.split(':'))
    d = dt.datetime.fromisoformat(date).replace(hour=h, minute=m, tzinfo=PARIS)
    return d.astimezone(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


if __name__ == '__main__':
    if len(sys.argv) == 3:
        print(utc(sys.argv[1], sys.argv[2]))
    elif len(sys.argv) == 2:
        lundi = dt.date.fromisoformat(sys.argv[1])
        for i in range(7):
            j = (lundi + dt.timedelta(days=i)).isoformat()
            for heure, typ, canaux in GRILLE:
                print(f'{j} {heure} Paris → {utc(j, heure)}  {typ:6} {canaux}')
    else:
        raise SystemExit(__doc__)
