# Générateur du plan de la semaine du 2026-11-16 (écrit par la tâche hebdomadaire ; source des textes)
import json, subprocess, os
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
LUNDI = '2026-11-16'
p_grille = os.path.join(ICI, f'_grille_{LUNDI}.json')
if os.path.exists(p_grille):          # heures réelles tirées une seule fois (reprise sans nouveau tirage)
    grille = json.load(open(p_grille, encoding='utf-8'))
else:
    grille = json.loads(subprocess.check_output(['python3', os.path.join(RACINE, 'outils/heure_utc.py'), LUNDI, '--varier']))
    json.dump(grille, open(p_grille, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
H = {(g['date'], g['creneau_nominal']): g for g in grille}
TYPE = {'13:00': 'visuel', '19:00': 'video'}
C = []
HT = '#FicheGoogle #GoogleBusinessProfile #ReferencementLocal'


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


L, M, ME, J, V, S, D = '2026-11-16', '2026-11-17', '2026-11-18', '2026-11-19', '2026-11-20', '2026-11-21', '2026-11-22'
ABO = "Abonnez-vous pour d'autres astuces sur votre fiche Google. 30 jours offerts, lien en bio."

# ───────────────────────── LUNDI 16 ─────────────────────────
add(L, '13:00', intention='utile', metier='chauffagiste', angle='peur-de-perdre', format='conseil', ton='constat', symptome='photos-anciennes',
    slug='chauffagiste-trois-gestes-avant-hiver',
    accroche="Les premiers froids arrivent, et c'est souvent sur Google qu'on cherche un chauffagiste en urgence.",
    premier_commentaire="Une astuce de plus. Prenez la photo de la chaudière juste après la pose, à la lumière du jour, avec le local bien rangé autour.",
    visuel={'gabarit': 'conseil', 'surtitre': "Chauffagistes, votre fiche Google avant l'hiver", 'titre': 'Trois gestes pour réveiller votre fiche Google',
            'mot': 'réveiller',
            'points': ["Publiez la photo d'une chaudière que vous venez de poser",
                       "Vérifiez que vos horaires de dépannage sont bien affichés",
                       "Répondez aux derniers avis, même aux plus courts"],
            'cta': 'question', 'question': 'Par lequel de ces trois gestes commencez-vous cette semaine ?',
            'slides': [
                {'type': 'point', 'numero': '1', 'titre': 'Une photo récente rassure', 'texte': "Une chaudière posée la semaine dernière montre au client que votre entreprise travaille en ce moment."},
                {'type': 'point', 'numero': '2', 'titre': 'Des horaires justes évitent un appel raté', 'texte': "Si vous dépannez le samedi, votre fiche Google doit le dire. Sinon, le client appelle quelqu'un d'autre."},
                {'type': 'point', 'numero': '3', 'titre': 'Une réponse montre que vous lisez', 'texte': "Un merci sous un avis montre au futur client qu'il y a quelqu'un derrière la fiche Google."},
                {'type': 'fin', 'titre': 'Et vous, cette semaine ?', 'texte': "Photo, horaires ou avis, par quoi commencez-vous avant les grands froids ?"}]},
    textes={
        'instagram': "Les premiers froids arrivent, et c'est souvent sur Google qu'on cherche un chauffagiste en urgence.\n\nLa chaudière s'arrête un soir, le client prend son téléphone et tape « chauffagiste » avec sa ville. Google lui montre des fiches Google, ces encadrés avec la note, les photos, les horaires et le bouton Appeler. Votre fiche Google en fait partie.\n\nTrois gestes pour la réveiller avant les grands froids.\n1. Publiez la photo d'une chaudière que vous venez de poser.\n2. Vérifiez que vos horaires de dépannage sont bien affichés.\n3. Répondez aux derniers avis, même aux plus courts.\n\nPar lequel commencez-vous cette semaine ?\n\n#FicheGoogle #Chauffagiste #Chauffage #ReferencementLocal #GoogleBusinessProfile",
    })

add(L, '19:00', intention='utile', metier='garage', angle='gain-de-temps', format='journee', ton='scene', symptome='avis-sans-reponse',
    slug='garage-soiree-avis-angers',
    accroche="Garagiste à Angers, l'atelier ferme, pas votre fiche Google.",
    premier_commentaire="Une réponse d'avis n'a pas besoin d'être longue. Un merci, le prénom du client et la réparation faite suffisent, et le client suivant voit que vous lisez.",
    tiktok_title="Garagiste à Angers, l'atelier ferme, pas votre fiche Google",
    youtube_title="Garagiste, l'atelier ferme le soir, mais votre fiche Google attend encore",
    textes={
        'tiktok': "Garagiste à Angers, l'atelier ferme, pas votre fiche Google.\nLes voitures sont rendues, et il reste les avis à lire et à remercier sur votre fiche Google, celle que vos clients voient sur Google Maps.\n\n#FicheGoogle #Garagiste #Angers\n\n" + ABO,
        'instagram': "Garagiste à Angers, l'atelier ferme, pas votre fiche Google.\n\nIl est presque 22 h. Les clés sont rendues, le rideau est baissé. Sur le téléphone, il reste votre fiche Google, l'encadré qu'un automobiliste ouvre sur Google Maps avant de vous confier sa voiture.\n\nUn client qui remercie pour une vidange, un autre qui raconte sa panne réparée, un avis plus sec à traiter calmement. Il y en a un peu chaque soir.\n\nProenligne répond à chaque avis à votre place, et vous fait valider les réponses aux avis négatifs.\n\nÀ quel moment de la journée répondez-vous à vos avis, vous ?\n\n30 jours offerts, lien en bio.\n\n#FicheGoogle #Garagiste #Garage #Angers #ReferencementLocal",
        'youtube': "Garagiste à Angers, l'atelier ferme le soir, mais votre fiche Google attend encore.\n\nLa fiche Google, c'est ce qui apparaît quand un automobiliste cherche un garage sur Google ou Google Maps, avec vos photos, vos avis et vos horaires. Répondre aux avis se fait souvent le soir, après la journée d'atelier.\n\nProenligne publie une photo le lundi, une publication le jeudi, et répond à chaque avis à votre place.\n\nEt vous, quand trouvez-vous le temps de répondre à vos avis ?\n\n#FicheGoogle #Garagiste #Angers",
        'facebook': "Garagiste à Angers, l'atelier ferme, pas votre fiche Google.\n\nLe soir, une fois le rideau baissé, il reste souvent les avis à lire. Ils s'affichent sur votre fiche Google, l'encadré que les automobilistes consultent sur Google Maps avant de choisir un garage.\n\nUn merci pour une réparation rapide, une remarque sur un délai, un client qui hésite encore. Chaque avis sans réponse reste visible longtemps.\n\nProenligne répond à chaque avis pour vous, et vous soumet toujours les réponses aux avis négatifs.\n\nVous répondez à vos avis le soir, ou plutôt le week-end ?\n\nEssayez Proenligne gratuitement, 30 jours offerts.\n\n#FicheGoogle #Garagiste #Garage #Angers #ReferencementLocal",
    })

# ───────────────────────── MARDI 17 ─────────────────────────
add(M, '13:00', intention='preuve', metier='paysagiste', angle='preuve', format='avant-apres', ton='avant-apres', symptome='pas-de-nouveaute',
    slug='paysagiste-avant-apres-novembre',
    accroche="Avant, la fiche Google du paysagiste Durand ne montrait plus rien depuis l'été. Après, elle montre les tailles de novembre.",
    premier_commentaire="En hiver, les sujets de photo ne manquent pas. Élagage, taille des haies, protection des massifs, plantation d'arbres fruitiers ou préparation des pelouses.",
    visuel={'gabarit': 'avant-apres', 'surtitre': "Démonstration sur la fiche Google d'un paysagiste", 'titre': 'La même fiche Google, réveillée en novembre',
            'mot': 'réveillée en novembre',
            'carte': {'enseigne': 'Paysagiste Durand', 'metier': 'Paysagiste', 'avant': 'Dernière photo en juillet', 'apres': 'Une taille de haie chaque lundi'},
            'cta': 'question', 'question': "Votre fiche Google montre-t-elle vos chantiers d'hiver ?",
            'slides': [
                {'type': 'point', 'numero': '1', 'titre': 'Avant, la fiche Google se taisait', 'texte': "Les dernières photos dataient de l'été. En novembre, le client pouvait se demander si l'entreprise travaillait encore."},
                {'type': 'point', 'numero': '2', 'titre': 'Après, une photo chaque lundi', 'texte': "Une haie taillée, un élagage, un massif préparé. Chaque semaine, la fiche Google montre un vrai chantier de saison."},
                {'type': 'point', 'numero': '3', 'titre': 'Le client voit une entreprise active', 'texte': "En comparant deux fiches Google, il voit tout de suite laquelle travaille en ce moment."},
                {'type': 'fin', 'titre': 'Et la vôtre, en ce moment ?', 'texte': "Votre fiche Google montre-t-elle l'été dernier, ou vos chantiers d'hiver ?"}]},
    textes={
        'instagram': "Avant, la fiche Google du paysagiste Durand ne montrait plus rien depuis l'été. Après, elle montre les tailles de novembre.\n\nC'est un exemple imaginaire, mais la scène est courante. La fiche Google, c'est la carte de visite que Google montre à votre place, avec vos photos, vos avis, vos horaires et votre téléphone.\n\nAvant, la dernière photo montrait une pelouse de juillet. Un client qui cherchait un paysagiste en novembre pouvait se demander si l'entreprise travaillait encore.\n\nAprès, chaque lundi, une photo de saison. Une haie taillée, un élagage, un massif protégé pour l'hiver.\n\nLe client qui compare deux fiches Google voit tout de suite laquelle est active.\n\nEt votre fiche Google, elle montre quelle saison en ce moment ?\n\n#FicheGoogle #Paysagiste #JardinDHiver #ReferencementLocal #GoogleBusinessProfile",
        'linkedin': "En novembre, la fiche Google d'une entreprise de paysage montre souvent encore l'été.\nC'est pourtant elle que le client consulte en premier quand il cherche un paysagiste près de chez lui.\n\nLa fiche Google, c'est l'encadré que Google affiche avec le nom, la note, les photos et le numéro de l'entreprise.\n\nPrenons un exemple imaginaire, le paysagiste Durand.\nAvant, sa dernière photo datait de juillet. Rien n'indiquait que l'entreprise travaillait encore à l'automne.\nAprès, une photo de chantier paraît chaque lundi. Une haie taillée, un élagage, un massif préparé pour l'hiver.\n\nLa note n'a pas changé. Ce qui change, c'est l'impression laissée au client qui compare deux entreprises. Une fiche Google active montre une équipe au travail et une saison prise au sérieux.\n\nC'est ce que fait Proenligne pour les artisans, avec une photo le lundi, une publication le jeudi et une réponse à chaque avis.\n\nDans votre entreprise, qui s'occupe de la fiche Google pendant la saison creuse ?\n\n#FicheGoogle #GoogleBusinessProfile #ReferencementLocal #Paysagiste #TPE",
    })

add(M, '19:00', intention='utile', metier='serrurier', angle='peur-de-perdre', format='fiche', ton='question', symptome='concurrent-plus-riche', ab='A',
    slug='serrurier-duel-tours',
    accroche="Serrurier à Tours, pourquoi on appelle l'autre sur Google ?",
    premier_commentaire="Le client bloqué dehors lit vite. Une réponse polie sous un avis difficile le rassure souvent plus qu'une note parfaite sans aucune réponse.",
    tiktok_title="Serrurier à Tours, pourquoi on appelle l'autre sur Google ?",
    youtube_title="Serrurier, pourquoi le client choisit la fiche Google d'en face ?",
    textes={
        'tiktok': "Serrurier à Tours, pourquoi on appelle l'autre sur Google ?\nBloqué dehors, le client compare deux fiches Google sur Google Maps. La sienne répond aux avis, la vôtre se tait.\n\n#FicheGoogle #Serrurier #Tours\n\n" + ABO,
        'instagram': "Serrurier à Tours, pourquoi on appelle l'autre sur Google ?\n\nUn soir, une cliente claque sa porte avec les clés à l'intérieur. Elle ouvre Google Maps et tape « serrurier ». Deux fiches Google apparaissent, ces encadrés avec la note, les avis et le bouton Appeler. Votre fiche Google est l'une des deux.\n\nMême note pour les deux. Mais sous chaque avis de l'autre serrurier, il y a une réponse. Sous les vôtres, rien.\n\nElle est pressée, elle a froid, elle ne connaît personne. Elle appelle celui qui a l'air présent.\n\nVous, vous répondez à vos avis ?\n\n30 jours offerts, lien en bio.\n\n#FicheGoogle #Serrurier #Serrurerie #Tours #ReferencementLocal",
        'youtube': "Serrurier à Tours, pourquoi le client appelle-t-il l'autre sur Google ?\n\nAvant d'appeler un serrurier, le client ouvre sa fiche Google sur Google Maps et lit les avis, les horaires et vos réponses. À note égale, une fiche Google où chaque avis a une réponse inspire confiance.\n\nProenligne répond à chacun de vos avis, publie une photo le lundi et une publication le jeudi.\n\nEt sur votre fiche Google, combien d'avis attendent encore une réponse ?\n\n#FicheGoogle #Serrurier #Tours",
        'facebook': "Serrurier à Tours, pourquoi on appelle l'autre sur Google ?\n\nBloqué dehors, le client prend son téléphone. Sur Google Maps, chaque serrurier a sa fiche Google, avec la note, les photos et le bouton Appeler. C'est elle qu'on regarde avant de choisir.\n\nDeux fiches Google, la même note. D'un côté, chaque avis a reçu une réponse. De l'autre, des avis restés sans un mot.\n\nDans l'urgence, le client appelle celui qui a l'air de répondre.\n\nSur votre fiche Google, le dernier avis a-t-il sa réponse ?\n\nEssayez Proenligne gratuitement, 30 jours offerts.\n\n#FicheGoogle #Serrurier #Serrurerie #Tours #ReferencementLocal",
    })

# ───────────────────────── MERCREDI 18 ─────────────────────────
add(ME, '13:00', intention='utile', metier='estheticienne', angle='peur-de-perdre', format='question', ton='replique', symptome='service-invisible',
    slug='estheticienne-sondage-soins-visibles',
    accroche="« Ah, vous faites aussi les soins du visage ? » Votre fiche Google ne le disait pas.",
    premier_commentaire="Dans la rubrique Services de votre fiche Google, chaque soin peut avoir sa propre description. Une ou deux phrases simples suffisent, avec le nom que vos clientes utilisent.",
    visuel={'gabarit': 'question', 'surtitre': 'Esthéticiennes, le petit sondage du mercredi', 'titre': 'Vos soins sont-ils visibles sur votre fiche Google ?',
            'mot': 'visibles',
            'reponses': ['Oui, tous, avec des photos', 'Quelques-uns, pas les nouveaux', "Non, seulement le nom de l'institut"],
            'cta': 'question', 'question': 'Et vous, quelle réponse choisissez-vous ?',
            'slides': [
                {'type': 'point', 'numero': '1', 'titre': 'Une cliente cherche un soin précis', 'texte': "Elle tape « soin du visage » et sa ville. Google lui montre des fiches Google avec photos et services."},
                {'type': 'point', 'numero': '2', 'titre': 'Un soin absent passe inaperçu', 'texte': "Si votre fiche Google ne cite pas ce soin, la cliente peut ne jamais savoir que vous le proposez."},
                {'type': 'point', 'numero': '3', 'titre': 'La rubrique Services sert à ça', 'texte': "Ajoutez chaque soin avec une phrase simple, puis une photo de la cabine prête à accueillir."},
                {'type': 'fin', 'titre': 'Alors, quelle réponse ?', 'texte': "Tous vos soins, quelques-uns ou aucun ? Dites-le-nous en commentaire."}]},
    textes={
        'instagram': "« Ah, vous faites aussi les soins du visage ? » Votre fiche Google ne le disait pas.\n\nCette phrase, beaucoup d'esthéticiennes l'entendent de la bouche de clientes fidèles. Et les nouvelles clientes, elles, ne la prononcent jamais, parce qu'elles ne savent pas.\n\nQuand on tape « soin du visage » et sa ville, Google affiche des fiches Google avec photos, avis et services. La vôtre en fait partie, mais elle ne montre que ce que vous y avez mis.\n\nPetit sondage du mercredi. Vos soins sont-ils visibles sur votre fiche Google ?\nA. Oui, tous, avec des photos.\nB. Quelques-uns, pas les nouveaux.\nC. Non, seulement le nom de l'institut.\n\nVous répondez A, B ou C ?\n\n#FicheGoogle #Estheticienne #InstitutDeBeaute #ReferencementLocal #GoogleBusinessProfile",
    })

add(ME, '19:00', intention='utile', metier='autoecole', angle='peur-de-perdre', format='fiche', ton='pendant-que', symptome='photos-anciennes',
    slug='autoecole-swipe-appels-caen',
    accroche="Auto-école à Caen, pendant que vous êtes en leçon, on passe votre fiche Google.",
    premier_commentaire="Une photo de la voiture école devant l'agence, une autre du moniteur avec un élève qui vient d'avoir son permis, avec son accord. Deux photos suffisent pour commencer.",
    tiktok_title="Auto-école à Caen, on passe votre fiche Google pendant la leçon ?",
    youtube_title="Auto-école, pendant la leçon, un futur élève passe votre fiche Google",
    textes={
        'tiktok': "Auto-école à Caen, pendant que vous êtes en leçon, on passe votre fiche Google.\nUn futur élève fait défiler les fiches Google des auto-écoles. Pas de photo des voitures, pas de nouvelles, et il passe à la suivante.\n\n#FicheGoogle #AutoEcole #Caen\n\n" + ABO,
        'instagram': "Auto-école à Caen, pendant que vous êtes en leçon, on passe votre fiche Google.\n\nUn lycéen et sa mère cherchent une auto-école. Ils tapent « auto-école » sur Google Maps. Chaque école a sa fiche Google, avec la note, les photos et le bouton Appeler.\n\nIls font défiler. Une fiche Google sans photo des voitures ni nouvelles récentes, ils la passent sans s'arrêter. Une autre montre la voiture école, l'équipe, une réussite au permis. C'est là qu'ils appellent.\n\nPendant ce temps, vous êtes en leçon, et vous ne le saurez jamais.\n\nQue montre la première photo de votre fiche Google aujourd'hui ?\n\n30 jours offerts, lien en bio.\n\n#FicheGoogle #AutoEcole #PermisDeConduire #Caen #ReferencementLocal",
        'youtube': "Auto-école à Caen, pendant que vous êtes en leçon, un futur élève passe votre fiche Google.\n\nLa fiche Google, c'est ce qui s'affiche quand on cherche « auto-école » sur Google ou Google Maps, avec vos photos, vos avis et vos horaires. Les familles comparent plusieurs fiches Google avant d'appeler.\n\nProenligne publie une photo le lundi, une publication le jeudi, et répond à chaque avis, pendant que vous êtes sur la route avec vos élèves.\n\nQuelle photo de votre auto-école mettriez-vous en premier ?\n\n#FicheGoogle #AutoEcole #Caen",
        'facebook': "Auto-école à Caen, pendant que vous êtes en leçon, on passe votre fiche Google.\n\nAvant de s'inscrire, une famille compare souvent plusieurs auto-écoles sur Google Maps. Chacune a sa fiche Google, cet encadré avec la note, les photos, les horaires et le bouton Appeler.\n\nUne fiche Google sans photo de la voiture école ni nouvelles récentes, on la fait défiler. Celle qui montre l'équipe et les élèves reçus donne envie d'appeler.\n\nEt vous, que voit une famille en ouvrant votre fiche Google ?\n\nEssayez Proenligne gratuitement, 30 jours offerts.\n\n#FicheGoogle #AutoEcole #PermisDeConduire #Caen #ReferencementLocal",
    })

# ───────────────────────── JEUDI 19 ─────────────────────────
add(J, '13:00', intention='utile', metier='macon', angle='gain-de-temps', format='conseil', ton='contre-intuitif', symptome='pas-de-nouveaute',
    slug='macon-chantier-en-cours',
    accroche="Un chantier n'a pas besoin d'être fini pour se montrer sur votre fiche Google.",
    premier_commentaire="Pensez à demander l'accord du client avant de publier une photo prise chez lui, surtout si la maison ou la rue sont reconnaissables.",
    visuel={'gabarit': 'conseil', 'surtitre': 'Maçons, une idée pour votre fiche Google', 'titre': "Montrez le chantier pendant qu'il avance",
            'mot': "pendant qu'il avance",
            'points': ["Photographiez les fondations avant de couler la dalle",
                       "Montrez le mur en cours de montage, chantier rangé",
                       "Publiez la photo finale quand tout est terminé"],
            'cta': 'question', 'question': 'Vous sortez le téléphone pendant vos chantiers, ou à la fin ?',
            'slides': [
                {'type': 'point', 'numero': '1', 'titre': 'Un chantier en cours rassure aussi', 'texte': "Le client voit votre façon de travailler, un chantier propre et le soin apporté à chaque étape."},
                {'type': 'point', 'numero': '2', 'titre': 'Une photo par étape suffit', 'texte': "Fondations, montage, finitions. Trois photos, et votre fiche Google raconte un vrai chantier."},
                {'type': 'point', 'numero': '3', 'titre': 'Le client se projette chez lui', 'texte': "Il voit ce qui l'attend, du premier coup de pelle jusqu'au mur terminé."},
                {'type': 'fin', 'titre': 'Et sur vos chantiers ?', 'texte': "Vous pensez à prendre des photos pendant les travaux, ou seulement à la fin ?"}]},
    textes={
        'instagram': "Un chantier n'a pas besoin d'être fini pour se montrer sur votre fiche Google.\n\nVotre fiche Google, c'est ce qui s'affiche quand un client cherche « maçon » sur Google ou Google Maps, avec vos photos, vos avis et vos horaires. Beaucoup de maçons n'y mettent que des chantiers terminés, et parfois rien pendant longtemps.\n\nUn chantier en cours parle aussi. Il montre votre façon de travailler.\n1. Photographiez les fondations avant de couler la dalle.\n2. Montrez le mur en cours de montage, chantier rangé.\n3. Publiez la photo finale quand tout est terminé.\n\nVous sortez le téléphone pendant vos chantiers, ou seulement à la fin ?\n\n#FicheGoogle #Macon #Maconnerie #ReferencementLocal #GoogleBusinessProfile",
        'linkedin': "Pour une entreprise de maçonnerie, la fiche Google n'a pas besoin d'attendre la fin d'un chantier.\nUn chantier en cours peut rassurer un futur client autant qu'une réalisation terminée.\n\nLa fiche Google, c'est l'encadré qui présente l'entreprise sur Google et Google Maps, avec la note, les photos et le téléphone. Beaucoup d'entreprises n'y publient que des chantiers finis, donc rarement.\n\nUne autre méthode consiste à photographier chaque étape.\nLes fondations, avant de couler la dalle.\nLe mur en cours de montage, sur un chantier rangé.\nLe résultat final, une fois le chantier terminé.\n\nTrois photos suffisent pour raconter un chantier. Le client y voit une méthode, une propreté et un suivi, des critères qu'il a du mal à juger autrement avant de signer un devis.\n\nProenligne s'occupe de la fiche Google des artisans chaque semaine, avec une photo le lundi, une publication le jeudi et une réponse à chaque avis.\n\nDans vos équipes, qui pense à prendre les photos pendant les travaux ?\n\n#FicheGoogle #GoogleBusinessProfile #ReferencementLocal #Maconnerie #Artisanat",
    })

add(J, '19:00', intention='utile', metier='electricien', angle='gain-de-temps', format='journee', ton='scene', symptome='avis-sans-reponse', ab='A',
    slug='electricien-soirees-saint-brieuc',
    accroche="Électricien à Saint-Brieuc, encore devant votre fiche Google à 23 h, après une longue journée de chantier ?",
    premier_commentaire="Une publication de fiche Google peut être très simple. Un tableau électrique refait, deux phrases sur le chantier, et c'est tout.",
    tiktok_title="Électricien à Saint-Brieuc, encore devant votre fiche Google à 23 h ?",
    youtube_title="Électricien, encore devant votre fiche Google le soir ?",
    textes={
        'tiktok': "Électricien à Saint-Brieuc, encore devant votre fiche Google à 23 h, après une longue journée de chantier ?\nIl est 23 h, et il reste des photos à publier et des avis à remercier sur la fiche Google que vos clients voient sur Google Maps.\n\n#FicheGoogle #Electricien #SaintBrieuc\n\n" + ABO,
        'instagram': "Électricien à Saint-Brieuc, encore devant votre fiche Google à 23 h, après une longue journée de chantier ?\n\nIl est 23 h. La camionnette est garée, la journée de chantier est finie. Sur le canapé, il reste votre fiche Google, l'encadré qu'on découvre sur Google Maps en cherchant un électricien.\n\nLa photo du tableau refait cet après-midi, deux clients à remercier pour leur avis, une question sur une borne de recharge. Un peu chaque soir.\n\nProenligne publie et répond pendant la journée, à votre place. Le soir, vous débranchez, vous aussi.\n\nÀ quelle heure vous occupez-vous de votre fiche Google, en général ?\n\n30 jours offerts, lien en bio.\n\n#FicheGoogle #Electricien #Electricite #SaintBrieuc #ReferencementLocal",
        'youtube': "Électricien à Saint-Brieuc, encore devant votre fiche Google le soir ?\n\nLa fiche Google, c'est l'encadré qui présente votre entreprise sur Google et Google Maps, avec vos photos, vos avis et votre numéro. La tenir à jour finit souvent tard, après les chantiers.\n\nProenligne publie une photo le lundi, une publication le jeudi, et répond à chaque avis pendant la journée.\n\nEt vous, quand mettez-vous votre fiche Google à jour ?\n\n#FicheGoogle #Electricien #SaintBrieuc",
        'facebook': "Électricien à Saint-Brieuc, encore devant votre fiche Google à 23 h, après une longue journée de chantier ?\n\nLa journée de chantier se termine, et une autre commence sur le téléphone. Photos à publier, avis à remercier, questions de clients. Tout cela s'affiche sur votre fiche Google, l'encadré que les clients consultent sur Google Maps avant d'appeler un électricien.\n\nProenligne s'en occupe en journée, avec une photo le lundi, une publication le jeudi et une réponse à chaque avis.\n\nLe soir, vous rangez le téléphone à quelle heure ?\n\nEssayez Proenligne gratuitement, 30 jours offerts.\n\n#FicheGoogle #Electricien #Electricite #SaintBrieuc #ReferencementLocal",
    })

add(J, '12:30', intention='utile', metier='serrurier', angle='peur-de-perdre', format='fiche', ton='question', symptome='concurrent-plus-riche', ab='B',
    slug='serrurier-duel-tours',
    accroche="Serrurier à Tours, le client compare deux fiches Google.",
    premier_commentaire="Une réponse courte suffit sous un avis. Un merci, le service rendu, et le client suivant voit que vous êtes joignable.",
    tiktok_title="Serrurier à Tours, le client compare deux fiches Google",
    textes={
        'tiktok': "Serrurier à Tours, le client compare deux fiches Google.\nBloqué dehors, il regarde la note, les photos et surtout les réponses aux avis. Votre fiche Google a-t-elle l'air aussi présente que celle d'en face ?\n\n#FicheGoogle #Serrurier #Tours\n\nAbonnez-vous pour voir les autres métiers face à leur concurrent. 30 jours offerts, lien en bio.",
    })

# ───────────────────────── VENDREDI 20 ─────────────────────────
add(V, '13:00', intention='utile', metier='coiffeur', angle='gain-de-temps', format='question', ton='question', symptome='avis-sans-reponse',
    slug='coiffeur-sondage-reponses-avis',
    accroche="Répondez-vous aux avis de votre fiche Google, ou seulement quand ils sont mauvais ?",
    premier_commentaire="Une réponse courte suffit. Remerciez, citez la prestation, et invitez la cliente à revenir pour sa prochaine coupe.",
    visuel={'gabarit': 'question', 'surtitre': 'Coiffeurs, le sondage du vendredi', 'titre': 'Répondez-vous aux avis de votre fiche Google ?',
            'mot': 'Répondez-vous',
            'reponses': ['Oui, à chaque avis', 'Seulement aux mauvais', 'Rarement, faute de temps'],
            'cta': 'question', 'question': 'Et vous, quelle réponse vous ressemble ?',
            'slides': [
                {'type': 'point', 'numero': '1', 'titre': 'Une réponse se lit aussi', 'texte': "Une cliente qui hésite entre deux salons lit les avis, et souvent les réponses du salon."},
                {'type': 'point', 'numero': '2', 'titre': 'Un merci suffit souvent', 'texte': "Sous un avis positif, une phrase avec le prénom et la coupe réalisée montre que vous lisez."},
                {'type': 'point', 'numero': '3', 'titre': 'Un avis négatif se traite au calme', 'texte': "Répondez le lendemain, poliment, et proposez d'en parler au salon. La cliente suivante verra votre sérieux."},
                {'type': 'fin', 'titre': 'Alors, laquelle vous ressemble ?', 'texte': "À chaque avis, seulement aux mauvais, ou rarement ? Dites-le-nous en commentaire."}]},
    textes={
        'instagram': "Répondez-vous aux avis de votre fiche Google, ou seulement quand ils sont mauvais ?\n\nSur Google Maps, chaque salon a sa fiche Google, avec la note, les photos et les avis. C'est elle qu'une cliente regarde avant de réserver, et elle lit souvent les réponses du salon autant que les avis.\n\nLe sondage du vendredi.\nA. Oui, à chaque avis.\nB. Seulement aux mauvais.\nC. Rarement, faute de temps.\n\nPas de bonne ou de mauvaise réponse, on est curieux de savoir comment vous faites. Vous êtes plutôt A, B ou C ?\n\n#FicheGoogle #Coiffeur #Coiffure #Salon #ReferencementLocal",
    })

add(V, '19:00', intention='utile', metier='boulangerie', angle='peur-de-perdre', format='recherche', ton='constat', symptome='fiche-oubliee',
    slug='boulangerie-classement-bordeaux',
    accroche="Boulangerie à Bordeaux, votre pain est sur Google ?",
    premier_commentaire="Les photos qui donnent le plus envie d'entrer sont souvent les plus simples. La vitrine du matin, une fournée qui sort du four, le comptoir garni.",
    tiktok_title="Boulangerie à Bordeaux, votre pain est sur Google ?",
    youtube_title="Boulangerie, votre fiche Google donne-t-elle envie de pousser la porte ?",
    textes={
        'tiktok': "Boulangerie à Bordeaux, votre pain est sur Google ?\nOn cherche une boulangerie près de chez soi, Google montre des fiches Google, et on entre souvent dans la première qui donne envie.\n\n#FicheGoogle #Boulangerie #Bordeaux\n\n" + ABO,
        'instagram': "Boulangerie à Bordeaux, votre pain est sur Google ?\n\nUn dimanche matin, dans un quartier qu'on connaît mal, on tape « boulangerie » sur son téléphone. Les encadrés avec une note, des photos et un itinéraire sont des fiches Google. On en regarde deux ou trois, rarement plus.\n\nUne fiche Google qui montre la vitrine du matin, les viennoiseries et les horaires du dimanche donne envie de faire le détour. Une fiche Google sans photo, on la passe.\n\nVotre fiche Google montre-t-elle votre vitrine, aujourd'hui ?\n\n30 jours offerts, lien en bio.\n\n#FicheGoogle #Boulangerie #Boulanger #Bordeaux #ReferencementLocal",
        'youtube': "Boulangerie à Bordeaux, votre pain est-il sur Google ?\n\nCherchez « boulangerie » dans votre ville. Les encadrés avec une note et des photos sont des fiches Google. Votre fiche Google en fait partie. Avant de pousser une porte, beaucoup de passants y regardent la vitrine, les horaires et l'itinéraire.\n\nProenligne publie une photo le lundi, une publication le jeudi, et répond à chaque avis de votre boulangerie.\n\nQuelle photo de votre boutique mettriez-vous en premier ?\n\n#FicheGoogle #Boulangerie #Bordeaux",
        'facebook': "Boulangerie à Bordeaux, votre pain est sur Google ?\n\nQuand on arrive dans un quartier, on cherche souvent la boulangerie sur son téléphone. Google affiche alors des fiches Google, avec la note, les photos, les horaires et l'itinéraire. La vôtre en fait partie.\n\nSi elle montre une vitrine bien garnie et des horaires justes, on fait le détour. Si elle ne montre rien, on entre dans celle d'à côté.\n\nQue voit-on aujourd'hui en ouvrant votre fiche Google ?\n\nEssayez Proenligne gratuitement, 30 jours offerts.\n\n#FicheGoogle #Boulangerie #Boulanger #Bordeaux #ReferencementLocal",
    })

# ───────────────────────── SAMEDI 21 ─────────────────────────
add(S, '13:00', intention='offre', metier='general', angle='gain-de-temps', format='conseil', ton='contre-intuitif', symptome=None,
    slug='offre-fiche-google-sans-vos-soirees',
    accroche="On pense qu'il faut des soirées pour tenir une fiche Google. Proenligne s'en charge à votre place.",
    premier_commentaire="Pendant l'essai, rien ne change dans votre façon de travailler. Vous continuez votre métier, la fiche Google est suivie chaque semaine. 30 jours offerts, le lien est en bio.",
    visuel={'gabarit': 'conseil', 'surtitre': "Proenligne s'occupe de votre fiche Google", 'titre': 'Trois choses faites pour vous chaque semaine',
            'mot': 'pour vous',
            'points': ["Publier une photo de votre travail chaque lundi",
                       "Publier une actualité sur votre fiche Google le jeudi",
                       "Répondre à chaque avis, négatifs validés par vous"],
            'cta': 'offre',
            'slides': [
                {'type': 'point', 'numero': '1', 'titre': 'Le lundi, une photo', 'texte': "Chaque lundi, une photo de votre travail est publiée sur votre fiche Google."},
                {'type': 'point', 'numero': '2', 'titre': 'Le jeudi, une publication', 'texte': "Une actualité courte sur votre métier, votre saison ou vos services, publiée sur votre fiche Google."},
                {'type': 'point', 'numero': '3', 'titre': 'Chaque avis reçoit une réponse', 'texte': "Les réponses aux avis négatifs vous sont toujours soumises avant d'être publiées."},
                {'type': 'fin', 'titre': 'Essayez Proenligne gratuitement', 'texte': "30 jours offerts, sans engagement. Le lien est dans la bio."}]},
    textes={
        'instagram': "On pense qu'il faut des soirées pour tenir une fiche Google. Proenligne s'en charge à votre place.\n\nLa fiche Google, c'est ce que vos clients voient en premier quand ils cherchent votre métier sur Google Maps, avec vos photos, vos avis et vos horaires. Elle demande un peu d'attention chaque semaine, et c'est souvent le soir qu'on la lui donne.\n\nAvec Proenligne, chaque semaine\n✅ une photo de votre travail est publiée le lundi\n✅ une publication paraît le jeudi\n✅ chaque avis reçoit une réponse, et vous validez celles aux avis négatifs\n\nEssayez Proenligne gratuitement, 30 jours offerts, sans engagement. Lien en bio.\n\n#FicheGoogle #Artisan #Commercant #ReferencementLocal #GoogleBusinessProfile",
    })

add(S, '19:00', intention='utile', metier='plombier', angle='peur-de-perdre', format='recherche', ton='replique', symptome='photos-anciennes',
    slug='plombier-swipe-appels-montpellier',
    accroche="« On prend le suivant. » Plombier à Montpellier, c'est votre fiche Google qu'on passe.",
    premier_commentaire="Pour une photo de chantier de plomberie, cadrez le travail fini et propre. Une salle de bains refaite ou une chaudière raccordée parlent plus qu'une photo de camionnette.",
    tiktok_title="Plombier à Montpellier, c'est votre fiche Google qu'on passe ?",
    youtube_title="Plombier, pourquoi le client passe votre fiche Google sans appeler ?",
    textes={
        'tiktok': "« On prend le suivant. » Plombier à Montpellier, c'est votre fiche Google qu'on passe.\nUne seule photo, ancienne, et le doigt glisse vers la fiche Google d'à côté.\n\n#FicheGoogle #Plombier #Montpellier\n\n" + ABO,
        'instagram': "« On prend le suivant. » Plombier à Montpellier, c'est votre fiche Google qu'on passe.\n\nUne fuite sous l'évier, un samedi. Le client tape « plombier » sur Google Maps et fait défiler les fiches Google, ces encadrés avec la note, les photos et le bouton Appeler.\n\nSur la vôtre, une seule photo, prise il y a longtemps. Il hésite une seconde, et il passe. Sur celle d'à côté, des chantiers récents. Il appelle.\n\nCombien de photos de chantiers récents montre votre fiche Google ?\n\n30 jours offerts, lien en bio.\n\n#FicheGoogle #Plombier #Plomberie #Montpellier #ReferencementLocal",
        'youtube': "« On prend le suivant. » Plombier à Montpellier, c'est votre fiche Google qu'on passe.\n\nVotre fiche Google, c'est ce que vos clients voient en premier quand ils cherchent « plombier » sur Google Maps. Une seule photo ancienne, et le client fait défiler vers la suivante.\n\nProenligne publie une photo de vos chantiers le lundi, une publication le jeudi, et répond à chaque avis.\n\nQuelle est la date de la dernière photo de votre fiche Google ?\n\n#FicheGoogle #Plombier #Montpellier",
        'facebook': "« On prend le suivant. » Plombier à Montpellier, c'est votre fiche Google qu'on passe.\n\nEn urgence, le client ne lit pas tout. Il ouvre Google Maps, regarde les fiches Google des plombiers, avec la note, les photos et le bouton Appeler, et il décide vite.\n\nUne fiche Google avec une seule photo ancienne, il la passe. Une fiche Google avec des chantiers récents, il s'y arrête et il appelle.\n\nVotre dernière photo de chantier date de quand ?\n\nEssayez Proenligne gratuitement, 30 jours offerts.\n\n#FicheGoogle #Plombier #Plomberie #Montpellier #ReferencementLocal",
    })

add(S, '12:30', intention='utile', metier='electricien', angle='gain-de-temps', format='journee', ton='scene', symptome='avis-sans-reponse', ab='B',
    slug='electricien-soirees-saint-brieuc',
    accroche="Électricien à Saint-Brieuc, la journée de chantier finit, mais pas les réponses aux avis Google.",
    premier_commentaire="Une astuce. Répondez aux avis le matin, au café, plutôt que le soir. Deux minutes suffisent souvent pour un merci.",
    tiktok_title="Électricien à Saint-Brieuc, la journée finit, pas les avis Google",
    textes={
        'tiktok': "Électricien à Saint-Brieuc, la journée de chantier finit, mais pas les réponses aux avis Google.\nLe chantier est terminé, mais votre fiche Google, celle qu'on voit sur Google Maps, attend encore ses photos et ses réponses.\n\n#FicheGoogle #Electricien #SaintBrieuc\n\nAbonnez-vous pour d'autres astuces qui libèrent vos soirées. 30 jours offerts, lien en bio.",
    })

# ───────────────────────── DIMANCHE 22 ─────────────────────────
add(D, '13:00', intention='preuve', metier='garage', angle='preuve', format='avant-apres', ton='avant-apres', symptome='horaires-faux',
    slug='garage-avant-apres-horaires-samedi',
    accroche="Le samedi matin, la fiche Google du garage Bernard affichait fermé. Après correction, elle dit enfin vrai.",
    premier_commentaire="Pensez aussi aux horaires exceptionnels. Noël et le jour de l'An arrivent vite, et Google prévoit une rubrique pour les annoncer à l'avance.",
    visuel={'gabarit': 'avant-apres', 'surtitre': "Démonstration sur la fiche Google d'un garage", 'titre': 'Des horaires justes sur votre fiche Google',
            'mot': 'horaires justes',
            'carte': {'enseigne': 'Garage Bernard', 'metier': 'Garage', 'avant': 'Fermé le samedi matin', 'apres': 'Ouvert le samedi matin'},
            'cta': 'question', 'question': 'Vos horaires du samedi sont-ils justes sur Google ?',
            'slides': [
                {'type': 'point', 'numero': '1', 'titre': 'Avant, le client trouvait fermé', 'texte': "Le samedi matin, la fiche Google affichait fermé. Le client qui voulait passer allait voir ailleurs."},
                {'type': 'point', 'numero': '2', 'titre': 'Après, des horaires justes', 'texte': "Les horaires du samedi sont corrigés, et une photo de l'atelier ouvert le confirme."},
                {'type': 'point', 'numero': '3', 'titre': 'Le client passe sans hésiter', 'texte': "Il voit que le garage l'attend, avec des horaires à jour et une photo récente."},
                {'type': 'fin', 'titre': 'Et chez vous, le samedi ?', 'texte': "Avez-vous vérifié vos horaires sur votre fiche Google depuis la rentrée ?"}]},
    textes={
        'instagram': "Le samedi matin, la fiche Google du garage Bernard affichait fermé. Après correction, elle dit enfin vrai.\n\nLe garage est imaginaire, la situation l'est beaucoup moins. Sur Google Maps, chaque garage a sa fiche Google, avec la note, les photos et les horaires. C'est elle qu'on regarde avant de passer.\n\nAvant, l'atelier était ouvert le samedi matin, mais Google disait fermé. Le client qui voulait faire contrôler ses pneus allait ailleurs, sans rien dire.\n\nAprès, les horaires sont corrigés et une photo de l'atelier ouvert le confirme. Le client vient sans même appeler pour vérifier.\n\nQuand avez-vous vérifié vos horaires sur votre fiche Google pour la dernière fois ?\n\n#FicheGoogle #Garage #Garagiste #ReferencementLocal #GoogleBusinessProfile",
    })

add(D, '19:00', intention='utile', metier='coiffeur', angle='peur-de-perdre', format='fiche', ton='question', symptome='concurrent-plus-riche',
    slug='coiffeuse-duel-rennes',
    accroche="Coiffeuse à Rennes, sa fiche Google montre ses coupes, et vous ?",
    premier_commentaire="Une photo de coupe se prend en dix secondes, à la lumière du jour, avec l'accord de la cliente. De dos ou de profil, elle montre le travail sans montrer le visage.",
    tiktok_title="Coiffeuse à Rennes, sa fiche Google montre ses coupes, et vous ?",
    youtube_title="Coiffeuse, pourquoi la cliente choisit le salon d'à côté sur Google ?",
    textes={
        'tiktok': "Coiffeuse à Rennes, sa fiche Google montre ses coupes, et vous ?\nLe salon d'à côté publie ses coupes chaque semaine sur sa fiche Google. La cliente compare sur Google Maps, et elle réserve chez celle qui montre son travail.\n\n#FicheGoogle #Coiffeuse #Rennes\n\n" + ABO,
        'instagram': "Coiffeuse à Rennes, sa fiche Google montre ses coupes, et vous ?\n\nUne cliente vient d'emménager. Elle cherche « coiffeur » sur Google Maps et compare deux fiches Google, ces encadrés avec la note, les photos et les avis.\n\nLe salon d'à côté montre un balayage de la semaine, une coupe courte, un chignon de mariage. Le vôtre montre la devanture, et plus rien depuis l'été.\n\nLe talent est peut-être le même. Mais elle ne peut juger que ce qu'elle voit.\n\nQuelle coupe de la semaine aimeriez-vous montrer sur votre fiche Google ?\n\n30 jours offerts, lien en bio.\n\n#FicheGoogle #Coiffeuse #Coiffure #Rennes #ReferencementLocal",
        'youtube': "Coiffeuse à Rennes, pourquoi la cliente choisit-elle le salon d'à côté sur Google ?\n\nQuand on tape « coiffeur près de moi », Google affiche des fiches Google avec photos, avis et horaires. Votre fiche Google en fait partie. Une cliente qui compare deux salons regarde surtout les coupes récentes.\n\nProenligne publie une photo de vos coupes le lundi, une publication le jeudi, et répond à chaque avis.\n\nQuelle coupe de la semaine montreriez-vous en premier ?\n\n#FicheGoogle #Coiffeuse #Rennes",
        'facebook': "Coiffeuse à Rennes, sa fiche Google montre ses coupes, et vous ?\n\nAvant de réserver, une cliente compare souvent deux ou trois salons sur Google Maps. Chacun a sa fiche Google, avec la note, les photos et les avis. Elle s'arrête sur celle qui montre des coupes récentes.\n\nLe talent ne se voit pas sur une devanture. Il se voit sur les photos du travail de la semaine.\n\nQuelle est la dernière coupe que vous avez montrée sur votre fiche Google ?\n\nEssayez Proenligne gratuitement, 30 jours offerts.\n\n#FicheGoogle #Coiffeuse #Coiffure #Rennes #ReferencementLocal",
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
T('2026-11-16', '19:00', 'textes.tiktok', "Garagiste à Angers, l'atelier ferme, pas votre fiche Google.\nLes voitures sont rendues, mais il reste des avis à lire et des clients à remercier sur votre fiche Google, celle que les automobilistes voient sur Google Maps.\n\n#FicheGoogle #Garagiste #Angers\n\nAbonnez-vous pour d'autres astuces sur votre fiche Google. 30 jours offerts, lien en bio.")  # ea395e1
T('2026-11-17', '13:00', 'textes.linkedin', "En novembre, la fiche Google d'une entreprise de paysage montre souvent encore l'été.\nC'est pourtant souvent elle que le client regarde d'abord quand il cherche un paysagiste près de chez lui.\n\nLa fiche Google, c'est l'encadré que Google affiche avec le nom, la note, les photos et le numéro de l'entreprise.\n\nPrenons un exemple imaginaire, le paysagiste Durand.\nAvant, sa dernière photo datait de juillet. Rien n'indiquait que l'entreprise travaillait encore à l'automne.\nAprès, une photo de chantier paraît chaque lundi. Une haie taillée, un élagage, un massif préparé pour l'hiver.\n\nLa note n'a pas changé. Ce qui change, c'est l'impression laissée au client qui compare deux entreprises. Une fiche Google active montre une équipe au travail et une saison prise au sérieux.\n\nC'est ce que fait Proenligne pour les artisans, avec une photo le lundi, une publication le jeudi et une réponse à chaque avis.\n\nDans votre entreprise, qui s'occupe de la fiche Google pendant la saison creuse ?\n\n#FicheGoogle #GoogleBusinessProfile #ReferencementLocal #Paysagiste #TPE")  # e67d90e
T('2026-11-17', '13:00', 'visuel.carte.apres', 'Une photo de chantier chaque lundi')  # e17798d
T('2026-11-17', '19:00', 'textes.tiktok', "Serrurier à Tours, pourquoi on appelle l'autre sur Google ?\nBloqué dehors, le client compare deux fiches Google sur Google Maps. Celle de l'autre serrurier répond aux avis, la vôtre se tait.\n\n#FicheGoogle #Serrurier #Tours\n\nAbonnez-vous pour d'autres astuces sur votre fiche Google. 30 jours offerts, lien en bio.")  # e3449ba
T('2026-11-17', '19:00', 'textes.youtube', "Serrurier à Tours, pourquoi le client appelle-t-il l'autre sur Google ?\n\nLa fiche Google, c'est l'encadré qui présente chaque serrurier sur Google et Google Maps, avec sa note, ses avis et ses horaires. Avant d'appeler, le client y lit les avis, et les réponses que le serrurier leur a faites. À note égale, une fiche Google où chaque avis a une réponse inspire confiance.\n\nProenligne répond à chacun de vos avis, publie une photo le lundi et une publication le jeudi.\n\nEt sur votre fiche Google, combien d'avis attendent encore une réponse ?\n\n#FicheGoogle #Serrurier #Tours")  # e86ed79
T('2026-11-18', '13:00', 'textes.instagram', "« Ah, vous faites aussi les soins du visage ? » Votre fiche Google ne le disait pas.\n\nCette phrase, beaucoup d'esthéticiennes l'entendent de la bouche de clientes fidèles. Les nouvelles clientes, elles, ne la prononcent jamais. Elles ne savent pas que vous proposez ce soin, et le réservent souvent ailleurs.\n\nQuand on tape « soin du visage » et sa ville, Google affiche des fiches Google avec photos, avis et services. La vôtre en fait partie, mais elle ne montre que ce que vous y avez mis.\n\nPetit sondage du mercredi. Vos soins sont-ils visibles sur votre fiche Google ?\nA. Oui, tous, avec des photos.\nB. Quelques-uns, pas les nouveaux.\nC. Non, seulement le nom de l'institut.\n\nVous répondez A, B ou C ?\n\n#FicheGoogle #Estheticienne #InstitutDeBeaute #ReferencementLocal #GoogleBusinessProfile")  # e5ec07f
T('2026-11-18', '19:00', 'accroche', "Auto-école à Caen, pendant que vous êtes en leçon, un futur élève passe votre fiche Google sans s'arrêter.")  # e1abbee
T('2026-11-18', '19:00', 'premier_commentaire', "Pour commencer, deux photos suffisent. Prenez la voiture école devant l'agence, puis le moniteur avec un élève qui vient d'avoir son permis, si l'élève est d'accord.")  # e442f8c
T('2026-11-18', '19:00', 'tiktok_title', 'Auto-école à Caen, pendant votre leçon, un futur élève passe votre fiche Google')  # e0c7db5
T('2026-11-18', '19:00', 'textes.tiktok', "Auto-école à Caen, pendant que vous êtes en leçon, un futur élève passe votre fiche Google sans s'arrêter.\nSur Google Maps, il fait défiler les fiches Google des auto-écoles. Si la vôtre n'a ni photo des voitures ni nouvelles récentes, il passe à la suivante.\n\n#FicheGoogle #AutoEcole #Caen\n\nAbonnez-vous pour d'autres astuces sur votre fiche Google. 30 jours offerts, lien en bio.")  # e591234
T('2026-11-18', '19:00', 'textes.instagram', "Auto-école à Caen, pendant que vous êtes en leçon, un futur élève passe votre fiche Google sans s'arrêter.\n\nUn lycéen et sa mère cherchent une auto-école. Ils tapent « auto-école » sur Google Maps. Chaque école a sa fiche Google, avec la note, les photos et le bouton Appeler.\n\nIls font défiler. Une fiche Google sans photo des voitures ni nouvelles récentes, ils la passent sans s'arrêter. Une autre montre la voiture école, l'équipe, une réussite au permis. C'est là qu'ils appellent.\n\nPendant ce temps, vous êtes en leçon, et vous ne le saurez jamais.\n\nQue montre la première photo de votre fiche Google aujourd'hui ?\n\n30 jours offerts, lien en bio.\n\n#FicheGoogle #AutoEcole #PermisDeConduire #Caen #ReferencementLocal")  # ec921f0
T('2026-11-18', '19:00', 'textes.facebook', "Auto-école à Caen, pendant que vous êtes en leçon, un futur élève passe votre fiche Google sans s'arrêter.\n\nAvant de s'inscrire, une famille compare souvent plusieurs auto-écoles sur Google Maps. Chacune a sa fiche Google, cet encadré avec la note, les photos, les horaires et le bouton Appeler.\n\nUne fiche Google sans photo de la voiture école ni nouvelles récentes, on la fait défiler. Celle qui montre l'équipe et les élèves reçus donne envie d'appeler.\n\nEt vous, que voit une famille en ouvrant votre fiche Google ?\n\nEssayez Proenligne gratuitement, 30 jours offerts.\n\n#FicheGoogle #AutoEcole #PermisDeConduire #Caen #ReferencementLocal")  # e0f92ca
T('2026-11-19', '13:00', 'visuel.slides.1.texte', 'Photographiez les fondations, le mur en montage, puis le travail fini. Avec ces trois photos, votre fiche Google raconte tout le chantier.')  # e916c4b
T('2026-11-19', '19:00', 'premier_commentaire', 'Une publication sur votre fiche Google peut rester très simple. Une photo du tableau électrique refait et deux phrases sur le chantier suffisent.')  # eb31dd0
T('2026-11-19', '19:00', 'textes.tiktok', "Électricien à Saint-Brieuc, encore devant votre fiche Google à 23 h, après une longue journée de chantier ?\nIl est 23 h, et il reste des photos à publier et des avis auxquels répondre sur votre fiche Google, celle que vos clients voient sur Google Maps.\n\n#FicheGoogle #Electricien #SaintBrieuc\n\nAbonnez-vous pour d'autres astuces sur votre fiche Google. 30 jours offerts, lien en bio.")  # eda9592
T('2026-11-19', '19:00', 'textes.instagram', "Électricien à Saint-Brieuc, encore devant votre fiche Google à 23 h, après une longue journée de chantier ?\n\nIl est 23 h. La camionnette est garée, la journée de chantier est finie. Sur le canapé, il reste votre fiche Google, l'encadré qu'on découvre sur Google Maps en cherchant un électricien.\n\nIl faut publier la photo du tableau refait cet après-midi et remercier deux clients pour leur avis. Et ça recommence un peu chaque soir.\n\nProenligne publie une photo le lundi, une publication le jeudi, et répond à chaque avis à votre place. Le soir, vous débranchez, vous aussi.\n\nÀ quelle heure vous occupez-vous de votre fiche Google, en général ?\n\n30 jours offerts, lien en bio.\n\n#FicheGoogle #Electricien #Electricite #SaintBrieuc #ReferencementLocal")  # e60f39b
T('2026-11-19', '19:00', 'textes.youtube', "Électricien à Saint-Brieuc, encore devant votre fiche Google le soir ?\n\nLa fiche Google, c'est l'encadré qui présente votre entreprise sur Google et Google Maps, avec vos photos, vos avis et votre numéro. La tenir à jour finit souvent tard, après les chantiers.\n\nProenligne publie une photo le lundi, une publication le jeudi, et répond à chaque avis à votre place.\n\nEt vous, quand mettez-vous votre fiche Google à jour ?\n\n#FicheGoogle #Electricien #SaintBrieuc")  # eca625a
T('2026-11-19', '19:00', 'textes.facebook', "Électricien à Saint-Brieuc, encore devant votre fiche Google à 23 h, après une longue journée de chantier ?\n\nLa journée de chantier se termine, et une autre commence sur le téléphone. Il reste des photos à publier et des avis auxquels répondre. Tout cela s'affiche sur votre fiche Google, l'encadré que les clients consultent sur Google Maps avant d'appeler un électricien.\n\nProenligne s'en occupe à votre place, avec une photo le lundi, une publication le jeudi et une réponse à chaque avis.\n\nLe soir, vous rangez le téléphone à quelle heure ?\n\nEssayez Proenligne gratuitement, 30 jours offerts.\n\n#FicheGoogle #Electricien #Electricite #SaintBrieuc #ReferencementLocal")  # ec5ed29
T('2026-11-21', '12:30', 'tiktok_title', 'Électricien à Saint-Brieuc, la journée finit, mais pas les réponses aux avis Google')  # e658d81
T('2026-11-21', '12:30', 'textes.tiktok', "Électricien à Saint-Brieuc, la journée de chantier finit, mais pas les réponses aux avis Google.\nLe chantier est terminé, mais votre fiche Google, celle qu'on voit sur Google Maps, attend encore ses photos et ses réponses.\n\n#FicheGoogle #Electricien #SaintBrieuc\n\nAbonnez-vous pour d'autres astuces sur votre fiche Google. 30 jours offerts, lien en bio.")  # e3eba9f
T('2026-11-21', '13:00', 'visuel.points.2', 'Répondre à chaque avis, avec votre accord pour les avis négatifs')  # effbfd8
T('2026-11-21', '13:00', 'visuel.slides.1.texte', 'Chaque jeudi, une actualité courte sur votre métier, votre saison ou vos services est publiée sur votre fiche Google.')  # e09a28b
T('2026-11-21', '19:00', 'textes.tiktok', "« On prend le suivant. » Plombier à Montpellier, c'est votre fiche Google qu'on passe.\nSur Google Maps, chaque plombier a sa fiche Google, avec ses photos, ses avis et le bouton Appeler. Une seule photo, ancienne, et le doigt glisse vers la fiche Google d'à côté.\n\n#FicheGoogle #Plombier #Montpellier\n\nAbonnez-vous pour d'autres astuces sur votre fiche Google. 30 jours offerts, lien en bio.")  # e0af997
T('2026-11-22', '13:00', 'visuel.slides.0.titre', 'Avant, la fiche Google affichait fermé le samedi')  # e2fed80
T('2026-11-22', '19:00', 'premier_commentaire', "Une photo de coupe se prend en quelques secondes, à la lumière du jour, avec l'accord de la cliente. Prise de dos, elle montre le travail sans montrer le visage.")  # e9bda3a

# ───────── Corrections après la relecture, passe 2 ─────────
T('2026-11-18', '13:00', 'textes.instagram', "« Ah, vous faites aussi les soins du visage ? » Votre fiche Google ne le disait pas.\n\nCette phrase, beaucoup d'esthéticiennes l'entendent de la bouche de clientes fidèles. Les nouvelles clientes, elles, ne la prononcent jamais. Elles ne savent pas que vous proposez ce soin, et le réservent souvent ailleurs.\n\nQuand on tape « soin du visage » et sa ville, Google affiche des fiches Google avec photos, avis et services. La vôtre en fait partie. Mais un soin que vous n'y avez pas ajouté, la cliente a peu de chances de le voir.\n\nPetit sondage du mercredi. Vos soins sont-ils visibles sur votre fiche Google ?\nA. Oui, tous, avec des photos.\nB. Quelques-uns, pas les nouveaux.\nC. Non, seulement le nom de l'institut.\n\nVous répondez A, B ou C ?\n\n#FicheGoogle #Estheticienne #InstitutDeBeaute #ReferencementLocal #GoogleBusinessProfile")  # e5ec07f
T('2026-11-18', '19:00', 'premier_commentaire', "Pour commencer, deux photos suffisent. Prenez la voiture-école devant l'agence, puis le moniteur avec un élève qui vient d'avoir son permis, si l'élève est d'accord.")  # e442f8c
T('2026-11-18', '19:00', 'textes.instagram', "Auto-école à Caen, pendant que vous êtes en leçon, un futur élève passe votre fiche Google sans s'arrêter.\n\nUn lycéen et sa mère cherchent une auto-école. Ils tapent « auto-école » sur Google Maps. Chaque école a sa fiche Google, avec la note, les photos et le bouton Appeler.\n\nIls font défiler. Une fiche Google sans photo des voitures ni nouvelles récentes, ils la passent sans s'arrêter. Une autre montre la voiture-école, l'équipe, une réussite au permis. C'est là qu'ils appellent.\n\nPendant ce temps, vous êtes en leçon, et vous ne le saurez jamais.\n\nQue montre la première photo de votre fiche Google aujourd'hui ?\n\n30 jours offerts, lien en bio.\n\n#FicheGoogle #AutoEcole #PermisDeConduire #Caen #ReferencementLocal")  # ec921f0
T('2026-11-18', '19:00', 'textes.facebook', "Auto-école à Caen, pendant que vous êtes en leçon, un futur élève passe votre fiche Google sans s'arrêter.\n\nAvant de s'inscrire, une famille compare souvent plusieurs auto-écoles sur Google Maps. Chacune a sa fiche Google, cet encadré avec la note, les photos, les horaires et le bouton Appeler.\n\nUne fiche Google sans photo de la voiture-école ni nouvelles récentes, on la fait défiler. Celle qui montre l'équipe et les élèves reçus donne envie d'appeler.\n\nEt vous, que voit une famille en ouvrant votre fiche Google ?\n\nEssayez Proenligne gratuitement, 30 jours offerts.\n\n#FicheGoogle #AutoEcole #PermisDeConduire #Caen #ReferencementLocal")  # e0f92ca
T('2026-11-21', '13:00', 'visuel.slides.1.texte', 'Chaque jeudi, une nouvelle publication paraît sur votre fiche Google.')  # e09a28b
T('2026-11-22', '19:00', 'accroche', "Coiffeuse à Rennes, le salon d'à côté montre ses coupes sur sa fiche Google. Et vous ?")  # ea224ed
T('2026-11-22', '19:00', 'tiktok_title', "Coiffeuse à Rennes, le salon d'à côté montre ses coupes sur sa fiche Google. Et vous ?")  # e6dc8c3
T('2026-11-22', '19:00', 'textes.tiktok', "Coiffeuse à Rennes, le salon d'à côté montre ses coupes sur sa fiche Google. Et vous ?\nIl publie ses coupes chaque semaine sur sa fiche Google. La cliente compare sur Google Maps, et elle réserve chez celle qui montre son travail.\n\n#FicheGoogle #Coiffeuse #Rennes\n\nAbonnez-vous pour d'autres astuces sur votre fiche Google. 30 jours offerts, lien en bio.")  # ea7a83c
T('2026-11-22', '19:00', 'textes.instagram', "Coiffeuse à Rennes, le salon d'à côté montre ses coupes sur sa fiche Google. Et vous ?\n\nUne cliente vient d'emménager. Elle cherche « coiffeur » sur Google Maps et compare deux fiches Google, ces encadrés avec la note, les photos et les avis.\n\nSur la fiche Google de l'autre salon, il y a un balayage de la semaine, une coupe courte, un chignon de mariage. Sur la vôtre, il y a la devanture, et plus rien depuis l'été.\n\nLe talent est peut-être le même. Mais elle ne peut juger que ce qu'elle voit.\n\nQuelle coupe de la semaine aimeriez-vous montrer sur votre fiche Google ?\n\n30 jours offerts, lien en bio.\n\n#FicheGoogle #Coiffeuse #Coiffure #Rennes #ReferencementLocal")  # e4e2999
T('2026-11-22', '19:00', 'textes.facebook', "Coiffeuse à Rennes, le salon d'à côté montre ses coupes sur sa fiche Google. Et vous ?\n\nAvant de réserver, une cliente compare souvent deux ou trois salons sur Google Maps. Chacun a sa fiche Google, avec la note, les photos et les avis. Elle s'arrête sur celle qui montre des coupes récentes.\n\nLe talent ne se voit pas sur une devanture. Il se voit sur les photos du travail de la semaine.\n\nQuelle est la dernière coupe que vous avez montrée sur votre fiche Google ?\n\nEssayez Proenligne gratuitement, 30 jours offerts.\n\n#FicheGoogle #Coiffeuse #Coiffure #Rennes #ReferencementLocal")  # ef0ced2

# ───────── Corrections après la relecture, passe 3 ─────────
T('2026-11-18', '19:00', 'premier_commentaire', "Pour démarrer votre fiche Google, deux photos suffisent. Photographiez la voiture-école devant l'agence, puis le moniteur avec un élève qui vient d'avoir son permis, si l'élève est d'accord.")  # e442f8c
T('2026-11-22', '19:00', 'textes.tiktok', "Coiffeuse à Rennes, le salon d'à côté montre ses coupes sur sa fiche Google. Et vous ?\nSur Google Maps, chaque salon a sa fiche Google, avec la note, les photos et les avis. Une cliente qui compare s'arrête souvent sur le salon qui montre son travail de la semaine.\n\n#FicheGoogle #Coiffeuse #Rennes\n\nAbonnez-vous pour d'autres astuces sur votre fiche Google. 30 jours offerts, lien en bio.")  # ea7a83c

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
