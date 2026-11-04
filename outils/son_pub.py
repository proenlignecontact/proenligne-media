"""Copie de scripts/son.py du skill pub-motion-proenligne (bande-son originale synthétisée), avec 3 ambiances
(PUB_AMBIANCE=0|1|2). Utilisée par outils/pub-video.py pour les pubs cinétiques et plan-séquence.
"""
"""Bande-son des pubs Proenligne : une musique originale de 15 s et des bruitages calés sur l'animation.

Tout est synthétisé ici (aucun échantillon, aucune musique tierce) : pas de question de droits.
La musique fait 8 mesures à 128 BPM, soit exactement 15 s, et boucle comme l'image :
  mesures 1-4 (0 → 7,5 s)   accroche + contraste : retenue, mineure (la mineur / fa)
  mesures 5-6 (7,5 → 11,25) réveil : s'éclaire (do / sol), batterie complète, arpège
  mesures 7-8 (11,25 → 15)  offre : fa / sol, qui relance vers la mineur au début de la boucle

Les bruitages viennent du champ `sons` de chaque pub (pubs/*.jsx, dans registerPub) :
  ["type", "Scène", décalage en s depuis le début de la scène]   ou, pour la frappe,
  ["frappe", "Scène", début, fin]
Types : frappe, apparition, alerte, balayage, pop, notif, appel, victoire, clic.
Les notifications montent d'un ton à chaque fois (mi, sol, do).

usage (test seul) : python3 scripts/son.py <sortie.wav> '<sons JSON>' '<scènes JSON>'
Dans le flux normal, render.py appelle generer() puis ajoute la piste aux MP4.
"""
import json, os, subprocess, sys, tempfile
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, sosfilt

SR = 48000
DURATION = 15.0
BPM = 128
BEAT = 60 / BPM                      # 0,46875 s ; 32 temps = 15 s
N = int(SR * DURATION)
MUSIQUE_DB, SFX_DB = -15.0, 0.0      # la musique reste sous les bruitages
CIBLE_LUFS = -14                     # niveau des réseaux sociaux ; crête ≤ -1 dBTP

rng = np.random.default_rng(7)


AMBIANCES = [(0, True), (3, False), (-4, True)]   # (demi-tons de transposition, arpège)
_amb = os.environ.get('PUB_AMBIANCE')
if _amb is None:
    _amb = sum(map(ord, os.environ.get('PUB_SLUG', ''))) % 3
TRANSPO, ARPEGE_ON = AMBIANCES[int(_amb) % 3]


def hz(note):
    """'A3' → fréquence."""
    names = {'C': -9, 'D': -7, 'E': -5, 'F': -4, 'G': -2, 'A': 0, 'B': 2}
    n = names[note[0]] + (1 if '#' in note else 0)
    octave = int(note[-1])
    return 440.0 * 2 ** ((n + TRANSPO + 12 * (octave - 4)) / 12)


def t_(n):
    return np.arange(n) / SR


def env(n, a=0.005, r=None, d=None):
    """Enveloppe : attaque linéaire, puis décroissance exponentielle (d = constante de temps) ou relâche linéaire."""
    t = t_(n)
    e = np.minimum(1, t / max(a, 1e-4))
    if d:
        e *= np.exp(-np.maximum(0, t - a) / d)
    if r:
        e *= np.clip((n / SR - t) / r, 0, 1)
    return e


def lp(x, f, order=2):
    return sosfilt(butter(order, f, 'low', fs=SR, output='sos'), x)


def hp(x, f, order=2):
    return sosfilt(butter(order, f, 'high', fs=SR, output='sos'), x)


def bp(x, lo, hi):
    return sosfilt(butter(2, [lo, hi], 'band', fs=SR, output='sos'), x)


def add(buf, sig, at, gain=1.0, pan=0.0):
    """Ajoute un signal mono (ou stéréo) à `at` secondes ; ce qui dépasse 15 s repart au début (boucle)."""
    if sig.ndim == 1:
        l, r = np.sqrt((1 - pan) / 2), np.sqrt((1 + pan) / 2)
        sig = np.stack([sig * l * 1.414, sig * r * 1.414], 1)
    i = int(round(at * SR)) % N
    n = len(sig)
    end = min(N, i + n)
    buf[i:end] += sig[:end - i] * gain
    if i + n > N:                     # la queue du son revient au début : la boucle reste continue
        buf[:i + n - N] += sig[end - i:] * gain


# ---------- instruments de la musique ----------

def saw(f, n, detune=0.0):
    t = t_(n)
    ph = (f * (1 + detune)) * t
    return 2 * (ph - np.floor(ph + 0.5))


