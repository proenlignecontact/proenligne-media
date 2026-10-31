# API de statistiques

Statut : **disponible** (format de réponse à découvrir au premier appel réussi, voir plus bas).

## Appel
```
GET https://postiz-stats.proenligne.fr/report?days=30
```
- `days` : nombre de jours couverts par le rapport (30 par défaut ; la tâche hebdomadaire peut passer 60 pour couvrir les posts plus anciens).

## Relevé automatique (GitHub Actions)
La session Claude n'appelle **pas** l'API elle-même. L'action `.github/workflows/releve-stats.yml` l'appelle chaque jour vers 6h17 (Paris) avec le jeton stocké dans le secret GitHub `STATS_TOKEN`, et enregistre la réponse brute dans `cerveau/stats/brut/AAAA-MM-JJ.json` (60 jours couverts).
- Lancement manuel : onglet Actions du dépôt > « Relevé des stats » > Run workflow.
- Le jeton n'est jamais dans le dépôt ni dans les journaux. Ne jamais l'écrire ici.
- Si le dernier fichier de `cerveau/stats/brut/` a plus de 3 jours : l'action échoue (voir l'onglet Actions sur GitHub) ; le signaler dans le rapport.

## Format de réponse et conversion
À compléter après le premier relevé réussi. En attendant, la tâche :
1. lit le relevé brut le plus récent de `cerveau/stats/brut/` ;
2. en déduit la correspondance avec le format de `cerveau/stats/` (postiz_id, canal, vues, likes, commentaires, partages, enregistrements, clics ; champs inconnus omis, jamais mis à zéro) ;
3. écrit le relevé converti dans `cerveau/stats/<date>.json` et décrit la correspondance retenue ici, dans cette section.
