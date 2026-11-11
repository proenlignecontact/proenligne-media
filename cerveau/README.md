# Second-brain Proenligne

Mémoire de tout ce qui est produit et publié, pour décider par les chiffres.

```
cerveau/
  productions/AAAA-MM-JJ_HHMM_<slug>.json   une fiche par production (= un créneau, tous canaux confondus)
  stats/AAAA-MM-JJ.json                      relevés bruts de l'API de stats, un fichier par relevé
  analyse.py                                 croise fiches + stats → rapport
  analyses/AAAA-MM-JJ.md                     rapport généré à chaque lot
  decisions.md                               journal des décisions prises et de leur raison
```

## Fiche de production (schéma)

```json
{
  "id": "2026-11-16_1300_test-position-plombier",
  "date_paris": "2026-11-16",
  "heure_paris": "13:15",
  "jour_semaine": "lundi",
  "creneau_nominal": "13:00",              // créneau de la grille ; heure_paris = heure réelle (± 45 min)
  "creneau": "visuel",                     // visuel | video (texte : créneau 06:30 supprimé depuis le 16/11/2026, reste dans les anciennes fiches)
  "intention": "utile",                    // utile (≥ 70 %) | preuve | offre (≤ 3 par semaine)
  "ab": null,                              // "A" | "B" pour les vidéos TikTok en test A/B, sinon null
  "premier_commentaire": "…",              // le commentaire posté avec le post (complément d'information, jamais une question depuis le 16/11/2026)
  "metier": "plombier",                    // un des 11 métiers, ou "general"
  "angle": "peur-de-perdre",               // peur-de-perdre | gain-de-temps | preuve
  "format": "test",                        // texte : conseil | test | constat | idee-recue | preuve ; visuel : avant-apres ; video : recherche | fiche | avis | journee | libre
  "ton": "question",                       // question | constat | scene | avant-apres | contre-intuitif | pendant-que | replique
  "symptome": "photos-anciennes",          // id de symptôme du skill (photos-anciennes, aucune-publication, avis-sans-reponse, horaires-faux…) ou null
  "offre": "essai",                        // essai (essai gratuit, sans prix ; règle depuis le 31/10/2026) | aucune — les fiches de reprise en "essai" affichaient encore 14,99 €
  "accroche": "Tapez votre métier + votre ville sur Google. Vous êtes où ?",
  "promesse": "photo lundi, publication jeudi, réponse aux avis",
  "hashtags": ["#FicheGoogle", "#Plombier"],
  "media": {"type": "aucun", "fichiers": [], "postiz": []},
  "publications": [
    {"canal": "x", "postiz_id": "…", "caracteres": 212, "texte": "…"},
    {"canal": "facebook", "postiz_id": "…", "caracteres": 640, "texte": "…"}
  ],
  "source": "tache-hebdo",                 // tache-hebdo | manuel | reprise
  "notes": ""
}
```

Règles :
- Une fiche est créée **au moment de la programmation**, jamais modifiée ensuite, sauf `notes`.
- Les statistiques ne vont **pas** dans la fiche : elles vivent dans `stats/`, reliées par `postiz_id`. Les relevés s'accumulent, l'analyse prend le plus récent par post.
- Les valeurs de `metier`, `angle`, `format`, `ton`, `offre` restent dans un vocabulaire fermé (ci-dessus et dans `suivi/regles-editoriales.md`) : c'est ce qui rend les comparaisons possibles.

## Relevé de stats (format attendu dans `stats/`)

```json
{"releve_le": "2026-11-08T08:00:00Z",
 "posts": [{"postiz_id": "…", "canal": "instagram", "vues": 812, "likes": 31, "commentaires": 4,
            "partages": 2, "enregistrements": 3, "clics": 5}]}
```
Champs absents = inconnus (pas zéro). Le format exact sera adapté à l'API de stats une fois disponible (voir `suivi/api-stats.md`).

## Outils

