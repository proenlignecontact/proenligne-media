"""Génère suivi/plan/2026-11-16-supp.json (textes des 14 vidéos supplémentaires de la semaine du 16/11/2026)."""
import json, os, subprocess, sys

ICI = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(ICI))
C = json.loads(subprocess.run([sys.executable, os.path.join(REPO, 'outils', 'videos-supp.py'), 'creneaux', '2026-11-16'],
                              capture_output=True, text=True).stdout)
SORTIE = os.path.join(ICI, '2026-11-16-supp.json')
ancien = {p['slug']: p for p in json.load(open(SORTIE, encoding='utf-8'))} if os.path.exists(SORTIE) else {}

E = []


def entree(slug, intention, tiktok_title, youtube_title, tiktok, instagram, facebook, youtube, x, commentaire):
    E.append(dict(slug=slug, intention=intention, tiktok_title=tiktok_title, youtube_title=youtube_title,
                  textes=dict(tiktok=tiktok, instagram=instagram, facebook=facebook, youtube=youtube, x=x),
                  premier_commentaire=commentaire))


ABO = "Abonnez-vous pour d'autres astuces sur votre fiche Google. 30 jours offerts, lien en bio."
ABO_M = "Abonnez-vous pour voir les autres métiers. 30 jours offerts, lien en bio."

# 1. lundi 10:15 — plombier, swipe, Plus de clients, Rennes
entree('supp-plombier-swipe-rennes', 'utile',
       "Plombier à Rennes, une fuite, et on fait glisser votre fiche Google",
       "Plombier à Rennes, pourquoi le client fait glisser votre fiche Google ?",
       "Plombier à Rennes, une fuite, et on fait glisser votre fiche Google.\n"
       "Le client pressé fait défiler les fiches Google sur Google Maps. Sans photo récente de chantier, il passe à la suivante.\n\n"
       "#FicheGoogle #Plombier #Rennes\n\n" + ABO,
       "Plombier à Rennes, une fuite, et on fait glisser votre fiche Google.\n\n"
       "Un lundi matin, l'eau coule sous l'évier. Le client tape « plombier » sur Google Maps et fait défiler les fiches Google, ces encadrés avec la note, les photos et le bouton Appeler.\n\n"
       "Il ne lit pas tout. Une fiche Google sans photo récente, il la fait glisser. Celle qui montre un chantier de la semaine, il s'y arrête.\n\n"
       "Proenligne publie une photo de vos chantiers chaque lundi, une publication le jeudi, et répond à vos avis.\n\n"
       "De quand date la dernière photo de chantier sur votre fiche Google ?\n\n"
       "30 jours offerts, lien en bio.\n\n"
       "#FicheGoogle #Plombier #Rennes #ReferencementLocal",
       "Plombier à Rennes, le client pressé fait glisser votre fiche Google sans s'arrêter.\n\n"
       "En urgence, on ne compare pas longtemps. Sur Google Maps, chaque plombier a sa fiche Google, avec la note, les photos et le bouton Appeler. Le pouce décide en une seconde.\n\n"
       "Une photo de chantier récente suffit souvent à faire s'arrêter le client. Une fiche Google sans photo, il la passe.\n\n"
       "Combien de photos de chantiers récents montre votre fiche Google aujourd'hui ?\n\n"
       "Essayez Proenligne gratuitement, 30 jours offerts.\n\n"
       "#FicheGoogle #Plombier #Rennes #ReferencementLocal",
       "Plombier à Rennes, une fuite, et le client fait défiler les fiches Google sur son téléphone.\n\n"
       "La fiche Google, c'est ce qui s'affiche quand on cherche « plombier » sur Google ou Google Maps, avec vos photos, vos avis et vos horaires. Sans photo récente, on passe à la suivante.\n\n"
       "Proenligne publie une photo de vos chantiers chaque lundi, une publication le jeudi, et répond à chaque avis.\n\n"
       "Quelle photo de chantier mettriez-vous en premier ?\n\n"
       "#FicheGoogle #Plombier #Rennes #ReferencementLocal",
       "Plombier à Rennes, une fuite, et on fait glisser votre fiche Google. Sans photo récente, le client passe au suivant. Proenligne publie vos chantiers chaque lundi. 30 jours offerts, lien en bio.\n\n#FicheGoogle #Plombier",
       "Une astuce de plus. Une photo prise juste après l'intervention, tuyaux propres et sol sec, parle mieux qu'une photo de catalogue. Le client voit votre vrai travail.")

