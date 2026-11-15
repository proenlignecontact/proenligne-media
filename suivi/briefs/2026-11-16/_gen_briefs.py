# Générateur des briefs vidéo de la semaine du 2026-11-16 (tirage suivi/plan/2026-11-16-videos.json)
import json, os
ICI = os.path.dirname(os.path.abspath(__file__))
B = [
 {"slug": "garage-soiree-avis-angers", "moteur": "cinetique", "angle": "Du temps libre", "metier": "garagiste", "ville": "Angers", "ambiance": 1,
  "valeur": "21h52",
  "accroches": ["Garagiste à Angers, l'atelier ferme, pas votre *fiche Google*.", "Garagiste à Angers, qui répond à vos *avis Google* le soir ?"],
  "voix": [{"scene": "Probleme", "texte": "Les voitures sont rendues, il reste les avis."},
           {"scene": "Bascule", "texte": "Pro en ligne répond à chaque avis pour vous."},
           {"scene": "Bascule", "texte": "Le soir, l'atelier est fermé, et vous aussi.", "ancre": 3.0},
           {"scene": "Offre", "texte": "Trente jours offerts, le lien est en bio."}],
  "offre_ligne": "Vos soirées, *loin de l'atelier.*", "musique": True},
 {"slug": "serrurier-duel-tours", "moteur": "plan-sequence", "angle": "Face au concurrent", "metier": "serrurier", "ville": "Tours", "ambiance": 2,
  "entreprise": "", "lieu": "",
  "accroches": ["Serrurier à Tours, pourquoi on appelle l'autre sur *Google* ?", "Serrurier à Tours, le client compare deux *fiches Google*."],
  "voix": [{"scene": "Probleme", "texte": "Sa fiche Google répond aux avis. La vôtre, non."},
           {"scene": "Bascule", "texte": "Pro en ligne répond à chacun de vos avis."},
           {"scene": "Bascule", "texte": "Et le client bloqué dehors vous appelle, vous.", "ancre": 3.0},
           {"scene": "Offre", "texte": "Essayez trente jours offerts, lien en bio."}],
  "offre_ligne": "Une *fiche Google* qui rassure.", "musique": True},
 {"slug": "autoecole-swipe-appels-caen", "moteur": "swipe", "angle": "Plus d'appels", "metier": "auto-école", "ville": "Caen", "ambiance": 0,
  "entreprise": "",
  "accroches": ["Auto-école à Caen, en pleine leçon, on passe votre fiche Google.", "Auto-école à Caen, un futur élève compare les fiches Google avant d'appeler."],
  "voix": [{"scene": "Probleme", "texte": "Pas de photo des voitures, on passe."},
           {"scene": "Bascule", "texte": "Pro en ligne montre vos voitures."},
           {"scene": "Bascule", "texte": "Et ce coup-ci, c'est vous qu'on appelle.", "ancre": 3.0},
           {"scene": "Offre", "texte": "Le lien est en bio, trente jours offerts."}],
  "offre_ligne": "Votre auto-école, *bien en vue.*", "musique": True},
 {"slug": "electricien-soirees-saint-brieuc", "moteur": "cinetique", "angle": "Du temps libre", "metier": "électricien", "ville": "Saint-Brieuc", "ambiance": 1,
  "valeur": "23h05",
  "accroches": ["Électricien à Saint-Brieuc, la *fiche Google* vous attend ?", "Électricien à Saint-Brieuc, *Google* vous garde tard ?"],
  "voix": [{"scene": "Probleme", "texte": "Après le chantier, il reste vos avis."},
           {"scene": "Bascule", "texte": "Pro en ligne publie et répond en journée."},
           {"scene": "Bascule", "texte": "Le soir, vous débranchez, vous aussi.", "ancre": 3.0},
           {"scene": "Offre", "texte": "Testez trente jours offerts, lien en bio."}],
  "offre_ligne": "Le soir, *vous débranchez.*", "musique": True},
 {"slug": "boulangerie-classement-bordeaux", "moteur": "plan-sequence", "angle": "Plus de clients", "metier": "boulangerie", "ville": "Bordeaux", "ambiance": 2,
  "entreprise": "", "lieu": "",
  "accroches": ["Votre pain, sur *Google ?*", "Et vous, sur *Google ?*"],
  "accroches_dites": ["Boulangerie à Bordeaux, votre pain est sur Google ?", "On cherche une boulangerie à Bordeaux. Et vous, sur Google ?"],
  "voix": [{"scene": "Probleme", "texte": "On entre souvent dans la première qu'on voit."},
           {"scene": "Bascule", "texte": "Pro en ligne montre votre vitrine chaque semaine."},
           {"scene": "Bascule", "texte": "Et c'est votre porte qu'on pousse.", "ancre": 3.0},
           {"scene": "Offre", "texte": "C'est trente jours offerts, le lien est en bio."}],
  "offre_ligne": "Votre vitrine, *aussi sur Google.*", "musique": True},
 {"slug": "plombier-swipe-appels-montpellier", "moteur": "swipe", "angle": "Plus d'appels", "metier": "plombier", "ville": "Montpellier", "ambiance": 0,
  "entreprise": "",
  "accroches": ["« Au suivant. » Plombier à Montpellier, on passe votre fiche Google.", "Plombier à Montpellier, votre fiche Google donne-t-elle envie d'appeler ?"],
  "voix": [{"scene": "Probleme", "texte": "Une photo ancienne, et le doigt glisse."},
           {"scene": "Bascule", "texte": "Pro en ligne montre vos chantiers."},
           {"scene": "Bascule", "texte": "Cette fois, le pouce appuie sur Appeler.", "ancre": 3.0},
           {"scene": "Offre", "texte": "Profitez de trente jours offerts, lien en bio."}],
  "offre_ligne": "Des chantiers *qui se voient.*", "musique": True},
 {"slug": "coiffeuse-duel-le-mans", "moteur": "cinetique", "angle": "Face au concurrent", "metier": "coiffeuse", "ville": "Le Mans", "ambiance": 1,
  "valeur": "Le salon d'à côté",
  "accroches": ["Coiffeuse sur Le Mans, sa *fiche Google* montre ses coupes.", "Coiffeuse sur Le Mans, on réserve à côté sur *Google* ?"],
  "voix": [{"scene": "Probleme", "texte": "Elle publie ses coupes. Vous, rien depuis l'été."},
           {"scene": "Bascule", "texte": "Pro en ligne montre vos coupes."},
           {"scene": "Bascule", "texte": "Et la cliente pousse votre porte.", "ancre": 3.0},
           {"scene": "Offre", "texte": "Trente jours offerts, lien en bio."}],
  "offre_ligne": "Vos plus belles coupes, *en vitrine.*", "musique": True},
]
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
