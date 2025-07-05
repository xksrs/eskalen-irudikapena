import matplotlib.pyplot as plt
import numpy as np

def irudikatu_zirkunferentzia_puntuak_lerroak(
    angeluak,
    etiketak=None,
    lerroak=None,
    erradioa=1,
    save_path=None
):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_aspect('equal')

    # Zirkunferentzia sortu
    zirkunferentzia = plt.Circle((0, 0), erradioa, fill=False, color='black', linewidth=1)
    ax.add_artist(zirkunferentzia)

    # Puntuen (x, y) koordenatuak
    thetas = np.pi / 2 - np.array(angeluak)
    x = erradioa * np.cos(thetas)
    y = erradioa * np.sin(thetas)

    # Puntuak irudikatu
    ax.scatter(x, y, color='red', s=50)

    # Lerroak irudikatu
    if lerroak:
        for hasi_idx, buka_idx in lerroak:
            ax.plot(
                [x[hasi_idx], x[buka_idx]],
                [y[hasi_idx], y[buka_idx]],
                color='blue',
                linewidth=1
            )

    # Etiketak gehitu
    if etiketak:
        for xi, yi, etiketa in zip(x, y, etiketak):
            ax.text(
                xi + 0.1,
                yi,
                etiketa,
                fontsize=10,
                ha='center',
                va='center',
                bbox=dict(facecolor='white', edgecolor='none', pad=1)
            )

    # Grafikoaren estilo kontuak
    margin = 0.2 * erradioa
    ax.set_xlim(-erradioa - margin, erradioa + margin)
    ax.set_ylim(-erradioa - margin, erradioa + margin)
    ax.axis('off')

    if save_path:
        plt.savefig(save_path, bbox_inches='tight', dpi=300)
    plt.show()


def irudikatu_eskala_zirkunferentzian(r, N):
    angeluak = [np.log2(r) * 2 * np.pi * i for i in range(N)]
    etiketak = [f"f{i}" for i in range(N)]
    lerroak = [(i, (i+1) % N) for i in range(N)]
    irudikatu_zirkunferentzia_puntuak_lerroak(angeluak, etiketak=etiketak, lerroak=lerroak, erradioa=1)



r = 3
N = 12

irudikatu_eskala_zirkunferentzian(r, N)