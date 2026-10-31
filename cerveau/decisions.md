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
