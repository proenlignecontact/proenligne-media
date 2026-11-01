# Générateur du plan de la semaine du 2026-11-02 (écrit par la tâche hebdomadaire ; source des textes)
import json, subprocess, os
ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))
grille = json.loads(subprocess.check_output(['python3', os.path.join(RACINE, 'outils/heure_utc.py'), '2026-11-02', '--varier']))
H = {(g['date'], g['creneau_nominal']): g for g in grille}
TYPE = {'06:30': 'texte', '13:00': 'visuel', '19:00': 'video'}
HT = '#FicheGoogle #GoogleBusinessProfile #ReferencementLocal'

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


# ───────────────────────── LUNDI 2 ─────────────────────────
add('2026-11-02', '06:30', intention='utile', metier='plombier', angle='peur-de-perdre', format='test', ton='question', symptome=None,
    slug='plombier-test-yeux-du-client',
    accroche="Avez-vous déjà regardé votre fiche Google avec les yeux d'un client qui a une fuite ?",
    premier_commentaire="Faites le test et dites-nous ce que vous avez remarqué en premier sur votre fiche Google. La photo, la note ou les horaires ?",
    visuel={'gabarit': 'question', 'surtitre': 'Le test du lundi sur Google', 'titre': "Que voit d'abord un client sur votre fiche Google ?",
            'mot': 'fiche Google', 'reponses': ['Une photo de mon travail', 'Des horaires à jour', 'Un avis avec ma réponse'],
            'cta': 'question', 'question': "Faites le test sur Google Maps. Qu'avez-vous remarqué en premier ?"},
    textes={
        'x': "Avez-vous déjà regardé votre fiche Google avec les yeux d'un client qui a une fuite ?\n\nTapez « plombier » et votre ville sur Google Maps. Votre fiche Google, c'est l'encadré avec votre nom, vos photos et vos avis.\n\nQu'avez-vous remarqué en premier ?\n\n#FicheGoogle #Plombier",
        'facebook': "Avez-vous déjà regardé votre fiche Google avec les yeux d'un client qui a une fuite ?\n\nLe test prend 30 secondes. Sur votre téléphone, ouvrez Google Maps en navigation privée et tapez « plombier » suivi du nom de votre ville.\n\nLes encadrés qui s'affichent, avec une note, des photos et un bouton Appeler, ce sont des fiches Google. La vôtre est dedans, quelque part.\n\nRegardez-la comme quelqu'un qui a de l'eau sous l'évier et pas le temps de comparer longtemps.\nLa dernière photo montre-t-elle votre travail ?\nLes horaires sont-ils justes ?\nLe dernier avis a-t-il une réponse ?\n\nQu'avez-vous remarqué en premier ? Dites-le en commentaire.\n\n#FicheGoogle #Plombier #ReferencementLocal #GoogleBusinessProfile",
    })

add('2026-11-02', '13:00', intention='utile', metier='coiffeur', angle='gain-de-temps', format='conseil', ton='constat', symptome='photos-anciennes',
    slug='coiffeur-coupes-dans-le-telephone',
    accroche="Vos plus belles coupes dorment dans votre téléphone au lieu d'être sur votre fiche Google.",
    premier_commentaire="Un petit test pour ce soir. Ouvrez votre fiche Google et regardez la date de la dernière photo. Elle remonte à quand ?",
    visuel={'gabarit': 'conseil', 'surtitre': 'Coiffeurs, votre fiche Google', 'titre': '3 réflexes pour montrer vos coupes', 'mot': '3 réflexes',
            'points': ["Photographiez la coupe près de la vitrine, à la lumière du jour",
                       "Demandez l'accord de la cliente avant la photo",
                       "Publiez-la sur votre fiche Google le soir même"],
            'cta': 'question', 'question': "Chez vous, qui prend les photos des coupes ?",
            'slides': [
                {'type': 'point', 'numero': '1', 'titre': 'La lumière du jour', 'texte': "Près de la vitrine et sans flash, la couleur reste fidèle et la coupe se voit tout de suite."},
                {'type': 'point', 'numero': '2', 'titre': "L'accord de la cliente", 'texte': "Une question suffit. « Je peux la prendre en photo ? » Beaucoup de clientes sont flattées."},
                {'type': 'point', 'numero': '3', 'titre': 'Le soir même', 'texte': "Une photo publiée le soir sur votre fiche Google montre que le salon vit cette semaine."},
                {'type': 'fin', 'titre': 'À vous de nous dire', 'texte': "Au salon, qui prend les photos des coupes, vous ou quelqu'un de l'équipe ?"}]},
    textes={
        'instagram': "Vos plus belles coupes dorment dans votre téléphone au lieu d'être sur votre fiche Google.\n\nQuand quelqu'un tape « coiffeur près de moi », Google affiche des fiches avec des photos, des avis et des horaires. La vôtre en fait partie, et ce sont les photos qu'on regarde d'abord.\n\nVoici 3 réflexes qui prennent deux minutes.\n1. Photographiez la coupe près de la vitrine, à la lumière du jour, sans flash.\n2. Demandez l'accord de la cliente. Beaucoup sont flattées qu'on leur pose la question.\n3. Publiez la photo sur votre fiche Google le soir même, pendant que vous y pensez.\n\nAu salon, qui prend les photos des coupes, vous ou quelqu'un de l'équipe ?\n\n#FicheGoogle #Coiffeur #Coiffure #ReferencementLocal #GoogleBusinessProfile",
        'facebook': "Vos plus belles coupes dorment dans votre téléphone au lieu d'être sur votre fiche Google.\n\nVotre fiche Google, c'est ce que voit une future cliente quand elle cherche « coiffeur » sur Google Maps. Avant de réserver, elle fait défiler les photos.\n\nTrois réflexes suffisent pour que vos coupes y arrivent.\n1. Photographiez la coupe près de la vitrine, à la lumière du jour, sans flash.\n2. Demandez l'accord de la cliente. Une simple question, et beaucoup sont flattées.\n3. Publiez la photo sur votre fiche Google le soir même, avant qu'elle se perde dans la galerie.\n\nEt chez vous, qui s'occupe des photos au salon ?\n\n#FicheGoogle #Coiffeur #Coiffure #ReferencementLocal",
        'linkedin': "Dans un salon de coiffure, les plus belles réalisations finissent souvent dans le téléphone du coiffeur, rarement sur la fiche Google du salon.\n\nLa fiche Google, c'est ce qu'une future cliente voit quand elle cherche « coiffeur » sur Google ou Google Maps. Avant de réserver, elle regarde les photos, la note et les horaires.\n\nLe constat revient dans beaucoup de salons. Les photos existent, mais personne n'a le réflexe de les publier. La fiche Google montre alors des coupes anciennes, ou aucune coupe.\n\nTrois habitudes changent la donne sans prendre de temps.\nPhotographier à la lumière du jour, près de la vitrine.\nDemander l'accord de la cliente, ce qui crée souvent un bon moment d'échange.\nPublier le soir même, plutôt que de garder les photos pour plus tard.\n\nProenligne publie une photo chaque lundi sur la fiche Google des salons qui lui confient la tâche, mais le réflexe de photographier reste celui de l'équipe.\n\nDans votre salon, qui est chargé des photos ?\n\n#FicheGoogle #GoogleBusinessProfile #ReferencementLocal #Coiffure",
    })

add('2026-11-02', '19:00', intention='utile', metier='paysagiste', angle='peur-de-perdre', format='fiche', ton='scene', symptome='aucune-publication',
    slug='paysagiste-fiche-endormie-hiver',
    accroche="Il est 20 h. Une cliente cherche un paysagiste et ouvre votre fiche Google.",
    premier_commentaire="Paysagistes, que publiez-vous sur votre fiche Google entre novembre et mars ? Des chantiers d'hiver, ou rien du tout ?",
    tiktok_title="Votre fiche Google dort-elle tout l'hiver ?",
    youtube_title="Paysagiste, votre fiche Google dort-elle pendant l'hiver ?",
    textes={
        'tiktok': "Il est 20 h. Une cliente cherche un paysagiste pour ses haies et ouvre votre fiche Google.\nRien n'est publié depuis le printemps. Elle se demande si vous travaillez encore l'hiver.\n\n#FicheGoogle #Paysagiste #Jardin",
        'instagram': "Il est 20 h. Une cliente cherche un paysagiste pour ses haies et ouvre votre fiche Google.\n\nVotre fiche Google, c'est ce qui s'affiche quand quelqu'un tape « paysagiste » sur Google Maps, avec vos photos, vos avis et vos publications.\n\nCe soir-là, elle voit une pelouse en plein été et rien de publié depuis le printemps. Elle se demande si vous travaillez encore l'hiver, et elle continue de chercher.\n\nL'hiver, il y a pourtant de quoi montrer. Une taille de haie, un ramassage de feuilles, une plantation d'arbres.\n\nQue publiez-vous sur votre fiche Google pendant l'hiver ?\n\n#FicheGoogle #Paysagiste #Jardin #ReferencementLocal #GoogleBusinessProfile",
        'youtube': "Il est 20 h. Une cliente cherche un paysagiste et ouvre sa fiche Google. Rien n'y est publié depuis le printemps.\n\nLa fiche Google, c'est la carte de visite que Google montre à votre place, avec vos photos, vos avis et vos publications. En hiver, quand elle ne bouge plus, on peut croire que l'entreprise est en pause.\n\nProenligne publie une photo le lundi et un article le jeudi, et répond à chaque avis, même l'hiver.\n\nEt vous, que montrez-vous sur votre fiche Google en novembre ?\n\n#FicheGoogle #Paysagiste #Jardin",
        'facebook': "Il est 20 h. Une cliente cherche un paysagiste et ouvre votre fiche Google.\n\nElle veut faire tailler ses haies avant l'hiver. Sur votre fiche Google, l'encadré que Google lui montre avec vos photos et vos avis, la dernière publication date du printemps.\n\nElle se pose une question simple. Est-ce qu'il travaille encore en novembre ?\n\nUne taille de haie ou un ramassage de feuilles en photo suffit souvent à lui répondre.\n\nQue publiez-vous sur votre fiche Google pendant l'hiver ?\n\n#FicheGoogle #Paysagiste #Jardin #ReferencementLocal",
    })

# ───────────────────────── MARDI 3 ─────────────────────────
add('2026-11-03', '06:30', intention='utile', metier='electricien', angle='peur-de-perdre', format='constat', ton='pendant-que', symptome='horaires-faux',
    slug='electricien-horaires-de-vacances',
    accroche="Pendant que vous êtes sur un chantier, votre fiche Google affiche peut-être encore vos horaires de vacances.",
    premier_commentaire="Une astuce. Google permet d'enregistrer à l'avance des horaires exceptionnels pour les jours fériés. Vous l'avez déjà fait pour Noël ?",
    visuel={'gabarit': 'conseil', 'surtitre': 'Électriciens, votre fiche Google', 'titre': 'Retirez vos horaires de vacances', 'mot': 'horaires de vacances',
            'points': ["Ouvrez votre fiche Google depuis votre téléphone",
                       "Vérifiez la ligne des horaires, jour par jour",
                       "Ajoutez dès maintenant les jours fériés de fin d'année"],
            'cta': 'question', 'question': "Vos horaires affichés sont-ils justes aujourd'hui ?"},
    textes={
        'x': "Pendant que vous êtes sur un chantier, votre fiche Google affiche peut-être encore vos horaires de vacances.\n\nUn client en panne lit « Fermé » et appelle un autre électricien.\n\nVous les avez vérifiés après la Toussaint ?\n\n#FicheGoogle #Electricien",
        'facebook': "Pendant que vous êtes sur un chantier, votre fiche Google affiche peut-être encore vos horaires de vacances.\n\nVotre fiche Google, c'est ce que Google montre quand quelqu'un cherche « électricien » près de chez lui, avec votre note, vos photos, vos horaires et votre numéro.\n\nUn client en panne regarde d'abord si vous êtes ouvert. S'il lit « Fermé », il ne prend pas le risque d'appeler. Il passe à l'électricien suivant.\n\nLes horaires de vacances sont pratiques, à condition de penser à les retirer. Après la Toussaint, c'est le bon moment.\nOuvrez votre fiche Google depuis votre téléphone.\nVérifiez la ligne des horaires, jour par jour.\nAjoutez dès maintenant les jours fériés de fin d'année.\n\nVos horaires affichés sont-ils justes aujourd'hui ?\n\n#FicheGoogle #Electricien #ReferencementLocal #GoogleBusinessProfile",
    })

