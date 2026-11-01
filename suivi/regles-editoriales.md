# Règles éditoriales — planning Proenligne

Ce fichier est la référence de la tâche planifiée hebdomadaire. À relire en entier avant chaque lot.

## Règle n°1 : on parle de « fiche Google », et ça doit sauter aux yeux

Le public (artisans, commerçants) ne sait pas ce qu'est « la fiche ». Il faut que chaque contenu fasse comprendre **dès la première ligne** qu'on parle de la **fiche Google** de leur entreprise.

- Toujours écrire **« fiche Google »**, jamais « la fiche », « votre fiche » ou « le profil » tout seuls. Un rappel plus loin dans le même texte peut dire « elle » ou « votre fiche Google ».
- L'accroche (première ligne, titre du visuel, accroche de la vidéo, titre YouTube) contient **« Google »**. Sur X, la mention doit tenir dans les 280 caractères.
- Apporter le contexte, au moins une fois par contenu : c'est **ce qui s'affiche quand un client cherche votre métier sur Google ou Google Maps** (nom, photos, avis, horaires, téléphone). Exemples de tournures :
  - « Votre fiche Google, c'est ce que vos clients voient en premier quand ils cherchent “plombier” sur Google Maps. »
  - « Quand on tape “coiffeur près de moi”, Google affiche des fiches : photos, avis, horaires. La vôtre en fait partie. »
- Vidéos : l'accroche ou la scène Contraste doit nommer la fiche Google (le téléphone montre une recherche ou une fiche ; le texte à l'écran doit dire « fiche Google »).
- Visuels : `outils/visuel.py` refuse un brief dont le surtitre et le titre ne contiennent pas « Google ».
- Ne jamais reproduire le logo ni l'interface de Google : le mot suffit.
- **Varier la phrase d'explication** : elle ne doit pas être copiée telle quelle dans tous les posts (le vérificateur refuse plus de 4 copies identiques par semaine). Tournures à alterner :
  - « Votre fiche Google, c'est ce qui s'affiche quand un client cherche “plombier” sur Google ou Google Maps : nom, photos, avis, horaires. »
  - « Quand on tape “coiffeur près de moi”, Google affiche des fiches : photos, avis, horaires. La vôtre en fait partie. »
  - « Sur Google Maps, chaque garage a sa fiche Google : la note, les photos, le bouton Appeler. C'est elle qu'on regarde avant de vous appeler. »
  - « La fiche Google, c'est la carte de visite que Google montre à votre place : photos, avis, horaires, téléphone. »
  - « Cherchez “boulangerie” dans votre ville : les encadrés avec note et photos sont des fiches Google. »
  - « Avant d'appeler un serrurier, le client ouvre sa fiche Google sur Google Maps : avis, horaires, et vos réponses. »

## Règle n°2 : l'essai est gratuit, aucun prix nulle part

Appel à l'action : « Essayez gratuitement » / « Essayez Proenligne gratuitement », éventuellement « sans engagement ». Jamais de montant, de « € », de « par mois », de « centimes par jour », d'abonnement ni de comparaison de prix, dans aucun texte, visuel, vidéo, titre ou commentaire.

## Règle n°3 : aucune statistique ni résultat chiffré venant de nos clients

**On ne donne jamais un chiffre de résultat de nos clients.** Ni « ×3 appels », ni « 100 appels en un semestre », ni « un de nos clients a triplé ses appels », ni pourcentage, ni « résultat : … », ni « en 6 mois ». Ni dans un texte, ni dans un visuel, ni dans une vidéo, ni dans un titre, ni dans un premier commentaire, ni dans un brief.

- La **preuve** se fait par une **démonstration** : un avant / après descriptif (ce qu'il y avait, ce qu'il y a maintenant), une scène vécue, le fonctionnement public de Google (une fiche complète et active rassure, un avis sans réponse fait douter), jamais par un chiffre de résultat.
- Les seuls chiffres autorisés décrivent une situation ou une action, pas un résultat : « 3 avis sans réponse », « une photo par semaine », « 5 secondes », « depuis 2021 ».
- Contrôle mécanique : `cerveau/regles_texte.py` (regex STATS) appliqué par `cerveau/verifier.py`, `outils/visuel.py` et le `brief.py valider` du skill vidéo adapté. L'angle `preuve` du skill vidéo est retiré ; le format texte « Preuve » devient « Démonstration ».

