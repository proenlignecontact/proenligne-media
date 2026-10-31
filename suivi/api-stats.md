# API de statistiques — à compléter

Statut : **pas encore disponible**. Tant que ce fichier dit « pas encore disponible », la tâche hebdomadaire ne relève pas de stats.

## Authentification
Le jeton Bearer est stocké comme **secret réseau** (Network secret) sur l'environnement cloud de la tâche.
Le proxy d'Anthropic ajoute `Authorization: Bearer …` aux requêtes vers l'hôte déclaré : les appels se font donc **sans en-tête d'authentification** (ex. `curl -s https://<hôte>/…`).
Le jeton n'est jamais visible dans la session et ne doit JAMAIS apparaître dans ce dépôt public.

## À renseigner quand l'API sera en ligne
- Hôte (adresse **publique**, pas en .ts.net), identique à celui déclaré dans le secret réseau :
- Endpoint(s) et paramètres (par post Postiz, par période…) :
- Exemple de réponse :
- Correspondance des champs vers le format de `cerveau/stats/` (vues, likes, commentaires, partages, enregistrements, clics) :
