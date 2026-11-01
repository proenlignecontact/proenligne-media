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
  "id": "2026-11-02_0630_test-position-plombier",
  "date_paris": "2026-11-02",
  "heure_paris": "06:30",
  "jour_semaine": "lundi",
  "creneau": "texte",                      // texte | visuel | video
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
| `outils/heure_utc.py <lundi>` | Grille des 21 créneaux de la semaine avec l'heure UTC exacte (heure d'été gérée). |
| `cerveau/verifier.py suivi/plan/<lundi>.json` | **Avant programmation** : règles « fiche Google » et « gratuit sans prix », vocabulaire fermé, canaux et heures de la grille, longueurs X / titres, rotation des métiers et formats, ressemblance des accroches (≥ 40 % de mots communs) avec le plan et avec toutes les fiches existantes. Code 1 tant que ce n'est pas « plan OK ». |
| `cerveau/fiche.py <plan.json> <ids.json>` | **Après programmation** : écrit les fiches à partir du plan et des postiz_id. Une fiche déjà présente pour le même créneau est complétée, jamais dupliquée. |
| `cerveau/convertir_stats.py` | Relevé brut → relevé converti. |
| `cerveau/analyse.py --sortie cerveau/analyses/<date>.md` | Rapport : comptes, médianes par canal, verdicts par dimension. |

Le plan (`suivi/plan/<lundi>.json`) est la source unique du lot : le vérificateur, la programmation et les fiches s'appuient dessus. Format en tête de `cerveau/verifier.py`.

## Décider

`python3 cerveau/analyse.py` produit, pour chaque dimension (canal, créneau, angle, format, métier, ton, symptôme, jour) :
le nombre de publications mesurées, l'audience médiane (vues, ou portée en secours), le taux d'engagement moyen
((likes + commentaires + partages + enregistrements) / audience) et un **indice normalisé par canal** (1,0 = médiane du canal).
Les verdicts se lisent sur l'indice : ≥ 1,2 « à renforcer », ≤ 0,8 « à réduire ».

Canaux : x, facebook, instagram, tiktok, youtube, **linkedin** (page Proenligne, depuis le 02/11/2026, créneau 13:00 en semaine ; plateforme Postiz `linkedin-page` notée `linkedin`). LinkedIn a une audience de décideurs : ne pas transposer telles quelles ses conclusions aux autres canaux, et inversement — d'où l'indice normalisé par canal.

Ce que les stats ne voient pas : X et Facebook texte ne renvoient rien par post. Le créneau texte de 06:30 se pilote donc
sur la section « Comptes » (abonnés, impressions de page) et sur le bon sens éditorial, pas sur un taux par post.

Règles de décision appliquées par la tâche hebdomadaire :
- Une valeur ne compte que si elle a **au moins 5 publications mesurées** (relevé ≥ 48 h après publication).
- **Démarrage** : tant que moins de 30 publications sont mesurées au total, exploration à **50 / 50** (le rapport le signale).
- Ensuite **70 / 30** : 70 % des créneaux sur ce qui marche (indice > 1), 30 % en exploration (valeurs peu testées), pour ne pas s'enfermer.
- Les dimensions larges (canal, créneau, angle, jour) atteignent le seuil en 2 à 3 semaines ; métier en un mois ; ton et symptôme beaucoup plus tard. Ne pas forcer une décision sur une dimension qui n'a pas le seuil.
- Chaque décision est écrite dans `decisions.md` avec le chiffre qui la justifie.