# 2. lundi 16:30 — fleuriste, cinétique, Face au concurrent, Lyon
entree('supp-fleuriste-cinetique-lyon', 'utile',
       "Fleuriste à Lyon, ses bouquets sont sur sa fiche Google, et les vôtres ?",
       "Fleuriste à Lyon, ses bouquets sont sur sa fiche Google, et les vôtres ?",
       "Fleuriste à Lyon, ses bouquets sont sur sa fiche Google.\n"
       "Avant de passer, on compare souvent deux boutiques sur Google Maps. Celle qui montre les bouquets du jour donne envie de faire le détour.\n\n"
       "#FicheGoogle #Fleuriste #Lyon\n\n" + ABO,
       "Fleuriste à Lyon, ses bouquets sont sur sa fiche Google. Et les vôtres ?\n\n"
       "Une cliente cherche un bouquet pour un anniversaire. Elle tape « fleuriste » sur son téléphone. Google lui montre des fiches Google, avec la note, les photos et l'itinéraire.\n\n"
       "Chez l'autre fleuriste, on voit les compositions de la semaine. Chez vous, la devanture, et rien d'autre. Elle prend l'itinéraire vers celle qui montre ses fleurs.\n\n"
       "Proenligne montre vos créations sur votre fiche Google chaque semaine, avec une photo le lundi et une publication le jeudi.\n\n"
       "Quel bouquet de la semaine aimeriez-vous montrer en premier ?\n\n"
       "30 jours offerts, lien en bio.\n\n"
       "#FicheGoogle #Fleuriste #Lyon #ReferencementLocal",
       "Fleuriste à Lyon, la boutique d'à côté montre ses bouquets sur sa fiche Google.\n\n"
       "Cherchez « fleuriste » dans votre ville. Les encadrés avec une note et des photos sont des fiches Google. La vôtre en fait partie, à côté de celles de vos voisins.\n\n"
       "Une cliente qui hésite entre deux boutiques choisit souvent celle dont elle a déjà vu les fleurs. Une fiche Google sans composition récente ne lui donne aucune raison de venir.\n\n"
       "Vos dernières compositions sont-elles visibles sur votre fiche Google ?\n\n"
       "Essayez Proenligne gratuitement, 30 jours offerts.\n\n"
       "#FicheGoogle #Fleuriste #Lyon #ReferencementLocal",
       "Fleuriste à Lyon, ses bouquets sont sur sa fiche Google. Et les vôtres ?\n\n"
       "Votre fiche Google, c'est la carte de visite que Google montre à votre place, avec vos photos, vos avis, vos horaires et l'itinéraire. Une cliente qui compare deux boutiques regarde d'abord les fleurs.\n\n"
       "Proenligne publie une photo de vos créations le lundi, une publication le jeudi, et répond à chaque avis.\n\n"
       "Quelle composition montreriez-vous cette semaine ?\n\n"
       "#FicheGoogle #Fleuriste #Lyon #ReferencementLocal",
       "Fleuriste à Lyon, ses bouquets sont sur sa fiche Google. Et les vôtres ? Une cliente qui compare deux boutiques va souvent vers celle qui montre ses fleurs. 30 jours offerts, lien en bio.\n\n#FicheGoogle #Fleuriste",
       "Une idée simple. Photographiez une composition le matin, à la lumière du jour près de la vitrine. Les couleurs sont plus justes, et la cliente reconnaît votre boutique en arrivant.")

# 3. mardi 10:00 — couvreur, cinétique, Plus d'appels, Nantes
entree('supp-couvreur-appels-nantes', 'utile',
       "Couvreur à Nantes, après l'orage, on lit votre fiche Google",
       "Couvreur à Nantes, après l'orage, que montre votre fiche Google ?",
       "Couvreur à Nantes, après l'orage, on lit votre fiche Google.\n"
       "Une tuile envolée, et le propriétaire cherche un couvreur sur Google Maps. Sans photo de toiture sur votre fiche Google, il hésite à vous appeler.\n\n"
       "#FicheGoogle #Couvreur #Nantes\n\n" + ABO,
       "Couvreur à Nantes, après l'orage, on lit votre fiche Google.\n\n"
       "Le vent est tombé dans la nuit. Au matin, il manque des tuiles et une tache apparaît au plafond. Le propriétaire tape « couvreur » sur Google Maps.\n\n"
       "Il ouvre des fiches Google, ces encadrés avec la note, les photos et le bouton Appeler. Il cherche des toitures refaites, des chantiers récents, quelqu'un qui a l'air de travailler en ce moment.\n\n"
       "Proenligne publie une photo de vos toitures chaque lundi, une publication le jeudi, et répond à chaque avis.\n\n"
       "Combien de photos de toiture montre votre fiche Google aujourd'hui ?\n\n"
       "30 jours offerts, lien en bio.\n\n"
       "#FicheGoogle #Couvreur #Nantes #ReferencementLocal",
       "Couvreur à Nantes, après un coup de vent, c'est votre fiche Google qu'on ouvre d'abord.\n\n"
       "Quand on cherche un couvreur en urgence, on ne connaît souvent personne. Sur Google Maps, chaque entreprise a sa fiche Google, avec la note, les photos et le bouton Appeler. C'est elle qui donne confiance, ou pas.\n\n"
       "Une fiche Google avec des toitures récentes rassure. Une fiche Google sans photo laisse le client hésiter, et il appelle souvent le suivant.\n\n"
       "Quelle est la dernière toiture que vous avez montrée sur votre fiche Google ?\n\n"
       "Essayez Proenligne gratuitement, 30 jours offerts.\n\n"
       "#FicheGoogle #Couvreur #Nantes #ReferencementLocal",
       "Couvreur à Nantes, après l'orage, le client lit votre fiche Google avant d'appeler.\n\n"
       "La fiche Google, c'est l'encadré qui présente votre entreprise sur Google et Google Maps, avec vos photos, vos avis et votre numéro. Sans photo de toiture, le client hésite.\n\n"
       "Proenligne publie une photo de vos toitures chaque lundi, une publication le jeudi, et répond à chaque avis.\n\n"
       "Vous photographiez vos toitures avant et après le chantier ?\n\n"
       "#FicheGoogle #Couvreur #Nantes #ReferencementLocal",
       "Couvreur à Nantes, après l'orage, on lit votre fiche Google avant d'appeler. Sans photo de toiture, on hésite. Proenligne publie vos toitures chaque lundi. 30 jours offerts, lien en bio.\n\n#FicheGoogle #Couvreur",
       "Une précision utile. Une photo prise depuis le sol, avec toute la toiture dans le cadre, se comprend mieux sur un téléphone qu'un gros plan sur trois tuiles.")

