# API de statistiques

Statut : **disponible**. Premier relevé réussi le 31/10/2026.

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
Réponse : `{generatedAt, days, channels[], posts[]}`.
- `channels[]` : `{id, platform, stats: {available, metrics: [{metric, latest, sum, percentageChange}]}}` — chiffres du compte.
- `posts[]` : `{id (= postiz_id), platform, integrationId, publishDate, state, url, content, stats: {available, reason?, metrics[]}}`.

Conversion : `python3 cerveau/convertir_stats.py` (relevé brut le plus récent → `cerveau/stats/<même date>.json`). La correspondance des métriques est décrite en tête du script (valeur `sum`).

Constat au 31/10/2026 :
- Instagram, YouTube et Facebook (vidéo) renvoient des stats par post.
- X : aucune stat par post (« Aucune statistique renvoyée par la plateforme »).
- TikTok : les posts envoyés en mode UPLOAD n'ont pas d'identifiant TikTok (« Postiz ne connaît pas l'ID du post ») — ils n'ont pas été publiés. Les posts en DIRECT_POST devraient être mesurables.
- Facebook texte (sans vidéo) : pas de stats pour le premier post ; à surveiller.