add('2026-11-03', '13:00', intention='preuve', metier='boulangerie', angle='peur-de-perdre', format='avant-apres', ton='avant-apres', symptome='photos-anciennes',
    slug='boulangerie-deux-visages',
    accroche="La même boulangerie peut avoir deux visages sur sa fiche Google. Lequel donne faim ?",
    premier_commentaire="Boulangers, quelle photo fait le plus réagir vos clients sur votre fiche Google ? Le pain, les gâteaux ou l'équipe ?",
    visuel={'gabarit': 'avant-apres', 'surtitre': 'La même fiche Google, deux visages', 'titre': 'Laquelle des deux vous donne faim ?', 'mot': 'donne faim',
            'carte': {'enseigne': 'Boulangerie Durand', 'metier': 'Boulangerie', 'avant': 'Une vitrine vide, un soir', 'apres': 'La fournée du matin, lundi'},
            'cta': 'question', 'question': "Laquelle vous ferait entrer, la photo du soir ou celle du matin ?",
            'slides': [
                {'type': 'point', 'numero': '1', 'titre': 'Avant', 'texte': "La seule photo montre une vitrine vide, prise un soir après la fermeture. Rien ne dit ce qu'on y trouve."},
                {'type': 'point', 'numero': '2', 'titre': 'Après', 'texte': "Chaque lundi, une photo de la fournée du matin. On voit les baguettes, les viennoiseries et l'équipe."},
                {'type': 'fin', 'titre': 'Et votre boutique ?', 'texte': "Quelle photo de votre boutique montreriez-vous en premier sur votre fiche Google ?"}]},
    textes={
        'instagram': "La même boulangerie peut avoir deux visages sur sa fiche Google. Lequel donne faim ?\n\nPrenons une boulangerie imaginaire, la boulangerie Durand.\n\nAvant, sa fiche Google n'avait qu'une photo, une vitrine vide prise un soir après la fermeture.\n\nAprès, une photo de la fournée du matin arrive chaque lundi. On voit les baguettes, les viennoiseries et l'équipe derrière le comptoir.\n\nLe pain est le même et la note aussi. Mais quand on cherche « boulangerie » sur Google Maps, ce sont les photos qu'on voit avant de choisir où s'arrêter.\n\nVous, vous entreriez dans laquelle ?\n\n#FicheGoogle #Boulangerie #Boulanger #ReferencementLocal #GoogleBusinessProfile",
        'facebook': "La même boulangerie peut avoir deux visages sur sa fiche Google. Lequel donne faim ?\n\nCherchez « boulangerie » dans votre ville. Les encadrés avec une note et des photos sont des fiches Google. C'est souvent là que se joue le choix du croissant du dimanche.\n\nVoici une boulangerie imaginaire, la boulangerie Durand, en deux versions.\nAvant, une seule photo, une vitrine vide prise un soir après la fermeture.\nAprès, une photo de la fournée du matin publiée chaque lundi, avec les baguettes, les viennoiseries et l'équipe.\n\nMême pain, même note. Seule la vitrine sur Google a changé.\n\nLaquelle vous donnerait envie d'entrer ?\n\n#FicheGoogle #Boulangerie #Boulanger #ReferencementLocal",
        'linkedin': "Deux versions de la même fiche Google de boulangerie, et une seule donne vraiment envie d'entrer.\nLa fiche Google, c'est l'encadré que Google affiche quand un client cherche « boulangerie » près de chez lui.\n\nPrenons une boulangerie imaginaire.\n\nDans la première version, sa fiche Google ne montre qu'une photo, une vitrine vide prise un soir après la fermeture. Rien n'indique ce qu'on y trouve ni qui sert au comptoir.\n\nDans la seconde, une photo de la fournée du matin est publiée chaque lundi. On voit le pain, les viennoiseries, l'équipe.\n\nLe produit est identique, la note aussi. Ce qui change, c'est ce que le client voit avant de pousser la porte.\n\nC'est ce travail régulier que Proenligne prend en charge pour les commerçants, une photo le lundi et un article le jeudi.\n\nQuelle image de votre commerce aimeriez-vous que vos clients voient en premier ?\n\n#FicheGoogle #GoogleBusinessProfile #ReferencementLocal #Boulangerie #Commerce",
    })

add('2026-11-03', '19:00', intention='utile', metier='garage', angle='gain-de-temps', format='avis', ton='replique', symptome='avis-sans-reponse',
    slug='garage-avis-sans-reponse-soir', ab='A',
    accroche="« Ce garage ne répond jamais ? » se demande un client devant votre fiche Google.",
    premier_commentaire="Garagistes, combien d'avis attendent une réponse sur votre fiche Google en ce moment ? Aucun, quelques-uns, ou vous n'osez pas regarder ?",
    tiktok_title="Vos avis sur votre fiche Google attendent-ils une réponse ?",
    youtube_title="Garage, ces avis sans réponse sur votre fiche Google font douter",
    textes={
        'tiktok': "« Ce garage ne répond jamais ? » C'est ce que se demande un client devant votre fiche Google quand les avis restent sans réponse.\n\n#FicheGoogle #Garage #Garagiste #Mecanique",
        'instagram': "« Ce garage ne répond jamais ? » se demande un client devant votre fiche Google.\n\nSur Google Maps, chaque garage a sa fiche Google, avec la note, les avis et le bouton Appeler. Les avis, tout le monde les lit. Les réponses aussi.\n\nTrois bons avis sans un mot en dessous, et le nouveau client se demande si quelqu'un lit ce qu'écrivent les clients.\n\nRépondre prend une phrase. « Merci Karim, ravi d'avoir pu vous dépanner samedi. »\n\nCombien d'avis attendent une réponse sur votre fiche Google ?\n\n#FicheGoogle #Garage #Garagiste #ReferencementLocal #GoogleBusinessProfile",
        'youtube': "« Ce garage ne répond jamais ? » C'est la question d'un client devant une fiche Google pleine de bons avis restés sans réponse.\n\nVotre fiche Google, c'est ce que vos clients voient en premier quand ils cherchent « garage » sur Google Maps. Les réponses aux avis montrent qu'une vraie personne écoute.\n\nProenligne répond à chaque avis, publie une photo le lundi et un article le jeudi.\n\nVous répondez à vos avis, vous ?\n\n#FicheGoogle #Garage #Garagiste",
        'facebook': "« Ce garage ne répond jamais ? » se demande un client devant votre fiche Google.\n\nIl cherche un garage pour sa révision. Sur votre fiche Google, il lit trois bons avis. Aucun n'a de réponse.\n\nCe n'est pas grave en soi, mais ça laisse un doute. Est-ce que quelqu'un lit vraiment ce qu'écrivent les clients ?\n\nUne phrase suffit sous chaque avis. Un merci, un prénom, un détail.\n\nVous répondez à vos avis le jour même, ou plutôt quand vous avez un moment ?\n\n#FicheGoogle #Garage #Garagiste #ReferencementLocal",
    })

# ───────────────────────── MERCREDI 4 ─────────────────────────
add('2026-11-04', '06:30', intention='utile', metier='serrurier', angle='peur-de-perdre', format='idee-recue', ton='contre-intuitif', symptome=None,
    slug='serrurier-urgence-et-mefiance',
    accroche="On pense qu'en urgence, personne ne regarde votre fiche Google. C'est souvent l'inverse.",
    premier_commentaire="Serruriers, quelle question vos clients vous posent-ils le plus souvent au téléphone avant de vous faire venir ?",
    visuel={'gabarit': 'conseil', 'surtitre': 'Serruriers, une idée reçue', 'titre': 'En urgence, le client vérifie souvent votre fiche Google', 'mot': 'vérifie souvent',
            'points': ["Montrez votre nom et votre camionnette en photo",
                       "Demandez un avis après chaque dépannage",
                       "Répondez poliment à chaque avis"],
            'cta': 'question', 'question': "Et vous, que regardez-vous avant d'appeler un artisan ?"},
    textes={
        'x': "On pense qu'en urgence, personne ne regarde votre fiche Google. C'est souvent l'inverse.\n\nBloqué dehors, le client a peur de tomber sur un serrurier malhonnête. Il lit 2 ou 3 avis avant d'appeler.\n\nVous, que regardez-vous en premier ?\n\n#FicheGoogle #Serrurier",
        'facebook': "On pense qu'en urgence, personne ne regarde votre fiche Google. C'est souvent l'inverse.\n\nImaginez quelqu'un bloqué devant sa porte un dimanche soir. Il a entendu des histoires de dépannages qui tournent mal. Alors avant d'appeler, il ouvre Google Maps et regarde les fiches Google des serruriers du coin, avec leur note, leurs avis et leurs photos.\n\nIl cherche des signes rassurants. Un nom et une camionnette en photo, des avis récents, des réponses polies.\n\nL'urgence ne fait pas disparaître la méfiance. Elle la rend plus forte.\n\nSi vous étiez bloqué dehors, qu'est-ce qui vous ferait appeler un serrurier plutôt qu'un autre ?\n\n#FicheGoogle #Serrurier #ReferencementLocal #GoogleBusinessProfile",
    })