def pad(notes, n):
    """Nappe douce : dents de scie désaccordées, filtrées, gauche/droite légèrement différentes."""
    L = sum(saw(hz(x), n, -0.004) + 0.6 * saw(hz(x), n, 0.003) for x in notes)
    R = sum(saw(hz(x), n, 0.004) + 0.6 * saw(hz(x), n, -0.003) for x in notes)
    e = env(n, a=0.25, r=0.25)
    return np.stack([lp(L, 1400), lp(R, 1400)], 1) * e[:, None] * 0.08


def basse(f, n):
    t = t_(n)
    x = np.sin(2 * np.pi * f * t) + 0.3 * np.sin(4 * np.pi * f * t)
    return np.tanh(1.6 * x) * env(n, a=0.006, d=0.22) * 0.45


def kick(n=int(SR * 0.35)):
    t = t_(n)
    f = 45 + 110 * np.exp(-t / 0.035)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, a=0.002, d=0.12) * 0.9


def hihat(n=int(SR * 0.06)):
    return hp(rng.standard_normal(n), 7000) * env(n, a=0.001, d=0.018) * 0.18


def clap(n=int(SR * 0.18)):
    x = bp(rng.standard_normal(n), 900, 3500)
    e = sum(env(n, a=0.001, d=0.012) * (np.arange(n) >= int(SR * k)) for k in (0, 0.011, 0.022))
    return x * (e + env(n, a=0.03, d=0.06) * 0.5) * 0.35


def pluck(f, n=int(SR * 0.35)):
    t = t_(n)
    x = np.sin(2 * np.pi * f * t) + 0.35 * np.sin(4 * np.pi * f * t) + 0.12 * np.sin(6 * np.pi * f * t)
    return x * env(n, a=0.003, d=0.12) * 0.22


ACCORDS = [  # (nappe, fondamentale de basse) par mesure
    (['A3', 'C4', 'E4'], 'A1'), (['F3', 'A3', 'C4'], 'F1'),
    (['A3', 'C4', 'E4'], 'A1'), (['F3', 'A3', 'C4', 'E4'], 'F1'),
    (['C4', 'E4', 'G4'], 'C2'), (['G3', 'B3', 'D4'], 'G1'),
    (['F3', 'A3', 'C4', 'E4'], 'F1'), (['G3', 'B3', 'D4', 'F4'], 'G1'),
]
ARPEGE = {4: ['C5', 'E5', 'G5', 'E5'], 5: ['B4', 'D5', 'G5', 'D5'],
          6: ['A4', 'C5', 'F5', 'C5'], 7: ['B4', 'D5', 'G5', 'F5']}


def musique():
    m = np.zeros((N, 2))
    bar = 4 * BEAT
    for b, (notes, root) in enumerate(ACCORDS):
        t0 = b * bar
        add(m, pad(notes, int(SR * (bar + 0.25))), t0)
        clair = b >= 4
        pas = BEAT / 2 if clair else BEAT          # basse en croches au réveil, en noires avant
        for k in range(int(round(bar / pas))):
            add(m, basse(hz(root), int(SR * pas * 0.95)), t0 + k * pas, 0.8 if k % 2 else 1.0)
        for k in range(4):
            beat = t0 + k * BEAT
            if clair or (b >= 2 and k in (0, 2)):  # rien au début, demi-temps aux mesures 3-4, complet ensuite
                add(m, kick(), beat, 1.0 if clair else 0.7)
            if clair:
                add(m, hihat(), beat + BEAT / 2, pan=0.3)
                if k in (1, 3):
                    add(m, clap(), beat, pan=-0.1)
            elif b >= 2:
                add(m, hihat(), beat + BEAT / 2, 0.5, pan=0.3)
        if ARPEGE_ON and b in ARPEGE:
            for k in range(8):
                add(m, pluck(hz(ARPEGE[b][k % 4])), t0 + k * BEAT / 2, pan=-0.35 if k % 2 else 0.35)
    return m


# ---------- bruitages ----------

def s_frappe():
    n = int(SR * 0.03)
    x = bp(rng.standard_normal(n), 2500, 9000) * env(n, a=0.0005, d=0.004)
    x += np.sin(2 * np.pi * 1800 * t_(n)) * env(n, a=0.0005, d=0.003) * 0.3
    return x * 0.9


def s_apparition():
    n = int(SR * 0.12)
    f = 520 + 380 * np.minimum(1, t_(n) / 0.06)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, a=0.004, d=0.04) * 0.35


def s_pop():
    n = int(SR * 0.1)
    f = 900 * np.exp(-t_(n) / 0.05) + 300
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, a=0.002, d=0.03) * 0.45