# 4. mardi 16:45 — esthéticienne, plan-séquence, Plus de clients, Lille
entree('supp-estheticienne-classement-lille', 'utile',
       "Esthéticienne à Lille, où êtes-vous sur Google ?",
       "Esthéticienne à Lille, où apparaît votre fiche Google quand on cherche un institut ?",
       "Esthéticienne à Lille, où êtes-vous sur Google ?\n"
       "Tapez « esthéticienne Lille ». La cliente réserve souvent dans l'institut qu'elle voit en premier sur les fiches Google.\n\n"
       "#FicheGoogle #Estheticienne #Lille\n\n" + ABO,
       "Esthéticienne à Lille, où êtes-vous sur Google ?\n\n"
       "Faites le test sur votre téléphone. Tapez « esthéticienne Lille » sur Google Maps. Les encadrés avec la note, les photos et les horaires sont des fiches Google. Cherchez la vôtre.\n\n"
       "Une cliente qui découvre le quartier ne fait pas défiler toute la liste. Elle regarde les premières fiches Google, compare les photos de soins, et réserve souvent là.\n\n"
       "Proenligne montre vos soins sur votre fiche Google chaque semaine, avec une photo le lundi et une publication le jeudi, et répond à chaque avis.\n\n"
       "Vous avez fait le test ? Votre institut apparaît où ?\n\n"
       "30 jours offerts, lien en bio.\n\n"
       "#FicheGoogle #Estheticienne #Lille #ReferencementLocal",
       "Esthéticienne à Lille, quand une cliente cherche un institut, votre fiche Google apparaît-elle ?\n\n"
       "Quand on tape « esthéticienne près de moi », Google affiche des fiches Google avec photos, avis et horaires. La vôtre en fait partie, quelque part dans la liste.\n\n"
       "On réserve souvent l'institut qu'on a vu en premier, surtout s'il montre ses soins. Une fiche Google sans photo récente se remarque moins.\n\n"
       "Quel soin aimeriez-vous que vos futures clientes voient en premier ?\n\n"
       "Essayez Proenligne gratuitement, 30 jours offerts.\n\n"
       "#FicheGoogle #Estheticienne #Lille #ReferencementLocal",
       "Esthéticienne à Lille, où êtes-vous sur Google ?\n\n"
       "Votre fiche Google, c'est ce qui s'affiche quand une cliente cherche « esthéticienne » sur Google ou Google Maps, avec vos photos, vos avis et vos horaires. Les premières fiches Google sont souvent celles qu'on compare.\n\n"
       "Proenligne publie une photo de vos soins le lundi, une publication le jeudi, et répond à chaque avis.\n\n"
       "Quand avez-vous cherché votre institut sur Google pour la dernière fois ?\n\n"
       "#FicheGoogle #Estheticienne #Lille #ReferencementLocal",
       "Esthéticienne à Lille, où êtes-vous sur Google ? Tapez « esthéticienne Lille » et cherchez votre fiche Google. On réserve souvent l'institut qu'on voit en premier. 30 jours offerts, lien en bio.\n\n#FicheGoogle #Estheticienne",
       "Pour faire le test sans fausser le résultat, cherchez depuis le téléphone d'une amie, ou en navigation privée. Votre propre téléphone connaît déjà votre institut.")

# 5. mercredi 09:45 — maçon, plan-séquence, Du temps libre, Lorient
entree('supp-macon-semaine-lorient', 'utile',
       "Maçon à Lorient, combien de soirées pour votre fiche Google ?",
       "Maçon à Lorient, combien de soirées par semaine pour votre fiche Google ?",
       "Maçon à Lorient, combien de soirées pour votre fiche Google ?\n"
       "Après le chantier, il reste les photos à trier et à publier, les avis à lire. Tout ça finit souvent le soir.\n\n"
       "#FicheGoogle #Macon #Lorient\n\n" + ABO,
       "Maçon à Lorient, combien de soirées passez-vous sur votre fiche Google ?\n\n"
       "Il est 22 h. La bétonnière est lavée, les outils sont dans le camion. Sur le canapé, vous ouvrez votre fiche Google, l'encadré que les clients voient sur Google Maps avant de demander un devis.\n\n"
       "Il faut choisir une photo du mur monté aujourd'hui, l'envoyer, répondre à l'avis d'un client content. Un peu chaque soir, et la semaine y passe.\n\n"
       "Proenligne s'en charge pendant vos chantiers, avec une photo le lundi, une publication le jeudi et une réponse à chaque avis.\n\n"
       "À quel moment de la journée vous occupez-vous de votre fiche Google ?\n\n"
       "30 jours offerts, lien en bio.\n\n"
       "#FicheGoogle #Macon #Lorient #ReferencementLocal",
       "Maçon à Lorient, votre fiche Google vous prend-elle vos soirées ?\n\n"
       "Sur Google Maps, chaque maçon a sa fiche Google, avec la note, les photos et le bouton Appeler. Pour qu'elle montre vos chantiers, il faut publier, et répondre aux avis.\n\n"
       "Dans une petite entreprise de maçonnerie, ce travail tombe presque toujours le soir, après la journée sur le chantier.\n\n"
       "Le soir, vous la faites plutôt tout de suite, ou le week-end ?\n\n"
       "Essayez Proenligne gratuitement, 30 jours offerts.\n\n"
       "#FicheGoogle #Macon #Lorient #ReferencementLocal",
       "Maçon à Lorient, combien de soirées passez-vous sur votre fiche Google ?\n\n"
       "La fiche Google, c'est ce qui apparaît quand un client cherche un maçon sur Google ou Google Maps, avec vos photos, vos avis et vos horaires. La tenir à jour finit souvent tard, après le chantier.\n\n"
       "Proenligne publie une photo le lundi, une publication le jeudi, et répond à chaque avis, pendant que vous êtes sur le chantier.\n\n"
       "Et vous, qui s'occupe de la fiche Google dans votre entreprise ?\n\n"
       "#FicheGoogle #Macon #Lorient #ReferencementLocal",
       "Maçon à Lorient, combien de soirées pour votre fiche Google ? Photos du chantier, avis à lire… Proenligne s'en charge pendant vos chantiers. Le soir, la truelle reste rangée. 30 jours offerts, lien en bio.\n\n#FicheGoogle #Macon",
       "Un bon réflexe qui ne prend pas de soirée. Prenez une photo du chantier avant de partir, tous les jours au même endroit. En fin de semaine, vous avez déjà de quoi montrer l'avancement.")