add('2026-11-04', '13:00', intention='utile', metier='estheticienne', angle='gain-de-temps', format='question', ton='question', symptome='note-sans-contexte',
    slug='estheticienne-sondage-reservation',
    accroche="Deux instituts ont la même note sur leur fiche Google. Qu'est-ce qui fait choisir l'un plutôt que l'autre ?",
    premier_commentaire="Votez avec une seule lettre, A, B ou C. Et si vous avez une autre idée, dites-la aussi.",
    visuel={'gabarit': 'question', 'surtitre': 'Un sondage sur la fiche Google', 'titre': "Qu'est-ce qui fait réserver une cliente ?", 'mot': 'réserver',
            'reponses': ['A. Des photos récentes des soins', 'B. Des réponses aux avis', 'C. Des horaires faciles à lire'],
            'cta': 'question', 'question': "Et vous, A, B ou C ? Répondez en commentaire.",
            'slides': [
                {'type': 'point', 'numero': 'A', 'titre': 'Des photos récentes', 'texte': "Une photo de la cabine ou d'une pose d'ongles publiée cette semaine montre que l'institut est actif."},
                {'type': 'point', 'numero': 'B', 'titre': 'Des réponses aux avis', 'texte': "Une réponse aimable sous chaque avis montre qu'une vraie personne lit et prend soin de ses clientes."},
                {'type': 'point', 'numero': 'C', 'titre': 'Des horaires lisibles', 'texte': "La pause du midi et le samedi bien indiqués évitent un appel pour rien."},
                {'type': 'fin', 'titre': 'Votre avis compte', 'texte': "Pour vous, qu'est-ce qui compte le plus, A, B ou C ? Dites-le en commentaire."}]},
    textes={
        'instagram': "Deux instituts ont la même note sur leur fiche Google. Qu'est-ce qui fait choisir l'un plutôt que l'autre ?\n\nSur Google Maps, chaque institut a sa fiche Google, avec la note, les photos, les avis et les horaires. Quand les notes se valent, la cliente regarde le reste.\n\nVoici trois pistes, détaillées dans le carrousel.\nA. Des photos récentes des soins\nB. Des réponses aux avis\nC. Des horaires faciles à lire\n\nIl n'y a pas de bonne réponse, on veut votre avis de professionnelle. Pour vous, c'est A, B ou C ?\n\n#FicheGoogle #Estheticienne #InstitutDeBeaute #ReferencementLocal #GoogleBusinessProfile",
        'facebook': "Deux instituts ont la même note sur leur fiche Google. Qu'est-ce qui fait choisir l'un plutôt que l'autre ?\n\nLa fiche Google, c'est ce qui apparaît quand une cliente cherche « institut de beauté » près de chez elle, avec les photos, les avis et les horaires.\n\nOn vous propose un petit sondage.\nA. Des photos récentes des soins\nB. Des réponses aux avis\nC. Des horaires faciles à lire\n\nChaque piste est expliquée dans les images. Vous, vous votez pour quelle lettre ?\n\n#FicheGoogle #Estheticienne #InstitutDeBeaute #ReferencementLocal",
        'linkedin': "Quand deux instituts affichent la même note sur leur fiche Google, qu'est-ce qui fait pencher la cliente ?\nLa fiche Google, c'est la présentation que Google affiche quand on cherche « institut de beauté » à proximité.\n\nLa note attire l'œil, mais elle ne suffit plus à départager deux adresses voisines. La cliente fait défiler le reste.\n\nTrois éléments reviennent souvent dans les échanges avec les gérantes d'institut.\nDes photos récentes des soins et de la cabine, qui montrent une activité réelle.\nDes réponses aux avis, qui montrent qu'une personne lit et prend soin de sa clientèle.\nDes horaires lisibles, avec la pause du midi et le samedi bien indiqués.\n\nAucun de ces éléments ne demande de budget. Ils demandent de la régularité, et c'est souvent là que le temps manque. Proenligne s'en charge chaque semaine pour les instituts qui le souhaitent.\n\nSelon vous, lequel des trois pèse le plus dans le choix d'une nouvelle cliente ?\n\n#FicheGoogle #GoogleBusinessProfile #ReferencementLocal #Esthetique #TPE",
    })

add('2026-11-04', '19:00', intention='offre', metier='chauffagiste', angle='gain-de-temps', format='journee', ton='constat', symptome='fiche-oubliee',
    slug='chauffagiste-soiree-sans-google',
    accroche="En novembre, un chauffagiste n'a plus une minute pour sa fiche Google.",
    premier_commentaire="Chauffagistes, à quel moment de la journée trouvez-vous le temps de vous occuper de votre fiche Google ?",
    tiktok_title="Chauffagiste, plus une minute pour votre fiche Google ?",
    youtube_title="Chauffagiste en pleine saison, qui s'occupe de votre fiche Google ?",
    textes={
        'tiktok': "En novembre, un chauffagiste n'a plus une minute pour sa fiche Google.\nProenligne publie à votre place et répond à vos avis. Essayez gratuitement, sans engagement.\n\n#FicheGoogle #Chauffagiste #Chauffage",
        'instagram': "En novembre, un chauffagiste n'a plus une minute pour sa fiche Google.\n\nVotre fiche Google, c'est ce qui s'affiche quand on cherche « chauffagiste » sur Google Maps, avec vos photos, vos avis et votre numéro. En pleine saison de chauffe, elle passe après la dernière chaudière.\n\nProenligne s'en occupe pour vous.\n✅ Une photo de vos chantiers publiée chaque lundi\n✅ Un article publié chaque jeudi\n✅ Une réponse à chaque avis, et vous validez celles aux avis négatifs\n\nEssayez Proenligne gratuitement, sans engagement.\n\n#FicheGoogle #Chauffagiste #Chauffage #ReferencementLocal #GoogleBusinessProfile",
        'youtube': "En novembre, un chauffagiste n'a plus une minute pour sa fiche Google.\n\nLa fiche Google, c'est la vitrine que Google montre quand un client cherche un chauffagiste près de chez lui. Le soir, après les dépannages, plus personne n'a la force de s'en occuper.\n\nProenligne publie une photo le lundi, un article le jeudi et répond à chaque avis. Vous validez les réponses aux avis négatifs.\n\nEssayez Proenligne gratuitement, sans engagement.\n\n#FicheGoogle #Chauffagiste #Chauffage",
        'facebook': "En novembre, un chauffagiste n'a plus une minute pour sa fiche Google.\n\nQuand un client cherche « chauffagiste » près de chez lui, Google lui montre des fiches avec des photos, des avis et un numéro. La vôtre en fait partie, même quand vous n'avez pas le temps d'y toucher.\n\nProenligne s'en charge chaque semaine.\n✅ Une photo de vos chantiers publiée le lundi\n✅ Un article publié le jeudi\n✅ Une réponse à chaque avis, validée par vous quand l'avis est négatif\n\nEssayez Proenligne gratuitement, sans engagement.\n\n#FicheGoogle #Chauffagiste #Chauffage #ReferencementLocal",
    })

# ───────────────────────── JEUDI 5 ─────────────────────────
add('2026-11-05', '06:30', intention='utile', metier='macon', angle='gain-de-temps', format='conseil', ton='scene', symptome='photos-anciennes',
    slug='macon-photo-avant-de-partir',
    accroche="Ce soir, le mur est monté et le chantier est propre. Votre fiche Google n'en montre rien.",
    premier_commentaire="Maçons, quel est le chantier dont vous êtes le plus fier cette année ? Il est visible sur votre fiche Google ?",
    visuel={'gabarit': 'conseil', 'surtitre': 'Maçons, votre fiche Google', 'titre': '3 gestes avant de quitter le chantier', 'mot': '3 gestes',
            'points': ["Reculez pour montrer l'ouvrage en entier",
                       "Rangez les outils qui traînent dans le cadre",
                       "Photographiez aussi un détail bien fait"],
            'cta': 'question', 'question': "Vous prenez vos chantiers en photo avant de partir ?"},
    textes={
        'x': "Ce soir, le mur est monté et le chantier est propre. Votre fiche Google n'en montre rien.\n\nLe bon réflexe, c'est une photo avant de remonter dans le camion.\n\nVous prenez vos chantiers en photo ?\n\n#FicheGoogle #Macon",
        'facebook': "Ce soir, le mur est monté et le chantier est propre. Votre fiche Google n'en montre rien.\n\nQuand un particulier cherche « maçon » sur Google Maps, il tombe sur des fiches Google avec des photos, des avis et un numéro. Ce sont les photos de chantiers qui lui montrent ce que vous savez faire.\n\nLe bon moment pour la photo, c'est juste avant de partir. Trois gestes suffisent.\nReculez de quelques pas pour montrer l'ouvrage en entier.\nRangez les outils et les sacs qui traînent dans le cadre.\nPhotographiez aussi un détail bien fait, un angle ou un joint propre.\n\nIl ne reste qu'à la publier sur votre fiche Google, ce soir ou lundi.\n\nVous prenez vos chantiers en photo avant de partir, ou ça vous échappe souvent ?\n\n#FicheGoogle #Macon #Maconnerie #ReferencementLocal #GoogleBusinessProfile",
    })

add('2026-11-05', '13:00', intention='utile', metier='autoecole', angle='gain-de-temps', format='conseil', ton='replique', symptome='avis-sans-reponse',
    slug='autoecole-repondre-en-3-temps',
    accroche="« Elle est sérieuse, cette auto-école ? » Les parents cherchent la réponse sur votre fiche Google.",
    premier_commentaire="Auto-écoles, vous répondez aux avis vous-même, ou c'est un moniteur qui s'en charge ?",
    visuel={'gabarit': 'conseil', 'surtitre': 'Auto-écoles, votre fiche Google', 'titre': 'Répondre à un avis en 3 temps', 'mot': '3 temps',
            'points': ["Remerciez l'élève par son prénom",
                       "Rappelez un détail de sa formation",
                       "Souhaitez-lui bonne route"],
            'cta': 'question', 'question': "Qui répond aux avis dans votre auto-école ?",
            'slides': [
                {'type': 'point', 'numero': '1', 'titre': 'Le prénom', 'texte': "« Merci Inès » sonne mieux que « Merci pour votre avis ». Les parents voient qu'une vraie personne répond."},
                {'type': 'point', 'numero': '2', 'titre': 'Un détail vrai', 'texte': "Une phrase sur son examen ou sa première conduite de nuit montre que vous vous souvenez de l'élève."},
                {'type': 'point', 'numero': '3', 'titre': 'Le mot de la fin', 'texte': "Un « bonne route » chaleureux termine la réponse. Deux ou trois phrases suffisent."},
                {'type': 'fin', 'titre': 'À votre tour', 'texte': "Dans votre auto-école, qui répond aux avis, vous ou un moniteur ?"}]},
    textes={
        'instagram': "« Elle est sérieuse, cette auto-école ? » Les parents cherchent la réponse sur votre fiche Google.\n\nAvant d'inscrire leur enfant, beaucoup tapent « auto-école » sur Google Maps. Ils tombent sur votre fiche Google, avec la note, les avis et surtout vos réponses.\n\nUne bonne réponse à un avis tient en 3 temps.\n1. Remerciez l'élève par son prénom.\n2. Rappelez un détail de sa formation, son examen ou sa première conduite de nuit.\n3. Souhaitez-lui bonne route.\n\nDeux ou trois phrases suffisent, et les parents voient qu'une vraie personne répond.\n\nDans votre auto-école, qui répond aux avis, vous ou un moniteur ?\n\n#FicheGoogle #AutoEcole #PermisDeConduire #ReferencementLocal #GoogleBusinessProfile",
        'facebook': "« Elle est sérieuse, cette auto-école ? » Les parents cherchent la réponse sur votre fiche Google.\n\nVotre fiche Google, c'est ce qui s'affiche quand des parents cherchent « auto-école » près de chez eux. Ils lisent les avis des anciens élèves, et ils lisent aussi vos réponses.\n\nUne réponse qui rassure se construit en 3 temps.\nRemerciez l'élève par son prénom.\nRappelez un détail de sa formation.\nSouhaitez-lui bonne route.\n\nExemple. « Merci Inès ! Votre première conduite de nuit vous faisait peur, et vous l'avez réussie haut la main. Bonne route ! »\n\nQui répond aux avis chez vous, vous ou un moniteur ?\n\n#FicheGoogle #AutoEcole #PermisDeConduire #ReferencementLocal",
        'linkedin': "« Elle est sérieuse, cette auto-école ? » C'est la question que se posent des parents devant votre fiche Google, avant d'inscrire leur enfant.\nLa fiche Google, c'est ce que Google affiche quand on cherche « auto-école » dans sa ville.\n\nLes avis des anciens élèves comptent. Les réponses de l'auto-école comptent aussi, parce qu'elles montrent la manière dont l'équipe parle à ses élèves.\n\nUne réponse efficace tient en trois temps.\nRemercier l'élève par son prénom.\nRappeler un détail de sa formation, un examen, une première conduite de nuit.\nLui souhaiter bonne route.\n\nDeux ou trois phrases suffisent. Le plus difficile reste la régularité, surtout quand les avis arrivent pendant les heures de conduite. Proenligne répond à chaque avis pour les auto-écoles qui lui confient leur fiche Google.\n\nDans votre structure, qui est chargé de répondre aux avis ?\n\n#FicheGoogle #GoogleBusinessProfile #ReferencementLocal #AutoEcole",
    })

