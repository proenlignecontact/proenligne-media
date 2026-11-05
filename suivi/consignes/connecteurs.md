<!-- Procédure commune à TOUTES les tâches planifiées Proenligne pour joindre les connecteurs postiz et ElevenLabs. Lue au démarrage de chaque exécution. Modifier ici, pas dans les tâches. -->

# Joindre les connecteurs (postiz, ElevenLabs) — procédure obligatoire

Le connecteur personnalisé **« postiz »** existe et fonctionne : ses outils s'écrivent en minuscules, `mcp__postiz__*`. Il est souvent encore « en cours de connexion » (still connecting) au démarrage d'une session planifiée, ou parfois ne se connecte pas du tout dans cette session-là alors qu'il marche très bien dans la suivante. **Une absence du connecteur n'est JAMAIS une raison d'abandonner la tâche** : on attend, puis on relance la tâche soi-même. L'utilisateur ne doit jamais avoir à relancer une tâche à la main.

## 1. Attendre (jusqu'à 10 minutes)
1. ToolSearch `select:mcp__postiz__integrationList` (ajoute dans la même requête les autres outils dont la tâche a besoin), puis un appel test `mcp__postiz__integrationList`.
2. Si l'outil est introuvable ou si l'appel échoue : fais aussi un ToolSearch par mot-clé `postiz` (max_results 10) pour voir sous quel nom il apparaît (il doit commencer par `mcp__postiz__`, en minuscules ; n'utilise jamais `mcp__Postiz__*`, le connecteur officiel qui refuse les pièces jointes). Attends 30 s (Bash `python3 -c 'import time; time.sleep(30)'`) et recommence l'étape 1.
3. Jusqu'à **20 essais** (environ 10 minutes). Pendant l'attente, tu peux avancer sur ce qui ne demande pas Postiz (clone du dépôt, lecture des consignes et des règles), mais n'écris rien dans le dépôt (pas de verrou) et ne génère rien d'ElevenLabs.
4. Une erreur ou un « still connecting » sur un AUTRE connecteur (n8n, Mermaid, Gmail, Google Drive, Claude_Docs…) ne compte pas : ignore-la.
5. ElevenLabs (`mcp__ElevenLabs__*`) suit la même attente, uniquement pour les tâches qui en ont besoin (vidéos, variante de l'amplificateur).

## 2. Relancer la tâche si le connecteur reste absent
Si après les 20 essais `mcp__postiz__*` est toujours absent ou en erreur (ou ElevenLabs pour une tâche qui doit produire des vidéos) :
1. Compte les relances déjà faites : cherche dans les messages de cette exécution la mention « RELANCE AUTOMATIQUE n°K ». Aucune mention = K vaut 0.
2. Si K < 3 : ToolSearch `select:mcp__claude-code-remote__fire_trigger` puis `mcp__claude-code-remote__fire_trigger` avec l'identifiant de TA tâche (tableau ci-dessous) et le texte : « RELANCE AUTOMATIQUE n°K+1 : le connecteur postiz (ou ElevenLabs) n'était pas joignable dans l'exécution précédente après 20 essais. Erreur vue : <erreur exacte>. Reprends la tâche normalement. » Une nouvelle session démarre alors avec des connecteurs neufs (c'est ce qui marche quand on relance à la main). Puis termine cette exécution par une seule ligne « Connecteur postiz absent, tâche relancée (relance n°K+1) », sans rien écrire dans le dépôt.
3. Si K = 3 (trois relances déjà faites) : arrête-toi et envoie un message qui cite mot pour mot l'erreur reçue et la liste des serveurs MCP signalés en échec au démarrage. C'est le seul cas où l'on abandonne.
4. Si l'outil `mcp__claude-code-remote__fire_trigger` est lui-même introuvable, attends-le comme postiz (étape 1, 10 essais), puis applique le point 3.

| Tâche (nom exact) | Identifiant à relancer |
|---|---|
| Gardien quotidien Proenligne | trig_01Adg31pNnFKfkNdASGwDxpS |
| Gardien quotidien Proenligne — secours | (voir la consigne gardien : ne se relance pas, le gardien du lendemain prend le relais) |
| Planning hebdo Proenligne | trig_0133XiVfnvCaVBi4Na7WyF1G |
| Planning hebdo Proenligne — secours | trig_01NCGbi1emYnLZFXBKtFeAS9 |
| Vidéos supplémentaires Proenligne | trig_01F1wWz3A5dR1o7joNbvcfDs |
| Vidéos supplémentaires Proenligne — secours | trig_01G7qVcAxFAPE9SHT9DFvN1q |

## 3. Dans le rapport final
Indique le nombre d'essais qu'il a fallu pour joindre postiz et, si l'exécution est une relance, son numéro (« relance automatique n°2, postiz joint au 1er essai »).