# 6. mercredi 16:15 — fromager, swipe, Face au concurrent, Vannes
entree('supp-fromager-swipe-vannes', 'utile',
       "Fromager à Vannes, votre fiche Google tient face au voisin ?",
       "Fromager à Vannes, votre fiche Google tient-elle face à celle du voisin ?",
       "Fromager à Vannes, votre fiche Google tient face au voisin ?\n"
       "Même note, mais lui montre ses plateaux sur sa fiche Google. On fait le détour vers celui dont on a vu le comptoir.\n\n"
       "#FicheGoogle #Fromager #Vannes\n\n" + ABO_M,
       "Fromager à Vannes, votre fiche Google tient-elle face au voisin ?\n\n"
       "Un samedi, un couple prépare un repas avec des amis. Il cherche « fromager » sur Google Maps et voit deux fiches Google, ces encadrés avec la note, les photos et l'itinéraire.\n\n"
       "Même note pour les deux. Mais chez le voisin, on voit le comptoir, les plateaux, la tomme de la semaine. Chez vous, rien qu'une devanture. Il prend l'itinéraire vers le voisin.\n\n"
       "Proenligne montre vos fromages sur votre fiche Google chaque semaine, avec une photo le lundi et une publication le jeudi.\n\n"
       "Quel fromage de votre comptoir mériterait sa photo cette semaine ?\n\n"
       "30 jours offerts, lien en bio.\n\n"
       "#FicheGoogle #Fromager #Vannes #ReferencementLocal",
       "Fromager à Vannes, face au voisin, que montre votre fiche Google ?\n\n"
       "Quand on cherche une fromagerie, Google affiche des fiches Google avec la note, les photos et l'itinéraire. Les clients comparent souvent deux boutiques avant de se déplacer.\n\n"
       "À note égale, on va plus volontiers chez celui dont on a déjà vu le comptoir. Une fiche Google sans photo de fromages ne donne pas envie de faire le détour.\n\n"
       "Vos clients voient-ils vos fromages avant de pousser votre porte ?\n\n"
       "Essayez Proenligne gratuitement, 30 jours offerts.\n\n"
       "#FicheGoogle #Fromager #Vannes #ReferencementLocal",
       "Fromager à Vannes, votre fiche Google tient-elle face au voisin ?\n\n"
       "Cherchez « fromager » dans votre ville. Les encadrés avec une note et des photos sont des fiches Google. À note égale, c'est souvent le comptoir en photo qui décide le détour.\n\n"
       "Proenligne publie une photo de vos fromages le lundi, une publication le jeudi, et répond à chaque avis.\n\n"
       "Quel plateau montreriez-vous en premier ?\n\n"
       "#FicheGoogle #Fromager #Vannes #ReferencementLocal",
       "Fromager à Vannes, votre fiche Google tient face au voisin ? Même note, mais lui montre ses plateaux. Proenligne montre vos fromages chaque semaine. 30 jours offerts, lien en bio.\n\n#FicheGoogle #Fromager",
       "Une astuce de comptoir. Une photo du plateau du jour avec l'étiquette du fromage bien lisible aide le client à savoir quoi demander en arrivant.")

# 7. jeudi 10:30 — chauffagiste, swipe, Du temps libre, Toulouse
entree('supp-chauffagiste-swipe-toulouse', 'utile',
       "Chauffagiste à Toulouse, le soir, votre fiche Google attend encore",
       "Chauffagiste à Toulouse, en pleine saison, qui s'occupe de votre fiche Google le soir ?",
       "Chauffagiste à Toulouse, le soir, votre fiche Google attend encore.\n"
       "Les chaudières le jour, les avis et les photos le soir. En pleine saison, la pile ne descend jamais.\n\n"
       "#FicheGoogle #Chauffagiste #Toulouse\n\n" + ABO,
       "Chauffagiste à Toulouse, le soir, votre fiche Google attend encore.\n\n"
       "Novembre, les premiers froids. Les dépannages s'enchaînent toute la journée. Le soir, il reste votre fiche Google, l'encadré que les clients ouvrent sur Google Maps quand leur chaudière s'arrête.\n\n"
       "Un avis à remercier, une photo de la chaudière posée cet après-midi, des horaires à vérifier. La pile se remplit plus vite qu'elle ne se vide.\n\n"
       "Proenligne s'occupe des photos et des réponses à votre place, avec une photo le lundi, une publication le jeudi et une réponse à chaque avis.\n\n"
       "En pleine saison, vous rangez le téléphone à quelle heure ?\n\n"
       "30 jours offerts, lien en bio.\n\n"
       "#FicheGoogle #Chauffagiste #Toulouse #ReferencementLocal",
       "Chauffagiste à Toulouse, en pleine saison, qui répond aux avis de votre fiche Google ?\n\n"
       "Quand la chaudière tombe en panne, le client ouvre Google Maps. Chaque chauffagiste y a sa fiche Google, avec la note, les avis et le bouton Appeler.\n\n"
       "C'est justement quand vous avez le moins de temps que les avis arrivent. Et un avis sans réponse reste visible longtemps.\n\n"
       "Vous répondez à vos avis le soir, ou vous attendez la fin de la saison ?\n\n"
       "Essayez Proenligne gratuitement, 30 jours offerts.\n\n"
       "#FicheGoogle #Chauffagiste #Toulouse #ReferencementLocal",
       "Chauffagiste à Toulouse, le soir, votre fiche Google attend encore.\n\n"
       "Sur Google Maps, chaque chauffagiste a sa fiche Google, avec la note, les photos et le bouton Appeler. C'est elle qu'on regarde avant de vous appeler. La tenir à jour en pleine saison prend vite des soirées.\n\n"
       "Proenligne publie une photo le lundi, une publication le jeudi, et répond à chaque avis à votre place.\n\n"
       "Combien de soirées par semaine y passez-vous en ce moment ?\n\n"
       "#FicheGoogle #Chauffagiste #Toulouse #ReferencementLocal",
       "Chauffagiste à Toulouse, le soir, votre fiche Google attend encore. Les chaudières le jour, les avis le soir. Proenligne s'occupe des photos et des réponses. 30 jours offerts, lien en bio.\n\n#FicheGoogle #Chauffagiste",
       "Une précision pour l'hiver. Si vous faites des dépannages le samedi, indiquez-le dans les horaires de votre fiche Google. Le client en panne regarde souvent cette ligne avant d'appeler.")