add('2026-11-05', '19:00', intention='utile', metier='plombier', angle='peur-de-perdre', format='fiche', ton='pendant-que', symptome='photos-anciennes',
    slug='plombier-photos-qui-datent', ab='A',
    accroche="Pendant que vous réparez une fuite, un client regarde les photos de votre fiche Google.",
    premier_commentaire="Plombiers, de quand date la dernière photo de votre fiche Google ? Cette semaine, cette année, ou vous préférez ne pas regarder ?",
    tiktok_title="Que montrent les photos de votre fiche Google ?",
    youtube_title="Plombier, les photos de votre fiche Google datent-elles ?",
    textes={
        'tiktok': "Pendant que vous réparez une fuite, un client regarde les photos de votre fiche Google.\nSi la dernière date de 2021, il se demande si vous êtes toujours là.\n\n#FicheGoogle #Plombier #Plomberie",
        'instagram': "Pendant que vous réparez une fuite, un client regarde les photos de votre fiche Google.\n\nLa fiche Google, c'est ce qu'un client voit quand il cherche « plombier » sur Google Maps, avec vos photos, vos avis et votre numéro.\n\nSi la dernière photo date de 2021, il ne voit pas la salle de bain refaite la semaine dernière ni le chauffe-eau posé ce matin. Il voit une entreprise dont il ne sait plus rien.\n\nQuelle photo de chantier aimeriez-vous qu'il voie en premier ?\n\n#FicheGoogle #Plombier #Plomberie #ReferencementLocal #GoogleBusinessProfile",
        'youtube': "Pendant que vous réparez une fuite, un client regarde les photos de votre fiche Google.\n\nQuand on cherche un plombier sur Google Maps, chaque entreprise a sa fiche Google, avec ses photos, sa note et le bouton Appeler. Des photos de 2021 ne montrent pas votre travail d'aujourd'hui.\n\nProenligne publie une photo de vos chantiers chaque lundi, un article le jeudi, et répond à chaque avis.\n\nDe quand date votre dernière photo ?\n\n#FicheGoogle #Plombier #Plomberie",
        'facebook': "Pendant que vous réparez une fuite, un client regarde les photos de votre fiche Google.\n\nIl a trouvé votre fiche Google sur Google Maps, l'encadré avec votre nom, votre note et vos photos. Il fait défiler les images pour se faire une idée.\n\nSi la plus récente date de 2021, il ne voit rien de votre travail actuel. Il se demande même si vous êtes toujours en activité.\n\nUne photo de chantier publiée chaque semaine suffit à lui répondre.\n\nDe quand date la dernière photo de votre fiche Google ?\n\n#FicheGoogle #Plombier #Plomberie #ReferencementLocal",
    })

# ───────────────────────── VENDREDI 6 ─────────────────────────
add('2026-11-06', '06:30', intention='preuve', metier='coiffeur', angle='gain-de-temps', format='preuve', ton='avant-apres', symptome='avis-sans-reponse',
    slug='coiffeur-salon-qui-repond',
    accroche="Avant, trois avis attendaient une réponse sur la fiche Google du salon. Après, chacun a la sienne.",
    premier_commentaire="Coiffeurs, vous répondez aux avis le jour même, dans la semaine, ou quand vous y pensez ?",
    visuel={'gabarit': 'avant-apres', 'surtitre': 'Avant et après sur une fiche Google', 'titre': 'Le même salon répond désormais à chaque avis', 'mot': 'chaque avis',
            'carte': {'enseigne': 'Salon Martin', 'metier': 'Coiffure', 'avant': 'Trois avis sans réponse', 'apres': 'Une réponse sous chaque avis'},
            'cta': 'question', 'question': "Laquelle des deux versions vous donnerait envie de réserver ?"},
    textes={
        'x': "Avant, trois avis attendaient une réponse sur la fiche Google du salon. Après, chacun a la sienne.\n\nLe salon n'a pas changé. Ce que voit la future cliente, si.\n\nVous répondez à vos avis ?\n\n#FicheGoogle #Coiffeur",
        'facebook': "Avant, trois avis attendaient une réponse sur la fiche Google du salon. Après, chacun a la sienne.\n\nPrenons un salon imaginaire, le salon Martin. Sa fiche Google, c'est ce que voit une future cliente quand elle cherche « coiffeur » dans son quartier, avec la note, les photos et les avis.\n\nAvant, on y lisait trois avis de Julie, Paul et Nadia. « Super coupe. » « Bon accueil. » « Un peu d'attente, mais ça valait le coup. » Aucune réponse en dessous. Impossible de savoir si le salon les avait lus.\n\nAprès, chaque avis a sa réponse. « Merci Julie, à bientôt pour l'entretien de votre couleur. » « Merci Nadia pour votre patience, nous avons revu l'organisation du samedi. »\n\nLa note n'a pas bougé. La future cliente, elle, voit un salon qui écoute.\n\nLaquelle des deux versions vous donnerait envie de réserver ?\n\n#FicheGoogle #Coiffeur #Coiffure #ReferencementLocal #GoogleBusinessProfile",
    })

add('2026-11-06', '13:00', intention='preuve', metier='electricien', angle='peur-de-perdre', format='avant-apres', ton='constat', symptome='service-invisible',
    slug='electricien-bornes-visibles',
    accroche="Vous installez des bornes de recharge, mais votre fiche Google n'en dit pas un mot.",
    premier_commentaire="Électriciens, quel service vous demande-t-on le plus en ce moment ? Il apparaît sur votre fiche Google ?",
    visuel={'gabarit': 'avant-apres', 'surtitre': 'Un service caché sur une fiche Google', 'titre': 'Le client voit enfin que vous posez des bornes', 'mot': 'posez des bornes',
            'carte': {'enseigne': 'Électricité Bernard', 'metier': 'Électricien', 'avant': 'Juste « électricien »', 'apres': 'Bornes de recharge en photo'},
            'cta': 'question', 'question': "Quel service faites-vous sans qu'il apparaisse sur Google ?",
            'slides': [
                {'type': 'point', 'numero': '1', 'titre': 'Avant', 'texte': "La fiche Google indique seulement « électricien ». Rien ne parle des bornes de recharge qu'il installe."},
                {'type': 'point', 'numero': '2', 'titre': 'Après', 'texte': "Une photo de borne posée le lundi, un article sur la recharge à domicile le jeudi. Le service devient visible."},
                {'type': 'fin', 'titre': 'Votre service caché', 'texte': "Quel service faites-vous souvent sans qu'il apparaisse sur votre fiche Google ?"}]},
    textes={
        'instagram': "Vous installez des bornes de recharge, mais votre fiche Google n'en dit pas un mot.\n\nLa fiche Google, c'est la carte de visite que Google montre à votre place quand quelqu'un cherche un électricien, avec vos photos, vos avis et votre numéro.\n\nPrenons un électricien imaginaire, Électricité Bernard.\nAvant, sa fiche Google indiquait seulement « électricien ». Un propriétaire de voiture électrique ne pouvait pas deviner qu'il posait des bornes.\nAprès, une photo de borne installée est publiée le lundi, et un article sur la recharge à domicile le jeudi. Le service se voit enfin.\n\nQuel service faites-vous souvent sans qu'il apparaisse sur votre fiche Google ?\n\n#FicheGoogle #Electricien #BorneDeRecharge #ReferencementLocal #GoogleBusinessProfile",
        'facebook': "Vous installez des bornes de recharge, mais votre fiche Google n'en dit pas un mot.\n\nVoici une démonstration avec un électricien imaginaire, Électricité Bernard.\n\nAvant, sa fiche Google, celle que Google affiche quand on cherche « électricien » près de chez soi, indiquait seulement son métier. Rien sur les bornes de recharge qu'il installe pourtant régulièrement.\n\nAprès, une photo de borne posée arrive le lundi, et un article sur la recharge à domicile le jeudi. Le client qui vient d'acheter une voiture électrique comprend tout de suite qu'il est au bon endroit.\n\nEt vous, quel service restez-vous seul à connaître ?\n\n#FicheGoogle #Electricien #BorneDeRecharge #ReferencementLocal",
        'linkedin': "Beaucoup d'électriciens installent des bornes de recharge sans que leur fiche Google en dise un mot.\nLa fiche Google, c'est l'encadré que Google présente quand un particulier cherche un électricien près de chez lui.\n\nPrenons une entreprise imaginaire.\n\nAvant, sa fiche Google mentionnait seulement « électricien ». Un propriétaire de voiture électrique qui cherchait un installateur ne pouvait pas deviner que cette entreprise en posait.\n\nAprès, une photo de borne installée est publiée le lundi, puis un article sur la recharge à domicile le jeudi. Le service devient visible pour les clients qui le cherchent.\n\nLe métier n'a pas changé. Ce qui a changé, c'est ce que la fiche Google raconte de l'activité réelle.\n\nC'est le principe de Proenligne, une photo chaque lundi, un article chaque jeudi, une réponse à chaque avis.\n\nQuel service de votre entreprise reste aujourd'hui invisible sur Google ?\n\n#FicheGoogle #GoogleBusinessProfile #ReferencementLocal #Electricien #Artisanat",
    })

add('2026-11-06', '19:00', intention='utile', metier='serrurier', angle='gain-de-temps', format='avis', ton='question', symptome='avis-negatif-seul',
    slug='serrurier-avis-negatif-en-haut',
    accroche="Bloqué dehors, que pense un client devant l'avis à une étoile de votre fiche Google ?",
    premier_commentaire="Serruriers, comment répondez-vous à un avis négatif ? Tout de suite, le lendemain à tête reposée, ou pas du tout ?",
    tiktok_title="Un avis négatif sur votre fiche Google, que répondre ?",
    youtube_title="Serrurier, un avis négatif en haut de votre fiche Google",
    textes={
        'tiktok': "Bloqué dehors, que pense un client devant l'avis à une étoile de votre fiche Google ?\nSans réponse, c'est souvent lui qu'on retient. Avec une réponse calme, on voit surtout un artisan qui assume.\n\n#FicheGoogle #Serrurier",
        'instagram': "Bloqué dehors, que pense un client devant l'avis à une étoile de votre fiche Google ?\n\nSur Google Maps, avant d'appeler un serrurier, le client ouvre sa fiche Google et lit les avis, les horaires et vos réponses.\n\nUn avis à une étoile sans réponse, c'est souvent lui qu'on retient. Le même avis avec une réponse calme, qui s'excuse de l'attente et propose d'en parler, montre surtout un artisan qui assume.\n\nComment répondez-vous à un avis négatif, vous ?\n\n#FicheGoogle #Serrurier #Serrurerie #ReferencementLocal #GoogleBusinessProfile",
        'youtube': "Bloqué dehors, que pense un client devant l'avis à une étoile de votre fiche Google ?\n\nVotre fiche Google, c'est ce qui s'affiche quand un client cherche « serrurier » sur Google ou Google Maps. Un avis négatif resté sans réponse y attire l'œil.\n\nProenligne prépare une réponse calme, vous la validez avant qu'elle parte. Et chaque autre avis reçoit aussi sa réponse.\n\nVous répondez aux avis négatifs, vous ?\n\n#FicheGoogle #Serrurier #Serrurerie",
        'facebook': "Bloqué dehors, que pense un client devant l'avis à une étoile de votre fiche Google ?\n\nIl ouvre votre fiche Google, celle qui affiche votre note et vos avis sur Google Maps. Il tombe d'abord sur une étoile et un reproche. Pas de réponse en dessous.\n\nPourtant, les avis suivants sont excellents. Mais c'est souvent le premier qu'on retient.\n\nUne réponse calme change la lecture. On s'excuse de l'attente, on propose d'en parler, on reste poli.\n\nComment répondez-vous à un avis négatif, vous ?\n\n#FicheGoogle #Serrurier #Serrurerie #ReferencementLocal",
    })

