# API de statistiques

Statut : **disponible** (format de réponse à découvrir au premier appel réussi, voir plus bas).

## Appel
```
GET https://postiz-stats.proenligne.fr/report?days=30
```
- `days` : nombre de jours couverts par le rapport (30 par défaut ; la tâche hebdomadaire peut passer 60 pour couvrir les posts plus anciens).

## Authentification
Le jeton Bearer est stocké comme **secret réseau** (Network secret) sur l'environnement cloud, pour l'hôte `postiz-stats.proenligne.fr`.
Le proxy d'Anthropic ajoute `Authorization: Bearer …` à la requête : appeler **sans en-tête d'authentification** :
```
curl -sS "https://postiz-stats.proenligne.fr/report?days=30"
```
Le jeton n'est jamais visible dans la session et ne doit JAMAIS apparaître dans ce dépôt public.
- 403 au CONNECT (avant même d'atteindre l'API) : le secret réseau n'est pas déclaré pour cet hôte dans l'environnement de la session.
- 401 / 403 renvoyé par l'API : le jeton du secret est absent, expiré ou invalide.

## Format de réponse et conversion
À compléter après le premier appel réussi. En attendant, la tâche :
1. enregistre la réponse brute dans `cerveau/stats/brut/<date>.json` ;
2. en déduit la correspondance avec le format de `cerveau/stats/` (postiz_id, canal, vues, likes, commentaires, partages, enregistrements, clics ; champs inconnus omis, jamais mis à zéro) ;
3. écrit le relevé converti dans `cerveau/stats/<date>.json` et décrit la correspondance retenue ici, dans cette section.