# 8. jeudi 16:00 — toiletteur, cinétique, Face au concurrent, Brest (preuve)
entree('supp-toiletteur-cinetique-brest', 'preuve',
       "Toiletteur à Brest, sa fiche Google montre ses toilettages, et la vôtre ?",
       "Toiletteur à Brest, le maître choisit la fiche Google qui montre les toilettages",
       "Toiletteur à Brest, sa fiche Google montre ses toilettages.\n"
       "Chez le salon voisin, on voit les chiens avant et après. Le maître qui compare sait déjà ce qu'il va obtenir.\n\n"
       "#FicheGoogle #Toiletteur #Brest\n\n" + ABO_M,
       "Toiletteur à Brest, sa fiche Google montre ses toilettages. Et la vôtre ?\n\n"
       "Prenons un exemple imaginaire, le salon de toilettage Martin. Avant, sa fiche Google montrait la vitrine, et c'était tout. Un maître qui cherchait un toiletteur ne savait pas à quoi s'attendre.\n\n"
       "Après, chaque lundi, une photo avant et après. Un caniche bien coupé, un berger démêlé, un chiot pour sa première visite. Le maître voit le travail avant de prendre rendez-vous.\n\n"
       "La fiche Google, c'est l'encadré que Google affiche avec la note, les photos et le numéro du salon. C'est souvent là qu'on compare.\n\n"
       "Vos photos avant et après sont-elles sur votre fiche Google ?\n\n"
       "30 jours offerts, lien en bio.\n\n"
       "#FicheGoogle #Toiletteur #Brest #ReferencementLocal",
       "Toiletteur à Brest, le salon voisin montre ses toilettages sur sa fiche Google.\n\n"
       "Sur Google Maps, chaque salon a sa fiche Google, avec la note, les photos et les avis. Un maître qui confie son chien pour la première fois a besoin d'être rassuré.\n\n"
       "Avant, une fiche Google avec une seule photo de devanture. Après, des photos avant et après chaque semaine. La note est la même, mais le maître voit enfin à qui il confie son chien.\n\n"
       "Quelle photo avant et après montreriez-vous en premier ?\n\n"
       "Essayez Proenligne gratuitement, 30 jours offerts.\n\n"
       "#FicheGoogle #Toiletteur #Brest #ReferencementLocal",
       "Toiletteur à Brest, sa fiche Google montre ses toilettages. Et la vôtre ?\n\n"
       "Votre fiche Google, c'est ce qui s'affiche quand un maître cherche « toiletteur » sur Google ou Google Maps, avec vos photos, vos avis et vos horaires. Des photos avant et après rassurent avant un premier rendez-vous.\n\n"
       "Proenligne publie une photo le lundi, une publication le jeudi, et répond à chaque avis.\n\n"
       "Vous prenez les chiens en photo avant et après le toilettage ?\n\n"
       "#FicheGoogle #Toiletteur #Brest #ReferencementLocal",
       "Toiletteur à Brest, sa fiche Google montre ses toilettages. Et la vôtre ? Des photos avant et après rassurent le maître qui compare. Proenligne les publie chaque semaine. 30 jours offerts, lien en bio.\n\n#FicheGoogle #Toiletteur",
       "Une précision. Pour une photo avant et après, gardez le même fond et le même angle. La différence se voit tout de suite, même en petit sur un téléphone.")

# 9. vendredi 09:30 — serrurier, cinétique, Plus d'appels, Quimper
entree('supp-serrurier-appels-quimper', 'utile',
       "Serrurier à Quimper, votre fiche Google rassure en urgence ?",
       "Serrurier à Quimper, votre fiche Google rassure-t-elle le client en urgence ?",
       "Serrurier à Quimper, votre fiche Google rassure en urgence ?\n"
       "Bloqué dehors, le client ne connaît personne. Il appelle celui dont la fiche Google a l'air sérieuse, avec des avis qui ont une réponse.\n\n"
       "#FicheGoogle #Serrurier #Quimper\n\n" + ABO,
       "Serrurier à Quimper, votre fiche Google rassure-t-elle en urgence ?\n\n"
       "Il pleut, la porte vient de claquer, les clés sont restées à l'intérieur. Le client tape « serrurier » sur Google Maps. Il voit des fiches Google, avec la note, les avis et le bouton Appeler.\n\n"
       "Dans l'urgence, il a peur de tomber sur n'importe qui. Il cherche des photos de vrais dépannages, des avis récents, des réponses. Il appelle celui qui rassure.\n\n"
       "Proenligne publie vos dépannages sur votre fiche Google, une photo le lundi et une publication le jeudi, et répond à chaque avis.\n\n"
       "Selon vous, qu'est-ce qui rassure le plus un client bloqué dehors ?\n\n"
       "30 jours offerts, lien en bio.\n\n"
       "#FicheGoogle #Serrurier #Quimper #ReferencementLocal",
       "Serrurier à Quimper, en urgence, le client appelle celui qui rassure sur Google.\n\n"
       "Avant d'appeler un serrurier, le client ouvre sa fiche Google sur Google Maps et lit les avis, les horaires et vos réponses. Dans l'urgence, il cherche surtout à éviter une mauvaise surprise.\n\n"
       "Une fiche Google avec des photos de dépannages et des avis qui ont une réponse inspire confiance. Une fiche Google vide le laisse hésiter.\n\n"
       "Vos derniers avis ont-ils tous une réponse ?\n\n"
       "Essayez Proenligne gratuitement, 30 jours offerts.\n\n"
       "#FicheGoogle #Serrurier #Quimper #ReferencementLocal",
       "Serrurier à Quimper, votre fiche Google rassure-t-elle en urgence ?\n\n"
       "La fiche Google, c'est l'encadré qui présente votre entreprise sur Google et Google Maps, avec la note, les avis et le bouton Appeler. Bloqué dehors, le client y cherche des signes de sérieux.\n\n"
       "Proenligne publie vos dépannages le lundi, une publication le jeudi, et répond à chaque avis.\n\n"
       "Quel détail de votre fiche Google rassure le plus, d'après vous ?\n\n"
       "#FicheGoogle #Serrurier #Quimper #ReferencementLocal",
       "Serrurier à Quimper, votre fiche Google rassure en urgence ? Bloqué dehors, le client appelle celui qui a l'air sérieux. Proenligne publie vos dépannages et répond aux avis. 30 jours offerts, lien en bio.\n\n#FicheGoogle #Serrurier",
       "Un détail qui compte. Une photo de vous avec votre véhicule identifié montre au client qu'il appelle une vraie entreprise du coin, pas un numéro inconnu.")

