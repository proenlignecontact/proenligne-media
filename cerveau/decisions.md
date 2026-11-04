# Journal des décisions

Chaque lot hebdomadaire ajoute ici ses décisions, avec le chiffre qui les justifie.

## 2026-10-31 — Mise en place

- Grille : 06:30 texte (X + Facebook), 13:00 visuel (Instagram + Facebook), 19:00 vidéo (TikTok + Instagram + YouTube).
- Règle n°1 : toujours écrire « fiche Google » et expliquer ce que c'est. Le public ne comprend pas « la fiche » seul.
- TikTok en DIRECT_POST pour les nouveaux posts (le mode UPLOAD ne publie pas).
- Pas encore de statistiques : rotation équilibrée des métiers, formats et offres.

## 2026-10-31 — Offre

- Appel à l'action unique : « Essayez gratuitement », sans aucun prix (demande de l'équipe). Plus de 14,99 €, d'offre annuelle ni de « centimes par jour ».
- Vidéos : le skill est utilisé via une copie adaptée (`outils/adapter-skill.py`) dont la scène Offre affiche « Essayez gratuitement · Sans engagement » et dont les contrôles refusent tout montant.
- Pour l'analyse : les 4 productions de reprise affichaient encore un prix ; à garder en tête en comparant avec les suivantes.

## 2026-10-31 — Lot de la semaine du 2 au 8 novembre