| Script | Rôle |
|---|---|
| `outils/heure_utc.py <lundi> --varier` | Grille des 14 créneaux (13:00 et 19:00) avec heures réelles tirées à ± 45 min et heure UTC exacte (heure d'été gérée). |
| `outils/visuel.py <brief> <sortie>` / `--carrousel` | Image 1080×1350 (gabarits avant-apres, conseil, question) ou carrousel de 3 à 5 slides. |
| `cerveau/regles_texte.py` | Règles de texte communes (n°1 « fiche Google », n°2 aucun prix, n°3 aucune statistique client, phrases complètes) et extraction de tous les éléments textuels d'un plan ou d'un brief. Importé par le vérificateur, la relecture, `visuel.py` et le skill vidéo adapté. |
| `cerveau/verifier.py suivi/plan/<lundi>.json [--briefs <dossier>] [--relecture]` | **Avant programmation** : règles n°1-2-3 sur chaque élément (textes, accroche, titres, 1er commentaire, briefs visuels et vidéo), vocabulaire fermé, canaux et heures, longueurs, mix, rotation, ressemblance des accroches, quiz sans réponse cochée, explication « fiche Google » variée. `--relecture` exige une relecture validée et à jour ; `--sans-medias` saute la présence des médias (avant rendu). Code 1 tant que ce n'est pas « plan OK ». |
| `cerveau/relecture.py extraire\|enregistrer\|controler\|etat <lundi> --briefs <dossier>` | **Règle n°4, incrémentale** : `extraire --tout` sort tous les éléments textuels (`suivi/relecture/<lundi>-textes.json`) pour un agent relecteur indépendant (consigne : `cerveau/relecture-consigne.md`) ; `enregistrer` inscrit ses « ok » dans le registre `suivi/relecture/<lundi>-valides.json` (clé stable + empreinte du texte) et archive ses verdicts ; ensuite `extraire` ne renvoie que les éléments nouveaux, modifiés ou refusés (plus leur post en contexte) ; `controler` répond « relecture OK » quand chaque élément a un « ok » à jour. |
| `cerveau/fiche.py <plan.json> <ids.json>` | **Après programmation** : écrit les fiches à partir du plan et des postiz_id. Une fiche déjà présente pour le même créneau est complétée, jamais dupliquée. |
| `cerveau/convertir_stats.py [--tout]` | Relevé brut → relevé converti. **Retire nos propres commentaires** (premier commentaire de chaque post + `cerveau/commentaires-maison.json`) : `commentaires` = commentaires venus de l'extérieur, `commentaires_bruts` = valeur de la plateforme. `--tout` reconvertit tout l'historique. |
| `cerveau/amplifier.py` | Posts qui décollent : > 2 × la médiane du canal **et ≥ 50 vues** (`--audience-min`). |
| `cerveau/analyse.py --sortie cerveau/analyses/<date>.md` | Rapport : comptes, **conversion** (abonnés pour 1 000 vues), médianes par canal, verdicts par dimension (indice d'engagement et **indice vues**). |

Le plan (`suivi/plan/<lundi>.json`) est la source unique du lot : le vérificateur, la programmation et les fiches s'appuient dessus. Format en tête de `cerveau/verifier.py`.

## Décider

`python3 cerveau/analyse.py` produit, pour chaque dimension (canal, créneau, intention, angle, format, métier, ton, symptôme, jour, heure réelle, A/B) :
le nombre de publications mesurées, l'audience médiane (vues, ou portée en secours), le taux d'engagement pondéré
((likes + 1,5 × enregistrements + 2 × commentaires + 3 × partages) / audience — partages et commentaires sont les signaux de viralité) et un **indice normalisé par canal** (1,0 = médiane du canal).
Les verdicts se lisent sur l'indice : ≥ 1,2 « à renforcer », ≤ 0,8 « à réduire ».
Les commentaires comptés sont ceux venus de l'extérieur (nos premiers commentaires sont retirés à la conversion, décision du 11/11/2026).
L'**indice vues** (audience rapportée à la médiane du canal) sert de verdict tant que l'engagement médian est nul : le rapport le signale en tête.

Canaux : x, facebook, instagram, tiktok, youtube, **linkedin** (page Proenligne, depuis le 02/11/2026, carrousel de 13:00 le mardi et le jeudi depuis le 16/11/2026 ; plateforme Postiz `linkedin-page` notée `linkedin`). Depuis le 16/11/2026, X et Facebook ne reçoivent plus que des vidéos. LinkedIn a une audience de décideurs : ne pas transposer telles quelles ses conclusions aux autres canaux, et inversement — d'où l'indice normalisé par canal.

Ce que les stats ne voient pas : X ne renvoie rien par post ; il se pilote sur la section « Comptes ». Les clics sur le lien de bio
ne se voient que dans l'outil d'analyse du site (liens de bio marqués `utm_source=<réseau>&utm_medium=bio`).

Règles de décision appliquées par la tâche hebdomadaire :
- Une valeur ne compte que si elle a **au moins 5 publications mesurées** (relevé ≥ 48 h après publication).
- **Démarrage** : tant que moins de 30 publications sont mesurées au total, exploration à **50 / 50** (le rapport le signale).
- Ensuite **70 / 30** : 70 % des créneaux sur ce qui marche (indice > 1), 30 % en exploration (valeurs peu testées), pour ne pas s'enfermer.
- Les dimensions larges (canal, créneau, angle, jour) atteignent le seuil en 2 à 3 semaines ; métier en un mois ; ton et symptôme beaucoup plus tard. Ne pas forcer une décision sur une dimension qui n'a pas le seuil.
- **Amplification** : `suivi/amplifier.json` (écrit par la tâche quotidienne) liste les posts qui ont dépassé 2 × la médiane de leur canal et 50 vues. La tâche hebdomadaire reprend ces sujets en priorité et le note dans `decisions.md`.
- **A/B** : la dimension `ab` compare, sur TikTok, l'accroche A (grille) et l'accroche B (surlendemain 12:30). Une variante gagnante 3 semaines de suite devient la règle d'ouverture par défaut.
- **Conversion** : le ratio abonnés TikTok pour 1 000 vues (section « Conversion ») est noté chaque semaine dans `decisions.md` avec son évolution.
- Chaque décision est écrite dans `decisions.md` avec le chiffre qui la justifie.
