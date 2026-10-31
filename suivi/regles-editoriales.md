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

## Grille quotidienne (heure de Paris)

| Créneau | Type | Canaux Postiz | Média |
|---|---|---|---|
| **06:30** | Texte | X + Facebook | aucun |
| **13:00** | Visuel fixe | Instagram + Facebook | PNG 1080×1350 fait avec `outils/visuel.py` |
| **19:00** | Vidéo | TikTok + Instagram + YouTube | pub motion 15 s (skill `pub-motion-proenligne`) : vertical pour TikTok et Instagram, horizontal pour YouTube |

3 publications par jour, 7 jours sur 7, soit 21 par semaine.

**Heure UTC à passer à Postiz** : Paris = UTC+1 en heure d'hiver (jusqu'au 28 mars 2027), UTC+2 en heure d'été.
Exemple en hiver : 06:30 → 05:30 UTC, 13:00 → 12:00 UTC, 19:00 → 18:00 UTC.

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

## Réglages par plateforme

| Plateforme | Limite texte | Réglages à passer |
|---|---|---|
| X | **280 caractères**, espaces, emojis et hashtags compris | `post_type: post`, `who_can_reply_post: everyone` |
| Facebook | pratiquement illimitée | `post_type: post` ; pour une vidéo, `title` facultatif |
| Instagram | 2 200 caractères, au moins 1 média | `post_type: post` |
| TikTok | 2 000 caractères, 1 vidéo obligatoire | `content_posting_method: DIRECT_POST` (UPLOAD ne publie pas !), `privacy_level: PUBLIC_TO_EVERYONE`, `duet: false`, `stitch: false`, `comment: true`, `autoAddMusic: no`, `brand_content_toggle: false`, `brand_organic_toggle: false`, `video_made_with_ai: false`, `title` ≤ 90 |
| YouTube | titre ≤ 100, description ≤ 5 000, 1 vidéo obligatoire | `title`, `type: public`, `selfDeclaredMadeForKids: no` |

Contenu Postiz en HTML : chaque ligne dans un `<p>`, ligne vide = `<p></p>`.

## Déclinaison des textes

Un même message se décline par plateforme, jamais copié tel quel :
- **X** : accroche + promesse + appel à l'action, ≤ 280 caractères. Garder l'accroche, c'est elle qui arrête le scroll. Pas de phrase coupée.
- **Facebook** : version complète (accroche, développement, 3 puces ✅, offre, 4-6 hashtags).
- **Instagram** : version complète, hashtags en fin de texte.
- **TikTok** : légende courte et directe, la vidéo porte le message.
- **YouTube** : titre accrocheur (≤ 100), description complète.

## Formats du créneau texte (06:30), en rotation

1. **Conseil pratique** : une action concrète sur sa fiche Google.
2. **Test** : « Tapez votre métier + votre ville… » ou équivalent, qui fait vérifier sa position.
3. **Constat métier** : une scène vraie pour un métier précis (fuite du soir, panne, rendez-vous coiffure…).
4. **Idée reçue** : « On croit que… En réalité… ».
5. **Preuve** : uniquement ×3 appels, 100 appels, 6 mois, attribués à « un de nos clients ».

Ne pas utiliser deux fois le même format le même jour, ni le même format deux jours de suite au même créneau.

## Règles de contenu (non négociables, reprises du skill)

- **Aucun client réel** : ni nom d'entreprise, ni prénom, ni ville, ni avis recopié. Enseignes fictives : métier + Weber, Martin, Durand, Bernard ou Petit. Prénoms : ceux du skill.
- **Chiffres autorisés uniquement** : 3 · ×3 · 100 · 6 · 5 · 2 · 1 · 2021 · 4 · 20 · 22 · 23 · 30. Pas d'heure, de pourcentage ni de montant inventés.
- **Promesses** : Proenligne publie une photo le lundi, une publication le jeudi, répond à chaque avis, fait valider les réponses aux avis négatifs. Rien d'autre.
- **Offre unique : l'essai gratuit, sans aucun prix.** Appel à l'action : « Essayez gratuitement » / « Essayez Proenligne gratuitement », éventuellement « sans engagement ». Jamais de montant, de « € », de « par mois », de « centimes par jour » ni de comparaison de prix, dans aucun texte, visuel ou vidéo.
- Hashtags de base : #FicheGoogle #GoogleBusinessProfile #ReferencementLocal, plus le hashtag du métier.

## Variété sur la semaine

- 11 métiers : plombier, électricien, chauffagiste, serrurier, paysagiste, maçon, coiffeur, esthéticienne, auto-école, boulangerie, garage. Pas le même métier deux créneaux de suite, et au moins 6 métiers différents par semaine.
- Lire les fiches de `cerveau/productions/` : ne pas reprendre une accroche déjà publiée ni un trio métier + angle + format des 3 dernières semaines. Suivre aussi les orientations de la dernière analyse (`cerveau/analyses/`) et de `cerveau/decisions.md`.
- Les 7 vidéos de la semaine passent par le tirage du skill avec `suivi/historique-pubs.json`.

## Médias

- Déposer chaque fichier dans `medias/AAAA-MM-JJ/` (date de publication), le pousser sur `main`, puis l'importer dans Postiz avec `uploadFromUrlTool` et l'URL `https://raw.githubusercontent.com/proenlignecontact/proenligne-media/main/<chemin>`.
- Utiliser l'URL `media.glidy.uk/...` renvoyée par Postiz comme pièce jointe, jamais l'URL GitHub.
- Nettoyage : supprimer (`git rm`) les dossiers `medias/` de plus de 14 jours, une fois les posts publiés.
