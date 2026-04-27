"""
Genera SVG dei grafici principali per il pacchetto didattico.
Esegui con: python3 _genera_svg.py

Output: SVG nella stessa cartella, da committare.

REGOLE DI QUALITA:
- Tutti i grafici hanno figsize generoso e padding sui titoli
- Annotazioni MAI sopra la curva o sopra il titolo
- Etichette dentro bbox bianchi semitrasparenti per leggibilità
- Funzione smooth_stall con picco ESATTAMENTE a alpha_stall
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mp
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent

plt.rcParams.update({
    "font.size": 11,
    "font.family": "sans-serif",
    "axes.labelsize": 12,
    "axes.titlesize": 13,
    "lines.linewidth": 2.2,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.3,
    "savefig.facecolor": "white",
    "axes.titlepad": 18,  # spazio sotto il titolo
})

BBOX_LABEL = dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="gray", alpha=0.92)


def save(fig, name):
    out = OUT / f"{name}.svg"
    fig.savefig(out, format="svg")
    plt.close(fig)
    print(f"  ✓ {out.name}")


def smooth_stall(a, alpha_stall, cl_max, slope=0.11, alpha_zero=-2):
    """Curva CL-alpha con picco ESATTAMENTE a (alpha_stall, cl_max).

    Il tratto lineare arriva all'85% di cl_max, poi una parabola monotonamente
    crescente raggiunge il picco a alpha_stall. Garantisce che il MASSIMO
    della curva sia in (alpha_stall, cl_max), evitando picchi spurii.
    """
    cl = np.zeros_like(a, dtype=float)
    # Calcoliamo dove finisce il lineare per arrivare all'85% del max
    cl_lin_end = 0.85 * cl_max
    a_lin_end = alpha_zero + cl_lin_end / slope
    # Sicurezza: a_lin_end deve essere strettamente prima di alpha_stall
    if a_lin_end >= alpha_stall:
        a_lin_end = alpha_stall - 2
        cl_lin_end = slope * (a_lin_end - alpha_zero)
    for i, x in enumerate(a):
        if x <= a_lin_end:
            cl[i] = slope * (x - alpha_zero)
        elif x <= alpha_stall:
            # Parabola con vertice in (alpha_stall, cl_max), passa per (a_lin_end, cl_lin_end)
            k = (cl_max - cl_lin_end) / (alpha_stall - a_lin_end) ** 2
            cl[i] = cl_max - k * (x - alpha_stall) ** 2
        else:
            # Crollo lineare ripido dopo lo stallo
            cl[i] = cl_max - 0.18 * (x - alpha_stall)
    return cl


# ─── 1. Curva C_p vs α (Lezione 2) ─────────────────────────────
def curva_cl_alpha():
    fig, ax = plt.subplots(figsize=(9, 5.5))
    a = np.linspace(-4, 22, 500)
    cl = smooth_stall(a, alpha_stall=16, cl_max=1.5, alpha_zero=-2)
    ax.plot(a, cl, color="#1976d2", linewidth=2.8, zorder=3)
    ax.axhline(0, color="black", linewidth=0.6)
    ax.axvline(0, color="black", linewidth=0.6)

    # Punto di stallo (in alto a destra)
    ax.scatter([16], [1.5], color="#d32f2f", s=130, zorder=5, edgecolors="black", linewidths=1.2)
    ax.annotate("STALLO\n$α = 16°$, $C_{L,max} = 1{,}5$",
                xy=(16, 1.5), xytext=(17.5, 0.9),
                fontsize=10, color="#d32f2f", fontweight="bold",
                arrowprops=dict(arrowstyle="->", color="#d32f2f", lw=1.5),
                bbox=BBOX_LABEL, ha="left")

    # Tratto lineare evidenziato
    ax.axvspan(0, 12, color="#1976d2", alpha=0.06, zorder=1)
    ax.text(6, -0.5, "Tratto lineare\n$C_p = 0{,}11(α + 2°)$",
            color="#0d47a1", fontsize=10, ha="center", bbox=BBOX_LABEL)

    # alpha_zero
    ax.scatter([-2], [0], color="#43a047", s=80, zorder=5)
    ax.annotate("$α_0 = -2°$ (NACA 2412)",
                xy=(-2, 0), xytext=(0.5, -0.7),
                fontsize=10, color="#2e7d32",
                arrowprops=dict(arrowstyle="->", color="#2e7d32", lw=1.2),
                bbox=BBOX_LABEL, ha="left")

    ax.set_xlabel("Angolo di attacco α (gradi)")
    ax.set_ylabel("Coefficiente di portanza $C_p$")
    ax.set_title("Curva $C_p$–α di un profilo NACA 2412")
    ax.set_xlim(-5, 22)
    ax.set_ylim(-1, 2.0)
    ax.grid(True, alpha=0.3)
    save(fig, "curva-cl-alpha")


# ─── 2. Polare totale = parassita + indotta (Lezione 3) ────────
def polare_decomposta():
    fig, ax = plt.subplots(figsize=(9, 5.5))
    cl = np.linspace(0, 1.4, 200)
    cd_0 = 0.025
    pi_lambda_e = np.pi * 10 * 0.85
    cd_indotta = cl ** 2 / pi_lambda_e
    cd_totale = cd_0 + cd_indotta

    ax.plot(cl, np.full_like(cl, cd_0), "--", color="#fb8c00", linewidth=2,
            label=f"Parassita $C_{{D,0}}$ = {cd_0} (costante)")
    ax.plot(cl, cd_indotta, "--", color="#43a047", linewidth=2,
            label=r"Indotta $C_p^2 / (\pi \lambda e)$")
    ax.plot(cl, cd_totale, color="#1976d2", linewidth=3,
            label="Totale $C_R$ = parassita + indotta")

    cl_star = np.sqrt(pi_lambda_e * cd_0)
    ax.axvline(cl_star, color="#d32f2f", linestyle=":", linewidth=2, alpha=0.8)
    ax.scatter([cl_star], [2 * cd_0], color="#d32f2f", s=100, zorder=5,
               edgecolors="black", linewidths=1.2)
    ax.annotate(f"$E_{{max}}$\n$C_p^*$ = {cl_star:.2f}\nparassita = indotta",
                xy=(cl_star, 2 * cd_0), xytext=(1.05, 0.04),
                fontsize=10, color="#d32f2f", fontweight="bold",
                arrowprops=dict(arrowstyle="->", color="#d32f2f", lw=1.5),
                bbox=BBOX_LABEL, ha="left")

    ax.set_xlabel("Coefficiente di portanza $C_p$")
    ax.set_ylabel("Coefficiente di resistenza $C_R$")
    ax.set_title("Decomposizione della resistenza: parassita + indotta")
    ax.set_xlim(0, 1.45)
    ax.set_ylim(0, 0.105)
    ax.legend(loc="upper left", fontsize=10)
    ax.grid(True, alpha=0.3)
    save(fig, "polare-decomposta")


# ─── 3. Polare con tangente per E_max (Lezione 4) ──────────────
def polare_con_tangente():
    fig, ax = plt.subplots(figsize=(9, 6))
    pi_lambda_e = np.pi * 10 * 0.85
    cd_0 = 0.025
    cl = np.linspace(0, 1.5, 300)
    cd = cd_0 + cl ** 2 / pi_lambda_e

    cl_star = np.sqrt(pi_lambda_e * cd_0)
    cd_star = 2 * cd_0
    e_max = cl_star / cd_star

    ax.plot(cd, cl, color="#1976d2", linewidth=2.8, label="Polare $C_p(C_R)$")

    cd_line = np.linspace(0, 0.13, 50)
    ax.plot(cd_line, e_max * cd_line, "--", color="#d32f2f", linewidth=2,
            label=f"Tangente all'origine: $E_{{max}}$ = {e_max:.1f}")

    # Punto E_max
    ax.scatter([cd_star], [cl_star], color="#d32f2f", s=120, zorder=5,
               edgecolors="black", linewidths=1.2)
    ax.annotate(f"$E_{{max}}$ = {e_max:.1f}\n$C_p^*$ = {cl_star:.2f}",
                xy=(cd_star, cl_star), xytext=(0.085, 1.3),
                fontsize=11, color="#d32f2f", fontweight="bold",
                arrowprops=dict(arrowstyle="->", color="#d32f2f", lw=1.5),
                bbox=BBOX_LABEL, ha="left")

    # Crociera
    cd_cr = cd_0 + 0.5 ** 2 / pi_lambda_e
    ax.scatter([cd_cr], [0.5], color="#43a047", s=100, zorder=5,
               edgecolors="black", linewidths=1.2)
    ax.annotate("Crociera\n($C_p \\approx 0{,}5$)",
                xy=(cd_cr, 0.5), xytext=(0.08, 0.30),
                fontsize=10, color="#2e7d32",
                arrowprops=dict(arrowstyle="->", color="#2e7d32", lw=1.2),
                bbox=BBOX_LABEL, ha="left")

    # Stallo
    ax.scatter([cd[-1]], [cl[-1]], color="#fb8c00", s=100, zorder=5,
               edgecolors="black", linewidths=1.2)
    ax.annotate("Stallo\n$C_{L,max}$",
                xy=(cd[-1], cl[-1]), xytext=(0.135, 1.1),
                fontsize=10, color="#e65100",
                arrowprops=dict(arrowstyle="->", color="#e65100", lw=1.2),
                bbox=BBOX_LABEL, ha="left")

    ax.set_xlabel("Coefficiente di resistenza $C_R$")
    ax.set_ylabel("Coefficiente di portanza $C_p$")
    ax.set_title("Polare di velivolo con punto di massima efficienza")
    ax.set_xlim(0, 0.17)
    ax.set_ylim(0, 1.7)
    ax.legend(loc="lower right", fontsize=10)
    ax.grid(True, alpha=0.3)
    save(fig, "polare-tangente-emax")


# ─── 4. Curva CL-α: pulita, +flap, +slat (Lezione 9) ──────────
def curva_cl_flap_slat():
    fig, ax = plt.subplots(figsize=(9, 5.5))
    a = np.linspace(-5, 28, 500)

    cl_pulito = smooth_stall(a, alpha_stall=16, cl_max=1.4, alpha_zero=-2)
    cl_flap = smooth_stall(a, alpha_stall=14, cl_max=2.0, alpha_zero=-8)
    cl_flap_slat = smooth_stall(a, alpha_stall=22, cl_max=2.8, alpha_zero=-8)

    ax.plot(a, cl_pulito, color="#1976d2", linewidth=2.6, label="Pulito ($C_{L,max}$ = 1,4 a 16°)")
    ax.plot(a, cl_flap, color="#43a047", linewidth=2.6, label="+ Flap ($C_{L,max}$ = 2,0 a 14°)")
    ax.plot(a, cl_flap_slat, color="#d32f2f", linewidth=2.6, label="+ Flap + Slat ($C_{L,max}$ = 2,8 a 22°)")

    ax.scatter([16, 14, 22], [1.4, 2.0, 2.8],
               color=["#1976d2", "#43a047", "#d32f2f"],
               s=80, zorder=5, edgecolors="black", linewidths=1)

    ax.axhline(0, color="black", linewidth=0.6)
    ax.axvline(0, color="black", linewidth=0.6)
    ax.set_xlabel("Angolo di attacco α (gradi)")
    ax.set_ylabel("Coefficiente di portanza $C_p$")
    ax.set_title("Effetto di flap e slat sulla curva $C_p$–α")
    ax.set_xlim(-6, 28)
    ax.set_ylim(-0.5, 3.4)
    ax.legend(loc="upper left", fontsize=10)
    ax.grid(True, alpha=0.3)
    save(fig, "curva-cl-flap-slat")


# ─── 5. Polare 737 con punti tabulati (Esercizio 10) ──────────
def polare_737_punti():
    fig, ax = plt.subplots(figsize=(9, 6))
    pi_lambda_e = np.pi * 10 * 0.85
    cd_0 = 0.025
    cl_smooth = np.linspace(0, 1.4, 300)
    cd_smooth = cd_0 + cl_smooth ** 2 / pi_lambda_e

    cl_punti = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.82, 1.0, 1.2, 1.4])
    cd_punti = cd_0 + cl_punti ** 2 / pi_lambda_e

    ax.plot(cd_smooth, cl_smooth, color="#1976d2", linewidth=2.5,
            label="Polare $C_R = C_{D,0} + C_p^2/(πλe)$")
    ax.scatter(cd_punti, cl_punti, color="#1976d2", s=70, zorder=5,
               edgecolors="black", linewidths=1.2)

    cl_star = 0.82
    cd_star = 2 * cd_0
    e_max = cl_star / cd_star
    cd_line = np.linspace(0, 0.13, 50)
    ax.plot(cd_line, e_max * cd_line, "--", color="#d32f2f", linewidth=1.8,
            label=f"$E_{{max}}$ = {e_max:.1f} (tangente all'origine)")

    # Annotazioni dei punti notevoli — POSIZIONATE BENE A DESTRA
    annotations = [
        (0.5, "Crociera reale\n$C_p = 0{,}5$, $E = 14{,}5$", "#fb8c00", 0.075, 0.30),
        (0.82, f"$E_{{max}}$ = {e_max:.1f}\n$C_p^*$ = 0,82", "#d32f2f", 0.085, 0.95),
        (1.4, f"Stallo\n$C_{{L,max}}$ = 1,4", "#7b1fa2", 0.13, 1.55),
    ]
    for cl_v, label, color, tx, ty in annotations:
        idx = np.argmin(np.abs(cl_punti - cl_v))
        cd_p = cd_punti[idx]
        marker = "*" if abs(cl_v - 0.5) < 0.01 else "o"
        size = 200 if marker == "*" else 100
        ax.scatter([cd_p], [cl_v], color=color, s=size, marker=marker,
                   zorder=6, edgecolors="black", linewidths=1.2)
        ax.annotate(label, xy=(cd_p, cl_v), xytext=(tx, ty),
                    fontsize=9, color=color, fontweight="bold",
                    arrowprops=dict(arrowstyle="->", color=color, lw=1.2),
                    bbox=BBOX_LABEL, ha="left")

    ax.axvline(cd_0, color="#888", linestyle=":", alpha=0.6)
    ax.text(cd_0 + 0.001, 0.05, "$C_{D,0}$ = 0,025\n(asintoto)",
            fontsize=9, color="#666", style="italic")

    ax.set_xlabel("Coefficiente di resistenza $C_R$")
    ax.set_ylabel("Coefficiente di portanza $C_p$")
    ax.set_title("Polare del Boeing 737-800 (modello del liceo)")
    ax.set_xlim(0, 0.17)
    ax.set_ylim(0, 1.75)
    ax.legend(loc="lower right", fontsize=9)
    ax.grid(True, alpha=0.3)
    save(fig, "polare-737")


# ─── 6. Profilo alare schematico (Lezione 1) ──────────────────
def profilo_alare():
    fig, ax = plt.subplots(figsize=(9, 4.5))
    x = np.linspace(0, 1, 200)
    m, p, t = 0.02, 0.4, 0.12
    yc = np.where(x < p, m / p ** 2 * (2 * p * x - x ** 2),
                  m / (1 - p) ** 2 * ((1 - 2 * p) + 2 * p * x - x ** 2))
    yt = 5 * t * (0.2969 * np.sqrt(x) - 0.1260 * x - 0.3516 * x ** 2 +
                  0.2843 * x ** 3 - 0.1015 * x ** 4)
    yu = yc + yt
    yl = yc - yt

    ax.fill_between(x, yu, yl, color="#bbdefb", alpha=0.7, edgecolor="#1976d2", linewidth=2)
    ax.plot(x, yc, "--", color="#d32f2f", linewidth=1.5, label="Linea media")
    ax.plot([0, 1], [0, 0], "-", color="black", linewidth=1, label="Corda (c)")

    ax.annotate("Bordo d'attacco\n(arrotondato)", xy=(0, 0), xytext=(-0.15, 0.10),
                fontsize=10, color="#1565c0", fontweight="bold",
                arrowprops=dict(arrowstyle="->", color="#1565c0", lw=1.2),
                bbox=BBOX_LABEL, ha="left")
    ax.annotate("Bordo d'uscita\n(tagliente)", xy=(1, 0), xytext=(1.08, -0.06),
                fontsize=10, color="#1565c0", fontweight="bold",
                arrowprops=dict(arrowstyle="->", color="#1565c0", lw=1.2),
                bbox=BBOX_LABEL, ha="left")

    x_t = 0.30
    yt_at_xt = 5 * t * (0.2969 * np.sqrt(x_t) - 0.1260 * x_t - 0.3516 * x_t ** 2 +
                         0.2843 * x_t ** 3 - 0.1015 * x_t ** 4)
    yc_at_xt = m / p ** 2 * (2 * p * x_t - x_t ** 2)
    ax.annotate("", xy=(x_t, yc_at_xt + yt_at_xt), xytext=(x_t, yc_at_xt - yt_at_xt),
                arrowprops=dict(arrowstyle="<->", color="#7b1fa2", lw=2))
    ax.text(x_t + 0.025, yc_at_xt - 0.005, "spessore max\n12% c", fontsize=9,
            color="#6a1b9a", bbox=BBOX_LABEL)

    x_c = 0.40
    yc_at_xc = m / p ** 2 * (2 * p * x_c - x_c ** 2)
    ax.annotate("", xy=(x_c, yc_at_xc), xytext=(x_c, 0),
                arrowprops=dict(arrowstyle="<->", color="#388e3c", lw=1.5))
    ax.text(x_c - 0.27, -0.06, "freccia $f$ = 2% c", fontsize=9,
            color="#1b5e20", bbox=BBOX_LABEL)

    ax.set_xlim(-0.3, 1.45)
    ax.set_ylim(-0.18, 0.20)
    ax.set_aspect("equal")
    ax.set_title("Profilo alare NACA 2412 (Cessna 172)")
    ax.legend(loc="lower right", fontsize=9, framealpha=0.95)
    ax.axis("off")
    save(fig, "profilo-naca-2412")


# ─── 7. Schema forze in volo livellato (Esercizio 1, 3) ──────
def schema_forze():
    fig, ax = plt.subplots(figsize=(8, 6))
    box = mp.FancyBboxPatch((-0.5, -0.18), 1.0, 0.36,
                             boxstyle="round,pad=0.05",
                             edgecolor="#1976d2", facecolor="#e3f2fd", linewidth=2)
    ax.add_patch(box)
    ax.text(0, 0, "Velivolo", ha="center", va="center",
            fontsize=12, fontweight="bold", color="#0d47a1")

    arrow_len = 0.85
    head = dict(head_width=0.08, head_length=0.10, length_includes_head=True)
    # Portanza ↑
    ax.arrow(0, 0.2, 0, arrow_len, fc="#d32f2f", ec="#d32f2f", linewidth=3, **head)
    ax.text(0.08, 0.7, "P (portanza)", fontsize=13, color="#b71c1c", fontweight="bold")
    # Peso ↓
    ax.arrow(0, -0.2, 0, -arrow_len, fc="#388e3c", ec="#388e3c", linewidth=3, **head)
    ax.text(0.08, -0.7, "Q = m·g (peso)", fontsize=13, color="#1b5e20", fontweight="bold")
    # Spinta →
    ax.arrow(0.5, 0, arrow_len, 0, fc="#fb8c00", ec="#fb8c00", linewidth=3, **head)
    ax.text(0.7, 0.10, "T (spinta)", fontsize=13, color="#e65100", fontweight="bold")
    # Resistenza ←
    ax.arrow(-0.5, 0, -arrow_len, 0, fc="#7b1fa2", ec="#7b1fa2", linewidth=3, **head)
    ax.text(-1.4, 0.10, "R (resistenza)", fontsize=13, color="#4a148c", fontweight="bold")

    ax.text(0, -1.6, "Volo livellato a velocità costante:",
            ha="center", fontsize=12, fontweight="bold")
    ax.text(0, -1.85, "L = W   (equilibrio verticale)", ha="center", fontsize=11)
    ax.text(0, -2.05, "T = D   (equilibrio orizzontale)", ha="center", fontsize=11)

    ax.set_xlim(-1.8, 1.8)
    ax.set_ylim(-2.3, 1.3)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Sistema delle 4 forze sul velivolo")
    save(fig, "forze-volo-livellato")


# ─── 8. Atmosfera ISA: T, p, ρ vs quota (Lezione 5) ──────────
def atmosfera_isa():
    fig, axes = plt.subplots(1, 3, figsize=(13, 5.5), sharey=True)
    h = np.linspace(0, 20000, 500)
    T0 = 288.15
    T = np.where(h <= 11000, T0 - 0.0065 * h, 216.65)
    p0 = 101325
    p = np.where(h <= 11000, p0 * (T / T0) ** 5.256,
                  22632 * np.exp(-9.81 / (287 * 216.65) * (h - 11000)))
    rho = p / (287 * T)

    for ax, x, color, xlabel, title in [
        (axes[0], T - 273.15, "#d32f2f", "Temperatura T (°C)", "T vs quota"),
        (axes[1], p / 1000, "#1976d2", "Pressione p (kPa)", "p vs quota"),
        (axes[2], rho, "#43a047", "Densità ρ (kg/m³)", "ρ vs quota"),
    ]:
        ax.plot(x, h / 1000, color=color, linewidth=2.5)
        ax.axhline(11, color="black", linestyle="--", linewidth=1, alpha=0.5)
        ax.set_xlabel(xlabel)
        ax.set_title(title)
        ax.grid(True, alpha=0.3)

    axes[0].text(-50, 12, "Tropopausa (11 km)", fontsize=10, color="#444",
                 bbox=BBOX_LABEL)
    axes[0].text(-78, 18, "STRATOSFERA\n(T costante)", fontsize=10, color="#444",
                 fontweight="bold", bbox=BBOX_LABEL)
    axes[0].text(-78, 4, "TROPOSFERA\n(T cala -6,5°C/km)", fontsize=10, color="#444",
                 fontweight="bold", bbox=BBOX_LABEL)

    axes[0].set_ylabel("Quota (km)")
    axes[0].set_xlim(-80, 25)
    axes[0].set_ylim(0, 21)

    fig.suptitle("Atmosfera Standard ISA — Troposfera + Stratosfera inferiore",
                 fontsize=14, fontweight="bold", y=1.00)
    plt.tight_layout()
    save(fig, "atmosfera-isa")


# ─── 9. Confronto profili NACA 2412 vs 0012 (Esercizio 6) ────
def confronto_profili_naca():
    fig, ax = plt.subplots(figsize=(9, 5.5))
    a = np.linspace(-5, 22, 500)
    cl_2412 = smooth_stall(a, alpha_stall=16, cl_max=1.55, alpha_zero=-2)
    cl_0012 = smooth_stall(a, alpha_stall=14, cl_max=1.40, alpha_zero=0)

    ax.plot(a, cl_2412, color="#1976d2", linewidth=2.8,
            label="NACA 2412 (asimmetrico, Cessna)")
    ax.plot(a, cl_0012, color="#d32f2f", linewidth=2.6,
            label="NACA 0012 (simmetrico)")

    # alpha_zero punti
    ax.scatter([-2, 0], [0, 0], color="black", s=70, zorder=5)
    ax.annotate("$α_0 = -2°$ (2412)", xy=(-2, 0), xytext=(-4.5, -0.55),
                fontsize=10, color="#1565c0",
                arrowprops=dict(arrowstyle="->", color="#1565c0", lw=1.2),
                bbox=BBOX_LABEL, ha="left")
    ax.annotate("$α_0 = 0°$ (0012)", xy=(0, 0), xytext=(2, -0.55),
                fontsize=10, color="#b71c1c",
                arrowprops=dict(arrowstyle="->", color="#b71c1c", lw=1.2),
                bbox=BBOX_LABEL, ha="left")

    # Differenza costante: misurata in zona libera (a=5)
    a_show = 5
    cl_2412_show = 0.11 * (a_show + 2)
    cl_0012_show = 0.11 * a_show
    ax.annotate("", xy=(a_show, cl_2412_show), xytext=(a_show, cl_0012_show),
                arrowprops=dict(arrowstyle="<->", color="#7b1fa2", lw=1.8))
    ax.text(a_show + 0.5, (cl_2412_show + cl_0012_show) / 2,
            "$ΔC_p = 0{,}22$\n(costante)", fontsize=10, color="#6a1b9a",
            bbox=BBOX_LABEL)

    # Picchi
    ax.scatter([16, 14], [1.55, 1.40], color=["#1976d2", "#d32f2f"],
               s=80, zorder=5, edgecolors="black", linewidths=1)

    ax.axhline(0, color="black", linewidth=0.6)
    ax.axvline(0, color="black", linewidth=0.6)
    ax.set_xlabel("Angolo di attacco α (gradi)")
    ax.set_ylabel("Coefficiente di portanza $C_p$")
    ax.set_title("Confronto profili NACA: 2412 (asimmetrico) vs 0012 (simmetrico)")
    ax.set_xlim(-5, 22)
    ax.set_ylim(-0.85, 1.85)
    ax.legend(loc="upper left", fontsize=10)
    ax.grid(True, alpha=0.3)
    save(fig, "confronto-profili-naca")


# ─── 10. Diedro: confronto +/0/- (Lezione 7) ──────────────────
def diedro_confronto():
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    cases = [
        ("Diedro positivo (+5°)", 5, "#43a047", "Stabile lateralmente\n(turismo, jet di linea)"),
        ("Diedro zero (0°)", 0, "#1976d2", "Neutro\n(addestramento)"),
        ("Anhedral (−5°)", -5, "#d32f2f", "Instabile = agile\n(caccia, F-104)"),
    ]
    for ax, (title, angle_deg, color, note) in zip(axes, cases):
        angle = np.deg2rad(angle_deg)
        fus = mp.Rectangle((-0.3, -0.15), 0.6, 0.3, color="#444", zorder=3)
        ax.add_patch(fus)
        wing_len = 1.4
        x_end_r = 0.3 + wing_len * np.cos(angle)
        y_end_r = wing_len * np.sin(angle)
        ax.plot([0.3, x_end_r], [0, y_end_r], color=color, linewidth=10,
                solid_capstyle="round", zorder=2)
        x_end_l = -0.3 - wing_len * np.cos(angle)
        ax.plot([-0.3, x_end_l], [0, y_end_r], color=color, linewidth=10,
                solid_capstyle="round", zorder=2)
        ax.plot([-2, 2], [0, 0], "--", color="#aaa", linewidth=1)
        if angle_deg != 0:
            arc = mp.Arc((0.3, 0), 0.7, 0.7, angle=0,
                          theta1=0 if angle_deg > 0 else angle_deg,
                          theta2=angle_deg if angle_deg > 0 else 0,
                          color="#7b1fa2", lw=2)
            ax.add_patch(arc)
            ax.text(0.85, 0.07 if angle_deg > 0 else -0.18,
                    f"{angle_deg:+}°", fontsize=12, color="#6a1b9a",
                    fontweight="bold")
        ax.set_xlim(-2.2, 2.2)
        ax.set_ylim(-0.8, 0.8)
        ax.set_aspect("equal")
        ax.set_title(title, fontsize=12, color=color, fontweight="bold")
        ax.text(0, -0.6, note, ha="center", fontsize=10, color="#444",
                style="italic", bbox=BBOX_LABEL)
        ax.axis("off")

    fig.suptitle("Diedro: angolo verticale tra ala e orizzontale (vista frontale)",
                 fontsize=13, fontweight="bold", y=1.0)
    plt.tight_layout()
    save(fig, "diedro-confronto")


# ─── 11. Geometrie ali: rettangolare, trapezoidale, delta (L7) ─
def geometrie_alari():
    """Vista dall'alto: fusoliera ORIZZONTALE (verso destra), ali ESPANSE in verticale.
    Per chi guarda: il muso del velivolo è a sinistra, le ali si aprono in alto e in basso."""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    b_half = 3.5  # semi-apertura alare (verticale nel grafico)

    # ─── Rettangolare (Cessna)
    ax = axes[0]
    cr = 1.0  # corda costante
    # Ala destra (in alto nella vista): rettangolo da y=0.3 (radice) a y=b_half (tip)
    # Coordinate: x = posizione lungo la corda (avanti-indietro), y = posizione lungo apertura
    fus_l, fus_r, fus_w = -1.5, 1.5, 0.3  # fusoliera orizzontale
    # Fusoliera centrale
    ax.add_patch(mp.Rectangle((fus_l, -fus_w/2), fus_r - fus_l, fus_w,
                                facecolor="#444", edgecolor="black", linewidth=1, zorder=3))
    # Cono muso
    ax.plot([fus_l, fus_l - 0.5, fus_l], [-fus_w/2, 0, fus_w/2], color="#444", linewidth=1)
    ax.fill([fus_l, fus_l - 0.5, fus_l], [-fus_w/2, 0, fus_w/2], color="#444")
    # Ala superiore (rettangolo)
    ax.add_patch(mp.Rectangle((-cr/2, fus_w/2), cr, b_half - fus_w/2,
                                facecolor="#bbdefb", edgecolor="#1976d2", linewidth=2.5, zorder=2))
    # Ala inferiore (specchio)
    ax.add_patch(mp.Rectangle((-cr/2, -b_half), cr, b_half - fus_w/2,
                                facecolor="#bbdefb", edgecolor="#1976d2", linewidth=2.5, zorder=2))
    ax.set_title("Rettangolare (τ = 1)", fontweight="bold")
    ax.text(0, -b_half - 0.5, "Cessna 172\nλ ≈ 7,5", ha="center", fontsize=11,
            fontweight="bold", bbox=BBOX_LABEL)
    ax.text(-1.7, b_half + 0.3, "↑ apertura $b$", fontsize=9, color="#666")
    ax.text(0.7, fus_w/2 + 0.3, "← corda $c$ →", fontsize=9, color="#666")
    ax.set_xlim(-2.8, 2.8); ax.set_ylim(-b_half - 1.0, b_half + 0.8)
    ax.set_aspect("equal"); ax.axis("off")

    # ─── Trapezoidale (Boeing 737)
    ax = axes[1]
    cr, ct = 1.5, 0.5
    ax.add_patch(mp.Rectangle((fus_l, -fus_w/2), fus_r - fus_l, fus_w,
                                facecolor="#444", edgecolor="black", linewidth=1, zorder=3))
    ax.plot([fus_l, fus_l - 0.5, fus_l], [-fus_w/2, 0, fus_w/2], color="#444", linewidth=1)
    ax.fill([fus_l, fus_l - 0.5, fus_l], [-fus_w/2, 0, fus_w/2], color="#444")
    # Ala superiore trapezoidale: radice (cr, a y=fus_w/2), tip (ct, a y=b_half)
    pts_top = [(-cr/2, fus_w/2), (cr/2, fus_w/2), (ct/2, b_half), (-ct/2, b_half)]
    ax.add_patch(mp.Polygon(pts_top, closed=True, facecolor="#c8e6c9",
                             edgecolor="#43a047", linewidth=2.5, zorder=2))
    pts_bot = [(p[0], -p[1]) for p in pts_top]
    ax.add_patch(mp.Polygon(pts_bot, closed=True, facecolor="#c8e6c9",
                             edgecolor="#43a047", linewidth=2.5, zorder=2))
    # Etichette c_r e c_t — c_r FUORI dalla zona scura della fusoliera
    ax.annotate("", xy=(-cr/2, b_half + 0.15), xytext=(cr/2, b_half + 0.15),
                arrowprops=dict(arrowstyle="<->", color="#7b1fa2", lw=1.5))
    ax.text(1.0, b_half - 0.4, "$c_r$ (radice)", fontsize=10,
            color="#6a1b9a", fontweight="bold", bbox=BBOX_LABEL)
    ax.annotate("", xy=(-ct/2, b_half + 0.45), xytext=(ct/2, b_half + 0.45),
                arrowprops=dict(arrowstyle="<->", color="#7b1fa2", lw=1.5))
    ax.text(0, b_half + 0.65, "$c_t$ (tip)", ha="center", fontsize=10,
            color="#6a1b9a", fontweight="bold")
    ax.set_title("Trapezoidale (τ ≈ 0,33)", fontweight="bold")
    ax.text(0, -b_half - 0.5, "Boeing 737\nλ ≈ 10", ha="center", fontsize=11,
            fontweight="bold", bbox=BBOX_LABEL)
    ax.set_xlim(-2.8, 2.8); ax.set_ylim(-b_half - 1.0, b_half + 0.85)
    ax.set_aspect("equal"); ax.axis("off")

    # ─── Delta a freccia (Eurofighter)
    ax = axes[2]
    fus_l_d, fus_r_d = -2.0, 2.0
    cr = fus_r_d - fus_l_d  # corda alla radice = lunghezza fusoliera
    b_half_d = 2.0
    sweep = np.deg2rad(53)
    # Corda all'estremità: 0 (delta puro)
    # Ala superiore triangolare: bordo d'attacco (avanti) inclinato indietro di 53°
    # Vertici: (fus_l_d, fus_w/2) leading edge alla radice, (fus_r_d, fus_w/2) trailing edge alla radice
    # tip: arretrato di b_half_d * tan(sweep) → x = fus_l_d + b_half_d * tan(sweep)
    x_tip = fus_l_d + b_half_d * np.tan(sweep)
    pts_top = [(fus_l_d, fus_w/2), (fus_r_d, fus_w/2), (x_tip, b_half_d)]
    ax.add_patch(mp.Polygon(pts_top, closed=True, facecolor="#ffcdd2",
                             edgecolor="#d32f2f", linewidth=2.5, zorder=2))
    pts_bot = [(p[0], -p[1]) for p in pts_top]
    ax.add_patch(mp.Polygon(pts_bot, closed=True, facecolor="#ffcdd2",
                             edgecolor="#d32f2f", linewidth=2.5, zorder=2))
    # Fusoliera (sopra)
    ax.add_patch(mp.Rectangle((fus_l_d, -fus_w/2), cr, fus_w,
                                facecolor="#444", edgecolor="black", linewidth=1, zorder=3))
    # Cono muso
    ax.plot([fus_l_d, fus_l_d - 0.5, fus_l_d], [-fus_w/2, 0, fus_w/2], color="#444")
    ax.fill([fus_l_d, fus_l_d - 0.5, fus_l_d], [-fus_w/2, 0, fus_w/2], color="#444")
    # Angolo freccia
    arc = mp.Arc((fus_l_d, fus_w/2), 1.5, 1.5, angle=0, theta1=0,
                  theta2=90 - 53, color="#7b1fa2", lw=2)
    ax.add_patch(arc)
    ax.text(fus_l_d + 0.85, fus_w/2 + 0.4, "Λ = 53°", fontsize=10,
            color="#6a1b9a", fontweight="bold", bbox=BBOX_LABEL)
    ax.set_title("Delta a freccia (Λ ≈ 53°)", fontweight="bold")
    ax.text(0, -b_half_d - 0.5, "Eurofighter\nλ ≈ 2,4", ha="center", fontsize=11,
            fontweight="bold", bbox=BBOX_LABEL)
    ax.set_xlim(-3.0, 3.0); ax.set_ylim(-b_half_d - 1.0, b_half_d + 0.6)
    ax.set_aspect("equal"); ax.axis("off")

    fig.suptitle("Geometrie alari (vista dall'alto, muso a sinistra)",
                 fontsize=14, fontweight="bold", y=1.0)
    plt.tight_layout()
    save(fig, "geometrie-alari")


# ─── 12. Planata aliante (Esercizio 4) ─────────────────────────
def planata_aliante():
    fig, ax = plt.subplots(figsize=(9, 5))
    quota = 1.0; distanza = 4.5
    ax.plot([0, distanza], [quota, 0], color="#1976d2", linewidth=3,
            label="Traiettoria di planata")
    ax.plot([0, 0], [0, quota], "--", color="#666", linewidth=1.5)
    ax.plot([0, distanza], [0, 0], "-", color="#888", linewidth=2)

    # Aliante
    ax.scatter([0], [quota], color="#d32f2f", s=250, zorder=5, marker="^",
               edgecolors="black", linewidths=1.5)
    ax.text(-0.15, quota + 0.08, "Aliante\n(quota h)", fontsize=11,
            color="#b71c1c", fontweight="bold", ha="right", bbox=BBOX_LABEL)

    # Atterraggio
    ax.scatter([distanza], [0], color="#43a047", s=150, zorder=5, marker="v",
               edgecolors="black", linewidths=1.5)
    ax.text(distanza + 0.1, -0.05, "Atterraggio", fontsize=11,
            color="#1b5e20", fontweight="bold", bbox=BBOX_LABEL)

    # distanza
    ax.text(distanza / 2, -0.25, "distanza = E · h",
            fontsize=13, ha="center", color="#0d47a1", fontweight="bold",
            bbox=BBOX_LABEL)
    # quota
    ax.text(-0.15, quota / 2, "h", fontsize=14, ha="right", color="#666",
            fontweight="bold")

    # Angolo gamma
    arc = mp.Arc((0, quota), 0.7, 0.5, angle=0, theta1=270, theta2=270 + 14,
                  color="#7b1fa2", lw=2)
    ax.add_patch(arc)
    ax.text(0.42, quota - 0.32, "γ\n(angolo planata)\ntan γ = 1/E",
            fontsize=10, color="#6a1b9a", bbox=BBOX_LABEL)

    ax.set_xlim(-1.2, distanza + 1.2)
    ax.set_ylim(-0.5, 1.4)
    ax.set_aspect("equal")
    ax.set_title("Planata stabilizzata di un aliante: distanza al suolo = E × quota persa")
    ax.grid(True, alpha=0.2)
    ax.set_xticks([]); ax.set_yticks([])
    save(fig, "planata-aliante")


# ─── 13. Planata con vento contrario (Esercizio 8) ─────────────
def planata_con_vento():
    fig, ax = plt.subplots(figsize=(10, 5))
    quota = 1.0
    distanza_aria = 4.5
    distanza_suolo = 2.8
    # Traiettoria aria (tratteggiata grigia)
    ax.plot([0, distanza_aria], [quota, 0], "--", color="#888", linewidth=2.5, alpha=0.8)
    ax.text(distanza_aria - 0.5, 0.20, "senza vento\n(in aria)", fontsize=9,
            color="#666", style="italic", ha="center")
    # Traiettoria al suolo (blu solida)
    ax.plot([0, distanza_suolo], [quota, 0], color="#1976d2", linewidth=3)
    ax.text(distanza_suolo / 2 - 0.2, 0.55, "con vento\n(al suolo)", fontsize=9,
            color="#1565c0", fontweight="bold", ha="center")
    ax.plot([0, 0], [0, quota], "--", color="#666", linewidth=1.5)
    ax.plot([0, max(distanza_aria, distanza_suolo) + 0.3], [0, 0], "-",
            color="#888", linewidth=2)

    # Aliante
    ax.scatter([0], [quota], color="#d32f2f", s=250, zorder=5, marker="^",
               edgecolors="black", linewidths=1.5)
    ax.text(-0.2, quota + 0.08, "Aliante\nh = 1500 m", fontsize=10,
            color="#b71c1c", fontweight="bold", ha="right", bbox=BBOX_LABEL)

    # Atterraggio (con vento)
    ax.scatter([distanza_suolo], [0], color="#43a047", s=150, zorder=5,
               marker="v", edgecolors="black", linewidths=1.5)

    # Frecce vento spostate IN ALTO (sopra le traiettorie)
    for x in [1.5, 2.5, 3.5]:
        ax.annotate("", xy=(x - 0.4, 1.20), xytext=(x, 1.20),
                    arrowprops=dict(arrowstyle="->", color="#fb8c00", lw=2.5))
    ax.text(2.5, 1.35, "VENTO CONTRARIO 20 kt", fontsize=11, color="#e65100",
            ha="center", fontweight="bold", bbox=BBOX_LABEL)

    # Etichette distanze SOTTO il piano del suolo
    ax.annotate("", xy=(0, -0.25), xytext=(distanza_aria, -0.25),
                arrowprops=dict(arrowstyle="<->", color="#888", lw=1.5))
    ax.text(distanza_aria / 2, -0.40, f"Senza vento: {distanza_aria:.1f} unità",
            ha="center", fontsize=10, color="#444", bbox=BBOX_LABEL)
    ax.annotate("", xy=(0, -0.65), xytext=(distanza_suolo, -0.65),
                arrowprops=dict(arrowstyle="<->", color="#1976d2", lw=2))
    ax.text(distanza_suolo / 2, -0.80, f"Con vento: {distanza_suolo:.1f} (-38%)",
            ha="center", fontsize=10, color="#1565c0", fontweight="bold",
            bbox=BBOX_LABEL)

    ax.set_xlim(-1.5, distanza_aria + 0.8)
    ax.set_ylim(-1.1, 1.6)
    ax.set_aspect("equal")
    ax.set_title("Planata con vento contrario: la distanza al suolo si riduce")
    ax.set_xticks([]); ax.set_yticks([])
    save(fig, "planata-con-vento")


# ─── 14. Sequenza decollo V_S → V_R → V_2 (Esercizio 9) ───────
def sequenza_decollo():
    fig, ax = plt.subplots(figsize=(11, 5.5))
    # Pista
    ax.fill_between([0, 10], -0.05, 0.05, color="#666", alpha=0.4)
    ax.text(5, -0.85, "PISTA", ha="center", fontsize=12, color="#444",
            fontweight="bold")

    # Punti chiave: label SOPRA i pallini (più chiaro), traiettoria sotto
    points = [
        (0.5, 0, "V = 0\n(fermo)", "#666", 0.45),
        (5, 0.05, "$V_R = 1{,}1 \\cdot V_S$\n(rotazione)", "#fb8c00", 0.55),
        (8.5, 1.0, "$V_2 = 1{,}2 \\cdot V_S$\n(decollo sicuro)\n+35 ft AGL", "#43a047", 0.55),
    ]
    for x, y, label, color, label_dy in points:
        ax.scatter([x], [y], color=color, s=300, zorder=5, marker="o",
                   edgecolors="black", linewidths=1.8)
        ax.text(x, y + label_dy, label, ha="center", fontsize=10,
                color=color, fontweight="bold", bbox=BBOX_LABEL)

    # Traiettoria
    xs = np.linspace(0.5, 10, 200)
    ys = np.where(xs < 5, 0,
                  np.where(xs < 8.5, 0.05 + (xs - 5) ** 1.7 * 0.08,
                           1.0 + (xs - 8.5) * 0.22))
    ax.plot(xs, ys, color="#1976d2", linewidth=2.5, alpha=0.6, zorder=3)

    # Frecce di accelerazione (più piccole, sotto la pista)
    for x in [1.5, 2.5, 3.5]:
        ax.annotate("", xy=(x + 0.5, -0.35), xytext=(x, -0.35),
                    arrowprops=dict(arrowstyle="->", color="#1976d2", lw=2))
    ax.text(2.7, -0.55, "accelerazione", fontsize=9, color="#1976d2",
            ha="center", style="italic")

    ax.text(5, 2.3, "Sequenza decollo", ha="center", fontsize=15,
            fontweight="bold")
    ax.text(5, 2.05,
            "0 → $V_R$: corsa al suolo · $V_R$ → $V_2$: salita iniziale",
            ha="center", fontsize=10, color="#444")

    ax.set_xlim(-0.5, 11)
    ax.set_ylim(-1.2, 2.6)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "sequenza-decollo")


# ─── 15. Schema stallo (Esercizio 2) ───────────────────────────
def schema_stallo():
    fig, ax = plt.subplots(figsize=(9, 5.5))
    a = np.linspace(-2, 22, 500)
    cl = smooth_stall(a, alpha_stall=16, cl_max=1.5, alpha_zero=-2)

    ax.plot(a, cl, color="#1976d2", linewidth=2.8, zorder=3)

    # Picco
    ax.scatter([16], [1.5], color="#d32f2f", s=140, zorder=5,
               edgecolors="black", linewidths=1.5)
    ax.annotate("STALLO\n$α = 16°$\n$C_{L,max} = 1{,}5$\nportanza < peso\n→ aereo scende",
                xy=(16, 1.5), xytext=(18, 0.7),
                fontsize=10, color="#d32f2f", fontweight="bold",
                arrowprops=dict(arrowstyle="->", color="#d32f2f", lw=1.5),
                bbox=BBOX_LABEL, ha="left")

    ax.axvspan(0, 16, color="#43a047", alpha=0.08, zorder=1)
    ax.text(8, 0.30, "REGIME OPERATIVO\n(α < α_stallo)", fontsize=11,
            color="#1b5e20", ha="center", fontweight="bold",
            bbox=BBOX_LABEL)

    ax.axvspan(16, 22, color="#d32f2f", alpha=0.10, zorder=1)
    ax.text(19, 0.30, "PERICOLO\n(stallo)", fontsize=10,
            color="#b71c1c", ha="center", fontweight="bold",
            bbox=BBOX_LABEL)

    ax.axhline(0, color="black", linewidth=0.6)
    ax.axvline(0, color="black", linewidth=0.6)
    ax.set_xlabel("Angolo di attacco α (gradi)")
    ax.set_ylabel("Coefficiente di portanza $C_p$")
    ax.set_title("Lo stallo: punto critico oltre cui $C_p$ crolla")
    ax.set_xlim(-1, 22)
    ax.set_ylim(0, 2.0)
    ax.grid(True, alpha=0.3)
    save(fig, "schema-stallo")


# ─── 16. NACA 4-cifre nomenclatura (Lezione 1) ─────────────────
def naca_codice():
    fig, ax = plt.subplots(figsize=(9, 4))
    # Grandi cifre del codice
    ax.text(0.5, 0.7, "NACA   2", fontsize=42, fontweight="bold", ha="right", color="#1976d2")
    ax.text(0.6, 0.7, "4", fontsize=42, fontweight="bold", ha="left", color="#43a047")
    ax.text(0.85, 0.7, "12", fontsize=42, fontweight="bold", ha="left", color="#d32f2f")
    # Frecce e annotazioni
    ax.annotate("Curvatura max\n= 2% della corda", xy=(0.50, 0.65), xytext=(0.10, 0.20),
                fontsize=11, color="#0d47a1", fontweight="bold",
                arrowprops=dict(arrowstyle="->", color="#0d47a1", lw=1.5),
                bbox=BBOX_LABEL, ha="center")
    ax.annotate("Posizione curvatura max\n= 4 decimi = 40% della corda",
                xy=(0.65, 0.65), xytext=(0.50, 0.20),
                fontsize=11, color="#1b5e20", fontweight="bold",
                arrowprops=dict(arrowstyle="->", color="#1b5e20", lw=1.5),
                bbox=BBOX_LABEL, ha="center")
    ax.annotate("Spessore max\n= 12% della corda", xy=(0.93, 0.65), xytext=(0.92, 0.20),
                fontsize=11, color="#b71c1c", fontweight="bold",
                arrowprops=dict(arrowstyle="->", color="#b71c1c", lw=1.5),
                bbox=BBOX_LABEL, ha="center")
    ax.set_xlim(0, 1.05)
    ax.set_ylim(0, 1)
    ax.axis("off")
    ax.set_title("Codice NACA 4-cifre — esempio: NACA 2412 (Cessna 172)",
                 fontsize=13, fontweight="bold")
    save(fig, "naca-4-cifre")


# ─── 17. Bernoulli + Newton — schema portanza (Lezione 2) ─────
def schema_portanza_bernoulli_newton():
    fig, ax = plt.subplots(figsize=(10, 5))
    # Profilo NACA 2412 (riuso)
    x = np.linspace(0, 1, 200)
    m, p, t = 0.04, 0.4, 0.14
    yc = np.where(x < p, m / p ** 2 * (2 * p * x - x ** 2),
                  m / (1 - p) ** 2 * ((1 - 2 * p) + 2 * p * x - x ** 2))
    yt = 5 * t * (0.2969 * np.sqrt(x) - 0.1260 * x - 0.3516 * x ** 2 +
                  0.2843 * x ** 3 - 0.1015 * x ** 4)
    ax.fill_between(x, yc + yt, yc - yt, color="#bbdefb", alpha=0.8,
                    edgecolor="#1976d2", linewidth=2.2, zorder=3)

    # Frecce flusso che entra
    for y in [0.18, 0.10, -0.10, -0.18]:
        ax.annotate("", xy=(0.0, y), xytext=(-0.25, y),
                    arrowprops=dict(arrowstyle="->", color="#666", lw=1.5))
    ax.text(-0.28, 0, "flusso V\n(aria)", fontsize=11, color="#444",
            ha="right", fontweight="bold")

    # Frecce pressione bassa (sopra) - vanno via dall'ala (suzione)
    for x_arr in [0.25, 0.45, 0.65]:
        y_arr = yc[int(x_arr*200)] + yt[int(x_arr*200)] + 0.02
        ax.annotate("", xy=(x_arr, y_arr + 0.18), xytext=(x_arr, y_arr),
                    arrowprops=dict(arrowstyle="->", color="#d32f2f", lw=2))
    # Etichetta pressione bassa SOPRA le frecce, a destra (no overlap con PORTANZA)
    ax.text(0.85, 0.30, "PRESSIONE BASSA (sopra)\n→ aria 'tira su' l'ala",
            fontsize=10, color="#b71c1c", fontweight="bold", ha="left",
            bbox=BBOX_LABEL)

    # Frecce pressione alta (sotto) - spingono l'ala verso l'alto
    for x_arr in [0.30, 0.55, 0.75]:
        y_arr = yc[int(x_arr*200)] - yt[int(x_arr*200)] - 0.02
        ax.annotate("", xy=(x_arr, y_arr + 0.04), xytext=(x_arr, y_arr - 0.12),
                    arrowprops=dict(arrowstyle="->", color="#43a047", lw=2))
    ax.text(0.85, -0.30, "PRESSIONE ALTA (sotto)\n→ aria 'spinge su' l'ala",
            fontsize=10, color="#1b5e20", fontweight="bold", ha="left",
            bbox=BBOX_LABEL)

    # Freccia downwash (Newton) — più in basso a destra per non sovrapporre
    ax.annotate("", xy=(1.35, -0.45), xytext=(1.05, 0),
                arrowprops=dict(arrowstyle="->", color="#fb8c00", lw=2.5))
    ax.text(1.45, -0.50, "downwash\n(aria deviata\n verso il basso)",
            fontsize=10, color="#e65100", fontweight="bold",
            bbox=BBOX_LABEL, va="top", ha="left")

    # Risultato netto: portanza grossa, in posizione separata
    ax.annotate("", xy=(0.40, 0.55), xytext=(0.40, 0.15),
                arrowprops=dict(arrowstyle="->", color="#7b1fa2", lw=4))
    ax.text(-0.25, 0.50, "PORTANZA L\n(forza NETTA\nverso l'alto)",
            fontsize=11, color="#4a148c", fontweight="bold", ha="left",
            bbox=BBOX_LABEL)

    ax.set_xlim(-0.45, 2.10)
    ax.set_ylim(-0.85, 0.70)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Come nasce la portanza — Bernoulli (pressioni) + Newton (downwash)",
                 fontsize=13, fontweight="bold")
    save(fig, "schema-bernoulli-newton")


# ─── 18. Freccia/Sweep — confronto angoli (Lezione 7) ─────────
def freccia_sweep():
    fig, axes = plt.subplots(1, 3, figsize=(13, 4.5))
    cases = [
        ("Λ = 0°\n(Cessna)", 0, "#1976d2"),
        ("Λ = 25°\n(Boeing 737)", 25, "#43a047"),
        ("Λ = 53°\n(Eurofighter)", 53, "#d32f2f"),
    ]
    for ax, (title, sweep_deg, color) in zip(axes, cases):
        sweep = np.deg2rad(sweep_deg)
        # Fusoliera centrale (orizzontale, muso a sinistra)
        ax.add_patch(mp.Rectangle((-1.5, -0.12), 3.0, 0.24,
                                    facecolor="#444", zorder=3))
        ax.plot([-1.5, -2.0, -1.5], [-0.12, 0, 0.12], color="#444")
        ax.fill([-1.5, -2.0, -1.5], [-0.12, 0, 0.12], color="#444")
        # Ala superiore: bordo d'attacco da (-0.5, 0) inclinato di sweep
        b_half = 1.7
        x_le_root = -0.5
        x_te_root = 0.7
        # Punta avanzata indietro per sweep
        x_le_tip = x_le_root + b_half * np.tan(sweep)
        x_te_tip = x_te_root + b_half * np.tan(sweep)
        ala = [(x_le_root, 0.12), (x_te_root, 0.12),
               (x_te_tip, b_half), (x_le_tip, b_half)]
        ax.add_patch(mp.Polygon(ala, closed=True, facecolor=color, alpha=0.4,
                                 edgecolor=color, linewidth=2, zorder=2))
        # Mirror sotto
        ala2 = [(p[0], -p[1]) for p in ala]
        ax.add_patch(mp.Polygon(ala2, closed=True, facecolor=color, alpha=0.4,
                                 edgecolor=color, linewidth=2, zorder=2))
        # Linea perpendicolare di riferimento (per visualizzare l'angolo)
        ax.plot([x_le_root, x_le_root], [0, b_half], "--", color="#888", lw=1)
        # Arco angolo se non zero
        if sweep_deg > 0:
            arc = mp.Arc((x_le_root, 0), 1.0, 1.0, angle=0,
                          theta1=90 - sweep_deg, theta2=90,
                          color="#7b1fa2", lw=2)
            ax.add_patch(arc)
            ax.text(x_le_root + 0.2, 0.6, f"{sweep_deg}°", fontsize=12,
                    color="#6a1b9a", fontweight="bold", bbox=BBOX_LABEL)
        ax.set_xlim(-2.3, 2.5)
        ax.set_ylim(-b_half - 0.4, b_half + 0.4)
        ax.set_aspect("equal")
        ax.set_title(title, fontsize=12, color=color, fontweight="bold")
        ax.axis("off")
    fig.suptitle("Freccia (sweep) Λ — angolo del bordo d'attacco rispetto alla perpendicolare",
                 fontsize=13, fontweight="bold", y=1.0)
    plt.tight_layout()
    save(fig, "freccia-sweep")


# ─── 19. Stabilità statica — CG davanti vs dietro al CP (L8) ──
def stabilita_cg():
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.5))

    for ax, titolo, x_cg, x_cp, color, esito in [
        (axes[0], "STABILE: CG davanti al CP", -0.4, 0.0, "#43a047",
         "Raffica → muso su → momento di richiamo → torna giù\n✓ aereo torna da solo all'equilibrio"),
        (axes[1], "INSTABILE: CG dietro al CP", 0.4, 0.0, "#d32f2f",
         "Raffica → muso su → momento amplifica → stallo\n✗ aereo diverge, serve fly-by-wire"),
    ]:
        # Fusoliera
        ax.add_patch(mp.FancyBboxPatch((-1.5, -0.15), 3.0, 0.3,
                                         boxstyle="round,pad=0.02",
                                         facecolor="#bbdefb",
                                         edgecolor="#1976d2", linewidth=2))
        # Cono muso
        ax.plot([-1.5, -2.0, -1.5], [-0.15, 0, 0.15], color="#1976d2", linewidth=2)
        ax.fill([-1.5, -2.0, -1.5], [-0.15, 0, 0.15], color="#bbdefb")
        # Coda
        ax.add_patch(mp.Polygon([(1.5, 0), (1.9, 0.4), (1.9, -0.4)],
                                 closed=True, facecolor="#bbdefb",
                                 edgecolor="#1976d2", linewidth=1.5))

        # CG (peso giù)
        ax.scatter([x_cg], [0], color="#388e3c", s=200, zorder=5,
                   edgecolors="black", linewidths=1.5, marker="o")
        ax.annotate("", xy=(x_cg, -0.55), xytext=(x_cg, -0.05),
                    arrowprops=dict(arrowstyle="->", color="#388e3c", lw=2.5))
        ax.text(x_cg, -0.7, f"CG\n(peso W)", ha="center", fontsize=10,
                color="#1b5e20", fontweight="bold", bbox=BBOX_LABEL)

        # CP (portanza su)
        ax.scatter([x_cp], [0], color="#d32f2f", s=200, zorder=5,
                   edgecolors="black", linewidths=1.5, marker="^")
        ax.annotate("", xy=(x_cp, 0.55), xytext=(x_cp, 0.05),
                    arrowprops=dict(arrowstyle="->", color="#d32f2f", lw=2.5))
        ax.text(x_cp, 0.65, f"CP\n(portanza L)", ha="center", fontsize=10,
                color="#b71c1c", fontweight="bold", bbox=BBOX_LABEL)

        ax.set_xlim(-2.3, 2.3)
        ax.set_ylim(-1.3, 1.0)
        ax.set_aspect("equal")
        ax.set_title(titolo, fontsize=12, color=color, fontweight="bold")
        ax.text(0, -1.15, esito, ha="center", fontsize=9, color="#444",
                style="italic", bbox=BBOX_LABEL)
        ax.axis("off")

    fig.suptitle("Stabilità statica longitudinale — la posizione relativa di CG e CP",
                 fontsize=13, fontweight="bold", y=1.0)
    plt.tight_layout()
    save(fig, "stabilita-cg")


# ─── 20. Busta di centraggio (W&B envelope) — Cessna 172 (L8) ──
def busta_centraggio():
    fig, ax = plt.subplots(figsize=(11, 3.5))
    # Asse percentuale MAC
    ax.set_xlim(0, 100)
    ax.set_ylim(-1, 2)
    # Busta verde (range ammissibile 15-36% MAC)
    ax.add_patch(mp.Rectangle((15, 0.2), 21, 0.6,
                                facecolor="#a5d6a7", edgecolor="#2e7d32",
                                linewidth=2, zorder=2))
    ax.text(25.5, 0.5, "BUSTA AMMISSIBILE\n(15% – 36% MAC)",
            ha="center", va="center", fontsize=11, color="#1b5e20",
            fontweight="bold")

    # Zona pericolo prima del 15%
    ax.add_patch(mp.Rectangle((0, 0.2), 15, 0.6, facecolor="#ffcdd2",
                                edgecolor="#c62828", linewidth=1, alpha=0.6, zorder=1))
    ax.text(7.5, 0.5, "STABILE\nMA INERTE", ha="center", va="center",
            fontsize=9, color="#b71c1c")
    # Zona pericolo dopo 36%
    ax.add_patch(mp.Rectangle((36, 0.2), 64, 0.6, facecolor="#ffcdd2",
                                edgecolor="#c62828", linewidth=1, alpha=0.6, zorder=1))
    ax.text(68, 0.5, "INSTABILE / STALLO NON RECUPERABILE",
            ha="center", va="center", fontsize=10, color="#b71c1c", fontweight="bold")

    # AC al 25%
    ax.axvline(25, color="#7b1fa2", linestyle="--", linewidth=2, alpha=0.7)
    ax.annotate("Centro aerodinamico\n(AC = 25% MAC)", xy=(25, 0.85),
                xytext=(25, 1.5), fontsize=10, color="#6a1b9a",
                arrowprops=dict(arrowstyle="->", color="#6a1b9a", lw=1.5),
                ha="center", bbox=BBOX_LABEL)

    # Ticks
    for x in [0, 15, 25, 36, 50, 75, 100]:
        ax.plot([x, x], [0.18, 0.13], color="black", lw=1)
        ax.text(x, 0.05, f"{x}%", ha="center", fontsize=9)

    ax.text(50, -0.5, "Posizione del CG (% MAC dal bordo d'attacco)",
            ha="center", fontsize=11, fontweight="bold")

    ax.axis("off")
    ax.set_title("Busta di centraggio del Cessna 172",
                 fontsize=13, fontweight="bold")
    save(fig, "busta-centraggio")


# ─── 21. 4 tipi di flap (Lezione 9) ────────────────────────────
def flap_tipi():
    fig, axes = plt.subplots(2, 2, figsize=(11, 6.5))
    types = [
        ("1. Plain (semplice)", "+0,3 in $C_{L,max}$\nCessna 172, ultraleggeri", "plain"),
        ("2. Slotted (a fessura)", "+0,5–0,7 in $C_{L,max}$\nGA moderna, regionali", "slotted"),
        ("3. Fowler (estensibile)", "+1,0–1,2 in $C_{L,max}$\n+15-25% superficie\nBoeing 737, A320", "fowler"),
        ("4. Multi-flap", "+1,2+ in $C_{L,max}$\n+30% superficie\nBoeing 747, A380", "multi"),
    ]
    for ax, (title, note, kind) in zip(axes.flat, types):
        # Profilo ala base (semplificato, senza flap)
        x = np.linspace(0, 0.7, 100)
        m, p, t = 0.02, 0.4, 0.10
        yc = np.where(x < p, m / p ** 2 * (2 * p * x - x ** 2),
                      m / (1 - p) ** 2 * ((1 - 2 * p) + 2 * p * x - x ** 2))
        yt = 5 * t * (0.2969 * np.sqrt(np.maximum(x, 1e-6)) - 0.1260 * x - 0.3516 * x ** 2 +
                      0.2843 * x ** 3 - 0.1015 * x ** 4)
        ax.fill_between(x, yc + yt, yc - yt, color="#bbdefb", edgecolor="#1976d2", linewidth=1.5)
        # Flap dipende dal tipo
        if kind == "plain":
            # Aletta che ruota verso il basso a 30°
            x_hinge = 0.7
            y_hinge_up = yc[-1] + yt[-1]
            y_hinge_dn = yc[-1] - yt[-1]
            angle = np.deg2rad(-30)
            flap_len = 0.25
            x_flap_end = x_hinge + flap_len * np.cos(angle)
            y_flap_end = (y_hinge_up + y_hinge_dn) / 2 + flap_len * np.sin(angle)
            ax.fill([x_hinge, x_flap_end + 0.02, x_flap_end - 0.02, x_hinge],
                    [y_hinge_up, y_flap_end + 0.015, y_flap_end - 0.015, y_hinge_dn],
                    color="#fb8c00", edgecolor="#e65100", linewidth=1.5)
        elif kind == "slotted":
            # Flap separato da fessura
            x_hinge = 0.7
            angle = np.deg2rad(-25)
            flap_len = 0.27
            slot_dx, slot_dy = 0.04, -0.025
            x_pivot = x_hinge + slot_dx
            y_pivot = -0.02 + slot_dy
            x_flap_end = x_pivot + flap_len * np.cos(angle)
            y_flap_end = y_pivot + flap_len * np.sin(angle)
            ax.fill([x_pivot - 0.01, x_flap_end + 0.02, x_flap_end - 0.01, x_pivot - 0.04],
                    [y_pivot + 0.02, y_flap_end + 0.015, y_flap_end - 0.015, y_pivot - 0.02],
                    color="#fb8c00", edgecolor="#e65100", linewidth=1.5)
            # Fessura indicata con freccia
            ax.annotate("fessura", xy=(x_hinge + 0.02, -0.005), xytext=(0.5, 0.22),
                        fontsize=9, color="#444",
                        arrowprops=dict(arrowstyle="->", color="#444", lw=1))
        elif kind == "fowler":
            # Flap traslato indietro + abbassato
            x_pivot = 0.85
            angle = np.deg2rad(-25)
            flap_len = 0.30
            x_flap_end = x_pivot + flap_len * np.cos(angle)
            y_flap_end = -0.05 + flap_len * np.sin(angle)
            ax.fill([x_pivot - 0.03, x_flap_end + 0.02, x_flap_end - 0.01, x_pivot - 0.06],
                    [-0.02, y_flap_end + 0.015, y_flap_end - 0.015, -0.05],
                    color="#fb8c00", edgecolor="#e65100", linewidth=1.5)
            # Freccia "scivolato indietro"
            ax.annotate("scivola\nindietro", xy=(x_pivot - 0.03, 0), xytext=(0.55, 0.18),
                        fontsize=9, color="#444",
                        arrowprops=dict(arrowstyle="->", color="#444", lw=1))
        elif kind == "multi":
            # 3 flap consecutivi a fessure
            colors_f = ["#fb8c00", "#f57c00", "#e65100"]
            for i, c in enumerate(colors_f):
                x_pivot = 0.74 + i * 0.07
                angle = np.deg2rad(-15 - i * 5)
                flap_len = 0.18
                x_end = x_pivot + flap_len * np.cos(angle)
                y_end = -0.05 + flap_len * np.sin(angle) - i * 0.03
                ax.fill([x_pivot - 0.02, x_end + 0.015, x_end - 0.01, x_pivot - 0.04],
                        [-0.01 - i*0.03, y_end + 0.015, y_end - 0.01, -0.04 - i*0.03],
                        color=c, edgecolor="#bf360c", linewidth=1.2)

        ax.set_xlim(-0.05, 1.25)
        ax.set_ylim(-0.35, 0.30)
        ax.set_aspect("equal")
        ax.set_title(title, fontsize=11, fontweight="bold", color="#0d47a1")
        ax.text(0.6, -0.30, note, ha="center", fontsize=9, color="#444",
                style="italic", bbox=BBOX_LABEL)
        ax.axis("off")

    fig.suptitle("I 4 tipi di flap — dal più semplice al più sofisticato",
                 fontsize=14, fontweight="bold", y=1.0)
    plt.tight_layout()
    save(fig, "flap-tipi")


# ─── 22. Slat con fessura (Lezione 9) ──────────────────────────
def slat_fessura():
    fig, axes = plt.subplots(1, 2, figsize=(11, 4))

    for ax, (titolo, esteso) in zip(axes, [("Ala normale (slat retratta)", False),
                                              ("Slat estesa: fessura sul bordo d'attacco", True)]):
        # Profilo principale
        x = np.linspace(0.05, 0.75, 100)
        m, p, t = 0.02, 0.4, 0.12
        yc = np.where(x < p, m / p ** 2 * (2 * p * x - x ** 2),
                      m / (1 - p) ** 2 * ((1 - 2 * p) + 2 * p * x - x ** 2))
        yt = 5 * t * (0.2969 * np.sqrt(x) - 0.1260 * x - 0.3516 * x ** 2 +
                      0.2843 * x ** 3 - 0.1015 * x ** 4)
        ax.fill_between(x, yc + yt, yc - yt, color="#bbdefb",
                        edgecolor="#1976d2", linewidth=2)

        if esteso:
            # Slat: piccola superficie staccata avanti dell'ala principale
            xs = np.linspace(-0.05, 0.10, 40)
            yc_s = m / p ** 2 * (2 * p * xs - xs ** 2)
            yt_s = 5 * t * (0.2969 * np.sqrt(np.maximum(xs - (-0.05), 1e-6)) -
                            0.1260 * (xs - (-0.05)) - 0.3516 * (xs - (-0.05)) ** 2)
            ax.fill_between(xs, yc_s + yt_s + 0.005, yc_s - yt_s + 0.005,
                            color="#c8e6c9", edgecolor="#43a047", linewidth=1.5)
            # Etichetta fessura
            ax.annotate("Fessura\n(aria 'energizza'\n strato limite sopra)",
                        xy=(0.07, 0.04), xytext=(0.45, 0.20),
                        fontsize=9, color="#444",
                        arrowprops=dict(arrowstyle="->", color="#444", lw=1.2),
                        bbox=BBOX_LABEL)
            # Frecce di flusso che attraversano la fessura
            ax.annotate("", xy=(0.10, 0.05), xytext=(0.05, -0.03),
                        arrowprops=dict(arrowstyle="->", color="#fb8c00", lw=2))

        ax.set_xlim(-0.15, 0.85)
        ax.set_ylim(-0.20, 0.35)
        ax.set_aspect("equal")
        ax.set_title(titolo, fontsize=11, fontweight="bold")
        ax.axis("off")

    fig.suptitle("Slat al bordo d'attacco — ritarda lo stallo da ~16° a ~22°",
                 fontsize=13, fontweight="bold", y=1.0)
    plt.tight_layout()
    save(fig, "slat-fessura")


if __name__ == "__main__":
    print("Generazione SVG...")
    curva_cl_alpha()
    polare_decomposta()
    polare_con_tangente()
    curva_cl_flap_slat()
    polare_737_punti()
    profilo_alare()
    schema_forze()
    atmosfera_isa()
    confronto_profili_naca()
    diedro_confronto()
    geometrie_alari()
    planata_aliante()
    planata_con_vento()
    sequenza_decollo()
    schema_stallo()
    naca_codice()
    schema_portanza_bernoulli_newton()
    freccia_sweep()
    stabilita_cg()
    busta_centraggio()
    flap_tipi()
    slat_fessura()
    print("Fatto!")