def s_alerte():
    """Deux notes graves un peu sourdes : le problème (anneau ambre)."""
    out = np.zeros(int(SR * 0.6))
    for k, note in enumerate(['E3', 'D#3']):
        n = int(SR * 0.4)
        t = t_(n)
        f = hz(note)
        x = (2 / np.pi) * np.arcsin(np.sin(2 * np.pi * f * t)) + 0.3 * np.sin(2 * np.pi * 2 * f * t)
        x = lp(x, 1200) * env(n, a=0.004, d=0.12)
        i = int(SR * 0.16 * k)
        out[i:i + n] += x * 0.5
    return out


def s_balayage():
    n = int(SR * 0.45)
    t = t_(n)
    x = rng.standard_normal(n)
    lo = 300 + 3000 * (t / t[-1]) ** 2
    y = np.zeros(n)
    for j in range(0, n, 2400):        # filtre qui monte, par blocs
        seg = x[j:j + 2400]
        f = lo[j]
        y[j:j + len(seg)] = bp(seg, f, min(f * 2.5, 20000))
    return y * np.sin(np.pi * t / t[-1]) ** 2 * 0.35


def cloche(f, n=int(SR * 0.7)):
    """Son de marimba clair : notification Proenligne."""
    t = t_(n)
    x = np.sin(2 * np.pi * f * t) + 0.25 * np.sin(2 * np.pi * 4 * f * t) * np.exp(-t / 0.03)
    return x * env(n, a=0.002, d=0.18) * 0.55


NOTIFS = ['E5', 'G5', 'C6', 'E6']


def s_notif(k):
    return cloche(hz(NOTIFS[min(k, len(NOTIFS) - 1)]))


def s_appel():
    out = np.zeros(int(SR * 0.9))
    for k in range(2):
        for j in range(6):
            n = int(SR * 0.04)
            f = 1300 if j % 2 else 1650
            i = int(SR * (k * 0.45 + j * 0.045))
            out[i:i + n] += np.sin(2 * np.pi * f * t_(n)) * env(n, a=0.002, r=0.01) * 0.3
    return out


def s_victoire():
    out = np.zeros(int(SR * 1.1))
    for k, note in enumerate(['C5', 'E5', 'G5', 'C6']):
        c = cloche(hz(note), int(SR * 0.8)) * (0.7 + 0.1 * k)
        i = int(SR * 0.07 * k)
        out[i:i + len(c)] += c
    n = int(SR * 0.6)
    out[:n] += hp(rng.standard_normal(n), 9000) * env(n, a=0.05, d=0.15) * 0.06   # scintillement
    return out


def s_clic():
    n = int(SR * 0.12)
    x = bp(rng.standard_normal(n), 1500, 6000) * env(n, a=0.0005, d=0.006) * 0.7
    x += np.sin(2 * np.pi * np.cumsum(180 * np.exp(-t_(n) / 0.02) + 80) / SR) * env(n, a=0.001, d=0.03) * 0.6
    return x * 1.3


SONS = {'apparition': s_apparition, 'pop': s_pop, 'alerte': s_alerte, 'balayage': s_balayage,
        'appel': s_appel, 'victoire': s_victoire, 'clic': s_clic}


def debuts_scenes(scenes):
    t, out = 0.0, {}
    for s in scenes:
        out[s['name']] = t
        t += s['dur']
    return out


def bruitages(sons, scenes):
    """Liste (temps absolu, signal, gain) ; la frappe donne un clic par lettre, irrégulier comme un vrai pouce."""
    start = debuts_scenes(scenes)
    out, k_notif = [], 0
    for c in sons:
        typ, scene, at = c[0], c[1], c[2]
        if scene not in start:
            raise ValueError(f'scène inconnue dans sons : {scene}')
        t0 = start[scene] + at
        if typ == 'frappe':
            t1 = start[scene] + c[3]
            n = max(4, int((t1 - at - start[scene]) / 0.075))
            for j in range(n):
                out.append((t0 + (t1 - t0) * j / n + rng.uniform(-0.012, 0.012), s_frappe(), rng.uniform(0.6, 1.0)))
        elif typ == 'notif':
            out.append((t0, s_notif(k_notif), 1.0))
            k_notif += 1
        elif typ in SONS:
            out.append((t0, SONS[typ](), 1.0))
        else:
            raise ValueError(f'type de son inconnu : {typ} ({", ".join(["frappe", "notif"] + list(SONS))})')
    return out