- **Pas de pondération 70/30** : 0 publication mesurée (analyse du 31/10 : 19 publications non mesurées ou trop récentes ; seuil = 5 par valeur). Rotation équilibrée.
- **Angles rééquilibrés** (exploration) : les 4 productions passées étaient toutes « peur-de-perdre ». Cette semaine : peur-de-perdre 9, gain-de-temps 7, preuve 5 sur 21 créneaux.
- **Les 11 métiers** sont couverts (électricien en texte seulement, déjà en vidéo le 31/10) ; vidéos sur 7 métiers jamais traités en vidéo (chauffagiste, garage, auto-école, coiffeur, serrurier, esthéticienne, maçon) pour ne pas répéter plombier/électricien.
- **Formats vidéo** : 3 « fiche », 2 « avis », 1 « recherche », 1 « journée », tirés par le skill (aucun « libre » cette semaine, pour comparer avec les 3 « libre » passés).
- **« mois » banni des textes publiés** : la preuve s'écrit « en un semestre » dans les textes (la vidéo et les visuels gardent « 6 mois », chiffre autorisé).
- **Comptes** (relevé du 31/10) : TikTok 87 vues compte, 0 abonné ; Facebook 40 vues de médias, 5 impressions ; YouTube 1 like. Trop faible pour orienter les plateformes.
- **Postiz** : les pièces jointes sont refusées (« URL must contain the domain: uploads.postiz.com »). Seuls les textes de 06:30 sont programmés ; les visuels et vidéos attendent dans `suivi/a-programmer/2026-11-02.json`.
- **Résolu le 31/10 à 21h45** : le refus venait du connecteur Postiz officiel (bug #2278). Programmation via le connecteur personnalisé « postiz » (outils `mcp__postiz__*`) ; les 35 posts avec médias sont programmés et la tâche hebdomadaire a été recréée avec ce connecteur.

## 2026-10-31 — Corrections après audit

- **Anti-doublon** : verrou `suivi/verrou-<lundi>.json` posé au début de chaque exécution (une seconde exécution simultanée s'arrête) ; fiches écrites par `cerveau/fiche.py`, qui complète une fiche existante au lieu d'en créer une seconde.
- **Contrôle avant programmation** : `cerveau/verifier.py` sur le plan (règles, vocabulaire, rotation, ressemblance des accroches à 40 %). Motif : les 3 posts « preuve » de la semaine du 2/11 partageaient 57 à 67 % de leurs mots.
- **Analyse** : portée en secours quand il n'y a pas de vues ; verdicts normalisés par canal ; section « Comptes » pour piloter X et Facebook texte ; exploration 50 / 50 tant que moins de 30 publications mesurées.
- **Heure UTC calculée** par `outils/heure_utc.py` (plus de décalage écrit en dur dans le prompt).
- **Tâche de secours** le dimanche à 16h04 : même consigne ; ne fait que les stats si la semaine est déjà pleine.
- **Anciens posts à prix** (1/11 19:00 et 2/11 09:00–09:20) supprimés : 14,99 €/mois, pas de « fiche Google » en accroche, TikTok en UPLOAD, et 4 publications Facebook le lundi.

## 2026-11-01 — Exécution de secours (dimanche 16 h) : semaine du 2/11 déjà pleine

- **Aucune programmation** : les 49 posts de la grille (7 × (2 + 2 + 3)) sont en file dans Postiz, tous en QUEUE, aux bonnes heures UTC (05:30 / 12:00 / 18:00). Rien à ajouter, rien modifié.
- **Pas de pondération 70 / 30** : 1 publication mesurée (seuil 30 pour sortir de l'exploration 50 / 50 ; seuil 5 par valeur) ; 57 trop récentes. Le plan de la semaine, déjà programmé le 31/10, n'est pas touché.
- **Premier signal TikTok** (relevé du 1/11, non encore « mesuré » car < 48 h) : la vidéo électricien du 31/10 19:00 en DIRECT_POST affiche 774 vues et 1 like en moins de 24 h, contre 2 vues sur Instagram, 1 sur YouTube et 0 sur Facebook pour la même production. Le mode DIRECT_POST publie bien (le post du 28/10 en UPLOAD n'a toujours pas d'identifiant TikTok). À confirmer avec les 7 vidéos de la semaine avant toute décision sur les canaux.
- **Comptes** : TikTok 861 vues de compte (+774), 0 abonné ; Facebook 5 impressions, 40 vues de médias (inchangé) ; YouTube 1 like. Toujours trop faible pour piloter X et Facebook texte.

## 2026-11-01 — Ajout de la page LinkedIn Proenligne

- **Où** : créneau 13:00 (visuel), **du lundi au vendredi seulement** → 5 posts LinkedIn par semaine, 54 posts au total.
- **Pourquoi ce créneau** : la mi-journée en semaine est l'une des meilleures plages LinkedIn ; l'engagement chute après 17h et le week-end (sources : guides 2026 AdCreate, Publer). 5 posts par semaine est la fréquence optimale indiquée pour une page de PME (minimum 3, maximum utile 1 par jour). 06:30 et 19:00 écartés.
- **Contenu** : même visuel que Instagram/Facebook, texte réécrit pour des gérants d'entreprise (ton pro, accroche « fiche Google » dans les ~200 premiers caractères visibles avant « voir plus », 700–1 300 caractères, ≤ 5 hashtags, pas de lien externe, ≤ 3 ✅). Contrôlé par `cerveau/verifier.py`.
- **Semaine du 2/11** : 5 posts LinkedIn ajoutés à la main sur les créneaux de 13:00 du lundi au vendredi (visuels existants), fiches complétées.
- **Stats** : la page LinkedIn est dans le relevé de l'API depuis le 01/11 16h30 (compte : vues de page, clics, partages, engagement, commentaires, abonnés). Stats par post attendues dès les premières publications.

## 2026-11-01 — Contenu à engagement (mise en place « viralité »)

- **Mix éditorial 70 / 20 / 10** (utile / preuve / offre) : au moins 13 créneaux utiles sur 21, au plus 3 posts offre ; les 3 ✅ et « Essayez Proenligne gratuitement » réservés aux posts offre. Motif : tous les posts de la semaine du 2/11 étaient des posts d'offre (21/21), ce qui limite partages et commentaires.
- **Grille portée à 61 posts** : Facebook reçoit la vidéo verticale à 19:00 (Reels), le créneau 13:00 devient un carrousel (3–5 slides, `outils/visuel.py --carrousel`), LinkedIn page du lundi au vendredi.
- **Premier commentaire** systématique (question ou précision, ≤ 300 caractères) ; **heures variées** ± 45 min par `outils/heure_utc.py --varier` ; **A/B TikTok** : 2 vidéos par semaine (mardi, jeudi) avec variante B en TikTok seul à 12:30 deux jours plus tard, dimension `ab` dans l'analyse.
- **Engagement pondéré** dans `cerveau/analyse.py` : likes × 1, enregistrements × 1,5, commentaires × 2, partages × 3 ; nouvelles dimensions `intention`, `jour_semaine`, `heure_paris`, `ab`.
- **Amplification** : `cerveau/amplifier.py` (tâche quotidienne 08:23) inscrit dans `suivi/amplifier.json` toute publication ≥ 2 × la médiane de son canal (≥ 5 posts mesurés sur 14 jours) ; la tâche hebdo doit reprendre ces sujets.
- **3 ambiances sonores** (`PUB_AMBIANCE=0|1|2`) en alternance, jamais la même deux jours de suite.
- **Vérificateur étendu** : mix, premier commentaire, rotation des formats texte et des gabarits visuels, ton ≤ 5 par semaine, ressemblance des accroches contre toutes les fiches, entrées A/B acceptées.
- **Semaine du 2/11 corrigée** : 7 posts YouTube recréés en vertical (Shorts) avec premier commentaire ; 7 Reels Facebook ajoutés à 19:00.
- **Non retenu** (choix de Maxime) : séries récurrentes avec un personnage fictif ; LinkedIn depuis un profil personnel. **Impossible via Postiz** : réponse aux commentaires, sons tendance TikTok (compte Business requis).

## 2026-11-01 17 h — Semaine du 2/11 remise à zéro pour tester le nouveau pipeline

- Les 61 posts programmés à la main (31/10 et 1/11) ont été supprimés de Postiz ; fiches, plan, médias et rapport de la semaine retirés du dépôt (jamais publiés, donc sans valeur statistique).
- La tâche hebdomadaire est déclenchée manuellement pour produire la semaine entière selon la nouvelle consigne (mix 70/20/10, carrousels, premiers commentaires, A/B, heures variées). Objectif : contrôler la conformité des posts générés sans intervention humaine.

## 2026-11-01 (dimanche, tâche hebdomadaire) — Semaine du 2 au 8 novembre, pipeline complet

- **Pas de pondération 70 / 30, exploration 50 / 50** : 1 publication mesurée au total (analyse du 01/11 ; seuil 30 pour sortir du démarrage, 5 par valeur). Aucune dimension n'atteint le seuil : aucun verdict appliqué.
- **Amplification** : `suivi/amplifier.json` vide (aucun post ≥ 2 × la médiane, faute de 5 posts mesurés par canal) : rien à reprendre.
- **Mix** : 15 utiles, 4 preuves, 2 offres sur 21 créneaux (≥ 13 / 2 à 5 / ≤ 3). Motif : semaine précédente 21/21 en offre, à corriger pour mesurer l'effet du contenu utile.
- **Vidéos sur 7 métiers** : paysagiste et boulangerie (jamais en vidéo), garage, plombier, coiffeur, serrurier, auto-école avec des symptômes nouveaux (service-invisible, réponses-tardives, pas-de-nouveauté, horaires-faux, concurrent-plus-riche). Mises en scène : 2 fiche, 2 avis, 2 recherche, 1 journée.
- **Angles** : gain-de-temps 9, peur-de-perdre 8, preuve 4 — rééquilibrage (les 3 fiches passées étaient toutes peur-de-perdre).
- **A/B TikTok** : garage (A mardi 19:00 « Pendant que vous êtes sous une voiture… » / B jeudi 12:30 « 5 étoiles sur votre fiche Google… ») et plombier (A jeudi « Il est 22 h… » / B samedi 12:30 « Vous trouvez les fuites sans casser… ») : ouverture « pendant que » / « scène » contre ouverture « constat chiffré ».
- **TikTok surveillé en priorité** : la vidéo du 31/10 en DIRECT_POST a fait 774 vues en < 24 h contre 0 à 2 ailleurs (non encore « mesurée »). Les 9 TikTok de la semaine sont en DIRECT_POST pour confirmer.
- **Outil** : `outils/visuel.py` n'affiche plus « Essayez gratuitement » en pied de la dernière slide d'un carrousel sauf si `cta = offre` (règle : jamais d'offre dans le visuel d'un contenu utile).

## 2026-11-01 17 h 30 (Paris) — 2e exécution (lancée à la main) : semaine du 2/11 déjà pleine

- **Aucune programmation, aucun média** : les 63 posts (61 de la grille + 2 variantes B) programmés une demi-heure plus tôt par l'exécution précédente sont tous en file dans Postiz et correspondent exactement à `suivi/plan/2026-11-02-ids.json`. Rien supprimé ni modifié.
- **Stats** : relevé frais reçu (action « success »). Toujours 1 publication mesurée → exploration 50 / 50, aucune décision chiffrée. À noter : la vidéo TikTok du 31/10 (774 vues la veille) renvoie désormais « Aucune statistique renvoyée par la plateforme » ; à surveiller au prochain relevé.

## 2026-11-01 18 h — Relecture de la 1re semaine générée sans intervention : règles n°3 et n°4

- **Constat** (lecture intégrale des 63 posts, 7 briefs vidéo, 14 briefs visuels) : la mécanique tient (63 posts en 23 min, mix 15/4/2, premiers commentaires, heures variées, LinkedIn en semaine, A/B, verrou efficace face à une 2e exécution), mais des textes passent le vérificateur sans avoir de sens pour un lecteur (« Nouveauté tue sur votre fiche Google, clients partis », « Des semaines sans merci sur votre fiche Google », « Réponse tardive sur votre fiche Google, élève perdu »), du jargon en accroche (« les fuites sans casser »), des contradictions texte / visuel (quiz dont la 1re slide coche la réponse alors que le texte dit « réponse dans le carrousel » ; « il voit 3 choses » vs une seule bonne réponse ; « 3 photos » pour 3 conseils), la même phrase d'explication copiée 42 fois, « Weber » dans 8 briefs sur 9, et des résultats chiffrés de clients (×3 appels, 100 appels, semestre) dans 5 créneaux.
- **Règle n°3 (Maxime)** : aucune statistique ni résultat chiffré de nos clients, nulle part. `preuve` = démonstration. Angle « preuve » et chiffres ×3 / 100 / 6 retirés du skill vidéo adapté ; regex STATS dans `cerveau/regles_texte.py`, appliquée par le vérificateur, `visuel.py` et `brief.py valider`.
- **Règle n°4** : relecture « lecteur humain » de chaque élément textuel par un agent indépendant avant tout rendu (`cerveau/relecture.py`, `cerveau/relecture-consigne.md`), empreinte des textes contrôlée, `verifier.py --relecture` bloquant. Ordre de la tâche : plan → briefs (sans rendu) → relecture → rendu → programmation.
- **Vérificateur** : règles n°1-2-3 sur tous les éléments (dont briefs vidéo avec `--briefs`), phrases complètes (sujet + verbe) pour accroches et `suite`, quiz sans `bonne`, titre-question, explication variée (≤ 4 copies), noms fictifs ≤ 3 par semaine, angle « preuve » refusé.
- **Visuels** : plus de réponse pré-cochée, typographie française (pas de « ? » orphelin), blocs plus grands pour moins de vide.
- **Règle n°5 (Maxime, 1/11 18 h)** : aucun « : » dans un texte publié, ça ne fait pas naturel. 147 occurrences dans la semaine générée. Contrôle mécanique dans `regles_texte.problemes`, critère n°7 de la relecture, prompts mis à jour.
- **Relecture test sur la semaine du 2/11** : 426 éléments, 75 refus (stats clients, classement Google affirmé, télégraphique, contradictions texte/visuel, Weber ×7). Verdicts conservés dans `suivi/relecture/2026-11-02.json`.

## 2026-11-01 18 h 15 — Semaine du 2/11 remise à zéro une 2e fois, relance avec les 5 règles et la relecture

- Les 63 posts du 1er essai supprimés de Postiz ; fiches, plan, médias, briefs et rapport retirés. Les verdicts de la relecture test sont archivés dans `suivi/relecture/archives/2026-11-02-essai1*.json` (75 refus sur 426) pour comparaison avec le 2e essai.

## 2026-11-01 soir — Semaine du 2/11, essai 2 (tâche hebdomadaire relancée à la main)

- **Exploration 50 / 50, aucune décision chiffrée** : relevé frais du 01/11 (action « success »), 1 seule publication mesurée (Instagram, 0 vue) sur 3 fiches ; seuil de 30 non atteint, aucune dimension à 5 publications.
- **Amplification** : `suivi/amplifier.json` vide, rien à reprendre.
- **Mix** : 15 utiles, 4 preuves (démonstrations sans chiffre), 2 offres. 11 métiers. Tons 3 fois chacun (question 4, contre-intuitif 2).
- **Vidéos** : mises en scène fiche, avis et journée seulement ; la mise en scène « recherche » est écartée parce qu'elle montre la fiche « remonter N° 1 », une promesse de classement invérifiable.
- **A/B TikTok** : garage (A mardi « « Ils ne lisent pas leurs avis ? » », réplique / B jeudi 12:30, constat) et plombier (A jeudi « Pendant que vous réparez une fuite… » / B samedi 12:30, question).
- **Historique des pubs** : les 7 entrées du 01/11 issues de l'essai 1 (vidéos jamais publiées) sont gardées dans `historique-pubs.json` par prudence ; elles bloquent des formulations proches.
- **Relecture** : 4 passes (82, 26, 21 puis 3 refus). Relecteurs neufs en parallèle par tranche de jours ; à partir de la passe 3, les verdicts « ok » des créneaux sans changement ni refus sont repris (fichier `part0`). Arrêt à la règle des 4 passes avec 3 éléments encore refusés (corrigés depuis dans les sources) : rien n'a été rendu ni programmé.

## 2026-11-01 (dimanche soir, exécution de secours) — Semaine du 2/11 rendue et programmée

- **Reprise à l'étape 7** : la tâche du matin avait laissé plan, briefs et relecture validés (433/433) mais rien de rendu ni programmé ; Postiz était vide pour la semaine. L'exécution de secours a rendu les 9 vidéos, 7 images et 7 carrousels, puis programmé les **63 posts** (tous en QUEUE), sans toucher au plan ni aux briefs validés (2 corrections de forme dans les briefs visuels, 1 élément relu à nouveau, 0 refus).
- **Exploration 50 / 50 maintenue, aucune décision chiffrée** : relevé du 01/11 (16 h 51 UTC), 1 publication mesurée sur 3 fiches, 8 trop récentes ; seuils (30 au total, 5 par valeur) non atteints. Rien dans `suivi/amplifier.json`.
- **Mix** : 15 utiles / 4 preuves / 2 offres ; A/B TikTok garage (mardi → jeudi 12:30) et plombier (jeudi → samedi 12:30) ; ambiances 0/1/2 en alternance.
- **À surveiller au prochain relevé** : les 9 TikTok en DIRECT_POST et les 5 premiers posts LinkedIn page (stats par post attendues) ; Facebook texte de 06:30 toujours sans stat par post.

## 2026-11-04 — TikTok en UPLOAD (provisoire)

- L'application TikTok n'est pas validée : la publication directe est refusée (« App not approved for public posting », post du 2/11 19:29). Tous les posts TikTok passent en `content_posting_method: UPLOAD` (téléversement dans la boîte de réception TikTok, publication finalisée à la main) jusqu'à la validation de l'application.
- Conséquence pour l'analyse : un TikTok en UPLOAD n'a pas d'identifiant tant qu'il n'est pas publié à la main ; ne pas le compter comme « publié sans audience ».

## 2026-11-04 (mercredi soir) — Semaine du 9/11, tâche hebdomadaire

- **Exploration 50 / 50 maintenue, aucune décision chiffrée** : relevé frais du 04/11 (action « success »), 11 publications mesurées sur 26 fiches (seuil de 30 non atteint) ; aucune valeur à 5 publications mesurées hors « video » (8, indice 1,12) et « utile » (6, indice 1,17), tous deux « dans la moyenne ». Le créneau vidéo concentre l'audience (TikTok 778 vues sur 1 post mesuré, 2 138 vues cumulées sur le compte) : rien ne justifie encore de déplacer la grille.
- **Amplification** : `suivi/amplifier.json` vide, rien à reprendre.
- **Moteurs vidéo** : aucune vidéo swipe / cinétique / plan-séquence encore mesurée (les premières partent le 5/11) ; rotation du tirage suivie telle quelle.
- **Mix** : 16 utiles, 3 preuves (garage, auto-école, serrurier, démonstrations sans chiffre), 2 offres (institut mercredi, garage samedi). 11 métiers, chaque ton 3 fois.
- **Actualité** : le jour férié du mercredi 11 novembre sert de sujet utile (boulangerie, horaires exceptionnels, lundi 13:00).
- **A/B TikTok** : maçon swipe (A mardi, B jeudi 12:30) et plombier plan-séquence (A jeudi, B samedi 12:30).
- **Outil** : `outils/pub-video.py` cherche aussi les skills dans `~/.claude/skills/**` (emplacement des skills synchronisés) ; deux textes fixes adaptés : « Vos appels aujourd'hui : N » (deux-points, swipe « Plus d'appels ») → « Appels aujourd'hui · N », et « Après dix heures de chantier. » (cinétique « Du temps libre », faux pour une coiffeuse) → « Après une longue journée de travail. ».
- **À surveiller** : le décor plan-séquence « Plus de clients » montre la carte « Votre entreprise » remonter au N° 1 avec « Les clients du coin vous trouvent, vous. » (texte fixe du skill), proche d'une promesse de classement ; deux vidéos de la semaine l'utilisent (lundi, jeudi). À arbitrer par Maxime (texte fixe à adapter ou combinaison à écarter).
