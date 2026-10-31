"""Copie le skill pub-motion-proenligne et l'adapte aux règles actuelles : essai gratuit, aucun prix.

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
    reste = [l for l in open(p, encoding='utf-8') if '€' in l]
    if reste:
        raise SystemExit('ATTENTION : un prix reste dans les données : ' + ' | '.join(reste))
    return dst


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    print(adapter(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else '/home/claude/skill-pub-gratuit'))