# ───────────────────────── SAMEDI 7 ─────────────────────────
add('2026-11-07', '06:30', intention='utile', metier='garage', angle='peur-de-perdre', format='test', ton='replique', symptome='note-sans-contexte',
    slug='garage-test-des-3-dates',
    accroche="« Ce garage existe toujours ? » Votre fiche Google répond à votre place, en 3 dates.",
    premier_commentaire="Répondez juste par photo, avis ou publication. C'est laquelle, la plus ancienne chez vous ?",
    visuel={'gabarit': 'question', 'surtitre': 'Le test des 3 dates sur Google', 'titre': 'Laquelle est la plus ancienne sur votre fiche Google ?', 'mot': 'la plus ancienne',
            'reponses': ['La dernière photo', 'La dernière réponse à un avis', 'La dernière publication'],
            'cta': 'question', 'question': "Répondez en commentaire, photo, avis ou publication."},
    textes={
        'x': "« Ce garage existe toujours ? » Votre fiche Google répond à votre place, en 3 dates.\n\nLa dernière photo, la dernière réponse à un avis, la dernière publication.\n\nChez vous, laquelle est la plus ancienne ?\n\n#FicheGoogle #Garage",
        'facebook': "« Ce garage existe toujours ? » Votre fiche Google répond à votre place, en 3 dates.\n\nSur Google Maps, chaque garage a sa fiche Google, avec la note, les photos et le bouton Appeler. Un automobiliste qui ne vous connaît pas la parcourt en quelques secondes.\n\nFaites le test ce week-end, depuis votre téléphone.\nRegardez la date de votre dernière photo.\nRegardez la date de votre dernière réponse à un avis.\nRegardez la date de votre dernière publication.\n\nSi les trois datent de cette saison, le client voit un garage en activité. Si l'une remonte à 2021, il peut se poser la question.\n\nChez vous, laquelle des trois dates est la plus ancienne ?\n\n#FicheGoogle #Garage #Garagiste #ReferencementLocal #GoogleBusinessProfile",
    })

add('2026-11-07', '13:00', intention='offre', metier='general', angle='gain-de-temps', format='conseil', ton='contre-intuitif', symptome=None,
    slug='offre-fiche-google-sans-soiree',
    accroche="Moins vous passez de temps sur votre fiche Google, plus elle peut bouger. C'est le principe de Proenligne.",
    premier_commentaire="Une question sur le fonctionnement ? Posez-la ici, on vous répond. L'essai est gratuit et sans engagement.",
    visuel={'gabarit': 'conseil', 'surtitre': 'Proenligne et votre fiche Google', 'titre': 'Votre fiche Google bouge sans vous prendre une soirée', 'mot': 'sans vous prendre une soirée',
            'points': ["Recevez une photo publiée chaque lundi",
                       "Retrouvez un article publié chaque jeudi",
                       "Validez les réponses aux avis négatifs"],
            'cta': 'offre',
            'slides': [
                {'type': 'point', 'numero': '1', 'titre': 'Le lundi, une photo', 'texte': "Proenligne publie une photo de votre travail sur votre fiche Google, chaque lundi."},
                {'type': 'point', 'numero': '2', 'titre': 'Le jeudi, un article', 'texte': "Un article sur votre métier ou sur la saison est publié chaque jeudi."},
                {'type': 'point', 'numero': '3', 'titre': 'Une réponse à chaque avis', 'texte': "Proenligne répond à chaque avis. Vous validez les réponses aux avis négatifs."},
                {'type': 'fin', 'titre': 'Essayez gratuitement', 'texte': "L'essai est gratuit et sans engagement. Vous gardez la main sur les réponses aux avis négatifs."}]},
    textes={
        'instagram': "Moins vous passez de temps sur votre fiche Google, plus elle peut bouger. C'est le principe de Proenligne.\n\nLa fiche Google, c'est ce que vos clients voient en premier quand ils cherchent votre métier sur Google ou Google Maps. Elle rassure quand elle montre une activité récente.\n\nProenligne s'en occupe chaque semaine.\n✅ Une photo de votre travail publiée le lundi\n✅ Un article publié le jeudi\n✅ Une réponse à chaque avis, et vous validez celles aux avis négatifs\n\nEssayez Proenligne gratuitement, sans engagement.\n\n#FicheGoogle #GoogleBusinessProfile #ReferencementLocal #Artisans #Commercants",
        'facebook': "Moins vous passez de temps sur votre fiche Google, plus elle peut bouger. C'est le principe de Proenligne.\n\nVotre fiche Google, c'est ce qui s'affiche quand un client cherche votre métier sur Google ou Google Maps, avec vos photos, vos avis et vos horaires. Une activité récente y rassure.\n\nChaque semaine, sans prendre votre soirée.\n✅ Une photo de votre travail publiée le lundi\n✅ Un article publié le jeudi\n✅ Une réponse à chaque avis, validée par vous quand l'avis est négatif\n\nEssayez Proenligne gratuitement, sans engagement.\n\n#FicheGoogle #GoogleBusinessProfile #ReferencementLocal #Artisans",
    })

add('2026-11-07', '19:00', intention='utile', metier='estheticienne', angle='peur-de-perdre', format='journee', ton='scene', symptome='pas-de-nouveaute',
    slug='estheticienne-nouveau-soin-cache',
    accroche="Il est 22 h. La cabine est rangée, mais votre nouveau soin manque sur votre fiche Google.",
    premier_commentaire="Esthéticiennes, quel est le dernier soin que vous avez ajouté à votre carte ? Il est annoncé sur votre fiche Google ?",
    tiktok_title="Votre nouveau soin est-il sur votre fiche Google ?",
    youtube_title="Esthéticienne, votre nouveau soin est-il annoncé sur votre fiche Google ?",
    textes={
        'tiktok': "Il est 22 h. La cabine est rangée, mais votre nouveau soin manque sur votre fiche Google.\nVos clientes ne peuvent pas réserver un soin dont elles ignorent l'existence.\n\n#FicheGoogle #Estheticienne #InstitutDeBeaute",
        'instagram': "Il est 22 h. La cabine est rangée, mais votre nouveau soin manque sur votre fiche Google.\n\nQuand une cliente cherche « institut de beauté » sur Google, elle voit des fiches avec des photos, des avis et des publications. La vôtre en fait partie.\n\nVous proposez depuis peu un rehaussement de cils. Mais après une journée pleine en cabine, l'annonce attend encore. Une cliente fidèle le fera peut-être ailleurs, sans savoir que vous le proposez.\n\nQuel soin aimeriez-vous mettre en avant cette semaine ?\n\n#FicheGoogle #Estheticienne #InstitutDeBeaute #ReferencementLocal #GoogleBusinessProfile",
        'youtube': "Il est 22 h. La cabine est rangée, mais votre nouveau soin manque sur votre fiche Google.\n\nLa fiche Google, c'est ce que Google affiche quand une cliente cherche un institut près de chez elle. Une nouveauté qui n'y figure pas reste invisible.\n\nProenligne publie un article le jeudi, une photo le lundi, et répond à chaque avis.\n\nQuel est votre dernier soin ajouté ?\n\n#FicheGoogle #Estheticienne #InstitutDeBeaute",
        'facebook': "Il est 22 h. La cabine est rangée, mais votre nouveau soin manque sur votre fiche Google.\n\nVotre fiche Google, c'est la vitrine que voient les clientes sur Google Maps avant de réserver. Ce qui n'y est pas, elles ne le savent pas.\n\nLa journée a été pleine, entre les soins du visage et les manucures. L'annonce du rehaussement de cils attendra encore un soir.\n\nPendant ce temps, une cliente fidèle cherche ce soin et le trouve ailleurs.\n\nQuel est le dernier soin que vous avez ajouté à votre carte ?\n\n#FicheGoogle #Estheticienne #InstitutDeBeaute #ReferencementLocal",
    })

# ───────────────────────── DIMANCHE 8 ─────────────────────────
add('2026-11-08', '06:30', intention='utile', metier='paysagiste', angle='gain-de-temps', format='constat', ton='question', symptome='photos-anciennes',
    slug='paysagiste-photo-d-avant',
    accroche="Pourquoi les plus beaux jardins restent-ils si rarement sur la fiche Google du paysagiste ?",
    premier_commentaire="Paysagistes, quel est le chantier dont vous regrettez de ne pas avoir la photo d'avant ?",
    visuel={'gabarit': 'conseil', 'surtitre': 'Paysagistes, votre fiche Google', 'titre': "Prenez la photo d'avant en arrivant", 'mot': "photo d'avant",
            'points': ["Photographiez le terrain avant de sortir le matériel",
                       "Gardez le même angle pour la photo finale",
                       "Publiez les deux photos sur votre fiche Google"],
            'cta': 'question', 'question': "Vous pensez à prendre la photo d'avant ?"},
    textes={
        'x': "Pourquoi les plus beaux jardins restent-ils si rarement sur la fiche Google du paysagiste ?\n\nSouvent, il manque la photo d'avant. Sans elle, l'après impressionne moins.\n\nVous pensez à la prendre ?\n\n#FicheGoogle #Paysagiste",
        'facebook': "Pourquoi les plus beaux jardins restent-ils si rarement sur la fiche Google du paysagiste ?\n\nCherchez « paysagiste » dans votre ville. Les encadrés avec une note et des photos sont des fiches Google. Regardez les photos. On y voit souvent des pelouses, rarement des transformations.\n\nLa raison est simple. Le jour où l'on arrive sur un terrain en friche, on pense au travail, pas à la photo. Et sans la photo d'avant, celle d'après impressionne beaucoup moins.\n\nLe réflexe tient en une photo. En arrivant, avant de sortir le matériel, photographiez le terrain depuis l'endroit où vous prendrez la photo finale.\n\nAvec les deux photos côte à côte sur votre fiche Google, un client comprend tout de suite ce que vous savez faire.\n\nVous pensez à prendre la photo d'avant, ou c'est toujours trop tard ?\n\n#FicheGoogle #Paysagiste #Jardin #ReferencementLocal #GoogleBusinessProfile",
    })

