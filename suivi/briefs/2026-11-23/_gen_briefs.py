# Générateur des briefs vidéo de la semaine du 2026-11-23 (tirage suivi/plan/2026-11-23-videos.json ; Le Mans → Brest)
import json, os
ICI = os.path.dirname(os.path.abspath(__file__))
B = [
 {"slug": "estheticienne-swipe-clients-lyon", "moteur": "swipe", "angle": "Plus de clients", "metier": "esthéticienne", "ville": "Lyon", "ambiance": 1,
  "entreprise": "",
  "accroches": ["Esthéticienne à Lyon, votre nouveau soin est sur votre fiche Google ?", "Esthéticienne à Lyon, on passe votre fiche Google sans s'arrêter ?"],
  "voix": [{"scene": "Probleme", "texte": "Rien de nouveau, alors on passe."},
           {"scene": "Bascule", "texte": "Pro en ligne montre vos soins."},
           {"scene": "Bascule", "texte": "Et la cliente s'arrête chez vous.", "ancre": 3.0},
           {"scene": "Offre", "texte": "Trente jours offerts, le lien est en bio."}],
  "offre_ligne": "Vos soins, *enfin visibles.*", "musique": True},
 {"slug": "chauffagiste-appels-nantes", "moteur": "cinetique", "angle": "Plus d'appels", "metier": "chauffagiste", "ville": "Nantes", "ambiance": 2,
  "valeur": "0",
  "accroches": ["Chauffagiste à Nantes, votre *fiche Google* est prête ?", "Chauffagiste à Nantes, on vous trouve sur *Google* cet hiver ?"],
  "voix": [{"scene": "Probleme", "texte": "Avant d'appeler, on regarde votre fiche Google."},
           {"scene": "Bascule", "texte": "Pro en ligne la fait vivre chaque semaine."},
           {"scene": "Bascule", "texte": "Et quand il fait froid, c'est vous qu'on appelle.", "ancre": 3.0},
           {"scene": "Offre", "texte": "Essayez trente jours offerts, lien en bio."}],
  "offre_ligne": "Cet hiver, *votre téléphone sonne.*", "musique": True},
 {"slug": "paysagiste-semaine-lille", "moteur": "plan-sequence", "angle": "Du temps libre", "metier": "paysagiste", "ville": "Lille", "ambiance": 0,
  "entreprise": "", "lieu": "",
  "accroches": ["Paysagiste à Lille, vos soirées partent sur *Google* ?", "Paysagiste à Lille, la *fiche Google* prend vos soirées ?"],
  "voix": [{"scene": "Probleme", "texte": "Après le chantier, il reste encore les avis."},
           {"scene": "Bascule", "texte": "Pro en ligne s'en charge pendant la journée."},
           {"scene": "Bascule", "texte": "Le soir, le jardin, c'est le vôtre.", "ancre": 3.0},
           {"scene": "Offre", "texte": "C'est trente jours offerts, le lien est en bio."}],
  "offre_ligne": "Vos soirées *vous reviennent.*", "musique": True},
 {"slug": "plombier-swipe-concurrent-brest", "moteur": "swipe", "angle": "Face au concurrent", "metier": "plombier", "ville": "Brest", "ambiance": 1,
  "entreprise": "",
  "accroches": ["Plombier à Brest, le voisin a votre note, mais sa fiche Google vit.", "Plombier à Brest, entre deux fiches Google, laquelle garde-t-on ?"],
  "voix": [{"scene": "Probleme", "texte": "La vôtre n'a rien de neuf."},
           {"scene": "Bascule", "texte": "Pro en ligne publie vos chantiers."},
           {"scene": "Bascule", "texte": "Et cette fois, c'est la sienne qui tombe.", "ancre": 3.0},
           {"scene": "Offre", "texte": "Lien en bio, et trente jours offerts."}],
  "offre_ligne": "Une *fiche Google* qui tient tête.", "musique": True},
 {"slug": "garage-appels-lorient", "moteur": "cinetique", "angle": "Plus d'appels", "metier": "garagiste", "ville": "Lorient", "ambiance": 2,
  "valeur": "0",
  "accroches": ["Garagiste à Lorient, on vous appelle depuis *Google* ?", "Garagiste à Lorient, votre *fiche Google* rassure ?"],
  "voix": [{"scene": "Probleme", "texte": "Une panne, et on compare les fiches Google."},
           {"scene": "Bascule", "texte": "Pro en ligne montre votre atelier chaque semaine."},
           {"scene": "Bascule", "texte": "Et c'est votre numéro qu'on compose.", "ancre": 3.0},
           {"scene": "Offre", "texte": "Testez trente jours offerts, lien en bio."}],
  "offre_ligne": "Le bon garage, *c'est le vôtre.*", "musique": True},
 {"slug": "electricien-classement-vannes", "moteur": "plan-sequence", "angle": "Plus de clients", "metier": "électricien", "ville": "Vannes", "ambiance": 0,
  "entreprise": "", "lieu": "",
  "accroches": ["Et vous, sur *Google* ?", "On vous voit sur *Google* ?"],
  "accroches_dites": ["Électricien à Vannes, et vous, sur Google, vous êtes où ?", "Électricien à Vannes, on vous voit sur Google ?"],
  "voix": [{"scene": "Probleme", "texte": "Les premières fiches Google reçoivent les appels."},
           {"scene": "Bascule", "texte": "Pro en ligne fait vivre la vôtre chaque semaine."},
           {"scene": "Bascule", "texte": "Et les clients du coin tombent sur vous.", "ancre": 3.0},
           {"scene": "Offre", "texte": "Le lien est en bio, trente jours offerts."}],
  "offre_ligne": "Votre fiche Google, *enfin réveillée.*", "musique": True},
 {"slug": "autoecole-swipe-soirees-toulouse", "moteur": "swipe", "angle": "Du temps libre", "metier": "auto-école", "ville": "Toulouse", "ambiance": 1,
  "entreprise": "",
  "accroches": ["Auto-école à Toulouse, la journée finit, pas votre fiche Google.", "Auto-école à Toulouse, vos soirées passent sur votre fiche Google ?"],
  "voix": [{"scene": "Probleme", "texte": "Les avis et les photos s'empilent."},
           {"scene": "Bascule", "texte": "Pro en ligne vide la pile."},
           {"scene": "Bascule", "texte": "Ce soir, vous restez libre.", "ancre": 3.0},
           {"scene": "Offre", "texte": "Profitez de trente jours offerts, lien en bio."}],
  "offre_ligne": "Vos soirées, *sans la fiche Google.*", "musique": True},
]