# 10. vendredi 17:00 — pressing, swipe, Plus de clients, Angers
entree('supp-pressing-swipe-angers', 'utile',
       "Pressing à Angers, on fait glisser votre fiche Google ?",
       "Pressing à Angers, votre fiche Google donne-t-elle envie de passer ?",
       "Pressing à Angers, on fait glisser votre fiche Google ?\n"
       "Pas d'horaires, pas de photo, et le client passe au pressing suivant sur Google Maps.\n\n"
       "#FicheGoogle #Pressing #Angers\n\n" + ABO,
       "Pressing à Angers, on fait glisser votre fiche Google ?\n\n"
       "Un costume à nettoyer avant un mariage. Le client tape « pressing » sur son téléphone et fait défiler les fiches Google, ces encadrés avec la note, les photos, les horaires et l'itinéraire.\n\n"
       "Il veut savoir deux choses. Êtes-vous ouvert à l'heure où il passe, et a-t-il envie de vous confier sa veste ? Sans horaires ni photo, il fait glisser vers le suivant.\n\n"
       "Proenligne montre votre boutique sur votre fiche Google chaque semaine, avec une photo le lundi et une publication le jeudi.\n\n"
       "Vos horaires du samedi sont-ils justes sur votre fiche Google ?\n\n"
       "30 jours offerts, lien en bio.\n\n"
       "#FicheGoogle #Pressing #Angers #ReferencementLocal",
       "Pressing à Angers, votre fiche Google donne-t-elle envie de passer ?\n\n"
       "Cherchez « pressing » dans votre ville. Les encadrés avec une note, des photos et un itinéraire sont des fiches Google. On y vérifie surtout les horaires avant de se déplacer.\n\n"
       "Une fiche Google avec des horaires justes et une photo de la boutique donne envie de faire le détour. Sans cela, on passe au suivant.\n\n"
       "Quand avez-vous vérifié vos horaires sur votre fiche Google ?\n\n"
       "Essayez Proenligne gratuitement, 30 jours offerts.\n\n"
       "#FicheGoogle #Pressing #Angers #ReferencementLocal",
       "Pressing à Angers, on fait glisser votre fiche Google ?\n\n"
       "Votre fiche Google, c'est ce que vos clients voient en premier quand ils cherchent « pressing » sur Google Maps, avec vos photos, vos horaires et l'itinéraire. Sans horaires ni photo, on passe.\n\n"
       "Proenligne publie une photo de votre boutique le lundi, une publication le jeudi, et répond à chaque avis.\n\n"
       "Quelle photo de votre boutique mettriez-vous en premier ?\n\n"
       "#FicheGoogle #Pressing #Angers #ReferencementLocal",
       "Pressing à Angers, on fait glisser votre fiche Google ? Pas d'horaires, pas de photo, et le client passe au suivant. Proenligne montre votre boutique chaque semaine. 30 jours offerts, lien en bio.\n\n#FicheGoogle #Pressing",
       "Une astuce simple. Ajoutez vos horaires exceptionnels avant les jours fériés. Le client qui voit « ouvert » et trouve porte close ne revient pas toujours.")

# 11. samedi 10:15 — paysagiste, plan-séquence, Du temps libre, Caen
entree('supp-paysagiste-semaine-caen', 'utile',
       "Paysagiste à Caen, votre fiche Google mange vos soirées ?",
       "Paysagiste à Caen, en hiver, la fiche Google mange-t-elle vos soirées ?",
       "Paysagiste à Caen, la fiche Google mange vos soirées ?\n"
       "La nuit tombe tôt, la journée de chantier finit, et les avis attendent encore sur votre fiche Google.\n\n"
       "#FicheGoogle #Paysagiste #Caen\n\n" + ABO,
       "Paysagiste à Caen, la fiche Google mange vos soirées ?\n\n"
       "En novembre, la nuit tombe tôt. Les haies sont taillées, la remorque est vidée. Le soir, il reste votre fiche Google, l'encadré qu'un client ouvre sur Google Maps avant de vous confier son jardin.\n\n"
       "Une photo de la haie du jour à publier, deux avis auxquels répondre. Ce n'est jamais long, mais c'est tous les soirs.\n\n"
       "Proenligne publie vos jardins et répond aux avis à votre place, avec une photo le lundi et une publication le jeudi.\n\n"
       "Le soir, vous rangez les gants à quelle heure ?\n\n"
       "30 jours offerts, lien en bio.\n\n"
       "#FicheGoogle #Paysagiste #Caen #ReferencementLocal",
       "Paysagiste à Caen, qui tient votre fiche Google le soir ?\n\n"
       "La fiche Google, c'est la carte de visite que Google montre à votre place, avec vos photos, vos avis, vos horaires et votre téléphone. Elle demande un peu d'attention chaque semaine.\n\n"
       "Dans une entreprise de paysage, cette attention tombe souvent le soir, après le chantier, quand on aimerait plutôt souffler.\n\n"
       "Vous vous en occupez le soir, ou plutôt le dimanche ?\n\n"
       "Essayez Proenligne gratuitement, 30 jours offerts.\n\n"
       "#FicheGoogle #Paysagiste #Caen #ReferencementLocal",
       "Paysagiste à Caen, la fiche Google mange vos soirées ?\n\n"
       "Sur Google Maps, chaque paysagiste a sa fiche Google, avec la note, les photos de jardins et le bouton Appeler. La tenir vivante prend quelques minutes, mais chaque soir.\n\n"
       "Proenligne publie une photo le lundi, une publication le jeudi, et répond à chaque avis à votre place.\n\n"
       "Combien de temps passez-vous sur votre fiche Google chaque semaine ?\n\n"
       "#FicheGoogle #Paysagiste #Caen #ReferencementLocal",
       "Paysagiste à Caen, la fiche Google mange vos soirées ? La nuit tombe tôt et les avis attendent. Proenligne publie vos jardins et répond aux avis à votre place. 30 jours offerts, lien en bio.\n\n#FicheGoogle #Paysagiste",
       "Une idée pour l'hiver. Les chantiers de saison, une haie taillée ou un massif paillé, montrent que l'entreprise travaille toute l'année, pas seulement au printemps.")