add('2026-11-08', '13:00', intention='utile', metier='macon', angle='peur-de-perdre', format='question', ton='pendant-que', symptome=None,
    slug='macon-sondage-gros-chantier',
    accroche="Pendant que vous préparez son devis, le client compare encore les fiches Google des maçons du coin.",
    premier_commentaire="Votez avec une lettre. Et si un client vous a déjà dit pourquoi il vous avait choisi, racontez-le.",
    visuel={'gabarit': 'question', 'surtitre': 'Maçons, un sondage sur la fiche Google', 'titre': "Qu'est-ce qui rassure avant un gros chantier ?", 'mot': 'rassure',
            'reponses': ['A. Des photos de chantiers finis', 'B. Des avis sur le respect des délais', 'C. Une réponse sous chaque avis'],
            'cta': 'question', 'question': "Pour vous, c'est A, B ou C ? Dites-le en commentaire.",
            'slides': [
                {'type': 'point', 'numero': 'A', 'titre': 'Des chantiers finis', 'texte': "Un mur, une terrasse ou une extension terminés. Le client imagine son propre chantier."},
                {'type': 'point', 'numero': 'B', 'titre': 'Le respect des délais', 'texte': "Un avis qui dit « fini à la date prévue » rassure souvent plus qu'une note parfaite."},
                {'type': 'point', 'numero': 'C', 'titre': 'Les réponses aux avis', 'texte': "Une réponse polie, même à un avis mitigé, montre comment vous gérez un souci."},
                {'type': 'fin', 'titre': 'À vous de voter', 'texte': "Qu'est-ce qui rassure le plus vos clients, A, B ou C ?"}]},
    textes={
        'instagram': "Pendant que vous préparez son devis, le client compare encore les fiches Google des maçons du coin.\n\nUne fiche Google, c'est ce que Google montre quand on cherche « maçon » près de chez soi, avec les photos, la note et les avis. Avant un gros chantier, on la lit de près.\n\nPetit sondage entre professionnels. Qu'est-ce qui rassure le plus ?\nA. Des photos de chantiers finis\nB. Des avis sur le respect des délais\nC. Une réponse sous chaque avis\n\nVotez en commentaire avec une lettre.\n\n#FicheGoogle #Macon #Maconnerie #ReferencementLocal #GoogleBusinessProfile",
        'facebook': "Pendant que vous préparez son devis, le client compare encore les fiches Google des maçons du coin.\n\nPour un mur, une terrasse ou une extension, il ne choisit pas au hasard. Il ouvre les fiches Google, ces encadrés avec photos, note et avis que Google affiche pour chaque entreprise.\n\nSelon vous, qu'est-ce qui le rassure le plus ?\nA. Des photos de chantiers finis\nB. Des avis sur le respect des délais\nC. Une réponse sous chaque avis\n\nChaque piste est détaillée dans les images. Et sur votre fiche Google, laquelle des trois est la plus visible ? Vous votez pour quelle lettre ?\n\n#FicheGoogle #Macon #Maconnerie #ReferencementLocal",
    })

add('2026-11-08', '19:00', intention='preuve', metier='autoecole', angle='gain-de-temps', format='fiche', ton='avant-apres', symptome='note-sans-contexte',
    slug='autoecole-bonne-note-sans-vie',
    accroche="Avant, votre fiche Google avait une bonne note et aucun signe de vie récent.",
    premier_commentaire="Auto-écoles, qu'est-ce qui montre le mieux que votre école est active ? Une photo de voiture, un conseil sur le code, une réponse à un élève ?",
    tiktok_title="Une bonne note sur votre fiche Google ne suffit pas toujours",
    youtube_title="Auto-école, votre fiche Google avant et après",
    textes={
        'tiktok': "Avant, votre fiche Google avait une bonne note et aucun signe de vie récent.\nAprès, une photo le lundi, un article le jeudi, une réponse à chaque élève.\n\n#FicheGoogle #AutoEcole #Permis",
        'instagram': "Avant, votre fiche Google avait une bonne note et aucun signe de vie récent.\n\nLa fiche Google, c'est ce que voient les parents quand ils cherchent « auto-école » sur Google Maps, avec la note, les photos et les avis.\n\nAvant, la note était bonne, mais aucune photo ni publication depuis 2021. Un parent pouvait se demander si l'école prenait encore des élèves.\n\nAprès, une photo de la voiture école le lundi, un article sur le code le jeudi, une réponse à chaque avis. La même note, avec une école qu'on voit vivre.\n\nQu'est-ce qui montre le mieux, selon vous, qu'une auto-école est active ?\n\n#FicheGoogle #AutoEcole #Permis #ReferencementLocal #GoogleBusinessProfile",
        'youtube': "Avant, votre fiche Google avait une bonne note et aucun signe de vie récent.\n\nVotre fiche Google, c'est ce qui s'affiche quand des parents cherchent « auto-école » sur Google ou Google Maps. Une bonne note sans rien de récent laisse un doute.\n\nAprès, Proenligne publie une photo le lundi, un article le jeudi et répond à chaque avis. Essayez gratuitement, sans engagement.\n\n#FicheGoogle #AutoEcole #Permis",
        'facebook': "Avant, votre fiche Google avait une bonne note et aucun signe de vie récent.\n\nUn père cherche une auto-école pour sa fille. Sur Google Maps, il ouvre votre fiche Google. La note est bonne, mais la dernière photo date de 2021 et rien n'a été publié depuis. Il se demande si l'école accepte encore des élèves.\n\nAprès, la même fiche Google montre une photo de la voiture école le lundi, un article sur le code le jeudi, une réponse sous chaque avis.\n\nMême école, même note. Cette fois, on la voit vivre.\n\nLaquelle des deux versions rassurerait un parent, selon vous ?\n\n#FicheGoogle #AutoEcole #Permis #ReferencementLocal",
    })

# ───────────────────────── VARIANTES B (TikTok seul, 12:30) ─────────────────────────
add('2026-11-05', '12:30', intention='utile', metier='garage', angle='gain-de-temps', format='avis', ton='constat', symptome='avis-sans-reponse',
    slug='garage-avis-sans-reponse-soir', ab='B',
    accroche="Quand chaque avis de votre fiche Google reçoit un merci, vos clients le remarquent.",
    premier_commentaire="Garagistes, vous répondez aux avis vous-même, ou personne n'a le temps ?",
    tiktok_title="Vos clients attendent une réponse sur votre fiche Google",
    textes={'tiktok': "Quand chaque avis de votre fiche Google reçoit un merci, vos clients le remarquent.\nUne phrase et un prénom suffisent pour montrer que vous lisez.\n\n#FicheGoogle #Garage #Garagiste"})

add('2026-11-07', '12:30', intention='utile', metier='plombier', angle='peur-de-perdre', format='fiche', ton='question', symptome='photos-anciennes',
    slug='plombier-photos-qui-datent', ab='B',
    accroche="Sur votre fiche Google, vos photos montrent-elles encore votre travail d'aujourd'hui ?",
    premier_commentaire="Plombiers, quelle photo de chantier mettriez-vous en premier sur votre fiche Google ?",
    tiktok_title="Vos photos sur votre fiche Google sont-elles à jour ?",
    textes={'tiktok': "Sur votre fiche Google, vos photos montrent-elles encore votre travail d'aujourd'hui ?\nUn client qui ne voit que des photos de 2021 se demande si vous êtes toujours là.\n\n#FicheGoogle #Plombier #Plomberie"})


# ───────── Corrections après la relecture n°1 (passe 1 : 82 refus) ─────────
def T(date, nom, champ, val):
    for c in C:
        if c['date'] == date and c['creneau_nominal'] == nom:
            if champ.startswith('textes.'): c['textes'][champ[7:]] = val
            elif champ.startswith('visuel.slides.'):
                i, k = champ.split('.')[2:]; c['visuel']['slides'][int(i)][k] = val
            elif champ.startswith('visuel.points.'):
                c['visuel']['points'][int(champ.split('.')[2])] = val
            elif champ.startswith('visuel.'): c['visuel'][champ[7:]] = val
            else: c[champ] = val
            return
    raise KeyError((date, nom, champ))

