"""Règles de texte communes à tout élément publié (plan, briefs vidéo, briefs visuels, titres, premiers commentaires).

Importé par cerveau/verifier.py, cerveau/relecture.py et par la copie adaptée du skill vidéo (outils/adapter-skill.py).

  problemes(texte, ou)  → liste de problèmes lisibles (vide = rien à signaler)
  textes_du_plan(plan)  → [(ref, champ, texte)] : tous les éléments textuels d'un plan (textes, accroche, titres, 1er commentaire, visuel)
  textes_du_brief(b)    → [(champ, texte)] : tous les textes d'un brief vidéo (accroches, suite, réveil, corps, notifs, scène)

RÈGLE N°5 — aucun deux-points « : » dans un texte publié (texte, accroche, titre, commentaire, visuel, vidéo) : ça ne fait pas naturel.
On écrit une phrase complète à la place (« Avant, deux photos floues. Après, une photo chaque lundi. »).

RÈGLE N°3 — aucune statistique ni résultat chiffré venant de nos clients : jamais « ×3 appels », « 100 appels »,
« en un semestre », « un de nos clients a triplé… », aucun pourcentage, aucun « résultat : … ». La preuve se fait par
une démonstration (avant / après descriptif, scène vécue, fonctionnement public de Google), jamais par un chiffre.
"""
import re

PRIX = re.compile(r'€|\bmois\b|centime|euro|\bprix\b|tarif|abonnement|par an\b', re.I)
STATS = re.compile(
    r'(?<![a-zà-ÿ])[×x]\s?\d|\d\s?[×x](?![a-zà-ÿ])|'               # ×3, x3, 3× (pas « aux 3 »)
    r'\d+\s?(appels?|clients?|devis|contacts?|nouveaux clients)\b|'  # 100 appels, 20 clients
    r'\b(semestre|trimestre)\b|'                                    # durée de mesure
    r'\bun(e)? de nos client(e)?s\b|\bnos client(e)?s (ont|a)\b|\bchez (un|une) client\b|'
    r'\b(tripl|doubl|multipli|quadrupl)[ée]s?\b|'                   # a triplé, doublé, multiplié
    r'\d+\s?%|pour ?cent|'
    r'\brésultat\s?:|\bresultat\s?:', re.I)
TELEGRAPHIQUE_MIN_MOTS = 4
VERBES = re.compile(r"\b(est|sont|a|ont|fait|font|dit|disent|parle|montre|montrent|attend|attendent|passe|passent|reste|restent|"
                    r"part|partent|appelle|appellent|cherche|cherchent|trouve|trouvent|lit|lisent|voit|voient|sort|sortent|"
                    r"répond|répondent|manque|manquent|coûte|existe|dort|vit|bouge|tue|perd|perdent|donne|change|suffit|"
                    r"aime|préfère|arrive|arrivent|laisse|laissent|reçoit|choisit|compare|regarde|regardent|ouvre|ferme|affiche|"
                    r"envoie|met|mettent|prend|prennent|tient|tombe|rate|gagne|marche|tourne|finit|commence|continue|sait|savent|"
                    r"peut|peuvent|veut|veulent|doit|doivent|faut|vient|viennent|va|vont|croit|pense|semble|paraît|fonctionne|"
                    r"bloque|oublie|publie|demande|compte|sonne|hésite|pose|traîne|tarde|repart|ignore|décide|réserve|"
                    r"[a-zéè]+(ez|ons|ent|era|ait|aient)|c'est|il y a|vous|on|se|s')\b|\bn'|\bne\b", re.I)


def problemes(texte, ou=''):
    """Contrôles mécaniques sur un élément de texte. La compréhension (sens, contradiction) relève de la relecture."""
    pb, t = [], texte or ''
    pre = f'{ou} : ' if ou else ''
    m = PRIX.search(t)
    if m: pb.append(f'{pre}prix ou abonnement (« {m.group(0)} ») — règle n°2')
    m = STATS.search(t)
    if m: pb.append(f'{pre}statistique ou résultat client (« {m.group(0)} ») — règle n°3, interdit')
    if re.search(r"\b(la|votre|sa|cette|une|ma) fiche\b(?! google)", t, re.I) and 'fiche google' not in t.lower():
        pb.append(f'{pre}« la fiche » sans « fiche Google » — règle n°1')
    if ':' in t or '：' in t:
        pb.append(f'{pre}deux-points « : » interdit (règle n°5), écrire une phrase à la place')
    return pb


def phrase_complete(texte, ou=''):
    """Un titre ou une accroche doit se lire comme une phrase : au moins 4 mots et un verbe (pas de style télégraphique)."""
    t = texte or ''
    mots = re.findall(r"[\w'’]+", t)
    if len(mots) < TELEGRAPHIQUE_MIN_MOTS:
        return [f'{ou} : trop court pour faire une phrase (« {t} »)']
    if not VERBES.search(t) and '?' not in t:
        return [f'{ou} : style télégraphique, aucun verbe (« {t} ») — écrire une vraie phrase']
    return []


def textes_du_plan(plan):
    cr = plan['creneaux'] if isinstance(plan, dict) else plan
    out = []
    for c in cr:
        ref = f"{c.get('date')} {c.get('creneau_nominal')}"
        out.append((ref, 'accroche', c.get('accroche', '')))
        out.append((ref, 'premier_commentaire', c.get('premier_commentaire', '')))
        for k in ('youtube_title', 'tiktok_title'):
            if c.get(k): out.append((ref, k, c[k]))
        for canal, t in (c.get('textes') or {}).items():
            out.append((ref, f'texte {canal}', t or ''))
        v = c.get('visuel') or {}
        for k in ('surtitre', 'titre', 'question'):
            if v.get(k): out.append((ref, f'visuel {k}', v[k]))
        for i, p in enumerate(v.get('points') or [], 1): out.append((ref, f'visuel point {i}', p))
        for i, r in enumerate(v.get('reponses') or [], 1): out.append((ref, f'visuel réponse {i}', r))
        for k, val in (v.get('carte') or {}).items(): out.append((ref, f'visuel carte {k}', str(val)))
        for i, s in enumerate(v.get('slides') or [], 2):
            out.append((ref, f'visuel slide {i} titre', s.get('titre', '')))
            out.append((ref, f'visuel slide {i} texte', s.get('texte', '')))
    return out


def textes_du_brief(b):
    out = [('probleme', b.get('probleme', ''))]
    for i, a in enumerate(b.get('accroches') or []): out.append((f'accroche {"ABC"[i] if i < 3 else i}', a))
    for k in ('suite', 'reveil', 'reveil_sous', 'corps', 'label'):
        if b.get(k): out.append((k, b[k]))
    for i, n in enumerate(b.get('notifs') or [], 1): out.append((f'notif {i}', n))
    for k, v in (b.get('desc') or {}).items(): out.append((f'desc {k}', v))
    sc = b.get('scene') or {}
    for k, v in sc.items():
        if isinstance(v, str): out.append((f'scène {k}', v))
        elif isinstance(v, list):
            for i, e in enumerate(v, 1):
                if isinstance(e, str): out.append((f'scène {k} {i}', e))
                elif isinstance(e, dict):
                    for kk, vv in e.items():
                        if isinstance(vv, str): out.append((f'scène {k} {i} {kk}', vv))
        elif isinstance(v, dict):
            for kk, vv in v.items():
                if isinstance(vv, str): out.append((f'scène {k} {kk}', vv))
    return out
