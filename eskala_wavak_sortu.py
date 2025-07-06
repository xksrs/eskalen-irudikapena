from pydub import AudioSegment
import numpy as np
from scipy.signal import sawtooth
from scipy.io.wavfile import write

def idatzi_sawtooth_wav(f, t, output_path):
    sample_rate = 44100

    # Denbora-bektorea
    t_samples = np.linspace(0, t, int(sample_rate * t), endpoint=False)

    # Zerra uhina sortu
    wave = sawtooth(2 * np.pi * f * t_samples)

    # 16-bit PCM
    wave_int16 = np.int16(wave * 32767)

    # .wav fitxategia idatzi
    write(f"{output_path}/{round(f, 2)}.wav", sample_rate, wave_int16)


def sortu_eskala_maiztasunak(f0, r, N, shift_idx = 0, output_path = "./sounds"):
    f_list = []

    # Maiztasunak sortu, eskalara ekarri eta zerrendan sartu
    for i in range(N):
        f = f0 * r ** i
        while f > 2 * f0:
            f = f / 2
        f_list.append(f)
    f_list.sort()

    # Eskalaren hasierako nota shift_idx-garren nota izan dadin beharrezko aldaketak egin. Oinarrizko maiztasuna mantenduta.
    shift_ratio = f0 / f_list[shift_idx]
    f_list = [f * shift_ratio for f in f_list]
    f_list = f_list[shift_idx:] + [f * 2 for f in f_list[:shift_idx]]

    # Nota bakoitzaren .wav fitxategia gorde, iraupena 1s
    for i in range(len(f_list)):
        idatzi_sawtooth_wav(f_list[i], 1, output_path)
        f_list[i] = round(f_list[i], 2)

    # Goiko zortziduneko f0 nota gorde
    idatzi_sawtooth_wav(2*f_list[0], 1, output_path)
    f_list.append(round(2*f_list[0], 2))

    print(f_list)        
    
    # Notak ordenatuta elkartu eta fitxategi bakarrean gorde
    file_paths = [f"{output_path}/{f}.wav" for f in f_list]
    file_paths.sort()

    snippets = []
    for path in file_paths:
        audio = AudioSegment.from_wav(path)
        snippet = audio[:750]
        snippets.append(snippet)

    combined = sum(snippets)

    combined.export(f"{output_path}/eskalak_r{r}N{N}-{shift_idx}.wav", format="wav")

# Eskala pentatonikoa
sortu_eskala_maiztasunak(220, 3, 5)

# 7 notako eskala, frigio modua
sortu_eskala_maiztasunak(220, 3, 7)

# 7 notako eskala, modu jonikoa (maiorra edo nagusia)
sortu_eskala_maiztasunak(220, 3, 7, 4)

# 7 notako eskala, modu eolikoa (minorra)
sortu_eskala_maiztasunak(220, 3, 7, 2)

# 12 notako eskala (kromatikoa), tenperamentu berdinekoa EZ dena
sortu_eskala_maiztasunak(220, 3, 12)

# 12 notako eskala (kromatikoa), tenperamentu berdinekoa
sortu_eskala_maiztasunak(220, 2**(1/12), 12)
