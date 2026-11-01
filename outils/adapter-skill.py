"""Copie le skill pub-motion-proenligne et l'adapte aux règles actuelles : essai gratuit, aucun prix, 3 ambiances sonores.

Ambiance : variable d'environnement PUB_AMBIANCE=0|1|2 au moment du rendu (0 = originale, 1 = +3 demi-tons sans arpège, 2 = -4 demi-tons) ;
sans la variable, elle est tirée de PUB_SLUG (ou aléatoire). Exemple : PUB_AMBIANCE=1 python3 $SK/scripts/render.py produit <slug> …

usage : python3 outils/adapter-skill.py <dossier du skill d'origine> [<dossier de la copie>]
        (copie par défaut : /home/claude/skill-pub-gratuit ; le chemin de la copie est affiché)

Ensuite, utiliser la copie comme $SK pour toutes les commandes du skill (brief.py, build.mjs, render.py).
Le skill d'origine n'est pas modifié.
"""
import json, os, shutil, sys

OFFRE = {
    'label': 'Essai gratuit',
    'bouton': 'Essayez gratuitement',
    'mention': 'Sans engagement',
    'description': '👉 Essayez Proenligne gratuitement, sans engagement.',
}
PRIX = {'14,99', '99,99', '8,33', '50'}  # montants retirés des chiffres autorisés : les contrôles du skill refuseront tout prix


def adapter(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    p = os.path.join(dst, 'data', 'proenligne.json')
    d = json.load(open(p, encoding='utf-8'))
    d['offres'] = {k: dict(OFFRE) for k in d['offres']}  # toutes les clés (essai, audit…) donnent l'essai gratuit
    d['chiffres_autorises'] = [c for c in d['chiffres_autorises'] if c not in PRIX]
    d['_adaptation'] = 'Copie adaptée par outils/adapter-skill.py : essai gratuit, aucun prix.'
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    # Ambiances sonores : 3 variantes (transposition + arpège), choisies par PUB_AMBIANCE=0|1|2 (défaut : tirée du slug)
    ps = os.path.join(dst, 'scripts', 'son.py')
    son = open(ps, encoding='utf-8').read()
    if 'PUB_AMBIANCE' not in son:
        son = son.replace("def hz(note):", """AMBIANCES = [(0, True), (3, False), (-4, True)]   # (demi-tons de transposition, arpège)
_amb = os.environ.get('PUB_AMBIANCE')
if _amb is None:
    _amb = sum(map(ord, os.environ.get('PUB_SLUG', ''))) % 3
TRANSPO, ARPEGE_ON = AMBIANCES[int(_amb) % 3]


def hz(note):""", 1)
        son = son.replace("    return 440.0 * 2 ** ((n + 12 * (octave - 4)) / 12)", "    return 440.0 * 2 ** ((n + TRANSPO + 12 * (octave - 4)) / 12)", 1)
        son = son.replace("        if b in ARPEGE:", "        if ARPEGE_ON and b in ARPEGE:", 1)
        if 'import os' not in son.split('def ')[0]:
            son = son.replace('import ', 'import os, ', 1)
        open(ps, 'w', encoding='utf-8').write(son)
    reste = [l for l in open(p, encoding='utf-8') if '€' in l]
    if reste:
        raise SystemExit('ATTENTION : un prix reste dans les données : ' + ' | '.join(reste))
    return dst


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    print(adapter(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else '/home/claude/skill-pub-gratuit'))