# 12. samedi 16:15 — carrossier, swipe, Face au concurrent, Tours (preuve)
entree('supp-carrossier-swipe-tours', 'preuve',
       "Carrossier à Tours, sa fiche Google montre ses réparations, et la vôtre ?",
       "Carrossier à Tours, deux fiches Google, la même note, laquelle choisit-on ?",
       "Carrossier à Tours, sa fiche Google montre ses réparations. Et la vôtre ?\n"
       "Même note, mais chez lui on voit son travail. L'automobiliste garde la fiche Google qui montre des ailes refaites.\n\n"
       "#FicheGoogle #Carrossier #Tours\n\n" + ABO_M,
       "Carrossier à Tours, sa fiche Google montre ses réparations. Et la vôtre ?\n\n"
       "Un pare-chocs enfoncé sur un parking. L'automobiliste cherche « carrossier » sur Google Maps et compare deux fiches Google, avec la note, les photos et le bouton Appeler.\n\n"
       "Même note pour les deux. Chez l'autre carrossier, on voit une aile avant et après, une portière remise à neuf. Chez vous, la façade de l'atelier. Il garde celle où il voit le travail.\n\n"
       "Proenligne publie vos réparations sur votre fiche Google chaque semaine, avec une photo le lundi et une publication le jeudi.\n\n"
       "Quelle réparation de la semaine montreriez-vous ?\n\n"
       "30 jours offerts, lien en bio.\n\n"
       "#FicheGoogle #Carrossier #Tours #ReferencementLocal",
       "Carrossier à Tours, deux fiches Google, la même note. Laquelle choisit-on ?\n\n"
       "Sur Google Maps, chaque atelier a sa fiche Google, avec la note, les photos et le bouton Appeler. C'est elle qu'on regarde avant de confier sa voiture.\n\n"
       "Avant, une fiche Google avec la façade et rien d'autre. Après, une réparation en photo chaque semaine, avant et après. La note n'a pas bougé, mais l'automobiliste voit enfin ce que vous savez faire.\n\n"
       "Vous photographiez vos voitures avant de les rendre ?\n\n"
       "Essayez Proenligne gratuitement, 30 jours offerts.\n\n"
       "#FicheGoogle #Carrossier #Tours #ReferencementLocal",
       "Carrossier à Tours, même note sur Google, mais lequel choisit-on ?\n\n"
       "Quand on tape « carrossier près de moi », Google affiche des fiches Google avec photos, avis et horaires. À note égale, celle qui montre des réparations récentes donne plus confiance.\n\n"
       "Proenligne publie une photo de vos réparations le lundi, une publication le jeudi, et répond à chaque avis.\n\n"
       "Quelle réparation mettriez-vous en premier sur votre fiche Google ?\n\n"
       "#FicheGoogle #Carrossier #Tours #ReferencementLocal",
       "Carrossier à Tours, même note que le voisin sur Google. Mais sa fiche Google montre ses réparations. Proenligne publie les vôtres chaque semaine. 30 jours offerts, lien en bio.\n\n#FicheGoogle #Carrossier",
       "Une astuce de photo. Prenez l'avant et l'après sous le même éclairage, à la même distance. Un reflet net sur la carrosserie montre le travail mieux qu'un long texte.")

