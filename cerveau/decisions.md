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