## Règle n°4 : chaque élément textuel est relu comme par un humain avant programmation

Le vérificateur contrôle des règles mécaniques ; il ne sait pas si une phrase a du sens. Avant tout rendu de média et toute programmation, **tous** les éléments textuels de la semaine (textes par canal, accroches, titres, premiers commentaires, textes des visuels, textes des briefs vidéo : accroches, suite, réveil, corps, notifications, scène) passent par une **relecture indépendante** :

1. `python3 cerveau/relecture.py extraire <lundi> --briefs <dossier des briefs vidéo>` → `suivi/relecture/<lundi>-textes.json`.
2. Un **agent relecteur distinct** (Agent tool, agent neuf qui n'a pas écrit les textes) lit `cerveau/relecture-consigne.md` et le fichier -textes, et écrit `suivi/relecture/<lundi>.json` avec un verdict par élément (ok / refuse + motif + proposition). Il se met à la place d'un artisan qui lit la phrase froidement : compréhensible seule, sans contradiction avec les autres éléments du même post, sans affirmation invérifiable, règles n°1-2-3, ton, français.
3. Chaque refus est corrigé (dans le plan ou le brief), puis on réextrait et on relit **jusqu'à zéro refus**. L'empreinte des textes est vérifiée : une relecture faite sur une version antérieure des textes ne compte pas.
4. `python3 cerveau/verifier.py suivi/plan/<lundi>.json --briefs <dossier> --relecture` doit répondre « plan OK + relecture validée ». Sans cela, rien n'est rendu ni programmé.

Exemples de phrases refusées : « Nouveauté tue sur votre fiche Google, clients partis » (télégraphique, incompréhensible seule) ; « Vous trouvez les fuites sans casser. Votre fiche Google ne le dit à personne » (jargon non expliqué en accroche) ; un quiz dont la 1re slide coche déjà la bonne réponse alors que le texte dit « réponse dans le carrousel » ; un texte qui dit « il regarde 3 choses » quand le visuel n'en retient qu'une.

## Grille quotidienne (heure de Paris)

| Créneau nominal | Type | Canaux Postiz | Média |
|---|---|---|---|
| **06:30** | Texte + image | X + Facebook | 1 image 1080×1350 (`outils/visuel.py`, gabarit `conseil` ou `question`) — sur Facebook un texte seul est le format le moins diffusé |
| **13:00** | Carrousel | Instagram + Facebook, **+ LinkedIn du lundi au vendredi** | carrousel de 3 à 5 images (`outils/visuel.py --carrousel`), le même pour les 3 canaux ; LinkedIn en mode carrousel (`post_as_images_carousel: true`) |
| **19:00** | Vidéo verticale | TikTok + Instagram (Reel) + YouTube (Short) + Facebook (Reel) | pub motion 15 s (skill `pub-motion-proenligne`), **toujours la version verticale 9:16** sur les 4 canaux. La version horizontale n'est plus publiée. |

3 créneaux par jour, 7 jours sur 7 : 21 créneaux, soit 7 × (2 + 2 + 4) + 5 LinkedIn = **61 posts par semaine**, plus 2 variantes A/B TikTok (voir plus bas).

**Heures réelles variées.** Chaque créneau part à ± 45 min de son heure nominale (06:00 à 07:15, 12:30 à 13:45, 18:30 à 19:45), tirées par `python3 outils/heure_utc.py <lundi> --varier`. C'est ce qui permet d'apprendre quels horaires marchent ; le créneau nominal reste la référence des fiches. Un créneau est « occupé » si un post existe sur ce canal à ± 75 min du nominal.

**Premier commentaire.** Chaque post part avec un premier commentaire (2e élément de `postsAndComments`, sans média) : une question, un complément ou le « où en savoir plus », jamais un prix. C'est là que va l'appel à l'action des contenus utiles.

**LinkedIn : seulement en semaine, au créneau de 13:00.** Pas le week-end (audience quasi nulle sur une page entreprise), pas à 06:30 ni à 19:00 (l'engagement chute après 17h). 5 posts par semaine : la fréquence optimale pour une page de PME.

**Heure UTC à passer à Postiz** : toujours celle donnée par `outils/heure_utc.py` (heure d'été et d'hiver gérées). Ne jamais calculer le décalage à la main.

## Mix éditorial : 70 % utile, 20 % preuve, 10 % offre

Les algorithmes distribuent peu les publicités. Chaque créneau porte une **intention** (champ `intention` du plan, contrôlé par `cerveau/verifier.py`) :

| Intention | Part de la semaine | Ce que c'est | Appel à l'action |
|---|---|---|---|
| `utile` | **au moins 13 créneaux sur 21** | Le lecteur repart avec quelque chose : un test à faire sur sa fiche Google, une astuce concrète, une erreur à éviter, une idée reçue démontée, une scène où il se reconnaît. Proenligne est cité une fois au plus, en passant. | **Une question** qui fait commenter (dans le texte ou le premier commentaire). « Essayez gratuitement » autorisé mais pas obligatoire, et jamais dans le visuel. |
| `preuve` | 2 à 5 créneaux | Une **démonstration** : avant / après descriptif d'une fiche Google (ce qu'il y avait, ce qu'il y a maintenant), scène où le client compare deux fiches, ce que Google affiche et pourquoi ça rassure. **Jamais un chiffre de résultat** (règle n°3). | Question ou « Essayez gratuitement », discret, en fin de texte. |
| `offre` | **3 créneaux au plus** | Ce que fait Proenligne (photo le lundi, publication le jeudi, réponse aux avis) et l'essai gratuit. | « Essayez Proenligne gratuitement, sans engagement. » Les 3 ✅ ne sont autorisés **que** dans ces posts. |

Règles transverses : jamais plus de 3 ✅ ; la règle n°1 « fiche Google » s'applique à toutes les intentions ; aucun prix nulle part (règle n°2) ; aucune statistique client (règle n°3) ; relecture de chaque élément (règle n°4) ; un contenu utile se termine par une question, pas par une promesse.

## A/B et amplification

- **A/B TikTok** : chaque semaine, 2 vidéos (mardi et jeudi) sont rendues en deux variantes d'accroche (`render.py lot-ab`). La variante A part dans la grille à 19:00 ; la variante B part sur TikTok seulement, **le surlendemain à 12:30** (poste supplémentaire, hors grille). Le champ `ab` du plan vaut "A" sur le créneau et une entrée séparée porte "B". L'analyse compare A et B sur TikTok.
- **Amplification** (tâche quotidienne) : un post dont l'audience dépasse 2 fois la médiane de son canal sur 14 jours (au moins 5 posts mesurés) est noté dans `suivi/amplifier.json` : sujet, angle, ton, métier, accroche. La tâche hebdomadaire suivante **reprend obligatoirement** ces sujets : une déclinaison en carrousel, une variante vidéo avec une autre accroche, le même angle sur un autre métier.
- **Gardien** (tâche quotidienne) : un post en état d'erreur dans Postiz est recréé une fois à l'identique (heure + 2 h si l'heure est passée) et signalé.

## Connecteur Postiz

Toujours le connecteur personnalisé « postiz » (outils `mcp__postiz__*`, en minuscules), branché directement sur l'instance. Le connecteur officiel (`mcp__Postiz__*`) passe par le relais de Postiz Cloud, qui refuse toute pièce jointe hors `uploads.postiz.com` (bug gitroomhq/postiz-app #2278).

## Identifiants des canaux Postiz

| Canal | integrationId |
|---|---|
| TikTok | `cmvsaqnzu0001pj8d4gk1ojzz` |
| Facebook | `cmvs9p6ky0001mq8gkj2c0a82` |
| Instagram | `cmvs9xsx80003mq8gnh6baz7n` |
| X | `cmvsbfk2y0001nr8eba2fo36u` (non Premium : 280 caractères max) |
| YouTube | `cmvsbyqw20001jv87195lx18q` |
| LinkedIn (page Proenligne) | `cmvxyqbk4001vkb7zbrwvu9pt` (plateforme Postiz `linkedin-page`) |

## Réglages par plateforme

| Plateforme | Limite texte | Réglages à passer |
|---|---|---|
| X | **280 caractères**, espaces, emojis et hashtags compris ; l'image de 06:30 en pièce jointe | `post_type: post`, `who_can_reply_post: everyone` |
| Facebook | pratiquement illimitée | `post_type: post` ; à 06:30 avec l'image, à 13:00 avec le carrousel (plusieurs images), à 19:00 avec la vidéo verticale (Reel) |
| Instagram | 2 200 caractères, au moins 1 média | `post_type: post` |
| TikTok | 2 000 caractères, 1 vidéo obligatoire | `content_posting_method: DIRECT_POST` (UPLOAD ne publie pas !), `privacy_level: PUBLIC_TO_EVERYONE`, `duet: false`, `stitch: false`, `comment: true`, `autoAddMusic: no`, `brand_content_toggle: false`, `brand_organic_toggle: false`, `video_made_with_ai: false`, `title` ≤ 90 |
| YouTube | titre ≤ 100, description ≤ 5 000, 1 vidéo obligatoire, **verticale 9:16 et ≤ 60 s → publiée en Short** | `title`, `type: public`, `selfDeclaredMadeForKids: no` |
| LinkedIn (page) | **3 000 caractères** ; carrousel de 3 à 5 images | `post_as_images_carousel: true`, `carousel_name` = l'accroche (≤ 60 car.) |

Contenu Postiz en HTML : chaque ligne dans un `<p>`, ligne vide = `<p></p>`.

## Déclinaison des textes

Un même message se décline par plateforme, jamais copié tel quel :
- **X** : accroche + promesse + appel à l'action, ≤ 280 caractères. Garder l'accroche, c'est elle qui arrête le scroll. Pas de phrase coupée.
- **Facebook** : version complète (accroche, développement, 3 puces ✅, offre, 4-6 hashtags).
- **Instagram** : version complète, hashtags en fin de texte.
- **TikTok** : légende courte et directe, la vidéo porte le message ; le premier commentaire pose la question.
- **YouTube** : titre accrocheur (≤ 100), description complète.
- **LinkedIn** : on parle à des **gérants d'entreprise**, pas à leurs clients. Ton professionnel, vouvoiement, phrases courtes, une idée par paragraphe.
  - Les **2 premières lignes (≈ 200 caractères)** sont les seules visibles avant « … voir plus » : elles portent l'accroche avec « fiche Google ».
  - Corps de 700 à 1 300 caractères : un constat du métier, ce que ça coûte en clients, ce que fait Proenligne (les 3 promesses), l'appel à l'action « Essayez Proenligne gratuitement, sans engagement ».
  - 3 à 5 hashtags maximum en fin de texte (#FicheGoogle #GoogleBusinessProfile #ReferencementLocal + métier ou #TPE / #Artisanat). Pas d'avalanche d'emojis : 3 ✅ au plus.
  - Jamais de lien externe dans le texte (LinkedIn réduit leur portée) ; « lien en bio » n'a pas de sens sur LinkedIn : renvoyer vers la page Proenligne ou ne rien dire.
  - Ne pas recopier le texte Facebook : reprendre l'idée du créneau, réécrite pour un décideur.

## Formats du créneau texte (06:30), en rotation

1. **Conseil pratique** : une action concrète sur sa fiche Google.
2. **Test** : « Tapez votre métier + votre ville… » ou équivalent, qui fait vérifier sa position.
3. **Constat métier** : une scène vraie pour un métier précis (fuite du soir, panne, rendez-vous coiffure…).
4. **Idée reçue** : « On croit que… En réalité… ».
5. **Démonstration** (format `preuve`) : un avant / après descriptif ou une scène de comparaison, sans aucun chiffre de résultat (règle n°3).

Ne pas utiliser deux fois le même format le même jour, ni le même format deux jours de suite au même créneau. Même règle pour le **ton** (jamais le même deux créneaux de suite, 5 fois par semaine au plus) et pour le **gabarit visuel** de 13:00 (`avant-apres`, `conseil`, `question`, en alternance).

## Règles de contenu (non négociables, reprises du skill)

- **Aucun client réel** : ni nom d'entreprise, ni prénom, ni ville, ni avis recopié. Enseignes fictives : métier + Weber, Martin, Durand, Bernard ou Petit, **en alternance** (jamais le même nom fictif deux fois le même jour, 3 fois par semaine au plus dans les vidéos). Prénoms : ceux du skill.
- **Chiffres autorisés uniquement** : 3 · 5 · 2 · 1 · 2021 · 4 · 20 · 22 · 23 · 30, pour décrire une situation ou une action. **Aucun chiffre de résultat** (règle n°3), pas d'heure, de pourcentage ni de montant inventés.
- **Rien d'invérifiable sur Google** : pas de « Google préfère », « sort en premier », « glisse vers le bas » présentés comme des certitudes. Dire ce que Google rend public (une fiche complète et active, des photos récentes, des réponses aux avis) et ce que ça change pour le client qui compare.
- **Des phrases, pas des télégrammes** : chaque accroche, titre de scène vidéo (`suite`), titre de visuel et légende a un sujet et un verbe et se comprend seule, lue froidement sur un téléphone. Le jargon du métier est explicité (« la recherche de fuite sans casser les murs », pas « les fuites sans casser »).
- **Promesses** : Proenligne publie une photo le lundi, une publication le jeudi, répond à chaque avis, fait valider les réponses aux avis négatifs. Rien d'autre.
- **Offre unique : l'essai gratuit, sans aucun prix** (règle n°2).
- Hashtags de base : #FicheGoogle #GoogleBusinessProfile #ReferencementLocal, plus le hashtag du métier.

## Variété sur la semaine

- 11 métiers : plombier, électricien, chauffagiste, serrurier, paysagiste, maçon, coiffeur, esthéticienne, auto-école, boulangerie, garage. Pas le même métier deux créneaux de suite, et au moins 6 métiers différents par semaine.
- Lire les fiches de `cerveau/productions/` : ne pas reprendre une accroche déjà publiée ni un trio métier + angle + format des 3 dernières semaines.
- **Ouvertures variées** : alterner question directe, réplique de client entre guillemets, scène au présent (« Il est 20 h… »), constat qui pique, idée contre-intuitive, « pendant que vous… ». Deux textes de la semaine ne commencent jamais par les mêmes 5 mots ; la structure accroche + 3 ✅ + CTA est réservée aux 3 posts « offre ».
- **Vidéos** : varier la mise en scène (recherche, fiche, avis, journée) et l'ambiance sonore (`PUB_AMBIANCE=0|1|2`, jamais la même deux jours de suite).
- Lire `suivi/amplifier.json` : les sujets qui ont décollé sont repris en priorité (voir « A/B et amplification »). Suivre aussi les orientations de la dernière analyse (`cerveau/analyses/`) et de `cerveau/decisions.md`.
- Les 7 vidéos de la semaine passent par le tirage du skill avec `suivi/historique-pubs.json`.

## Visuels : tests et quiz

- Gabarit `question` : le titre est une vraie question (finit par « ? »). **Aucune réponse n'est cochée** sur l'image ou la 1re slide : un sondage n'a pas de bonne réponse ; un quiz révèle la réponse sur une slide suivante (`numero` = la lettre), et le texte du post peut dire « réponse dans le carrousel ».
- Le titre annonce ce que le contenu donne : « 3 réflexes » si ce sont 3 conseils, pas « 3 photos ».
- Le visuel et le texte disent la même chose : mêmes chiffres, mêmes jours, même nombre d'éléments.

## Médias

- Déposer chaque fichier dans `medias/AAAA-MM-JJ/` (date de publication), le pousser sur `main`, puis l'importer dans Postiz avec `uploadFromUrlTool` et l'URL `https://raw.githubusercontent.com/proenlignecontact/proenligne-media/main/<chemin>`. Un carrousel = un dossier `carrousel-<slug>/01.png … 0N.png`, chaque image importée séparément, dans l'ordre.
- Les briefs vidéo (`pub-work/briefs/<slug>.json`) sont copiés dans `suivi/briefs/<lundi>/` : la tâche quotidienne s'en sert pour rendre une variante.
- Utiliser l'URL `media.glidy.uk/...` renvoyée par Postiz comme pièce jointe, jamais l'URL GitHub.
- Nettoyage : supprimer (`git rm`) les dossiers `medias/` de plus de 14 jours, une fois les posts publiés.
