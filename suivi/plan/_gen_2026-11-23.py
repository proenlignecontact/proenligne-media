# Générateur du plan de la semaine du 2026-11-23 (écrit par la tâche hebdomadaire ; source des textes)
import json, subprocess, os
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
LUNDI = '2026-11-23'
p_grille = os.path.join(ICI, f'_grille_{LUNDI}.json')
if os.path.exists(p_grille):          # heures réelles tirées une seule fois (reprise sans nouveau tirage)
    grille = json.load(open(p_grille, encoding='utf-8'))
else:
    grille = json.loads(subprocess.check_output(['python3', os.path.join(RACINE, 'outils/heure_utc.py'), LUNDI, '--varier']))
    json.dump(grille, open(p_grille, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
H = {(g['date'], g['creneau_nominal']): g for g in grille}
TYPE = {'13:00': 'visuel', '19:00': 'video'}
C = []


def add(date, nominal, **kw):
    if nominal == '12:30':
        g = {'heure': '12:30', 'utc': subprocess.check_output(['python3', os.path.join(RACINE, 'outils/heure_utc.py'), date, '12:30']).decode().strip()}
        typ = 'video'
    else:
        g = H[(date, nominal)]; typ = TYPE[nominal]
    c = {'date': date, 'creneau_nominal': nominal, 'heure': g['heure'], 'utc': g['utc'], 'creneau': typ, 'offre': 'essai'}
    c.update(kw)
    c.setdefault('media', {})
    C.append(c)


L, M, ME, J, V, S, D = '2026-11-23', '2026-11-24', '2026-11-25', '2026-11-26', '2026-11-27', '2026-11-28', '2026-11-29'
ABO = "Abonnez-vous pour d'autres astuces sur votre fiche Google. 30 jours offerts, lien en bio."
ABO2 = "Abonnez-vous pour voir les autres métiers et leur fiche Google. 30 jours offerts, lien en bio."

# ───────────────────────── LUNDI 23 ─────────────────────────
# Reprise amplifiée (esthéticienne « nouveau soin caché », YouTube 98 vues) : même angle sur un autre métier, en carrousel.
add(L, '13:00', intention='utile', metier='coiffeur', angle='peur-de-perdre', format='conseil', ton='scene', symptome='service-invisible',
    slug='coiffeur-nouvelle-prestation-invisible',
    accroche="Il est 22 h. Le salon est balayé, mais votre nouvelle prestation n'apparaît nulle part sur votre fiche Google.",
    premier_commentaire="Une précision utile. Dans la rubrique Services de votre fiche Google, donnez à la prestation le nom que vos clients emploient, par exemple « balayage » plutôt qu'un nom maison.",
    visuel={'gabarit': 'conseil', 'surtitre': 'Coiffeurs, une nouveauté sur votre fiche Google', 'titre': 'Trois gestes pour montrer une nouvelle prestation sur votre fiche Google',
            'mot': 'nouvelle prestation',
            'points': ["Ajoutez la prestation dans la rubrique Services",
                       "Publiez une photo du résultat, avec l'accord du client",
                       "Annoncez-la dans une publication courte"],
            'cta': 'question', 'question': 'Votre dernière nouveauté est-elle déjà sur votre fiche Google ?',
            'slides': [
                {'type': 'point', 'numero': '1', 'titre': 'Une rubrique faite pour ça', 'texte': "La rubrique Services de votre fiche Google liste ce que vous proposez. Une prestation absente reste invisible."},
                {'type': 'point', 'numero': '2', 'titre': 'Une photo vaut une explication', 'texte': "Un balayage ou une coupe réussie, photographiés de dos et à la lumière du jour, parlent d'eux-mêmes."},
                {'type': 'point', 'numero': '3', 'titre': 'Une publication pour la lancer', 'texte': "Deux phrases suffisent pour dire ce qui est nouveau au salon et pour qui c'est fait."},
                {'type': 'fin', 'titre': 'Et chez vous ?', 'texte': "Quelle est la dernière prestation que vous avez ajoutée au salon ?"}]},
    textes={
        'instagram': "Il est 22 h. Le salon est balayé, mais votre nouvelle prestation n'apparaît nulle part sur votre fiche Google.\n\nVous avez appris une nouvelle technique, vous en parlez à vos clients fidèles. Mais une personne qui tape « coiffeur » et sa ville sur Google Maps voit seulement votre fiche Google, avec vos photos, vos avis et vos services. Ce qui n'y est pas, elle ne le devine pas.\n\nTrois gestes pour la montrer.\n1. Ajoutez la prestation dans la rubrique Services.\n2. Publiez une photo du résultat, avec l'accord du client.\n3. Annoncez-la dans une publication courte.\n\nQuelle est la dernière prestation que vous avez ajoutée au salon ?\n\n#FicheGoogle #Coiffeur #Coiffure #ReferencementLocal #GoogleBusinessProfile",
    })

add(L, '19:00', intention='utile', metier='estheticienne', angle='peur-de-perdre', format='recherche', ton='replique', symptome='service-invisible',
    slug='estheticienne-swipe-clients-lyon',
    accroche="« Elle ne fait pas ce soin, on passe. » Esthéticienne à Lyon, votre nouveau soin manque sur votre fiche Google.",
    premier_commentaire="Une astuce simple. Ajoutez chaque nouveau soin dans la rubrique Services de votre fiche Google le jour où vous le lancez, avec une phrase qui dit à qui il s'adresse.",
    tiktok_title="Esthéticienne à Lyon, votre nouveau soin est-il sur votre fiche Google ?",
    youtube_title="Esthéticienne, votre nouveau soin est-il visible sur votre fiche Google ?",
    textes={
        'tiktok': "« Elle ne fait pas ce soin, on passe. » Esthéticienne à Lyon, votre nouveau soin manque sur votre fiche Google.\nSur Google Maps, la cliente fait défiler les fiches Google des instituts. Si votre soin n'y est pas, elle s'arrête ailleurs.\n\n#FicheGoogle #Estheticienne #Lyon\n\n" + ABO,
        'instagram': "« Elle ne fait pas ce soin, on passe. » Esthéticienne à Lyon, votre nouveau soin manque sur votre fiche Google.\n\nUne cliente cherche un soin précis. Elle tape le nom du soin et sa ville, et Google lui montre des fiches Google d'instituts, avec les photos, les avis et la liste des services.\n\nVous proposez ce soin depuis la rentrée. Mais sur votre fiche Google, il n'apparaît pas. Elle fait glisser son doigt et s'arrête sur l'institut d'à côté, qui l'affiche.\n\nVotre dernier soin, il est sur votre fiche Google ou seulement dans la cabine ?\n\n30 jours offerts, lien en bio.\n\n#FicheGoogle #Estheticienne #InstitutDeBeaute #Lyon #ReferencementLocal",
        'youtube': "Esthéticienne à Lyon, votre nouveau soin est-il visible sur votre fiche Google ?\n\nLa fiche Google, c'est l'encadré qui présente votre institut sur Google et Google Maps, avec vos photos, vos avis, vos horaires et vos services. Une cliente qui cherche un soin précis compare ces fiches Google avant de réserver.\n\nProenligne publie une photo le lundi, une publication le jeudi, et répond à chaque avis.\n\nQuel soin avez-vous lancé en dernier, et se voit-il sur votre fiche Google ?\n\n#FicheGoogle #Estheticienne #Lyon",
        'facebook': "« Elle ne fait pas ce soin, on passe. » Esthéticienne à Lyon, votre nouveau soin manque sur votre fiche Google.\n\nAvant de réserver, beaucoup de clientes regardent la fiche Google de l'institut, ce que Google affiche avec les photos, les avis et les services. C'est là qu'elles vérifient que le soin existe.\n\nUn soin lancé au salon mais absent de votre fiche Google, une nouvelle cliente ne peut pas le connaître.\n\nDepuis quand votre liste de soins n'a-t-elle pas bougé sur Google ?\n\nEssayez Proenligne gratuitement, 30 jours offerts.\n\n#FicheGoogle #Estheticienne #InstitutDeBeaute #Lyon #ReferencementLocal",
    })

# ───────────────────────── MARDI 24 ─────────────────────────
add(M, '13:00', intention='preuve', metier='macon', angle='preuve', format='avant-apres', ton='avant-apres', symptome='photos-anciennes',
    slug='macon-avant-apres-chantiers-hiver',
    accroche="Avant, la fiche Google du maçon Martin montrait un muret de 2021. Après, elle montre le chantier de la semaine.",
    premier_commentaire="En hiver, les chantiers intérieurs font de bonnes photos. Une ouverture de mur porteur, une chape coulée ou un escalier en béton montrent un savoir-faire qu'on voit rarement.",
    visuel={'gabarit': 'avant-apres', 'surtitre': "Démonstration sur la fiche Google d'un maçon", 'titre': 'La même fiche Google, avec des chantiers récents',
            'mot': 'chantiers récents',
            'carte': {'enseigne': 'Maçonnerie Martin', 'metier': 'Maçon', 'avant': 'Un muret photographié en 2021', 'apres': 'Le chantier de la semaine'},
            'cta': 'question', 'question': 'Quelle est la date de la dernière photo de votre fiche Google ?',
            'slides': [
                {'type': 'point', 'numero': '1', 'titre': 'Avant, une seule vieille photo', 'texte': "Un muret de 2021, et plus rien depuis. Le client pouvait se demander si l'entreprise existait encore."},
                {'type': 'point', 'numero': '2', 'titre': 'Après, un chantier chaque lundi', 'texte': "Une chape, une ouverture de mur, une terrasse. Chaque semaine, la fiche Google montre un vrai chantier."},
                {'type': 'point', 'numero': '3', 'titre': 'Le client voit une équipe au travail', 'texte': "En comparant deux fiches Google, il repère vite celle d'une entreprise active."},
                {'type': 'fin', 'titre': 'Et la vôtre ?', 'texte': "Votre fiche Google montre-t-elle vos chantiers de cette année ?"}]},
    textes={
        'instagram': "Avant, la fiche Google du maçon Martin montrait un muret de 2021. Après, elle montre le chantier de la semaine.\n\nC'est un exemple imaginaire, mais la situation est courante. Sur Google Maps, chaque maçon a sa fiche Google, avec la note, les photos et le bouton Appeler. C'est elle qu'on regarde avant de demander un devis.\n\nAvant, une seule photo, un muret de 2021. Rien ne disait que l'entreprise travaillait encore.\n\nAprès, chaque lundi, une photo de chantier. Une chape coulée, une ouverture de mur, une terrasse en cours.\n\nLe client qui compare voit tout de suite quelle entreprise est active.\n\nDe quand date la dernière photo de votre fiche Google ?\n\n#FicheGoogle #Macon #Maconnerie #ReferencementLocal #GoogleBusinessProfile",
        'linkedin': "Dans le bâtiment, la fiche Google d'une entreprise de maçonnerie montre souvent un chantier vieux de plusieurs années.\nOr c'est elle que beaucoup de clients regardent avant de demander un devis.\n\nLa fiche Google, c'est l'encadré que Google affiche avec le nom de l'entreprise, sa note, ses photos et son numéro.\n\nPrenons un exemple imaginaire, la maçonnerie Martin.\nAvant, une seule photo, un muret de 2021. Rien n'indiquait que l'équipe travaillait encore.\nAprès, une photo de chantier paraît chaque lundi. Une chape, une ouverture de mur, une terrasse.\n\nLa note n'a pas bougé. Ce qui change, c'est l'image laissée au client qui compare deux entreprises. Des chantiers récents montrent une équipe au travail et un savoir-faire concret.\n\nC'est ce que fait Proenligne pour les artisans, avec une photo le lundi, une publication le jeudi et une réponse à chaque avis.\n\nDans votre entreprise, qui prend les photos de chantier, et que deviennent-elles ?\n\n#FicheGoogle #GoogleBusinessProfile #ReferencementLocal #Maconnerie #TPE",
    })

add(M, '19:00', intention='utile', metier='chauffagiste', angle='peur-de-perdre', format='fiche', ton='question', symptome='pas-de-nouveaute', ab='A',
    slug='chauffagiste-appels-nantes',
    accroche="Chauffagiste à Nantes, votre fiche Google est-elle prête pour l'hiver ?",
    premier_commentaire="Avant l'hiver, vérifiez une chose simple. Vos horaires de dépannage et votre numéro doivent être justes sur votre fiche Google, sinon le client appelle dans le vide.",
    tiktok_title="Chauffagiste à Nantes, votre fiche Google est-elle prête pour l'hiver ?",
    youtube_title="Chauffagiste, votre fiche Google est-elle prête pour l'hiver ?",
    textes={
        'tiktok': "Chauffagiste à Nantes, votre fiche Google est-elle prête pour l'hiver ?\nUne chaudière en panne, et le client ouvre Google Maps. Il regarde les fiches Google avant d'appeler.\n\n#FicheGoogle #Chauffagiste #Nantes\n\n" + ABO,
        'instagram': "Chauffagiste à Nantes, votre fiche Google est-elle prête pour l'hiver ?\n\nUn matin, la chaudière ne redémarre pas. Le client prend son téléphone et tape « chauffagiste » sur Google Maps. Il voit des fiches Google, avec la note, les photos, les horaires et le bouton Appeler.\n\nIl regarde vite. Des photos récentes, des avis qui ont une réponse, des horaires justes. Ou une fiche Google qui n'a pas bougé depuis l'hiver dernier.\n\nIl appelle celui qui a l'air présent.\n\nQu'avez-vous publié sur votre fiche Google depuis le début de l'automne ?\n\n30 jours offerts, lien en bio.\n\n#FicheGoogle #Chauffagiste #Chauffage #Nantes #ReferencementLocal",
        'youtube': "Chauffagiste à Nantes, votre fiche Google est-elle prête pour l'hiver ?\n\nQuand on cherche « chauffagiste » sur Google Maps, Google affiche des fiches Google avec photos, avis et horaires. La vôtre en fait partie. En hiver, le client pressé les compare en quelques secondes avant d'appeler.\n\nProenligne publie une photo le lundi, une publication le jeudi, et répond à chaque avis.\n\nVos horaires de dépannage sont-ils à jour sur votre fiche Google ?\n\n#FicheGoogle #Chauffagiste #Nantes",
        'facebook': "Chauffagiste à Nantes, votre fiche Google est-elle prête pour l'hiver ?\n\nLes premiers matins froids, les chaudières capricieuses se réveillent. Le client cherche un chauffagiste sur Google et tombe sur des fiches Google, ces encadrés avec la note, les photos et le bouton Appeler.\n\nUne fiche Google qui montre des installations récentes et des avis qui ont une réponse inspire confiance. Une fiche Google figée depuis l'an dernier fait hésiter.\n\nLa vôtre montre quoi, ce matin ?\n\nEssayez Proenligne gratuitement, 30 jours offerts.\n\n#FicheGoogle #Chauffagiste #Chauffage #Nantes #ReferencementLocal",
    })

# ───────────────────────── MERCREDI 25 ─────────────────────────
add(ME, '13:00', intention='utile', metier='boulangerie', angle='peur-de-perdre', format='question', ton='constat', symptome='horaires-faux',
    slug='boulangerie-sondage-horaires-fetes',
    accroche="Les fêtes approchent, et les horaires d'une boulangerie changent. Sur Google, les vôtres suivent ?",
    premier_commentaire="Une précision. Votre fiche Google permet d'ajouter des horaires exceptionnels pour un jour précis, comme le 24 ou le 31 décembre, sans toucher à vos horaires habituels.",
    visuel={'gabarit': 'question', 'surtitre': 'Boulangers, le petit sondage du mercredi', 'titre': 'Vos horaires de fêtes seront-ils sur votre fiche Google ?',
            'mot': 'horaires de fêtes',
            'reponses': ['Oui, je les ajoute à chaque fois', "J'y pense souvent trop tard", "Je ne savais pas que c'était possible"],
            'cta': 'question', 'question': 'Et vous, quelle réponse choisissez-vous ?',
            'slides': [
                {'type': 'point', 'numero': '1', 'titre': 'Un client vérifie avant de sortir', 'texte': "Le matin du 24, il ouvre Google Maps pour savoir si votre boulangerie est ouverte."},
                {'type': 'point', 'numero': '2', 'titre': 'Des horaires faux coûtent cher', 'texte': "Si votre fiche Google affiche fermé alors que vous êtes ouvert, il va acheter sa bûche ailleurs."},
                {'type': 'point', 'numero': '3', 'titre': 'Les horaires exceptionnels', 'texte': "Votre fiche Google accepte des horaires pour un jour précis, sans changer vos horaires habituels."},
                {'type': 'fin', 'titre': 'À vous de répondre', 'texte': "Oui à chaque fois, souvent trop tard, ou pas encore ? Dites-le en commentaire."}]},
    textes={
        'instagram': "Les fêtes approchent, et les horaires d'une boulangerie changent. Sur Google, les vôtres suivent ?\n\nLe matin du 24, un client veut sa bûche. Avant de sortir, il cherche « boulangerie » sur Google Maps. Les encadrés avec une note, des photos et des horaires sont des fiches Google, et la vôtre en fait partie.\n\nSi elle affiche vos horaires habituels alors que vous ouvrez plus tôt, ou fermé alors que vous êtes là, il ira ailleurs sans même essayer.\n\nPetit sondage du mercredi. Vos horaires de fêtes seront-ils sur votre fiche Google ?\nA. Oui, je les ajoute à chaque fois.\nB. J'y pense souvent trop tard.\nC. Je ne savais pas que c'était possible.\n\nVous répondez A, B ou C ?\n\n#FicheGoogle #Boulangerie #Boulanger #ReferencementLocal #GoogleBusinessProfile",
    })

add(ME, '19:00', intention='utile', metier='paysagiste', angle='gain-de-temps', format='journee', ton='question', symptome='avis-sans-reponse',
    slug='paysagiste-semaine-lille',
    accroche="Paysagiste à Lille, pendant que vous rangez le matériel, vos soirées partent sur Google.",
    premier_commentaire="Une façon de gagner du temps. Prenez vos photos de chantier pendant la journée, au fil du travail, puis publiez-en une seule par semaine sur votre fiche Google.",
    tiktok_title="Paysagiste à Lille, vos soirées partent sur votre fiche Google ?",
    youtube_title="Paysagiste, combien de soirées donnez-vous à votre fiche Google ?",
    textes={
        'tiktok': "Paysagiste à Lille, pendant que vous rangez le matériel, vos soirées partent sur Google.\nPhotos, avis, publications, votre fiche Google, celle qu'on voit sur Google Maps, se rappelle à vous chaque soir.\n\n#FicheGoogle #Paysagiste #Lille\n\n" + ABO,
        'instagram': "Paysagiste à Lille, pendant que vous rangez le matériel, vos soirées partent sur Google.\n\nLa journée finit tôt en hiver, mais elle ne finit pas vraiment. Une fois le camion vidé, il reste votre fiche Google, cette carte de visite que Google montre à votre place avec vos photos, vos avis et vos horaires.\n\nUne photo de la haie taillée à trier, un avis à remercier, une publication à écrire. Un peu chaque soir.\n\nProenligne s'en charge en journée, avec une photo le lundi, une publication le jeudi et une réponse à chaque avis.\n\nEt vous, à quel moment vous occupez-vous de votre fiche Google ?\n\n30 jours offerts, lien en bio.\n\n#FicheGoogle #Paysagiste #Jardin #Lille #ReferencementLocal",
        'youtube': "Paysagiste à Lille, combien de soirées donnez-vous à votre fiche Google ?\n\nLa fiche Google, c'est ce qui s'affiche quand un client cherche « paysagiste » sur Google ou Google Maps, avec vos photos, vos avis et vos horaires. La tenir à jour prend un peu de temps chaque semaine, souvent le soir.\n\nProenligne publie une photo le lundi, une publication le jeudi, et répond à chaque avis à votre place.\n\nCombien de temps y passez-vous chaque semaine ?\n\n#FicheGoogle #Paysagiste #Lille",
        'facebook': "Paysagiste à Lille, pendant que vous rangez le matériel, vos soirées partent sur Google.\n\nLe chantier est fini, mais la fiche Google, elle, attend encore. C'est l'encadré qu'un client ouvre sur Google Maps avant de vous appeler, avec vos photos, vos avis et vos horaires.\n\nTrier les photos, répondre aux avis, publier une nouvelle. Rien de long, mais un peu chaque soir, et la soirée y passe.\n\nProenligne s'en occupe en journée, à votre place.\n\nVous préférez y passer vos soirées ou vos week-ends ?\n\nEssayez Proenligne gratuitement, 30 jours offerts.\n\n#FicheGoogle #Paysagiste #Jardin #Lille #ReferencementLocal",
    })

# ───────────────────────── JEUDI 26 ─────────────────────────
add(J, '12:30', intention='utile', metier='chauffagiste', angle='peur-de-perdre', format='fiche', ton='question', symptome='pas-de-nouveaute', ab='B',
    slug='chauffagiste-appels-nantes',
    accroche="Chauffagiste à Nantes, on vous trouve sur Google cet hiver ?",
    premier_commentaire="Une photo d'une chaudière que vous venez de poser, prise à la lumière du jour, montre au client que vous travaillez en ce moment.",
    tiktok_title="Chauffagiste à Nantes, on vous trouve sur Google cet hiver ?",
    textes={
        'tiktok': "Chauffagiste à Nantes, on vous trouve sur Google cet hiver ?\nQuand la chaudière lâche, le client compare les fiches Google sur Google Maps et appelle celle qui a l'air active.\n\n#FicheGoogle #Chauffagiste #Nantes\n\n" + ABO,
    })

add(J, '13:00', intention='utile', metier='serrurier', angle='peur-de-perdre', format='conseil', ton='contre-intuitif', symptome='avis-negatif-seul',
    slug='serrurier-repondre-avis-negatif',
    accroche="Un avis négatif sur votre fiche Google n'est pas toujours une catastrophe. Votre réponse compte souvent plus que lui.",
    premier_commentaire="Un exemple de réponse courte. « Merci pour votre retour. Nous sommes désolés pour l'attente ce soir-là, et nous avons revu notre organisation pour les urgences. »",
    visuel={'gabarit': 'conseil', 'surtitre': 'Serruriers, un avis négatif sur votre fiche Google', 'titre': 'Trois règles pour répondre à un avis négatif sur Google',
            'mot': 'répondre',
            'points': ["Remerciez le client, même s'il est injuste",
                       "Expliquez les faits en une ou deux phrases calmes",
                       "Dites ce que vous avez changé, sans vous justifier"],
            'cta': 'question', 'question': 'Comment répondez-vous à un avis négatif, vous ?',
            'slides': [
                {'type': 'point', 'numero': '1', 'titre': 'Le merci désamorce', 'texte': "Un merci en première ligne montre au futur client que vous restez calme, même face à un reproche."},
                {'type': 'point', 'numero': '2', 'titre': 'Des faits, pas un débat', 'texte': "Une ou deux phrases suffisent. Le client qui lit votre fiche Google veut comprendre, pas assister à une dispute."},
                {'type': 'point', 'numero': '3', 'titre': 'Ce qui a changé rassure', 'texte': "Dire ce que vous avez corrigé montre une entreprise sérieuse, qui écoute ses clients."},
                {'type': 'fin', 'titre': 'Et vous ?', 'texte': "Répondez-vous tout de suite, le lendemain, ou jamais ?"}]},
    textes={
        'instagram': "Un avis négatif sur votre fiche Google n'est pas toujours une catastrophe. Votre réponse compte souvent plus que lui.\n\nAvant d'appeler un serrurier, le client ouvre sa fiche Google sur Google Maps et lit les avis, les horaires et vos réponses. Un avis sévère avec une réponse calme peut le rassurer. Un avis sévère sans réponse le fait douter.\n\nTrois règles pour répondre.\n1. Remerciez le client, même s'il est injuste.\n2. Expliquez les faits en une ou deux phrases calmes.\n3. Dites ce que vous avez changé, sans vous justifier.\n\nVous répondez plutôt tout de suite, le lendemain, ou jamais ?\n\n#FicheGoogle #Serrurier #AvisClients #ReferencementLocal #GoogleBusinessProfile",
        'linkedin': "Un avis négatif sur la fiche Google d'une entreprise n'est pas toujours une catastrophe.\nLa réponse du dirigeant compte souvent davantage que l'avis lui-même.\n\nLa fiche Google, c'est l'encadré que Google affiche quand on cherche votre métier, avec la note, les avis et le téléphone. Dans les métiers d'urgence comme la serrurerie, le client la lit en quelques secondes.\n\nTrois règles simples pour répondre.\nRemercier, même quand le reproche semble injuste.\nExposer les faits en une ou deux phrases, sans polémique.\nDire ce qui a été corrigé dans l'organisation.\n\nUne réponse calme montre au prochain client une entreprise qui écoute. Un avis sans réponse laisse le doute s'installer.\n\nProenligne répond à chaque avis pour les artisans, et fait toujours valider les réponses aux avis négatifs par le dirigeant. S'y ajoutent une photo le lundi et une publication le jeudi.\n\nDans votre entreprise, qui répond aux avis négatifs, et dans quel délai ?\n\n#FicheGoogle #GoogleBusinessProfile #ReferencementLocal #AvisClients #TPE",
    })

add(J, '19:00', intention='utile', metier='plombier', angle='peur-de-perdre', format='fiche', ton='scene', symptome='concurrent-plus-riche', ab='A',
    slug='plombier-swipe-concurrent-brest',
    accroche="Plombier à Brest, le voisin a la même note que vous, mais sa fiche Google montre ses chantiers.",
    premier_commentaire="À note égale, le client regarde souvent les photos. Une salle de bains refaite ou un ballon d'eau chaude bien raccordé parlent plus qu'une photo du camion.",
    tiktok_title="Plombier à Brest, la même note, mais sa fiche Google vit",
    youtube_title="Plombier, la même note que le voisin, mais sa fiche Google montre ses chantiers",
    textes={
        'tiktok': "Plombier à Brest, le voisin a la même note que vous, mais sa fiche Google montre ses chantiers.\nDeux fiches Google sur Google Maps, la même note. Le client garde celle qui a l'air vivante.\n\n#FicheGoogle #Plombier #Brest\n\n" + ABO,
        'instagram': "Plombier à Brest, le voisin a la même note que vous, mais sa fiche Google montre ses chantiers.\n\nIl est 22 h, l'eau coule sous l'évier. Le client ouvre Google Maps et compare deux fiches Google, ces encadrés avec la note, les photos et le bouton Appeler.\n\nMême note pour les deux. Chez le voisin, des chantiers de la semaine. Chez vous, rien de neuf depuis longtemps.\n\nIl ne vous connaît pas. Il garde celui qui a l'air de travailler en ce moment.\n\nQuelle photo de chantier mettriez-vous en premier sur votre fiche Google ?\n\n30 jours offerts, lien en bio.\n\n#FicheGoogle #Plombier #Plomberie #Brest #ReferencementLocal",
        'youtube': "Plombier à Brest, la même note que le voisin, mais sa fiche Google montre ses chantiers.\n\nLa fiche Google, c'est la carte de visite que Google montre à votre place, avec vos photos, vos avis, vos horaires et votre téléphone. Quand deux plombiers ont la même note, le client regarde ce qui est récent.\n\nProenligne publie une photo de vos chantiers le lundi, une publication le jeudi, et répond à chaque avis.\n\nVotre fiche Google montre-t-elle vos chantiers de cette semaine ?\n\n#FicheGoogle #Plombier #Brest",
        'facebook': "Plombier à Brest, le voisin a la même note que vous, mais sa fiche Google montre ses chantiers.\n\nSur Google Maps, chaque plombier a sa fiche Google, avec la note, les photos et le bouton Appeler. C'est elle qu'on regarde avant de choisir.\n\nDeux fiches Google, la même note. L'une montre des chantiers récents, l'autre n'a rien publié depuis longtemps. Dans l'urgence, on garde celle qui a l'air active.\n\nSur votre fiche Google, quelle est la photo la plus récente ?\n\nEssayez Proenligne gratuitement, 30 jours offerts.\n\n#FicheGoogle #Plombier #Plomberie #Brest #ReferencementLocal",
    })

# ───────────────────────── VENDREDI 27 ─────────────────────────
add(V, '13:00', intention='preuve', metier='estheticienne', angle='preuve', format='avant-apres', ton='avant-apres', symptome='avis-sans-reponse',
    slug='estheticienne-avant-apres-reponses-avis',
    accroche="Avant, l'institut Petit laissait ses avis sans un mot sur sa fiche Google. Désormais, chaque cliente reçoit un merci.",
    premier_commentaire="Une réponse d'avis n'a pas besoin d'être longue. Le prénom de la cliente, le soin reçu et un merci sincère suffisent souvent.",
    visuel={'gabarit': 'avant-apres', 'surtitre': "Démonstration sur la fiche Google d'un institut", 'titre': 'La même fiche Google, avec une réponse à chaque avis',
            'mot': 'sa réponse',
            'carte': {'enseigne': 'Institut Petit', 'metier': 'Esthéticienne', 'avant': 'Des avis restés sans réponse', 'apres': 'Une réponse sous chaque avis'},
            'cta': 'question', 'question': 'Combien d\'avis attendent une réponse sur votre fiche Google ?',
            'slides': [
                {'type': 'point', 'numero': '1', 'titre': 'Avant, des avis sans réponse', 'texte': "Des clientes contentes avaient écrit, et personne ne les avait remerciées. La fiche Google semblait abandonnée."},
                {'type': 'point', 'numero': '2', 'titre': 'Après, chaque avis a sa réponse', 'texte': "Un merci personnalisé sous chaque avis, et les réponses aux avis négatifs validées par l'institut."},
                {'type': 'point', 'numero': '3', 'titre': 'La future cliente le voit', 'texte': "En lisant les avis de votre fiche Google, elle voit qu'il y a quelqu'un derrière la porte."},
                {'type': 'fin', 'titre': 'Et chez vous ?', 'texte': "Votre dernier avis a-t-il reçu sa réponse ?"}]},
    textes={
        'instagram': "Avant, l'institut Petit laissait ses avis sans un mot sur sa fiche Google. Désormais, chaque cliente reçoit un merci.\n\nC'est un exemple imaginaire. La fiche Google, c'est ce que vos clientes voient en premier quand elles cherchent un institut sur Google Maps, avec vos photos, vos horaires et vos avis.\n\nAvant, des clientes ravies avaient laissé un mot. Aucun merci en retour. Une future cliente pouvait se demander si quelqu'un lisait.\n\nAprès, chaque avis a sa réponse, avec le prénom et le soin. Les réponses aux avis négatifs sont validées par l'institut avant d'être publiées.\n\nLa note n'a pas changé. L'impression, si.\n\nCombien d'avis attendent encore une réponse sur votre fiche Google ?\n\n#FicheGoogle #Estheticienne #InstitutDeBeaute #ReferencementLocal #GoogleBusinessProfile",
    })

add(V, '19:00', intention='utile', metier='garage', angle='peur-de-perdre', format='avis', ton='replique', symptome='avis-sans-reponse',
    slug='garage-appels-lorient',
    accroche="« Je vais appeler l'autre garage. » Garagiste à Lorient, votre fiche Google y est pour quelque chose.",
    premier_commentaire="Un geste qui rassure. Ajoutez sur votre fiche Google une photo de l'atelier rangé et de l'équipe, l'automobiliste voit à qui il confie sa voiture.",
    tiktok_title="Garagiste à Lorient, on vous appelle depuis Google ?",
    youtube_title="Garagiste, pourquoi l'automobiliste appelle l'autre garage sur Google ?",
    textes={
        'tiktok': "« Je vais appeler l'autre garage. » Garagiste à Lorient, votre fiche Google y est pour quelque chose.\nEn panne, on compare les fiches Google sur Google Maps, et on appelle celle qui rassure.\n\n#FicheGoogle #Garagiste #Lorient\n\n" + ABO2,
        'instagram': "« Je vais appeler l'autre garage. » Garagiste à Lorient, votre fiche Google y est pour quelque chose.\n\nUn voyant s'allume sur la route. L'automobiliste se gare et tape « garage » sur Google Maps. Il voit des fiches Google, avec la note, les avis, les photos et le bouton Appeler.\n\nSous vos avis, aucune réponse. Pas de photo de l'atelier. Sur la fiche Google d'à côté, l'équipe, les réponses, des nouvelles récentes.\n\nIl appelle l'autre, sans même vous avoir comparé longtemps.\n\nQue voit un automobiliste en panne quand il ouvre votre fiche Google ?\n\n30 jours offerts, lien en bio.\n\n#FicheGoogle #Garagiste #Garage #Lorient #ReferencementLocal",
        'youtube': "Garagiste à Lorient, pourquoi l'automobiliste appelle l'autre garage sur Google ?\n\nSur Google Maps, chaque garage a sa fiche Google, avec la note, les photos et le bouton Appeler. C'est elle qu'on regarde avant d'appeler. Des avis qui ont une réponse et des photos de l'atelier rassurent l'automobiliste en panne.\n\nProenligne publie une photo le lundi, une publication le jeudi, et répond à chaque avis.\n\nVos derniers avis ont-ils reçu une réponse ?\n\n#FicheGoogle #Garagiste #Lorient",
        'facebook': "« Je vais appeler l'autre garage. » Garagiste à Lorient, votre fiche Google y est pour quelque chose.\n\nEn panne, on n'a pas le temps de chercher longtemps. On ouvre Google Maps, on compare deux ou trois fiches Google, et on appelle celle qui inspire confiance.\n\nDes avis sans réponse et aucune photo de l'atelier, ça fait hésiter. Une équipe en photo et des réponses polies, ça rassure.\n\nQue montre la première photo de votre fiche Google ?\n\nEssayez Proenligne gratuitement, 30 jours offerts.\n\n#FicheGoogle #Garagiste #Garage #Lorient #ReferencementLocal",
    })

# ───────────────────────── SAMEDI 28 ─────────────────────────
add(S, '12:30', intention='utile', metier='plombier', angle='peur-de-perdre', format='fiche', ton='scene', symptome='concurrent-plus-riche', ab='B',
    slug='plombier-swipe-concurrent-brest',
    accroche="Plombier à Brest, entre deux fiches Google, laquelle le client garde-t-il ?",
    premier_commentaire="Une seule photo de chantier par semaine suffit à montrer que votre entreprise travaille en ce moment.",
    tiktok_title="Plombier à Brest, entre deux fiches Google, laquelle garde-t-on ?",
    textes={
        'tiktok': "Plombier à Brest, entre deux fiches Google, laquelle le client garde-t-il ?\nMême note sur Google Maps. L'une montre des chantiers récents, l'autre rien de neuf.\n\n#FicheGoogle #Plombier #Brest\n\n" + ABO,
    })

add(S, '13:00', intention='offre', metier='general', angle='gain-de-temps', format='conseil', ton='constat', symptome=None,
    slug='offre-fiche-google-suivie-chaque-semaine',
    accroche="Une fiche Google active demande un peu de temps chaque semaine. Proenligne le prend pour vous.",
    premier_commentaire="Pendant l'essai, vous continuez votre métier comme d'habitude. Vous validez seulement les réponses aux avis négatifs. 30 jours offerts, le lien est en bio.",
    visuel={'gabarit': 'conseil', 'surtitre': 'Proenligne tient votre fiche Google à jour', 'titre': 'Votre fiche Google suivie chaque semaine, sans vous',
            'mot': "s'occupe",
            'points': ["Publier une photo de votre travail chaque lundi",
                       "Publier une actualité sur votre fiche Google le jeudi",
                       "Répondre à chaque avis, avec votre accord pour les négatifs"],
            'cta': 'offre',
            'slides': [
                {'type': 'point', 'numero': '1', 'titre': 'Le lundi, une photo', 'texte': "Chaque lundi, une photo de votre travail paraît sur votre fiche Google."},
                {'type': 'point', 'numero': '2', 'titre': 'Le jeudi, une publication', 'texte': "Chaque jeudi, une nouvelle publication paraît sur votre fiche Google."},
                {'type': 'point', 'numero': '3', 'titre': 'Chaque avis a sa réponse', 'texte': "Les réponses aux avis négatifs vous sont toujours soumises avant d'être publiées."},
                {'type': 'fin', 'titre': 'Essayez Proenligne gratuitement', 'texte': "30 jours offerts, sans engagement. Le lien est dans la bio."}]},
    textes={
        'instagram': "Une fiche Google active demande un peu de temps chaque semaine. Proenligne le prend pour vous.\n\nVotre fiche Google, c'est ce qui s'affiche quand un client cherche votre métier sur Google ou Google Maps, avec vos photos, vos avis et vos horaires. Pour qu'elle montre une entreprise vivante, il faut la nourrir régulièrement.\n\nAvec Proenligne, chaque semaine\n✅ une photo de votre travail est publiée le lundi\n✅ une publication paraît le jeudi\n✅ chaque avis reçoit une réponse, et vous validez celles aux avis négatifs\n\nEssayez Proenligne gratuitement, 30 jours offerts, sans engagement. Lien en bio.\n\n#FicheGoogle #Artisan #Commercant #ReferencementLocal #GoogleBusinessProfile",
    })

add(S, '19:00', intention='utile', metier='electricien', angle='peur-de-perdre', format='recherche', ton='question', symptome='fiche-oubliee',
    slug='electricien-classement-vannes',
    accroche="Électricien à Vannes, on vous voit sur Google quand on cherche un électricien ?",
    premier_commentaire="Faites le test vous-même. Tapez « électricien » et votre ville sur Google Maps depuis le téléphone d'un proche, et regardez quelles fiches Google apparaissent avant la vôtre.",
    tiktok_title="Électricien à Vannes, on vous voit sur Google ?",
    youtube_title="Électricien, quand on cherche votre métier sur Google, on vous voit ?",
    textes={
        'tiktok': "Électricien à Vannes, on vous voit sur Google quand on cherche un électricien ?\nTapez « électricien Vannes » sur Google Maps. Les fiches Google qui apparaissent, ce sont celles qu'on appelle.\n\n#FicheGoogle #Electricien #Vannes\n\n" + ABO2,
        'instagram': "Électricien à Vannes, on vous voit sur Google quand on cherche un électricien ?\n\nUn test simple. Tapez « électricien » et votre ville sur Google Maps. Google affiche des fiches Google, ces encadrés avec la note, les photos et le bouton Appeler.\n\nRegardez lesquelles sortent avant votre fiche Google. Souvent, elles ont des photos récentes, des publications et des avis qui ont une réponse. Ce sont des signes qu'un client voit tout de suite.\n\nVous avez fait le test ? Vous êtes où dans la liste ?\n\n30 jours offerts, lien en bio.\n\n#FicheGoogle #Electricien #Electricite #Vannes #ReferencementLocal",
        'youtube': "Électricien à Vannes, quand on cherche votre métier sur Google, on vous voit ?\n\nQuand on tape « électricien près de moi », Google affiche des fiches Google avec photos, avis et horaires. La vôtre en fait partie. Le client appelle souvent l'une des premières qu'il voit.\n\nProenligne fait vivre votre fiche Google, avec une photo le lundi, une publication le jeudi et une réponse à chaque avis.\n\nAvez-vous déjà cherché votre propre métier sur Google Maps ?\n\n#FicheGoogle #Electricien #Vannes",
        'facebook': "Électricien à Vannes, on vous voit sur Google quand on cherche un électricien ?\n\nFaites l'essai avec le téléphone d'un proche. Tapez « électricien » et votre ville sur Google Maps. Les encadrés qui apparaissent sont des fiches Google, avec la note, les photos et le téléphone.\n\nCelles qui ont des photos récentes et des avis avec réponse donnent envie d'appeler. Une fiche Google oubliée passe inaperçue.\n\nQuand avez-vous regardé votre fiche Google pour la dernière fois ?\n\nEssayez Proenligne gratuitement, 30 jours offerts.\n\n#FicheGoogle #Electricien #Electricite #Vannes #ReferencementLocal",
    })

# ───────────────────────── DIMANCHE 29 ─────────────────────────
add(D, '13:00', intention='utile', metier='paysagiste', angle='gain-de-temps', format='question', ton='contre-intuitif', symptome='pas-de-nouveaute',
    slug='paysagiste-quiz-photo-hiver',
    accroche="En hiver, le jardin dort, mais votre fiche Google n'a pas besoin de dormir avec lui. Petit quiz du dimanche.",
    premier_commentaire="Une idée de photo pour décembre. Le tas de bois bien rangé après un élagage, ou une haie taillée net sous la lumière du matin, montrent un chantier fini et propre.",
    visuel={'gabarit': 'question', 'surtitre': 'Paysagistes, le petit quiz du dimanche', 'titre': 'Quelle photo publier en hiver sur votre fiche Google ?',
            'mot': 'en hiver',
            'reponses': ['A. Une pelouse de l\'été dernier', 'B. Une haie taillée cette semaine', 'C. Le logo de l\'entreprise'],
            'cta': 'question', 'question': 'Votre réponse, A, B ou C ?',
            'slides': [
                {'type': 'point', 'numero': 'B', 'titre': 'La bonne réponse est la B', 'texte': "Une haie taillée cette semaine montre au client que vous travaillez aussi en hiver."},
                {'type': 'point', 'numero': '2', 'titre': "Pourquoi pas la pelouse d'été", 'texte': "Elle est belle, mais en décembre elle rappelle surtout que votre fiche Google n'a pas bougé depuis."},
                {'type': 'point', 'numero': '3', 'titre': 'Et le logo ?', 'texte': "Il a sa place, mais il ne montre pas votre travail. Le client veut voir un vrai chantier."},
                {'type': 'fin', 'titre': 'À vous de jouer', 'texte': "Quelle photo d'hiver allez-vous publier cette semaine sur votre fiche Google ?"}]},
    textes={
        'instagram': "En hiver, le jardin dort, mais votre fiche Google n'a pas besoin de dormir avec lui. Petit quiz du dimanche.\n\nLa fiche Google, c'est la carte de visite que Google montre à votre place quand on cherche un paysagiste, avec vos photos, vos avis et votre téléphone. En hiver, c'est souvent là qu'on prépare les travaux du printemps.\n\nQuelle photo publier en décembre ?\nA. Une pelouse de l'été dernier.\nB. Une haie taillée cette semaine.\nC. Le logo de l'entreprise.\n\nLa réponse est dans le carrousel. Et vous, quelle photo d'hiver publiez-vous cette semaine ?\n\n#FicheGoogle #Paysagiste #JardinDHiver #ReferencementLocal #GoogleBusinessProfile",
    })

add(D, '19:00', intention='utile', metier='autoecole', angle='gain-de-temps', format='journee', ton='scene', symptome='avis-sans-reponse',
    slug='autoecole-swipe-soirees-toulouse',
    accroche="Auto-école à Toulouse, il est 22 h, la dernière leçon est finie, et votre fiche Google vous attend.",
    premier_commentaire="Une astuce pour les auto-écoles. Après chaque permis réussi, demandez à l'élève s'il veut bien laisser un avis, c'est le moment où il est le plus content.",
    tiktok_title="Auto-école à Toulouse, la dernière leçon finie, la fiche Google vous attend",
    youtube_title="Auto-école, la dernière leçon est finie, mais votre fiche Google vous attend",
    textes={
        'tiktok': "Auto-école à Toulouse, il est 22 h, la dernière leçon est finie, et votre fiche Google vous attend.\nLes avis des élèves, les photos, les nouvelles, ça s'empile sur votre fiche Google, celle que les familles voient sur Google Maps.\n\n#FicheGoogle #AutoEcole #Toulouse\n\n" + ABO,
        'instagram': "Auto-école à Toulouse, il est 22 h, la dernière leçon est finie, et votre fiche Google vous attend.\n\nLa voiture est rangée, le planning de demain est prêt. Reste votre fiche Google, cet encadré qu'une famille ouvre sur Google Maps avant d'inscrire un élève.\n\nUn avis d'élève reçu au permis à remercier, une photo de la nouvelle voiture à publier, une question restée sans réponse. Rien de long, mais tout s'empile.\n\nProenligne s'en charge à votre place, avec une photo le lundi, une publication le jeudi et une réponse à chaque avis.\n\nÀ quelle heure finissez-vous vraiment votre journée ?\n\n30 jours offerts, lien en bio.\n\n#FicheGoogle #AutoEcole #PermisDeConduire #Toulouse #ReferencementLocal",
        'youtube': "Auto-école à Toulouse, la dernière leçon est finie, mais votre fiche Google vous attend.\n\nLa fiche Google, c'est ce que les familles voient en premier quand elles cherchent une auto-école sur Google Maps, avec vos photos, vos avis et vos horaires. La tenir à jour se fait souvent le soir, après les leçons.\n\nProenligne publie une photo le lundi, une publication le jeudi, et répond à chaque avis à votre place.\n\nEt vous, quand répondez-vous aux avis de vos élèves ?\n\n#FicheGoogle #AutoEcole #Toulouse",
        'facebook': "Auto-école à Toulouse, il est 22 h, la dernière leçon est finie, et votre fiche Google vous attend.\n\nAvant d'inscrire un enfant, beaucoup de parents regardent la fiche Google de l'auto-école sur Google Maps, avec la note, les photos et les avis des anciens élèves.\n\nRemercier un élève reçu, publier une photo, répondre à une question. Chaque soir, il y a un petit quelque chose, et la soirée raccourcit.\n\nProenligne s'en occupe pour vous, chaque semaine.\n\nVous gardez combien de soirées libres par semaine ?\n\nEssayez Proenligne gratuitement, 30 jours offerts.\n\n#FicheGoogle #AutoEcole #PermisDeConduire #Toulouse #ReferencementLocal",
    })


def T(date, nom, champ, val):
    c = next(c for c in C if c['date'] == date and c['creneau_nominal'] == nom)
    *chemin, der = champ.split('.')
    o = c
    for k in chemin:
        o = o[int(k)] if isinstance(o, list) else o[k]
    if isinstance(o, list): o[int(der)] = val
    else: o[der] = val


# ───────── Corrections (vérificateur et relecture) ─────────

# ───────── Corrections après la relecture, passe 1 ─────────
T('2026-11-23', '13:00', 'textes.instagram', "Il est 22 h. Le salon est balayé, mais votre nouvelle prestation n'apparaît nulle part sur votre fiche Google.\n\nVous avez appris une nouvelle technique, vous en parlez à vos clients fidèles. Mais une personne qui tape « coiffeur » et sa ville sur Google Maps ne connaît de votre salon que votre fiche Google, avec vos photos, vos avis et vos services. Ce qui n'y est pas, elle ne le devine pas.\n\nTrois gestes pour la montrer.\n1. Ajoutez la prestation dans la rubrique Services.\n2. Publiez une photo du résultat, avec l'accord du client.\n3. Annoncez-la dans une publication courte.\n\nQuelle est la dernière prestation que vous avez ajoutée au salon ?\n\n#FicheGoogle #Coiffeur #Coiffure #ReferencementLocal #GoogleBusinessProfile")  # e689d77
T('2026-11-24', '13:00', 'textes.instagram', "Avant, la fiche Google du maçon Martin montrait un muret de 2021. Après, elle montre le chantier de la semaine.\n\nC'est un exemple imaginaire, mais la situation est courante. Sur Google Maps, chaque maçon a sa fiche Google, avec la note, les photos et le bouton Appeler. C'est elle qu'on regarde avant de demander un devis.\n\nAvant, il n'y avait qu'une seule photo, un muret de 2021. Rien ne disait que l'entreprise travaillait encore.\n\nAprès, une photo de chantier paraît chaque lundi, une chape coulée, une ouverture de mur ou une terrasse en cours.\n\nLe client qui compare voit tout de suite quelle entreprise est active.\n\nDe quand date la dernière photo de votre fiche Google ?\n\n#FicheGoogle #Macon #Maconnerie #ReferencementLocal #GoogleBusinessProfile")  # e06906d
T('2026-11-24', '13:00', 'textes.linkedin', "Dans le bâtiment, la fiche Google d'une entreprise de maçonnerie montre souvent un chantier vieux de plusieurs années.\nOr c'est elle que beaucoup de clients regardent avant de demander un devis.\n\nLa fiche Google, c'est l'encadré que Google affiche avec le nom de l'entreprise, sa note, ses photos et son numéro.\n\nPrenons un exemple imaginaire, la maçonnerie Martin.\nAvant, il n'y avait qu'une seule photo, un muret de 2021. Rien n'indiquait que l'équipe travaillait encore.\nAprès, une photo de chantier paraît chaque lundi, une chape, une ouverture de mur ou une terrasse.\n\nLa note n'a pas bougé. Ce qui change, c'est l'image laissée au client qui compare deux entreprises. Des chantiers récents montrent une équipe au travail et un savoir-faire concret.\n\nC'est ce que fait Proenligne pour les artisans, avec une photo le lundi, une publication le jeudi et une réponse à chaque avis.\n\nDans votre entreprise, qui prend les photos de chantier, et que deviennent-elles ?\n\n#FicheGoogle #GoogleBusinessProfile #ReferencementLocal #Maconnerie #TPE")  # e798810
T('2026-11-24', '13:00', 'visuel.slides.0.texte', "La seule photo montrait un muret de 2021, et plus rien depuis. Le client pouvait se demander si l'entreprise existait encore.")  # ea1d8ce
T('2026-11-24', '13:00', 'visuel.slides.1.texte', 'Chaque semaine, la fiche Google montre un vrai chantier, comme une chape, une ouverture de mur ou une terrasse.')  # e957d21
T('2026-11-24', '19:00', 'textes.instagram', "Chauffagiste à Nantes, votre fiche Google est-elle prête pour l'hiver ?\n\nUn matin, la chaudière ne redémarre pas. Le client prend son téléphone et tape « chauffagiste » sur Google Maps. Il voit des fiches Google, avec la note, les photos, les horaires et le bouton Appeler.\n\nIl regarde vite. Il voit des photos récentes, des avis qui ont une réponse, des horaires justes. Ou bien il tombe sur une fiche Google qui n'a pas bougé depuis l'hiver dernier.\n\nSouvent, il appelle celui qui a l'air présent.\n\nQu'avez-vous publié sur votre fiche Google depuis le début de l'automne ?\n\n30 jours offerts, lien en bio.\n\n#FicheGoogle #Chauffagiste #Chauffage #Nantes #ReferencementLocal")  # ea4a963
T('2026-11-25', '13:00', 'accroche', 'Les fêtes approchent et les horaires de votre boulangerie changent. Votre fiche Google suit-elle ?')  # edcc30f
T('2026-11-25', '13:00', 'textes.instagram', "Les fêtes approchent et les horaires de votre boulangerie changent. Votre fiche Google suit-elle ?\n\nLe matin du 24, un client veut sa bûche. Avant de sortir, il cherche « boulangerie » sur Google Maps. Les encadrés avec une note, des photos et des horaires sont des fiches Google, et la vôtre en fait partie.\n\nSi elle affiche vos horaires habituels alors que vous ouvrez plus tôt, ou fermé alors que vous êtes là, il ira ailleurs sans même essayer.\n\nPetit sondage du mercredi. Vos horaires de fêtes seront-ils sur votre fiche Google ?\nA. Oui, je les ajoute à chaque fois.\nB. J'y pense souvent trop tard.\nC. Je ne savais pas que c'était possible.\n\nVous répondez A, B ou C ?\n\n#FicheGoogle #Boulangerie #Boulanger #ReferencementLocal #GoogleBusinessProfile")  # e262a2c
T('2026-11-25', '13:00', 'visuel.slides.3.texte', "Oui à chaque fois, souvent trop tard, ou vous ne saviez pas que c'était possible ? Dites-le en commentaire.")  # e1ad39f
T('2026-11-25', '19:00', 'accroche', 'Paysagiste à Lille, le matériel rangé, vous passez encore la soirée sur votre fiche Google ?')  # ee70c4b
T('2026-11-25', '19:00', 'textes.tiktok', "Paysagiste à Lille, le matériel rangé, vous passez encore la soirée sur votre fiche Google ?\nVotre fiche Google, celle que vos clients voient sur Google Maps, demande chaque soir des photos à trier, des avis à lire et une publication à écrire.\n\n#FicheGoogle #Paysagiste #Lille\n\nAbonnez-vous pour d'autres astuces sur votre fiche Google. 30 jours offerts, lien en bio.")  # e45216e
T('2026-11-25', '19:00', 'textes.instagram', "Paysagiste à Lille, le matériel rangé, vous passez encore la soirée sur votre fiche Google ?\n\nLa journée finit tôt en hiver, mais elle ne finit pas vraiment. Une fois le camion vidé, il reste votre fiche Google, cette carte de visite que Google montre à votre place avec vos photos, vos avis et vos horaires.\n\nIl faut trier la photo de la haie taillée, remercier un client pour son avis, écrire une publication. Ce n'est jamais long, mais il y en a un peu chaque soir.\n\nProenligne s'en charge à votre place, avec une photo le lundi, une publication le jeudi et une réponse à chaque avis.\n\nEt vous, à quel moment vous occupez-vous de votre fiche Google ?\n\n30 jours offerts, lien en bio.\n\n#FicheGoogle #Paysagiste #Jardin #Lille #ReferencementLocal")  # ee68e1d
T('2026-11-25', '19:00', 'textes.facebook', "Paysagiste à Lille, le matériel rangé, vous passez encore la soirée sur votre fiche Google ?\n\nLe chantier est fini, mais la fiche Google, elle, attend encore. C'est l'encadré qu'un client ouvre sur Google Maps avant de vous appeler, avec vos photos, vos avis et vos horaires.\n\nIl faut trier les photos, répondre aux avis, écrire une nouvelle publication. Ce n'est jamais long, mais il y en a un peu chaque soir, et la soirée y passe.\n\nProenligne s'en occupe à votre place.\n\nVous préférez y passer vos soirées ou vos week-ends ?\n\nEssayez Proenligne gratuitement, 30 jours offerts.\n\n#FicheGoogle #Paysagiste #Jardin #Lille #ReferencementLocal")  # e6cc1ed
T('2026-11-26', '13:00', 'textes.instagram', "Un avis négatif sur votre fiche Google n'est pas toujours une catastrophe. Votre réponse compte souvent plus que lui.\n\nAvant d'appeler un serrurier, le client regarde votre fiche Google sur Google Maps, l'encadré où il lit vos horaires, les avis et vos réponses. Un avis sévère avec une réponse calme peut le rassurer. Un avis sévère sans réponse le fait douter.\n\nTrois règles pour répondre.\n1. Remerciez le client, même s'il est injuste.\n2. Expliquez les faits en une ou deux phrases calmes.\n3. Dites ce que vous avez changé, sans vous justifier.\n\nVous répondez plutôt tout de suite, le lendemain, ou jamais ?\n\n#FicheGoogle #Serrurier #AvisClients #ReferencementLocal #GoogleBusinessProfile")  # ed95954
T('2026-11-26', '13:00', 'visuel.slides.0.titre', 'Un merci désamorce la tension')  # e231c44
T('2026-11-26', '19:00', 'tiktok_title', 'Plombier à Brest, le voisin a votre note, mais sa fiche Google montre ses chantiers')  # e54e0a0
T('2026-11-26', '19:00', 'textes.tiktok', "Plombier à Brest, le voisin a la même note que vous, mais sa fiche Google montre ses chantiers.\nSur Google Maps, deux fiches Google ont la même note. Le client garde souvent celle qui a l'air vivante.\n\n#FicheGoogle #Plombier #Brest\n\nAbonnez-vous pour d'autres astuces sur votre fiche Google. 30 jours offerts, lien en bio.")  # ef58061
T('2026-11-26', '19:00', 'textes.instagram', "Plombier à Brest, le voisin a la même note que vous, mais sa fiche Google montre ses chantiers.\n\nIl est 22 h, l'eau coule sous l'évier. Le client ouvre Google Maps et compare deux fiches Google, ces encadrés avec la note, les photos et le bouton Appeler.\n\nLes deux ont la même note. Le voisin montre ses chantiers de la semaine. Si votre fiche Google ne montre rien de récent, le client ne peut pas savoir que vous travaillez.\n\nIl ne vous connaît pas. Il garde celui qui a l'air de travailler en ce moment.\n\nQuelle photo de chantier mettriez-vous en premier sur votre fiche Google ?\n\n30 jours offerts, lien en bio.\n\n#FicheGoogle #Plombier #Plomberie #Brest #ReferencementLocal")  # ede0c1c
T('2026-11-26', '19:00', 'textes.facebook', "Plombier à Brest, le voisin a la même note que vous, mais sa fiche Google montre ses chantiers.\n\nSur Google Maps, chaque plombier a sa fiche Google, avec la note, les photos et le bouton Appeler. C'est elle qu'on regarde avant de choisir.\n\nDeux fiches Google affichent la même note. L'une montre des chantiers récents, l'autre n'a rien publié depuis longtemps. Dans l'urgence, on garde celle qui a l'air active.\n\nSur votre fiche Google, quelle est la photo la plus récente ?\n\nEssayez Proenligne gratuitement, 30 jours offerts.\n\n#FicheGoogle #Plombier #Plomberie #Brest #ReferencementLocal")  # e8edaeb
T('2026-11-27', '13:00', 'accroche', "Avant, les avis de l'institut Petit restaient sans réponse sur sa fiche Google. Désormais, chaque avis reçoit un merci.")  # ee70c20
T('2026-11-27', '13:00', 'textes.instagram', "Avant, les avis de l'institut Petit restaient sans réponse sur sa fiche Google. Désormais, chaque avis reçoit un merci.\n\nC'est un exemple imaginaire. La fiche Google, c'est ce que vos clientes voient en premier quand elles cherchent un institut sur Google Maps, avec vos photos, vos horaires et vos avis.\n\nAvant, des clientes ravies avaient laissé un mot, et personne ne les avait remerciées. Une future cliente pouvait se demander si quelqu'un lisait.\n\nAprès, chaque avis a sa réponse, avec le prénom et le soin. Les réponses aux avis négatifs sont validées par l'institut avant d'être publiées.\n\nLa note n'a pas changé. L'impression, si.\n\nCombien d'avis attendent encore une réponse sur votre fiche Google ?\n\n#FicheGoogle #Estheticienne #InstitutDeBeaute #ReferencementLocal #GoogleBusinessProfile")  # e3af29a
T('2026-11-27', '13:00', 'visuel.titre', 'Sur cette fiche Google, chaque avis a maintenant sa réponse')  # e38c168
T('2026-11-27', '13:00', 'visuel.slides.0.titre', 'Avant, les avis restaient sans réponse')  # e305e38
T('2026-11-27', '13:00', 'visuel.slides.1.texte', "Chaque avis reçoit un merci personnalisé, et l'institut valide les réponses aux avis négatifs.")  # ea5ac4d
T('2026-11-27', '13:00', 'visuel.slides.2.texte', "En lisant les réponses sur la fiche Google de l'institut, elle voit qu'il y a quelqu'un derrière la porte.")  # e560032
T('2026-11-27', '19:00', 'premier_commentaire', "Un geste qui rassure. Ajoutez sur votre fiche Google une photo de l'atelier rangé et de l'équipe, pour que l'automobiliste voie à qui il confie sa voiture.")  # e06a2bf
T('2026-11-27', '19:00', 'textes.instagram', "« Je vais appeler l'autre garage. » Garagiste à Lorient, votre fiche Google y est pour quelque chose.\n\nUn voyant s'allume sur la route. L'automobiliste se gare et tape « garage » sur Google Maps. Il voit des fiches Google, avec la note, les avis, les photos et le bouton Appeler.\n\nImaginez que vos avis n'aient aucune réponse et qu'aucune photo ne montre l'atelier. Sur la fiche Google d'à côté, on voit l'équipe, des réponses aux avis et des nouvelles récentes.\n\nIl appelle l'autre garage, presque sans hésiter.\n\nQue voit un automobiliste en panne quand il ouvre votre fiche Google ?\n\n30 jours offerts, lien en bio.\n\n#FicheGoogle #Garagiste #Garage #Lorient #ReferencementLocal")  # e435310
T('2026-11-28', '12:30', 'textes.tiktok', "Plombier à Brest, entre deux fiches Google, laquelle le client garde-t-il ?\nSur Google Maps, ces deux fiches Google ont la même note. L'une montre des chantiers récents, l'autre n'a rien publié depuis longtemps.\n\n#FicheGoogle #Plombier #Brest\n\nAbonnez-vous pour d'autres astuces sur votre fiche Google. 30 jours offerts, lien en bio.")  # ef68ec9
T('2026-11-28', '13:00', 'visuel.titre', "Chaque semaine, Proenligne s'occupe de votre fiche Google")  # eb4d8dd
T('2026-11-28', '19:00', 'premier_commentaire', 'Une astuce de plus. Refaites la recherche avec « dépannage électrique » ou « électricien urgence », car vos clients ne tapent pas tous le même mot.')  # e4bc3f8
T('2026-11-28', '19:00', 'textes.tiktok', "Électricien à Vannes, on vous voit sur Google quand on cherche un électricien ?\nTapez « électricien Vannes » sur Google Maps. Les encadrés qui s'affichent sont des fiches Google, et celles du haut de la liste sont souvent celles qu'on appelle.\n\n#FicheGoogle #Electricien #Vannes\n\nAbonnez-vous pour voir les autres métiers et leur fiche Google. 30 jours offerts, lien en bio.")  # e6a44df
T('2026-11-29', '13:00', 'textes.instagram', "En hiver, le jardin dort, mais votre fiche Google n'a pas besoin de dormir avec lui. Petit quiz du dimanche.\n\nLa fiche Google, c'est la carte de visite que Google montre à votre place quand on cherche un paysagiste, avec vos photos, vos avis et votre téléphone. Certains clients préparent dès l'hiver leurs travaux du printemps et regardent déjà les fiches Google des paysagistes.\n\nQuelle photo publier en décembre ?\nA. Une pelouse de l'été dernier.\nB. Une haie taillée cette semaine.\nC. Le logo de l'entreprise.\n\nLa réponse est dans le carrousel. Et vous, quelle photo d'hiver publiez-vous cette semaine ?\n\n#FicheGoogle #Paysagiste #JardinDHiver #ReferencementLocal #GoogleBusinessProfile")  # e5a846c
T('2026-11-29', '13:00', 'visuel.slides.1.titre', "Pourquoi la pelouse d'été ne convient pas")  # edae2be
T('2026-11-29', '19:00', 'premier_commentaire', "Une astuce pour les auto-écoles. Après chaque permis réussi, demandez à l'élève s'il veut bien laisser un avis, car c'est le moment où il est le plus content.")  # ea4d069
T('2026-11-29', '19:00', 'textes.instagram', "Auto-école à Toulouse, il est 22 h, la dernière leçon est finie, et votre fiche Google vous attend.\n\nLa voiture est rangée, le planning de demain est prêt. Reste votre fiche Google, cet encadré qu'une famille ouvre sur Google Maps avant d'inscrire un élève.\n\nUn élève reçu au permis attend un merci sous son avis, et la photo de la nouvelle voiture attend d'être publiée. Rien de long, mais tout s'empile.\n\nProenligne s'en charge à votre place, avec une photo le lundi, une publication le jeudi et une réponse à chaque avis.\n\nÀ quelle heure finissez-vous vraiment votre journée ?\n\n30 jours offerts, lien en bio.\n\n#FicheGoogle #AutoEcole #PermisDeConduire #Toulouse #ReferencementLocal")  # e874143
T('2026-11-29', '19:00', 'textes.facebook', "Auto-école à Toulouse, il est 22 h, la dernière leçon est finie, et votre fiche Google vous attend.\n\nAvant d'inscrire un enfant, beaucoup de parents regardent la fiche Google de l'auto-école sur Google Maps, avec la note, les photos et les avis des anciens élèves.\n\nIl faut remercier un élève reçu, publier une photo de la voiture. Chaque soir, il y a un petit quelque chose, et la soirée raccourcit.\n\nProenligne s'en occupe pour vous, avec une photo le lundi, une publication le jeudi et une réponse à chaque avis.\n\nVous gardez combien de soirées libres par semaine ?\n\nEssayez Proenligne gratuitement, 30 jours offerts.\n\n#FicheGoogle #AutoEcole #PermisDeConduire #Toulouse #ReferencementLocal")  # e5c8b19

# ───────── Corrections après la relecture, passe 2 ─────────
T('2026-11-25', '13:00', 'visuel.slides.3.texte', "Vous les ajoutez toujours, vous y pensez trop tard, ou vous ne saviez pas que c'était possible ? Dites-le en commentaire.")  # e1ad39f
T('2026-11-25', '19:00', 'textes.tiktok', "Paysagiste à Lille, le matériel rangé, vous passez encore la soirée sur votre fiche Google ?\nVotre fiche Google, celle que vos clients voient sur Google Maps, demande un peu de temps chaque semaine, souvent le soir, avec des photos à trier, des avis à lire et une publication à écrire.\n\n#FicheGoogle #Paysagiste #Lille\n\nAbonnez-vous pour d'autres astuces sur votre fiche Google. 30 jours offerts, lien en bio.")  # e45216e
T('2026-11-25', '19:00', 'textes.facebook', "Paysagiste à Lille, le matériel rangé, vous passez encore la soirée sur votre fiche Google ?\n\nLe chantier est fini, mais la fiche Google, elle, attend encore. C'est l'encadré qu'un client ouvre sur Google Maps avant de vous appeler, avec vos photos, vos avis et vos horaires.\n\nIl faut trier les photos, répondre aux avis, écrire une nouvelle publication. Ce n'est jamais long, mais il y en a un peu chaque soir, et la soirée y passe.\n\nProenligne s'en occupe à votre place.\n\nCombien de soirées par semaine passez-vous sur votre fiche Google ?\n\nEssayez Proenligne gratuitement, 30 jours offerts.\n\n#FicheGoogle #Paysagiste #Jardin #Lille #ReferencementLocal")  # e6cc1ed
T('2026-11-27', '13:00', 'textes.instagram', "Avant, les avis de l'institut Petit restaient sans réponse sur sa fiche Google. Désormais, chaque avis reçoit un merci.\n\nC'est un exemple imaginaire. La fiche Google, c'est ce que vos clientes voient en premier quand elles cherchent un institut sur Google Maps, avec vos photos, vos horaires et vos avis.\n\nAvant, des clientes ravies avaient laissé un mot, et personne ne les avait remerciées. Une future cliente pouvait se demander si quelqu'un lisait.\n\nAprès, chaque avis a sa réponse, avec le prénom et le soin. C'est Proenligne qui écrit ces réponses, et l'institut valide celles aux avis négatifs avant qu'elles soient publiées.\n\nLa note n'a pas changé. L'impression, si.\n\nCombien d'avis attendent encore une réponse sur votre fiche Google ?\n\n#FicheGoogle #Estheticienne #InstitutDeBeaute #ReferencementLocal #GoogleBusinessProfile")  # e3af29a

# ───────── Corrections après la relecture, passe 3 ─────────
T('2026-11-25', '19:00', 'textes.facebook', "Paysagiste à Lille, le matériel rangé, vous passez encore la soirée sur votre fiche Google ?\n\nLe chantier est fini, mais la fiche Google, elle, attend encore. C'est l'encadré qu'un client ouvre sur Google Maps avant de vous appeler, avec vos photos, vos avis et vos horaires.\n\nIl faut choisir une photo, répondre aux avis, écrire une nouvelle publication. Chaque tâche est courte, mais elles reviennent chaque soir, et la soirée finit par y passer.\n\nProenligne s'en occupe à votre place, avec une photo le lundi, une publication le jeudi et une réponse à chaque avis.\n\nCombien de soirées par semaine passez-vous sur votre fiche Google ?\n\nEssayez Proenligne gratuitement, 30 jours offerts.\n\n#FicheGoogle #Paysagiste #Jardin #Lille #ReferencementLocal")  # e6cc1ed
T('2026-11-25', '13:00', 'visuel.slides.3.texte', 'Vous les ajoutez toujours, vous y pensez trop tard, ou vous ne saviez pas ? Dites-le en commentaire.')  # e1ad39f

# ───────── Ajustements de longueur imposés par outils/visuel.py (relus à nouveau) ─────────
T('2026-11-23', '13:00', 'visuel.titre', 'Faites voir votre nouvelle prestation sur Google')
T('2026-11-24', '13:00', 'visuel.slides.0.texte', "La seule photo montrait un muret de 2021. Le client pouvait se demander si l'entreprise existait encore.")
T('2026-11-29', '13:00', 'visuel.slides.1.titre', "La pelouse d'été ne convient pas")

# ───────── Corrections après la relecture, passe 4 ─────────
T('2026-11-25', '13:00', 'visuel.slides.3.texte', "Vous ajoutez toujours vos horaires de fêtes, vous y pensez trop tard, ou c'est une découverte ? Dites-le en commentaire.")  # e1ad39f
T('2026-11-25', '19:00', 'textes.facebook', "Paysagiste à Lille, le matériel rangé, vous passez encore la soirée sur votre fiche Google ?\n\nLe chantier est fini, mais la fiche Google, elle, attend encore. C'est l'encadré qu'un client ouvre sur Google Maps avant de vous appeler, avec vos photos, vos avis et vos horaires.\n\nIl faut choisir une photo, répondre aux avis, écrire une nouvelle publication. Chaque tâche est courte, mais elles reviennent chaque semaine, souvent le soir, une fois le camion vidé.\n\nProenligne s'en occupe à votre place, avec une photo le lundi, une publication le jeudi et une réponse à chaque avis.\n\nCombien de soirées par semaine passez-vous sur votre fiche Google ?\n\nEssayez Proenligne gratuitement, 30 jours offerts.\n\n#FicheGoogle #Paysagiste #Jardin #Lille #ReferencementLocal")  # e6cc1ed

# ───────── Corrections après la relecture, passe 5 ─────────


# ───────── Corrections après la relecture, passe 6 ─────────


C.sort(key=lambda c: (c['date'], c['creneau_nominal']))
p = os.path.join(ICI, f'{LUNDI}.json')
ancien = {}
if os.path.exists(p):
    for c in json.load(open(p, encoding='utf-8'))['creneaux']:
        ancien[(c['date'], c['creneau_nominal'])] = c.get('media') or {}
for c in C:
    if ancien.get((c['date'], c['creneau_nominal'])):
        c['media'] = ancien[(c['date'], c['creneau_nominal'])]
json.dump({'lundi': LUNDI, 'creneaux': C}, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(C), 'entrées')
