# Briefs vidéo de la semaine du 2026-11-09 (tirage suivi/plan/2026-11-09-videos.json)
import json, os
ICI = os.path.dirname(os.path.abspath(__file__))
B = [
 dict(slug='electricien-classement-le-mans', moteur='plan-sequence', angle='Plus de clients', metier='électricien', ville='Le Mans', ambiance=2,
      entreprise='', lieu='',
      accroches=["Google vous place *où ?*", "Vous êtes où sur *Google ?*"],
      accroches_dites=["Tapez électricien Le Mans. Google vous place où ?", "Un client tape électricien Le Mans. Vous êtes où sur Google ?"],
      voix=[{'scene': 'Probleme', 'texte': "Le client appelle souvent les premiers de la liste."},
            {'scene': 'Bascule', 'texte': "Pro en ligne fait vivre votre fiche Google chaque semaine."},
            {'scene': 'Bascule', 'texte': "Et le client voit une fiche Google bien vivante.", 'ancre': 3.0},
            {'scene': 'Offre', 'texte': "Trente jours offerts, le lien est en bio."}],
      offre_ligne="Votre *fiche Google*, bien vivante."),
 dict(slug='macon-swipe-concurrent-tours', moteur='swipe', angle='Face au concurrent', metier='maçon', ville='Tours', ambiance=0, entreprise='',
      accroches=["Maçon à Tours, même note Google que le voisin. Pourquoi lui ?", "Maçon à Tours, comparez votre fiche Google à celle d'en face."],
      voix=[{'scene': 'Probleme', 'texte': "Sa fiche Google montre ses chantiers récents."},
            {'scene': 'Bascule', 'texte': "Pro en ligne publie les vôtres chaque lundi."},
            {'scene': 'Bascule', 'texte': "Et votre fiche Google montre votre travail récent.", 'ancre': 3.0},
            {'scene': 'Offre', 'texte': "C'est trente jours offerts, lien en bio."}],
      offre_ligne="Vos chantiers, *enfin visibles.*"),
 dict(slug='coiffeuse-soiree-avis-caen', moteur='cinetique', angle='Du temps libre', metier='coiffeuse', ville='Caen', ambiance=1, valeur='22h47',
      accroches=["Coiffeuse à Caen, encore vos *avis Google* à cette heure-ci ?", "Coiffeuse à Caen, *Google* vous prend vos soirées ?"],
      voix=[{'scene': 'Probleme', 'texte': "Le salon est fermé, votre fiche Google vous attend."},
            {'scene': 'Bascule', 'texte': "Pro en ligne s'en charge en journée."},
            {'scene': 'Bascule', 'texte': "Et le soir, vous rentrez vraiment chez vous.", 'ancre': 3.0},
            {'scene': 'Offre', 'texte': "Essayez trente jours offerts, lien en bio."}],
      offre_ligne="Vos soirées *vous reviennent.*"),
 dict(slug='plombier-classement-bordeaux', moteur='plan-sequence', angle='Plus de clients', metier='plombier', ville='Bordeaux', ambiance=2,
      entreprise='', lieu='',
      accroches=["On vous voit sur *Google ?*", "Votre nom est sur *Google ?*"],
      accroches_dites=["Plombier à Bordeaux, on vous voit sur Google ?", "Un client tape plombier Bordeaux. Votre nom est sur Google ?"],
      voix=[{'scene': 'Probleme', 'texte': "Le client appelle souvent l'un des premiers qu'il voit."},
            {'scene': 'Bascule', 'texte': "Chaque semaine, Pro en ligne publie pour vous."},
            {'scene': 'Bascule', 'texte': "Et votre fiche Google se met à vivre.", 'ancre': 3.0},
            {'scene': 'Offre', 'texte': "Trente jours offerts, et le lien est en bio."}],
      offre_ligne="Une *fiche Google* qui travaille."),
 dict(slug='estheticienne-swipe-appels-lyon', moteur='swipe', angle="Plus d'appels", metier='esthéticienne', ville='Lyon', ambiance=0, entreprise='',
      accroches=["Esthéticienne à Lyon, on saute votre fiche Google ?", "Esthéticienne à Lyon, avant de réserver, on lit votre fiche Google."],
      voix=[{'scene': 'Probleme', 'texte': "Des photos anciennes, et on appelle la suivante."},
            {'scene': 'Bascule', 'texte': "Pro en ligne montre vos soins chaque semaine."},
            {'scene': 'Bascule', 'texte': "Et cette fois, c'est chez vous qu'on appelle.", 'ancre': 3.0},
            {'scene': 'Offre', 'texte': "Le lien est en bio, trente jours offerts."}],
      offre_ligne="Vos soins *se voient enfin.*"),
 dict(slug='paysagiste-duel-lille', moteur='cinetique', angle='Face au concurrent', metier='paysagiste', ville='Lille', ambiance=1, valeur='Le voisin',
      accroches=["Paysagiste à Lille, le voisin montre ses *jardins* sur Google.", "Paysagiste à Lille, qui a la *fiche Google* la plus vivante ?"],
      voix=[{'scene': 'Probleme', 'texte': "Il montre ses jardins chaque semaine. Vous, rarement."},
            {'scene': 'Bascule', 'texte': "Pro en ligne montre enfin vos chantiers d'hiver."},
            {'scene': 'Bascule', 'texte': "À travail égal, on vous choisit, vous.", 'ancre': 3.0},
            {'scene': 'Offre', 'texte': "Trente jours offerts vous attendent, lien en bio."}],
      offre_ligne="Vos jardins, *sur Google.*"),
 dict(slug='chauffagiste-semaine-toulouse', moteur='plan-sequence', angle='Du temps libre', metier='chauffagiste', ville='Toulouse', ambiance=2,
      entreprise='', lieu='',
      accroches=["Chauffagiste à Toulouse, la *fiche Google* prend vos soirées ?", "Chauffagiste à Toulouse, encore votre *fiche Google* ce soir ?"],
      voix=[{'scene': 'Probleme', 'texte': "Après les dépannages, il reste les avis le soir."},
            {'scene': 'Bascule', 'texte': "Pro en ligne prend tout ça en charge."},
            {'scene': 'Bascule', 'texte': "Vos soirées redeviennent libres.", 'ancre': 3.0},
            {'scene': 'Offre', 'texte': "Testez trente jours offerts, le lien est en bio."}],
      offre_ligne="Vos soirées, *au chaud.*"),
]
for b in B:
    p = os.path.join(ICI, b['slug'] + '.json')
    old = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}
    b.setdefault('musique', True)
    b['audio_src'] = old.get('audio_src', {})
    for k in ('prises',):
        if k in old: b[k] = old[k]
    json.dump(b, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(B), 'briefs')