def P(slug, path, val):
    b = next(x for x in B if x['slug'] == slug)
    k, i, sub = path
    if sub: b[k][i][sub] = val
    else: b[k][i] = val


# ───────── CORRECTIONS ─────────

# passe 1
P('chauffagiste-appels-nantes', ('accroches', 0, None), 'Chauffagiste à Nantes, votre *fiche Google* est-elle à jour ?')  # e017731
P('chauffagiste-appels-nantes', ('voix', 2, 'texte'), 'Quand il fait froid, votre fiche Google rassure le client.')  # eec2fa3
P('estheticienne-swipe-clients-lyon', ('accroches', 1, None), 'Esthéticienne à Lyon, votre fiche Google arrête la cliente ?')  # e4634c5
P('estheticienne-swipe-clients-lyon', ('voix', 0, 'texte'), 'La cliente ne voit rien de neuf et passe.')  # ebb03b1
P('paysagiste-semaine-lille', ('accroches', 0, None), 'Paysagiste à Lille, le soir, vous gérez votre *fiche Google* ?')  # e88a3bf
P('paysagiste-semaine-lille', ('voix', 1, 'texte'), "Pro en ligne s'en charge à votre place.")  # ee5b5ba
P('plombier-swipe-concurrent-brest', ('voix', 0, 'texte'), 'Et la vôtre, elle montre quoi de neuf ?')  # e1015b3
P('plombier-swipe-concurrent-brest', ('voix', 2, 'texte'), "Cette fois, c'est le voisin qu'on passe.")  # e24e5af
P('autoecole-swipe-soirees-toulouse', ('accroches', 0, None), 'Auto-école à Toulouse, après les leçons, votre fiche Google attend encore.')  # ef44181
P('electricien-classement-vannes', ('voix', 0, 'texte'), 'Souvent, on appelle les premières fiches Google.')  # eb09b0e
P('electricien-classement-vannes', ('voix', 2, 'texte'), 'Et les clients du coin voient une entreprise active.')  # efc66d0
P('garage-appels-lorient', ('voix', 2, 'texte'), "Et votre fiche Google donne envie d'appeler.")  # e04d77a

for b in B:
    p = os.path.join(ICI, b['slug'] + '.json')
    if os.path.exists(p):
        old = json.load(open(p, encoding='utf-8'))
        b['audio_src'] = old.get('audio_src', {})
        for k in old:
            if k.startswith('_') or k in ('calage',): b[k] = old[k]
    b.setdefault('audio_src', {})
    json.dump(b, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'briefs')
