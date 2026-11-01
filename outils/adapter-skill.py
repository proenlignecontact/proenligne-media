"""Copie le skill pub-motion-proenligne et l'adapte aux règles actuelles : essai gratuit, aucun prix, aucune statistique client
(règle n°3 : angle « preuve » et chiffres ×3 / 100 / 6 retirés, contrôle regles_texte injecté dans brief.py valider), 3 ambiances sonores.

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
STATS = {'×3', '100', '6'}  # règle n°3 : aucun résultat chiffré de nos clients (×3 appels, 100 appels, 6 mois)
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def adapter(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    p = os.path.join(dst, 'data', 'proenligne.json')
    d = json.load(open(p, encoding='utf-8'))
    d['offres'] = {k: dict(OFFRE) for k in d['offres']}  # toutes les clés (essai, audit…) donnent l'essai gratuit
    d['chiffres_autorises'] = [c for c in d['chiffres_autorises'] if c not in PRIX and c not in STATS]
    d['_adaptation'] = 'Copie adaptée par outils/adapter-skill.py : essai gratuit, aucun prix, aucune statistique client (règle n°3).'
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    # Angle « preuve » retiré du tirage (il reposait sur ×3 appels / 100 appels / 6 mois)
    pi = os.path.join(dst, 'data', 'ingredients.json')
    ing = json.load(open(pi, encoding='utf-8'))
    ing['angles'] = [a for a in ing['angles'] if a != 'preuve']
    json.dump(ing, open(pi, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    # Règles de texte du dépôt (n°1, n°2, n°3 + phrases complètes) injectées dans brief.py valider
    pb_ = os.path.join(dst, 'scripts', 'brief.py')
    bp = open(pb_, encoding='utf-8').read()
    if 'regles_texte' not in bp:
        bp = bp.replace("import check  # noqa: E402", f"import check  # noqa: E402\nsys.path.insert(0, {REPO + '/cerveau'!r})\nimport regles_texte  # noqa: E402  (règles n°1-2-3 du dépôt proenligne-media)", 1)
        bp = bp.replace("    pb += [f'nom propre à vérifier dans les titres : {w}' for w in check.names_problems(titres)]",
                        "    pb += [f'nom propre à vérifier dans les titres : {w}' for w in check.names_problems(titres)]\n"
                        "    for champ_, txt_ in regles_texte.textes_du_brief(b):\n"
                        "        pb += regles_texte.problemes(txt_, champ_)\n"
                        "    for i_, a_ in enumerate(b['accroches']):\n"
                        "        pb += regles_texte.phrase_complete(a_, f'accroche {\"ABC\"[i_] if i_ < 3 else i_}')\n"
                        "    pb += regles_texte.phrase_complete(b['suite'], 'suite')", 1)
        open(pb_, 'w', encoding='utf-8').write(bp)
    # SKILL.md : la ligne « Preuve » du skill d'origine ne s'applique plus
    sk = os.path.join(dst, 'SKILL.md')
    md = open(sk, encoding='utf-8').read().replace("- **Preuve** : l'angle `preuve` s'appuie uniquement sur ×3 appels, 100 appels et 6 mois.",
        "- **Aucune statistique client** (règle n°3) : l'angle `preuve` est retiré ; jamais ×3 appels, 100 appels, « en 6 mois », « un de nos clients a… ». La scène Contraste montre le problème, pas un résultat chiffré.\n- **Titres = vraies phrases** : `suite` et chaque accroche ont un sujet et un verbe et se comprennent seules (pas « Nouveauté tue sur votre fiche Google, clients partis »).")
    open(sk, 'w', encoding='utf-8').write(md)
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
