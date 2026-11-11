"""Repère les publications qui décollent et les inscrit dans suivi/amplifier.json (lu par la tâche hebdomadaire).

usage : python3 cerveau/amplifier.py [--jours 14] [--facteur 2.0] [--min 5] [--audience-min 50]

Règle : une publication publiée depuis au moins 20 h, dont l'audience (vues, ou portée) dépasse --facteur × la médiane
de son canal sur les --jours derniers jours (au moins --min publications mesurées sur ce canal) ET au moins --audience-min
vues (plancher absolu, décision du 11/11/2026 : 15 vues contre une médiane de 2,5 n'est pas un décollage, c'est du bruit),
est « à amplifier ».
Chaque entrée garde : fiche, canal, audience, médiane, métier, angle, ton, intention, format, accroche.
Une fiche déjà inscrite (à reprendre ou reprise) n'est pas réinscrite.
"""
import argparse, datetime as dt, glob, json, os, statistics
from zoneinfo import ZoneInfo

ICI = os.path.dirname(os.path.abspath(__file__))
AMP = os.path.join(ICI, '..', 'suivi', 'amplifier.json')
PARIS = ZoneInfo('Europe/Paris')


def dernier_releve():
    fichiers = sorted(glob.glob(os.path.join(ICI, 'stats', '*.json')))
    if not fichiers:
        return None, {}
    r = json.load(open(fichiers[-1], encoding='utf-8'))
    return dt.datetime.fromisoformat(r['releve_le'].replace('Z', '+00:00')), {p['postiz_id']: p for p in r.get('posts', [])}


def main(jours, facteur, mini, audience_min=50):
    quand, stats = dernier_releve()
    if not quand:
        print('aucun relevé'); return
    amp = json.load(open(AMP, encoding='utf-8')) if os.path.exists(AMP) else {'a_reprendre': [], 'repris': []}
    deja = {e['fiche'] for e in amp['a_reprendre'] + amp['repris']}
    lignes = []
    for f in glob.glob(os.path.join(ICI, 'productions', '*.json')):
        fi = json.load(open(f, encoding='utf-8'))
        pub = dt.datetime.fromisoformat(f"{fi['date_paris']}T{fi['heure_paris']}").replace(tzinfo=PARIS)
        age_h = (quand - pub).total_seconds() / 3600
        if not 20 <= age_h <= jours * 24:
            continue
        for p in fi.get('publications', []):
            s = stats.get(p['postiz_id'])
            if not s:
                continue
            aud = s.get('vues') if s.get('vues') is not None else s.get('portee')
            if aud is None:
                continue
            lignes.append((p['canal'], aud, fi, s))
    nouveaux = []
    for canal in {l[0] for l in lignes}:
        auds = [l[1] for l in lignes if l[0] == canal]
        if len(auds) < mini:
            continue
        med = statistics.median(auds)
        for c, aud, fi, s in lignes:
            if c != canal or fi['id'] in deja or med <= 0 or aud < facteur * med or aud < audience_min:
                continue
            nouveaux.append({'fiche': fi['id'], 'canal': canal, 'audience': aud, 'mediane_canal': med,
                             'partages': s.get('partages'), 'commentaires': s.get('commentaires'),
                             'metier': fi.get('metier'), 'angle': fi.get('angle'), 'ton': fi.get('ton'),
                             'intention': fi.get('intention'), 'format': fi.get('format'), 'creneau': fi.get('creneau'),
                             'accroche': fi.get('accroche'), 'detecte_le': quand.date().isoformat()})
            deja.add(fi['id'])
    amp['a_reprendre'] += nouveaux
    json.dump(amp, open(AMP, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'{len(lignes)} publications regardées (plancher {audience_min} vues), {len(nouveaux)} nouvelle(s) à amplifier, {len(amp["a_reprendre"])} en attente')
    for n in nouveaux:
        print(f"  → {n['fiche']} · {n['canal']} · {n['audience']} vs médiane {n['mediane_canal']:.0f}")


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--jours', type=int, default=14)
    ap.add_argument('--facteur', type=float, default=2.0)
    ap.add_argument('--min', type=int, default=5)
    ap.add_argument('--audience-min', type=int, default=50)
    a = ap.parse_args()
    main(a.jours, a.facteur, a.min, a.audience_min)
