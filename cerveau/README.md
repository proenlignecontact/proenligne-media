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
  "offre": "essai",                        // essai | audit | unEuro | annuel | aucune
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

## Décider

`python3 cerveau/analyse.py` produit, pour chaque dimension (métier, angle, format, ton, offre, créneau, jour, heure, canal) :
le nombre de posts mesurés, les vues médianes et le taux d'engagement moyen ((likes + commentaires + partages + enregistrements) / vues).

Règles de décision appliquées par la tâche hebdomadaire :
- Une valeur ne compte que si elle a **au moins 5 posts mesurés** et des stats relevées **au moins 48 h** après publication.
- **70 / 30** : 70 % des créneaux sur ce qui marche (valeurs au-dessus de la médiane), 30 % en exploration (valeurs peu testées ou nouvelles), pour ne pas s'enfermer.
- Chaque décision est écrite dans `decisions.md` avec le chiffre qui la justifie.
