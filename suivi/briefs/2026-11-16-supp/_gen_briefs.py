import json, os
D = os.path.dirname(os.path.abspath(__file__))
T = json.load(open(os.path.join(D, '..', '..', 'plan', '2026-11-16-supp-videos.json'), encoding='utf-8'))
def V(p, b1, b2, o): return [{"scene": "Probleme", "texte": p}, {"scene": "Bascule", "texte": b1}, {"scene": "Bascule", "texte": b2, "ancre": 3.0}, {"scene": "Offre", "texte": o}]
B = [
 dict(slug="supp-plombier-swipe-rennes", ville="Rennes", entreprise="",
      accroches=["Plombier à Rennes, une fuite, et on fait glisser votre fiche Google.", "Plombier à Rennes, votre fiche Google retient-elle le client pressé ?"],
      voix=V("Sans photo récente, on passe au suivant.", "Pro en ligne publie vos chantiers chaque lundi.", "Cette fois, le client s'arrête sur vous.", "Trente jours offerts, lien en bio."),
      offre_ligne="Vos chantiers, *chaque lundi sur Google.*"),
 dict(slug="supp-fleuriste-cinetique-lyon", valeur="L'autre fleuriste",
      accroches=["Fleuriste à Lyon, ses bouquets sont sur sa *fiche Google*.", "Fleuriste à Lyon, quelle *fiche Google* donne envie ?"],
      voix=V("Chez elle, on voit les bouquets du jour.", "Pro en ligne montre vos créations chaque semaine.", "Et c'est chez vous qu'on vient choisir.", "Essayez trente jours offerts, le lien est en bio."),
      offre_ligne="Vos bouquets, *vus avant la visite.*"),
 dict(slug="supp-couvreur-appels-nantes", valeur="0",
      accroches=["Couvreur à Nantes, après l'orage, on lit votre *fiche Google*.", "Couvreur à Nantes, votre *fiche Google* montre vos toitures ?"],
      voix=V("Sans photo de toiture, on hésite à appeler.", "Pro en ligne publie vos toitures chaque lundi.", "Et c'est votre numéro qu'on compose.", "Trente jours offerts, le lien vous attend en bio."),
      offre_ligne="Vos toitures, *en photo chaque lundi.*"),
 dict(slug="supp-estheticienne-classement-lille", entreprise="", lieu="",
      accroches=["Où êtes-vous sur *Google ?*", "Vous êtes *sur Google ?*"],
      accroches_dites=["Tapez esthéticienne Lille. Où êtes-vous sur Google ?", "Esthéticienne à Lille, on vous voit sur Google ?"],
      voix=V("On réserve souvent l'institut qu'on voit en premier.", "Pro en ligne montre vos soins chaque semaine.", "Et les clientes découvrent enfin votre institut.", "Trente jours offerts, c'est le lien en bio."),
      offre_ligne="Vos soins, *vus avant le rendez-vous.*"),
 dict(slug="supp-macon-semaine-lorient", entreprise="", lieu="",
      accroches=["Maçon à Lorient, combien de soirées pour la *fiche Google ?*", "Maçon à Lorient, la *fiche Google* vous prend vos soirées ?"],
      voix=V("Après le chantier, restent les photos à publier.", "Pro en ligne s'en charge pendant vos chantiers.", "Le soir, la truelle reste rangée.", "Profitez de trente jours offerts, lien en bio."),
      offre_ligne="La truelle rangée, *la soirée à vous.*"),
 dict(slug="supp-fromager-swipe-vannes", entreprise="",
      accroches=["Fromager à Vannes, votre fiche Google tient face au voisin ?", "Fromager à Vannes, entre deux fiches Google, laquelle donne envie d'entrer ?"],
      voix=V("Lui montre ses plateaux, vous, rien du tout.", "Pro en ligne montre vos fromages chaque semaine.", "Cette fois, on fait le détour jusqu'à vous.", "Trente jours offerts, lien en bio."),
      offre_ligne="Votre comptoir, *vu depuis Google.*"),
 dict(slug="supp-chauffagiste-swipe-toulouse", entreprise="",
      accroches=["Chauffagiste à Toulouse, le soir, votre fiche Google attend encore.", "Chauffagiste à Toulouse, après les dépannages, qui répond sur votre fiche Google ?"],
      voix=V("Les chaudières le jour, les avis le soir.", "Pro en ligne s'occupe des photos et des réponses.", "Et vos soirées d'hiver restent au chaud.", "Testez trente jours offerts, lien en bio."),
      offre_ligne="Les soirées d'hiver, *au chaud.*"),
 dict(slug="supp-toiletteur-cinetique-brest", valeur="Le salon voisin",
      accroches=["Toiletteur à Brest, sa *fiche Google* montre ses toilettages.", "Toiletteur à Brest, votre *fiche Google* rassure les maîtres ?"],
      voix=V("Chez lui, on voit les chiens avant et après.", "Pro en ligne montre vos toilettages chaque semaine.", "Et les maîtres vous confient leur chien.", "Trente jours offerts, le lien se trouve en bio."),
      offre_ligne="Vos toilettages, *avant et après.*"),
 dict(slug="supp-serrurier-appels-quimper", valeur="0",
      accroches=["Serrurier à Quimper, votre *fiche Google* rassure en urgence ?", "Serrurier à Quimper, votre *fiche Google* inspire confiance ?"],
      voix=V("En urgence, on appelle celui qui rassure.", "Pro en ligne publie vos dépannages et répond aux avis.", "Et le client bloqué dehors compose votre numéro.", "Trente jours offerts, lien en bio."),
      offre_ligne="Vos dépannages, *vus avant l'appel.*"),
 dict(slug="supp-pressing-swipe-angers", entreprise="",
      accroches=["Pressing à Angers, on fait glisser votre fiche Google ?", "Pressing à Angers, votre fiche Google donne-t-elle envie de passer ?"],
      voix=V("Pas d'horaires, pas de photo, on passe.", "Pro en ligne montre votre boutique chaque semaine.", "Et cette fois, on garde votre fiche Google.", "Trente jours offerts, le lien est en bio."),
      offre_ligne="Votre boutique, *sur le chemin.*"),
 dict(slug="supp-paysagiste-semaine-caen", entreprise="", lieu="",
      accroches=["Paysagiste à Caen, la *fiche Google* mange vos soirées ?", "Paysagiste à Caen, le soir, qui tient la *fiche Google ?*"],
      voix=V("La nuit tombe tôt, et les avis attendent.", "Pro en ligne publie vos jardins et répond aux avis.", "Le soir, vous rangez enfin les gants.", "Trente jours offerts, le lien attend en bio."),
      offre_ligne="Le sécateur rangé, *le soir à vous.*"),
 dict(slug="supp-carrossier-swipe-tours", entreprise="",
      accroches=["Carrossier à Tours, sa fiche Google montre ses réparations, et la vôtre ?", "Carrossier à Tours, deux fiches Google, la même note, laquelle choisit-on ?"],
      voix=V("Même note, mais lui, on voit son travail.", "Pro en ligne publie vos réparations chaque semaine.", "Cette fois, c'est votre atelier qu'on garde.", "Trente jours offerts, lien en bio."),
      offre_ligne="Vos réparations, *en photo.*"),
 dict(slug="supp-menuisier-cinetique-bordeaux", valeur="22 h",
      accroches=["Menuisier à Bordeaux, encore sur la *fiche Google* ?", "Menuisier à Bordeaux, le soir, la *fiche Google* vous attend ?"],
      voix=V("L'atelier est propre, restent les photos et les avis.", "Pro en ligne s'en occupe en journée.", "Le soir, vous dînez enfin à votre table.", "Trente jours offerts, le lien est en bio."),
      offre_ligne="L'atelier fermé, *la soirée à table.*"),
 dict(slug="supp-boulangerie-duel-saint-brieuc", entreprise="", lieu="",
      accroches=["Boulangerie à Saint-Brieuc, et la *fiche Google* d'en face ?", "Boulangerie à Saint-Brieuc, votre *fiche Google* donne faim ?"],
      voix=V("En face, on voit la vitrine du matin.", "Pro en ligne montre vos viennoiseries chaque semaine.", "Et le matin, c'est chez vous qu'on entre.", "Profitez-en, trente jours offerts, lien en bio."),
      offre_ligne="Vos viennoiseries, *vues dès le matin.*"),
]
for t, b in zip(T, B):
    f = os.path.join(D, b['slug'] + '.json')
    old = json.load(open(f, encoding='utf-8')) if os.path.exists(f) else {}
    out = {"slug": b['slug'], "moteur": t['moteur'], "angle": t['angle'], "metier": t['metier'], "ville": b.get('ville', t['ville']), "ambiance": t['ambiance']}
    out.update({k: v for k, v in b.items() if k not in ('slug', 'ville')})
    out["musique"] = True
    if old.get('audio_src'): out['audio_src'] = old['audio_src']
    json.dump(out, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok')