# 13. dimanche 10:00 — menuisier, cinétique, Du temps libre, Bordeaux
entree('supp-menuisier-cinetique-bordeaux', 'utile',
       "Menuisier à Bordeaux, encore sur votre fiche Google à 22 h ?",
       "Menuisier à Bordeaux, encore sur votre fiche Google à 22 h ?",
       "Menuisier à Bordeaux, encore sur votre fiche Google à 22 h ?\n"
       "L'atelier est balayé, mais il reste les photos et les avis sur votre fiche Google, celle que vos clients voient sur Google Maps.\n\n"
       "#FicheGoogle #Menuisier #Bordeaux\n\n" + ABO,
       "Menuisier à Bordeaux, encore sur votre fiche Google à 22 h ?\n\n"
       "L'atelier est propre, les machines sont coupées. À la maison, vous ouvrez votre fiche Google, l'encadré qu'un client regarde sur Google Maps avant de vous demander un placard ou un escalier.\n\n"
       "Il faudrait publier la photo de l'escalier livré cette semaine, et remercier le client pour son avis. Ça attendra encore un soir.\n\n"
       "Proenligne s'en occupe en journée, avec une photo le lundi, une publication le jeudi et une réponse à chaque avis. Le soir, vous dînez enfin à votre table.\n\n"
       "La dernière réalisation que vous avez publiée, c'était quoi ?\n\n"
       "30 jours offerts, lien en bio.\n\n"
       "#FicheGoogle #Menuisier #Bordeaux #ReferencementLocal",
       "Menuisier à Bordeaux, le soir, votre fiche Google vous attend ?\n\n"
       "Votre fiche Google, c'est ce qui s'affiche quand un client cherche « menuisier » sur Google ou Google Maps, avec vos photos, vos avis et vos horaires. Elle montre votre savoir-faire, si on la fait vivre.\n\n"
       "Le problème, c'est le moment. Après une journée à l'atelier, publier une photo et répondre aux avis passe souvent après le reste.\n\n"
       "Vous publiez vos réalisations le jour de la pose, ou bien plus tard ?\n\n"
       "Essayez Proenligne gratuitement, 30 jours offerts.\n\n"
       "#FicheGoogle #Menuisier #Bordeaux #ReferencementLocal",
       "Menuisier à Bordeaux, encore sur votre fiche Google à 22 h ?\n\n"
       "La fiche Google, c'est l'encadré qui présente votre atelier sur Google et Google Maps, avec vos photos, vos avis et votre numéro. La tenir à jour finit souvent le soir.\n\n"
       "Proenligne publie une photo le lundi, une publication le jeudi, et répond à chaque avis, pendant que vous êtes à l'atelier.\n\n"
       "Quelle réalisation de l'année montreriez-vous en premier ?\n\n"
       "#FicheGoogle #Menuisier #Bordeaux #ReferencementLocal",
       "Menuisier à Bordeaux, encore sur votre fiche Google à 22 h ? Photos, avis… Proenligne s'en occupe en journée. Le soir, vous dînez enfin à votre table. 30 jours offerts, lien en bio.\n\n#FicheGoogle #Menuisier",
       "Une astuce d'atelier. Gardez un coin de mur clair près de l'établi pour vos photos de pièces finies. Le bois ressort mieux, et toutes vos photos ont le même style.")

# 14. dimanche 16:30 — boulangerie, plan-séquence, Face au concurrent, Saint-Brieuc (offre)
entree('supp-boulangerie-duel-saint-brieuc', 'offre',
       "Boulangerie à Saint-Brieuc, et la fiche Google d'en face ?",
       "Boulangerie à Saint-Brieuc, votre fiche Google face à celle d'en face",
       "Boulangerie à Saint-Brieuc, et la fiche Google d'en face ?\n"
       "En face, on voit la vitrine du matin sur sa fiche Google. Proenligne montre vos viennoiseries chaque semaine.\n\n"
       "#FicheGoogle #Boulangerie #SaintBrieuc\n\n" + ABO,
       "Boulangerie à Saint-Brieuc, et la fiche Google d'en face ?\n\n"
       "Sur Google Maps, chaque boulangerie a sa fiche Google, avec la note, les photos, les horaires et l'itinéraire. En face, on voit la vitrine du matin. Chez vous, on ne voit pas encore vos viennoiseries.\n\n"
       "Avec Proenligne, chaque semaine\n"
       "✅ une photo de votre vitrine ou de vos pains est publiée le lundi\n"
       "✅ une publication paraît le jeudi\n"
       "✅ chaque avis reçoit une réponse, et vous validez celles aux avis négatifs\n\n"
       "Essayez Proenligne gratuitement, 30 jours offerts, sans engagement. Lien en bio.\n\n"
       "#FicheGoogle #Boulangerie #SaintBrieuc #ReferencementLocal",
       "Boulangerie à Saint-Brieuc, la boulangerie d'en face montre sa vitrine sur sa fiche Google.\n\n"
       "Quand on arrive dans un quartier, on cherche souvent la boulangerie sur son téléphone. Google affiche alors des fiches Google, avec la note, les photos et l'itinéraire. Le matin, c'est souvent la vitrine en photo qui décide.\n\n"
       "Avec Proenligne, chaque semaine\n"
       "✅ une photo de vos pains ou de vos viennoiseries le lundi\n"
       "✅ une publication le jeudi\n"
       "✅ une réponse à chaque avis, validée par vous si l'avis est négatif\n\n"
       "Essayez Proenligne gratuitement, 30 jours offerts, sans engagement.\n\n"
       "#FicheGoogle #Boulangerie #SaintBrieuc #ReferencementLocal",
       "Boulangerie à Saint-Brieuc, et la fiche Google d'en face ?\n\n"
       "Cherchez « boulangerie » dans votre ville. Les encadrés avec une note et des photos sont des fiches Google. Celle qui montre sa vitrine du matin donne envie d'entrer.\n\n"
       "Proenligne publie une photo de vos viennoiseries le lundi, une publication le jeudi, et répond à chaque avis. Essayez gratuitement, 30 jours offerts, sans engagement.\n\n"
       "#FicheGoogle #Boulangerie #SaintBrieuc #ReferencementLocal",
       "Boulangerie à Saint-Brieuc, et la fiche Google d'en face ? Elle montre sa vitrine du matin. Proenligne montre vos viennoiseries chaque semaine et répond à vos avis. 30 jours offerts, sans engagement, lien en bio.\n\n#FicheGoogle",
       "Pour essayer, tout passe par le lien en bio. Les 30 jours sont offerts et sans engagement, la boulangerie reste libre d'arrêter quand elle veut.")

assert len(E) == len(C) == 14
for e, c in zip(E, C):
    e['utc'], e['heure_paris'] = c['utc'], c['heure_paris']
    e['media'] = (ancien.get(e['slug']) or {}).get('media') or {}
ordre = ['slug', 'utc', 'heure_paris', 'intention', 'tiktok_title', 'youtube_title', 'textes', 'premier_commentaire', 'media']
json.dump([{k: e[k] for k in ordre} for e in E], open(SORTIE, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('écrit', SORTIE)