def generer(sons, scenes, wav):
    """Écrit la bande-son (WAV 48 kHz stéréo, non normalisée) et renvoie la liste des temps des bruitages."""
    total = sum(s['dur'] for s in scenes)
    if abs(total - DURATION) > 1e-6:
        raise ValueError(f'durée des scènes {total} s ≠ {DURATION} s')
    mus = musique()
    sfx = np.zeros((N, 2))
    temps = []
    for at, sig, g in bruitages(sons, scenes):
        add(sfx, sig, at, g)
        temps.append(round(at, 2))
    # la musique s'efface légèrement sous chaque bruitage (ducking), pour qu'on l'entende
    duck = np.ones(N)
    for at in temps:
        i = int(at * SR) % N
        n = int(SR * 0.35)
        idx = (np.arange(n) + i) % N
        duck[idx] = np.minimum(duck[idx], 0.45 + 0.55 * np.linspace(0, 1, n) ** 2)
    mix = mus * 10 ** (MUSIQUE_DB / 20) * duck[:, None] + sfx * 10 ** (SFX_DB / 20)
    mix = np.tanh(mix * 1.2) / 1.2                     # écrêtage doux
    wavfile.write(wav, SR, (mix / max(1e-9, np.abs(mix).max()) * 0.7 * 32767).astype(np.int16))
    return sorted(temps)


def mesure(f):
    """(LUFS intégrés, crête vraie en dBTP) d'un fichier audio ou vidéo."""
    r = subprocess.run(['ffmpeg', '-hide_banner', '-i', f, '-af', 'loudnorm=print_format=json', '-f', 'null', '-'],
                       capture_output=True, text=True).stderr
    m = json.loads(r[r.rindex('{'):r.rindex('}') + 1])
    return float(m['input_i']), float(m['input_tp'])


def normaliser(wav_in, out_m4a):
    """Niveau réseaux sociaux : gain mesuré vers -14 LUFS, limiteur suréchantillonné, AAC ; la crête est remesurée
    après encodage et le limiteur resserré tant qu'elle dépasse -1,2 dBTP."""
    lufs, _ = mesure(wav_in)
    gain, lim = CIBLE_LUFS - lufs, 0.8
    for _ in range(8):
        af = f'volume={gain:.2f}dB,aresample=192000,alimiter=limit={lim:.3f}:attack=1:release=50:level=false,aresample={SR}'
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', wav_in, '-af', af, '-c:a', 'aac', '-b:a', '192k',
                        '-t', str(DURATION), out_m4a], check=True)
        lu, tp = mesure(out_m4a)
        if tp > -1.2:
            lim *= 10 ** ((-1.6 - tp) / 20)      # crête trop haute : resserrer le limiteur
        elif lu < CIBLE_LUFS - 0.7:
            gain += CIBLE_LUFS - lu                # le limiteur a mangé du niveau : compenser
        else:
            return


def ajouter_aux_videos(m4a, mp4s):
    """Remplace la piste audio des MP4 (vidéo copiée telle quelle, aucun nouveau rendu)."""
    for mp4 in mp4s:
        tmp = mp4 + '.tmp.mp4'
        subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', mp4, '-i', m4a, '-map', '0:v:0', '-map', '1:a:0',
                        '-c:v', 'copy', '-c:a', 'copy', '-shortest', '-movflags', '+faststart', tmp], check=True)
        os.replace(tmp, mp4)


def controler(mp4):
    """Piste audio présente, durée 15 s, niveau proche de -14 LUFS, crête ≤ -1 dB, début et fin calmes (boucle)."""
    pb = []
    r = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'a', '-show_entries', 'stream=duration',
                        '-of', 'csv=p=0', mp4], capture_output=True, text=True).stdout.strip()
    if not r:
        return [f'{os.path.basename(mp4)} : pas de piste audio']
    if abs(float(r) - DURATION) > 0.1:
        pb.append(f'{os.path.basename(mp4)} : audio de {float(r):.2f} s au lieu de {DURATION} s')
    lufs, tp = mesure(mp4)
    if abs(lufs - CIBLE_LUFS) > 1.5:
        pb.append(f'{os.path.basename(mp4)} : niveau {lufs} LUFS (cible {CIBLE_LUFS})')
    if tp > -1.0:
        pb.append(f'{os.path.basename(mp4)} : crête {tp} dB (max -1)')
    return pb


def bande_son(sons, scenes, mp4s):
    """Flux complet pour un produit : génère, normalise, ajoute aux MP4, contrôle. Renvoie (problèmes, temps)."""
    with tempfile.TemporaryDirectory() as tmp:
        wav, m4a = os.path.join(tmp, 'son.wav'), os.path.join(tmp, 'son.m4a')
        temps = generer(sons, scenes, wav)
        normaliser(wav, m4a)
        ajouter_aux_videos(m4a, mp4s)
    return [p for f in mp4s for p in controler(f)], temps


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    print(generer(json.loads(sys.argv[2]), json.loads(sys.argv[3]), sys.argv[1]))