L, M, ME, J, V, S, D = ('2026-11-%02d' % i for i in range(2, 9))
T(L, '06:30', 'premier_commentaire', "Faites le test et dites-nous ce que vous avez remarqué en premier sur votre fiche Google. La photo, les horaires ou le dernier avis ?")
T(L, '13:00', 'textes.instagram', "Vos plus belles coupes dorment dans votre téléphone au lieu d'être sur votre fiche Google.\n\nQuand quelqu'un tape « coiffeur près de moi », Google affiche des fiches avec des photos, des avis et des horaires. La vôtre en fait partie, et ce sont souvent les photos qu'on regarde en premier.\n\nVoici 3 réflexes qui prennent deux minutes.\n1. Photographiez la coupe près de la vitrine, à la lumière du jour, sans flash.\n2. Demandez l'accord de la cliente. Beaucoup sont flattées qu'on leur pose la question.\n3. Publiez la photo sur votre fiche Google le soir même, pendant que vous y pensez.\n\nAu salon, qui prend les photos des coupes, vous ou quelqu'un de l'équipe ?\n\n#FicheGoogle #Coiffeur #Coiffure #ReferencementLocal #GoogleBusinessProfile")
T(L, '19:00', 'textes.tiktok', "Il est 20 h. Une cliente cherche un paysagiste pour ses haies et ouvre votre fiche Google, l'encadré que Google affiche avec vos photos et vos avis.\nRien n'y a été publié depuis le printemps. Elle se demande si vous travaillez encore l'hiver.\n\n#FicheGoogle #Paysagiste #Jardin")
T(L, '19:00', 'textes.instagram', "Il est 20 h. Une cliente cherche un paysagiste pour ses haies et ouvre votre fiche Google.\n\nVotre fiche Google, c'est ce qui s'affiche quand quelqu'un tape « paysagiste » sur Google Maps, avec vos photos, vos avis et vos publications.\n\nCe soir-là, la dernière photo montre une tonte du printemps, et rien n'a été publié depuis. Elle se demande si vous travaillez encore l'hiver, et elle continue de chercher.\n\nL'hiver, il y a pourtant de quoi montrer. Une taille de haie, un ramassage de feuilles, une plantation d'arbres.\n\nQue publiez-vous sur votre fiche Google pendant l'hiver ?\n\n#FicheGoogle #Paysagiste #Jardin #ReferencementLocal #GoogleBusinessProfile")
T(L, '19:00', 'textes.youtube', "Il est 20 h. Une cliente cherche un paysagiste et ouvre votre fiche Google. Rien n'y a été publié depuis le printemps.\n\nLa fiche Google, c'est la carte de visite que Google montre à votre place, avec vos photos, vos avis et vos publications. En hiver, quand elle ne bouge plus, on peut croire que l'entreprise est en pause.\n\nProenligne publie une photo le lundi et un article le jeudi, et répond à chaque avis, même l'hiver.\n\nEt vous, que montrez-vous sur votre fiche Google en novembre ?\n\n#FicheGoogle #Paysagiste #Jardin")
T(L, '19:00', 'textes.facebook', "Il est 20 h. Une cliente cherche un paysagiste et ouvre votre fiche Google.\n\nElle veut faire tailler ses haies avant l'hiver. Sur votre fiche Google, l'encadré que Google lui montre avec vos photos et vos avis, la dernière publication date du printemps.\n\nElle se pose une question simple. Est-ce qu'il travaille encore en novembre ?\n\nUne taille de haie ou un ramassage de feuilles en photo suffit souvent à lui répondre.\n\nQue publiez-vous sur votre fiche Google pendant l'hiver ?\n\n#FicheGoogle #Paysagiste #Jardin #ReferencementLocal")
# mardi
T(M, '06:30', 'textes.x', "Pendant que vous êtes sur un chantier, votre fiche Google affiche peut-être encore vos horaires de vacances.\n\nC'est l'encadré que Google montre à qui cherche un électricien. S'il lit « Fermé », il appelle ailleurs.\n\nVous les avez vérifiés ?\n\n#FicheGoogle #Electricien")
T(M, '06:30', 'visuel.titre', "Vos horaires de vacances sont-ils encore affichés ?")
T(M, '13:00', 'textes.instagram', "La même boulangerie peut avoir deux visages sur sa fiche Google. Lequel donne faim ?\n\nLa fiche Google, c'est l'encadré qui s'affiche quand on cherche « boulangerie » sur Google Maps, avec la note, les photos et les horaires.\n\nPrenons une boulangerie imaginaire, la boulangerie Durand.\n\nAvant, sa fiche Google n'avait qu'une photo, une vitrine vide prise un soir après la fermeture.\n\nAprès, une photo de la fournée du matin arrive chaque lundi. On voit les baguettes, les viennoiseries et l'équipe derrière le comptoir.\n\nLe pain est le même et la note aussi. Ce qui change, c'est ce que le client voit avant de choisir où s'arrêter.\n\nVous, vous entreriez dans laquelle ?\n\n#FicheGoogle #Boulangerie #Boulanger #ReferencementLocal #GoogleBusinessProfile")
T(M, '13:00', 'textes.facebook', "La même boulangerie peut avoir deux visages sur sa fiche Google. Lequel donne faim ?\n\nCherchez « boulangerie » dans votre ville. Les encadrés avec une note et des photos sont des fiches Google. C'est souvent là que se joue le choix du croissant du dimanche.\n\nVoici une boulangerie imaginaire, la boulangerie Durand, en deux versions.\nAvant, sa fiche Google n'avait qu'une photo, une vitrine vide prise un soir après la fermeture.\nAprès, une photo de la fournée du matin est publiée chaque lundi, avec les baguettes, les viennoiseries et l'équipe.\n\nLe pain est le même, la note aussi. Seule la vitrine sur Google a changé.\n\nLaquelle vous donnerait envie d'entrer ?\n\n#FicheGoogle #Boulangerie #Boulanger #ReferencementLocal")
T(M, '13:00', 'visuel.slides.1.texte', "Chaque lundi, une photo de la fournée du matin est publiée. On y voit les baguettes, les viennoiseries et l'équipe.")
T(M, '19:00', 'premier_commentaire', "Garagistes, combien d'avis attendent une réponse sur votre fiche Google en ce moment ? Aucun, quelques-uns ou beaucoup ?")
T(M, '19:00', 'youtube_title', "Garagiste, vos avis sans réponse sur votre fiche Google font-ils douter vos clients ?")
T(M, '19:00', 'textes.tiktok', "« Ce garage ne répond jamais ? » C'est ce que se demande un client quand les avis de votre fiche Google restent sans réponse.\nVotre fiche Google, c'est l'encadré que Google affiche avec votre note et vos avis quand on cherche un garage.\n\n#FicheGoogle #Garage #Garagiste #Mecanique")
T(M, '19:00', 'textes.instagram', "« Ce garage ne répond jamais ? » se demande un client devant votre fiche Google.\n\nSur Google Maps, chaque garage a sa fiche Google, avec la note, les avis et le bouton Appeler. Les avis, la plupart des clients les lisent. Les réponses aussi.\n\nTrois bons avis sans un mot en dessous, et le nouveau client se demande si quelqu'un lit ce qu'écrivent les clients.\n\nRépondre prend une phrase. « Merci Karim, ravis d'avoir pu vous dépanner ce samedi. »\n\nCombien d'avis attendent une réponse sur votre fiche Google ?\n\n#FicheGoogle #Garage #Garagiste #ReferencementLocal #GoogleBusinessProfile")
T(M, '19:00', 'textes.youtube', "« Ce garage ne répond jamais ? » C'est la question d'un client devant une fiche Google où trois bons avis restent sans réponse.\n\nVotre fiche Google, c'est ce que vos clients voient en premier quand ils cherchent « garage » sur Google Maps. Les réponses aux avis montrent qu'une vraie personne écoute.\n\nProenligne répond à chaque avis, publie une photo le lundi et un article le jeudi.\n\nVous répondez à vos avis, vous ?\n\n#FicheGoogle #Garage #Garagiste")
T(M, '19:00', 'textes.facebook', "« Ce garage ne répond jamais ? » se demande un client devant votre fiche Google.\n\nIl cherche un garage pour sa révision. Sur votre fiche Google, l'encadré que Google lui montre avec votre note et vos avis, il lit trois bons avis. Aucun n'a de réponse.\n\nCe n'est pas grave en soi, mais ça laisse un doute. Est-ce que quelqu'un lit vraiment ce qu'écrivent les clients ?\n\nUne phrase suffit sous chaque avis, avec un merci, un prénom et un détail.\n\nVous répondez à vos avis le jour même, ou plutôt quand vous avez un moment ?\n\n#FicheGoogle #Garage #Garagiste #ReferencementLocal")
# mercredi
T(ME, '06:30', 'textes.x', "On pense qu'en urgence, personne ne regarde votre fiche Google. C'est souvent l'inverse.\n\nBloqué dehors, le client ouvre les fiches Google des serruriers sur Google Maps et lit leurs avis.\n\nÀ sa place, que regarderiez-vous en premier ?\n\n#FicheGoogle #Serrurier")
T(ME, '06:30', 'textes.facebook', "On pense qu'en urgence, personne ne regarde votre fiche Google. C'est souvent l'inverse.\n\nImaginez quelqu'un bloqué devant sa porte un dimanche soir. Il a entendu des histoires de dépannages qui tournent mal. Alors avant d'appeler, il ouvre Google Maps et regarde les fiches Google des serruriers du coin, avec leur note, leurs avis et leurs photos.\n\nIl cherche des signes rassurants, comme un nom et une camionnette en photo, des avis récents et des réponses polies.\n\nL'urgence ne fait pas disparaître la méfiance. Elle la rend plus forte.\n\nSi vous étiez bloqué dehors, qu'est-ce qui vous ferait appeler un serrurier plutôt qu'un autre ?\n\n#FicheGoogle #Serrurier #ReferencementLocal #GoogleBusinessProfile")
T(ME, '06:30', 'visuel.surtitre', "Serruriers, contrairement à une idée reçue")
T(ME, '13:00', 'textes.linkedin', "Quand deux instituts affichent la même note sur leur fiche Google, qu'est-ce qui fait pencher la cliente ?\nLa fiche Google, c'est la présentation que Google affiche quand on cherche « institut de beauté » à proximité.\n\nLa note attire l'œil, mais quand deux adresses voisines ont la même, la cliente fait défiler le reste.\n\nTrois éléments peuvent faire la différence.\nA. Des photos récentes des soins et de la cabine, qui montrent une activité réelle.\nB. Des réponses aux avis, qui montrent qu'une personne lit et prend soin de sa clientèle.\nC. Des horaires lisibles, avec la pause du midi et le samedi bien indiqués.\n\nAucun de ces éléments ne demande de budget. Ils demandent de la régularité, et c'est souvent là que le temps manque. Proenligne s'en charge chaque semaine pour les instituts qui le souhaitent.\n\nSelon vous, lequel pèse le plus dans le choix d'une nouvelle cliente, A, B ou C ?\n\n#FicheGoogle #GoogleBusinessProfile #ReferencementLocal #Esthetique #TPE")
T(ME, '19:00', 'tiktok_title', "Chauffagiste, avez-vous encore une minute pour votre fiche Google ?")
T(ME, '19:00', 'textes.tiktok', "En novembre, un chauffagiste n'a plus une minute pour sa fiche Google.\nC'est pourtant elle que voit un client qui cherche « chauffagiste » sur Google Maps. Proenligne publie une photo le lundi, un article le jeudi et répond à vos avis. Essayez gratuitement, sans engagement.\n\n#FicheGoogle #Chauffagiste #Chauffage")
T(ME, '19:00', 'textes.instagram', "En novembre, un chauffagiste n'a plus une minute pour sa fiche Google.\n\nVotre fiche Google, c'est ce qui s'affiche quand on cherche « chauffagiste » sur Google Maps, avec vos photos, vos avis et votre numéro. En pleine saison de chauffe, les chaudières passent avant elle.\n\nProenligne s'en occupe pour vous.\n✅ Une photo de vos chantiers publiée chaque lundi\n✅ Un article publié chaque jeudi\n✅ Une réponse à chaque avis, et vous validez celles aux avis négatifs\n\nEssayez Proenligne gratuitement, sans engagement.\n\n#FicheGoogle #Chauffagiste #Chauffage #ReferencementLocal #GoogleBusinessProfile")
# jeudi
T(J, '06:30', 'textes.x', "Ce soir, le mur est monté et le chantier est propre. Votre fiche Google n'en montre rien.\n\nC'est pourtant elle qu'on voit en cherchant « maçon » sur Google Maps. Une photo avant de remonter dans le camion suffit.\n\nVous prenez vos chantiers en photo ?\n\n#FicheGoogle #Macon")
T(J, '12:30', 'premier_commentaire', "Garagistes, quel avis client vous a fait le plus plaisir cette année sur votre fiche Google ?")
T(J, '12:30', 'textes.tiktok', "Quand chaque avis de votre fiche Google reçoit un merci, vos clients le remarquent.\nVotre fiche Google, c'est l'encadré de votre garage sur Google Maps, avec la note et les avis. Une phrase et le prénom du client suffisent pour montrer que vous lisez.\n\n#FicheGoogle #Garage #Garagiste")
T(J, '13:00', 'textes.facebook', "« Elle est sérieuse, cette auto-école ? » Les parents cherchent la réponse sur votre fiche Google.\n\nVotre fiche Google, c'est ce qui s'affiche quand des parents cherchent « auto-école » près de chez eux. Ils lisent les avis des anciens élèves, et ils lisent aussi vos réponses.\n\nUne réponse qui rassure se construit en 3 temps.\nRemerciez l'élève par son prénom.\nRappelez un détail de sa formation.\nSouhaitez-lui bonne route.\n\nVoici un exemple de réponse. « Merci Inès ! Votre première conduite de nuit vous faisait peur, et vous l'avez réussie haut la main. Bonne route ! »\n\nQui répond aux avis chez vous, vous ou un moniteur ?\n\n#FicheGoogle #AutoEcole #PermisDeConduire #ReferencementLocal")
T(J, '19:00', 'premier_commentaire', "Plombiers, de quand date la dernière photo de chantier publiée sur votre fiche Google ? De cette semaine, de cette année, ou de plus longtemps ?")
T(J, '19:00', 'textes.tiktok', "Pendant que vous réparez une fuite, un client regarde les photos de votre fiche Google, l'encadré qui s'affiche sur Google Maps quand on cherche « plombier ».\nSi la dernière photo date de 2021, il se demande si vous êtes toujours là.\n\n#FicheGoogle #Plombier #Plomberie")
# vendredi
acc_v = "Avant, trois avis attendaient une réponse sur la fiche Google d'un salon de coiffure. Après, chacun a la sienne."
T(V, '06:30', 'accroche', acc_v)
T(V, '06:30', 'textes.x', acc_v + "\n\nC'est ce que lit une cliente qui cherche « coiffeur » sur Google Maps.\n\nVous répondez à vos avis ?\n\n#FicheGoogle #Coiffeur")
T(V, '06:30', 'textes.facebook', acc_v + "\n\nPrenons un salon imaginaire, le salon Martin. Sa fiche Google, c'est ce que voit une future cliente quand elle cherche « coiffeur » dans son quartier, avec la note, les photos et les avis.\n\nAvant, on y lisait trois avis de Julie, Karim et Nadia. « Super coupe. » « Bon accueil. » « Un peu d'attente, mais ça valait le coup. » Aucune réponse en dessous. Impossible de savoir si le salon les avait lus.\n\nAprès, chaque avis a sa réponse. « Merci Julie, à bientôt pour l'entretien de votre couleur. » « Merci Nadia pour votre patience, nous avons revu l'organisation du samedi. »\n\nLa note n'a pas bougé. La future cliente, elle, voit un salon qui écoute.\n\nLaquelle des deux versions vous donnerait envie de réserver ?\n\n#FicheGoogle #Coiffeur #Coiffure #ReferencementLocal #GoogleBusinessProfile")
T(V, '13:00', 'textes.facebook', "Vous installez des bornes de recharge, mais votre fiche Google n'en dit pas un mot.\n\nVoici une démonstration avec un électricien imaginaire, Électricité Bernard.\n\nAvant, sa fiche Google, celle que Google affiche quand on cherche « électricien » près de chez soi, indiquait seulement son métier. Rien sur les bornes de recharge qu'il installe pourtant régulièrement.\n\nAprès, une photo de borne installée arrive le lundi, et un article sur la recharge à domicile le jeudi. Le client qui vient d'acheter une voiture électrique comprend tout de suite qu'il est au bon endroit.\n\nEt vous, quel service faites-vous souvent sans qu'il apparaisse sur votre fiche Google ?\n\n#FicheGoogle #Electricien #BorneDeRecharge #ReferencementLocal")
T(V, '13:00', 'visuel.titre', "Le client voit enfin que vous posez des bornes de recharge")
T(V, '13:00', 'visuel.mot', "bornes de recharge")
T(V, '13:00', 'visuel.slides.0.texte', "La fiche Google d'Électricité Bernard indique seulement « électricien ». Rien ne parle des bornes de recharge installées.")
T(V, '13:00', 'visuel.slides.1.texte', "Une photo de borne installée est publiée le lundi, puis un article sur la recharge à domicile le jeudi.")
T(V, '19:00', 'youtube_title', "Serrurier, que répondre à un avis négatif sur votre fiche Google ?")
T(V, '19:00', 'textes.tiktok', "Bloqué dehors, que pense un client devant l'avis à une étoile de votre fiche Google, l'encadré qui montre votre note sur Google Maps ?\nSans réponse, c'est souvent cet avis qu'on retient. Avec une réponse calme, on voit surtout un artisan qui assume.\n\n#FicheGoogle #Serrurier")
T(V, '19:00', 'textes.instagram', "Bloqué dehors, que pense un client devant l'avis à une étoile de votre fiche Google ?\n\nSur Google Maps, avant d'appeler un serrurier, le client ouvre votre fiche Google et lit les avis, les horaires et vos réponses.\n\nUn avis à une étoile sans réponse, c'est souvent celui qu'on retient. Le même avis avec une réponse calme, qui s'excuse de l'attente et propose d'en parler, montre surtout un artisan qui assume.\n\nComment répondez-vous à un avis négatif, vous ?\n\n#FicheGoogle #Serrurier #Serrurerie #ReferencementLocal #GoogleBusinessProfile")
T(V, '19:00', 'textes.facebook', "Bloqué dehors, que pense un client devant l'avis à une étoile de votre fiche Google ?\n\nIl ouvre votre fiche Google, celle qui affiche votre note et vos avis sur Google Maps. Il tombe d'abord sur une étoile et un reproche sur une longue attente. Pas de réponse en dessous.\n\nPourtant, les avis suivants sont excellents. Mais c'est souvent le premier qu'on retient.\n\nUne réponse calme change la lecture. On s'excuse de l'attente, on propose d'en parler, on reste poli.\n\nComment répondez-vous à un avis négatif, vous ?\n\n#FicheGoogle #Serrurier #Serrurerie #ReferencementLocal")
# samedi
T(S, '06:30', 'premier_commentaire', "Chez vous, quelle date est la plus ancienne, celle de la dernière photo, de la dernière réponse à un avis ou de la dernière publication ?")
T(S, '06:30', 'textes.x', "« Ce garage existe toujours ? » Votre fiche Google répond à votre place, en 3 dates.\n\nSur cet encadré de Google Maps, regardez la dernière photo, la dernière réponse à un avis et la dernière publication.\n\nLaquelle est la plus ancienne ?\n\n#FicheGoogle #Garage")
T(S, '06:30', 'visuel.titre', "Quelle date est la plus ancienne sur votre fiche Google ?")
T(S, '06:30', 'visuel.question', "Dites en commentaire laquelle des trois est la plus ancienne chez vous.")
T(S, '12:30', 'textes.tiktok', "Sur votre fiche Google, vos photos montrent-elles encore votre travail d'aujourd'hui ?\nC'est l'encadré que voit un client qui cherche « plombier » sur Google Maps. S'il ne voit que des photos de 2021, il se demande si vous êtes toujours là.\n\n#FicheGoogle #Plombier #Plomberie")
acc_o = "Votre fiche Google peut rester active sans vous prendre de temps. C'est le principe de Proenligne."
T(S, '13:00', 'accroche', acc_o)
T(S, '13:00', 'premier_commentaire', "Une question sur le fonctionnement de Proenligne ? Posez-la ici, on vous répond. L'essai est gratuit et sans engagement.")
T(S, '13:00', 'textes.instagram', acc_o + "\n\nLa fiche Google, c'est ce que vos clients voient en premier quand ils cherchent votre métier sur Google ou Google Maps. Elle rassure quand elle montre une activité récente.\n\nProenligne s'en occupe chaque semaine.\n✅ Une photo de votre travail publiée le lundi\n✅ Un article publié le jeudi\n✅ Une réponse à chaque avis, et vous validez celles aux avis négatifs\n\nEssayez Proenligne gratuitement, sans engagement.\n\n#FicheGoogle #GoogleBusinessProfile #ReferencementLocal #Artisans #Commercants")
T(S, '13:00', 'textes.facebook', acc_o + "\n\nVotre fiche Google, c'est ce qui s'affiche quand un client cherche votre métier sur Google ou Google Maps, avec vos photos, vos avis et vos horaires. Une activité récente y rassure.\n\nChaque semaine, Proenligne s'en occupe sans vous prendre une soirée.\n✅ Une photo de votre travail publiée le lundi\n✅ Un article publié le jeudi\n✅ Une réponse à chaque avis, validée par vous quand l'avis est négatif\n\nEssayez Proenligne gratuitement, sans engagement.\n\n#FicheGoogle #GoogleBusinessProfile #ReferencementLocal #Artisans")
T(S, '13:00', 'visuel.titre', "Votre fiche Google reste active sans vous prendre une soirée")
T(S, '13:00', 'visuel.points.0', "Proenligne publie une photo chaque lundi")
T(S, '13:00', 'visuel.points.1', "Proenligne publie un article chaque jeudi")
T(S, '13:00', 'visuel.points.2', "Chaque avis reçoit une réponse, validée par vous s'il est négatif")
T(S, '13:00', 'visuel.slides.1.texte', "Proenligne publie un article sur votre fiche Google chaque jeudi.")
T(S, '19:00', 'textes.tiktok', "Il est 22 h. La cabine est rangée, mais votre nouveau soin manque sur votre fiche Google.\nC'est pourtant elle que voient les clientes qui cherchent un institut sur Google Maps. Elles ne peuvent pas réserver un soin dont elles ignorent l'existence.\n\n#FicheGoogle #Estheticienne #InstitutDeBeaute")
# dimanche
acc_d = "Pourquoi les plus beaux jardins apparaissent-ils si rarement sur la fiche Google des paysagistes ?"
T(D, '06:30', 'accroche', acc_d)
T(D, '06:30', 'textes.x', acc_d + "\n\nC'est l'encadré avec photos et avis que Google montre aux clients. Souvent, il y manque la photo d'avant. Vous pensez à la prendre ?\n\n#FicheGoogle #Paysagiste")
T(D, '06:30', 'textes.facebook', acc_d + "\n\nCherchez « paysagiste » dans votre ville. Les encadrés avec une note et des photos sont des fiches Google. Regardez les photos. On y voit souvent des pelouses, rarement des transformations.\n\nLa raison est simple. Le jour où l'on arrive sur un terrain en friche, on pense au travail, pas à la photo. Et sans la photo d'avant, celle d'après impressionne beaucoup moins.\n\nLe réflexe tient en une photo. En arrivant, avant de sortir le matériel, photographiez le terrain depuis l'endroit où vous prendrez la photo finale.\n\nAvec les deux photos côte à côte sur votre fiche Google, un client comprend tout de suite ce que vous savez faire.\n\nVous pensez à prendre la photo d'avant, ou c'est toujours trop tard ?\n\n#FicheGoogle #Paysagiste #Jardin #ReferencementLocal #GoogleBusinessProfile")
T(D, '13:00', 'textes.facebook', "Pendant que vous préparez son devis, le client compare encore les fiches Google des maçons du coin.\n\nPour un mur, une terrasse ou une extension, il ne choisit pas au hasard. Il ouvre les fiches Google, ces encadrés avec photos, note et avis que Google affiche pour chaque entreprise. Votre fiche Google en fait partie.\n\nSelon vous, qu'est-ce qui le rassure le plus ?\nA. Des photos de chantiers finis\nB. Des avis sur le respect des délais\nC. Une réponse sous chaque avis\n\nChaque piste est détaillée dans les images. Vous votez pour quelle lettre ?\n\n#FicheGoogle #Macon #Maconnerie #ReferencementLocal")
T(D, '13:00', 'visuel.slides.0.texte', "Un mur, une terrasse ou une extension terminés, en photo, aident le client à imaginer son propre chantier.")
T(D, '19:00', 'youtube_title', "Auto-école, une bonne note suffit-elle sur votre fiche Google ?")
T(D, '19:00', 'textes.tiktok', "Avant, votre fiche Google avait une bonne note et aucun signe de vie récent.\nC'est l'encadré que voient les parents qui cherchent une auto-école sur Google Maps. Après, une photo est publiée le lundi, un article le jeudi, et chaque avis reçoit une réponse.\n\n#FicheGoogle #AutoEcole #Permis")
T(D, '19:00', 'textes.instagram', "Avant, votre fiche Google avait une bonne note et aucun signe de vie récent.\n\nLa fiche Google, c'est ce que voient les parents quand ils cherchent « auto-école » sur Google Maps, avec la note, les photos et les avis.\n\nAvant, la note était bonne, mais rien n'avait été publié depuis 2021, ni photo ni article. Un parent pouvait se demander si l'école prenait encore des élèves.\n\nAprès, une photo de la voiture école paraît le lundi, un article sur le code le jeudi, et chaque avis reçoit une réponse. La note reste la même, mais on voit l'école vivre.\n\nQu'est-ce qui montre le mieux, selon vous, qu'une auto-école est active ?\n\n#FicheGoogle #AutoEcole #Permis #ReferencementLocal #GoogleBusinessProfile")

C.sort(key=lambda c: (c['date'], c['creneau_nominal']))
ancien = {}
p = os.path.join(ICI, '2026-11-02.json')
if os.path.exists(p):
    for c in json.load(open(p, encoding='utf-8'))['creneaux']:
        ancien[(c['date'], c['creneau_nominal'])] = c.get('media') or {}
for c in C:
    if ancien.get((c['date'], c['creneau_nominal'])):
        c['media'] = ancien[(c['date'], c['creneau_nominal'])]
json.dump({'lundi': '2026-11-02', 'creneaux': C}, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(C), 'entrées')
