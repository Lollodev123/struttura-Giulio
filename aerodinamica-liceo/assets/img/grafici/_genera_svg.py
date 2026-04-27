"""
Genera SVG dei grafici principali per il pacchetto didattico.
Esegui con: python3 _genera_svg.py

Output: SVG nella stessa cartella, da committare.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUT = Path(__file__).parent

# Stile didattico: chiaro, leggibile su mobile
plt.rcParams.update({
    "font.size": 12,
    "font.family": "sans-serif",
    "axes.labelsize": 13,
    "axes.titlesize": 14,
    "lines.linewidth": 2.2,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "savefig.bbox": "tight",
    "savefig.facecolor": "white",
})


def save(fig, name):
    out = OUT / f"{name}.svg"
    fig.savefig(out, format="svg")
    plt.close(fig)
    print(f"  ✓ {out.name}")


# ─── 1. Curva C_L vs α (Lezione 2 — Portanza) ────────────────────
def curva_cl_alpha():
    fig, ax = plt.subplots(figsize=(7, 4.5))
    a = np.linspace(-4, 20, 200)
    cl_lin = 0.11 * (a + 2)
    # Modello con stallo: tratto lineare fino a 12°, poi curva, picco a 16°, crollo
    cl = np.where(a <= 12, cl_lin,
                  np.where(a <= 16,
                           cl_lin[a <= 12][-1] + 0.05 * (a - 12) - 0.012 * (a - 12) ** 2,
                           1.5 - 0.15 * (a - 16)))
    cl_max_at = a[np.argmax(cl)]
    cl_max = max(cl)

    ax.plot(a, cl, color="#1976d2", linewidth=2.5)
    ax.axhline(0, color="black", linewidth=0.6)
    ax.axvline(0, color="black", linewidth=0.6)

    # Annotazioni punti chiave
    ax.scatter([cl_max_at], [cl_max], color="#d32f2f", s=80, zorder=5)
    ax.annotate("STALLO\n(α ≈ 16°, C_L,max ≈ 1,5)",
                xy=(cl_max_at, cl_max), xytext=(18, 1.3),
                fontsize=11, color="#d32f2f",
                arrowprops=dict(arrowstyle="->", color="#d32f2f"))

    # Tratto lineare evidenziato
    ax.fill_between([0, 12], -0.2, 1.6, color="#e3f2fd", alpha=0.5,
                    label="regime lineare")
    ax.text(6, -0.35, "regime lineare", color="#1565c0", fontsize=10, ha="center")

    # Punto α=0
    ax.scatter([0], [0.22], color="#43a047", s=60, zorder=5)
    ax.annotate("α₀ = -2°\n(NACA 2412)",
                xy=(-2, 0), xytext=(-3.5, -0.4),
                fontsize=10, color="#2e7d32",
                arrowprops=dict(arrowstyle="->", color="#2e7d32"))

    ax.set_xlabel("Angolo di attacco α (gradi)")
    ax.set_ylabel("Coefficiente di portanza  $C_L$")
    ax.set_title("Curva $C_L$–α di un profilo NACA 2412")
    ax.set_xlim(-5, 22)
    ax.set_ylim(-0.5, 1.8)
    ax.grid(True, alpha=0.3)
    save(fig, "curva-cl-alpha")


# ─── 2. Polare totale = parassita + indotta (Lezione 3) ──────────
def polare_decomposta():
    fig, ax = plt.subplots(figsize=(7, 4.5))
    cl = np.linspace(0, 1.4, 200)
    cd_0 = 0.025
    pi_lambda_e = np.pi * 10 * 0.85
    cd_indotta = cl ** 2 / pi_lambda_e
    cd_totale = cd_0 + cd_indotta

    ax.plot(cl, np.full_like(cl, cd_0), "--", color="#fb8c00",
            label=f"Parassita $C_{{D,0}}$ = {cd_0}", linewidth=2)
    ax.plot(cl, cd_indotta, "--", color="#43a047",
            label=r"Indotta $C_L^2 / (\pi \lambda e)$", linewidth=2)
    ax.plot(cl, cd_totale, color="#1976d2",
            label="Totale $C_D$", linewidth=2.8)

    # Punto di pareggio (parassita = indotta)
    cl_star = np.sqrt(pi_lambda_e * cd_0)
    ax.axvline(cl_star, color="#d32f2f", linestyle=":", alpha=0.7)
    ax.scatter([cl_star], [2 * cd_0], color="#d32f2f", s=70, zorder=5)
    ax.annotate(f"$E_{{max}}$\n($C_L^*$ ≈ {cl_star:.2f})",
                xy=(cl_star, 2 * cd_0), xytext=(0.95, 0.04),
                fontsize=11, color="#d32f2f",
                arrowprops=dict(arrowstyle="->", color="#d32f2f"))

    ax.set_xlabel("Coefficiente di portanza $C_L$")
    ax.set_ylabel("Coefficiente di resistenza $C_D$")
    ax.set_title("Decomposizione della resistenza: parassita + indotta")
    ax.set_xlim(0, 1.4)
    ax.set_ylim(0, 0.10)
    ax.legend(loc="upper left", fontsize=10)
    ax.grid(True, alpha=0.3)
    save(fig, "polare-decomposta")


# ─── 3. Polare con tangente per E_max (Lezione 4) ───────────────
def polare_con_tangente():
    fig, ax = plt.subplots(figsize=(7, 5.2))
    pi_lambda_e = np.pi * 10 * 0.85
    cd_0 = 0.025
    cl = np.linspace(0, 1.5, 300)
    cd = cd_0 + cl ** 2 / pi_lambda_e

    cl_star = np.sqrt(pi_lambda_e * cd_0)
    cd_star = 2 * cd_0
    e_max = cl_star / cd_star

    # Polare (assi scambiati: C_L su Y, C_D su X)
    ax.plot(cd, cl, color="#1976d2", linewidth=2.8, label="Polare $C_L(C_D)$")

    # Tangente all'origine = retta di max efficienza
    cd_line = np.linspace(0, 0.12, 50)
    cl_line = e_max * cd_line
    ax.plot(cd_line, cl_line, "--", color="#d32f2f", linewidth=2,
            label=f"Tangente: $E_{{max}}$ = {e_max:.1f}")

    # Punti notevoli
    ax.scatter([cd_star], [cl_star], color="#d32f2f", s=100, zorder=5)
    ax.annotate(f"$E_{{max}}$\n$C_L^*$ = {cl_star:.2f}\n$C_D^*$ = {cd_star:.3f}",
                xy=(cd_star, cl_star), xytext=(0.075, 1.25),
                fontsize=11, color="#d32f2f",
                arrowprops=dict(arrowstyle="->", color="#d32f2f"))

    # Punto crociera (esempio)
    cd_cr = cd_0 + 0.5 ** 2 / pi_lambda_e
    ax.scatter([cd_cr], [0.5], color="#43a047", s=80, zorder=5)
    ax.annotate("Crociera\n(C_L≈0,5)",
                xy=(cd_cr, 0.5), xytext=(0.065, 0.3),
                fontsize=10, color="#2e7d32",
                arrowprops=dict(arrowstyle="->", color="#2e7d32"))

    # Stallo
    ax.scatter([cd[-1]], [cl[-1]], color="#fb8c00", s=80, zorder=5)
    ax.annotate("Stallo\n$C_{L,max}$",
                xy=(cd[-1], cl[-1]), xytext=(0.13, 1.55),
                fontsize=10, color="#e65100",
                arrowprops=dict(arrowstyle="->", color="#e65100"))

    ax.set_xlabel("Coefficiente di resistenza $C_D$")
    ax.set_ylabel("Coefficiente di portanza $C_L$")
    ax.set_title("Polare di velivolo con punto di massima efficienza")
    ax.set_xlim(0, 0.16)
    ax.set_ylim(0, 1.7)
    ax.legend(loc="upper left", fontsize=10)
    ax.grid(True, alpha=0.3)
    save(fig, "polare-tangente-emax")


# ─── 4. Curva CL-α: pulita, +flap, +slat (Lezione 9) ──────────
def curva_cl_flap_slat():
    fig, ax = plt.subplots(figsize=(7, 4.8))
    a = np.linspace(-5, 28, 300)

    def cl_curva(a, cl_max, alpha_stallo, alpha_zero):
        slope = 0.11
        cl_lin = slope * (a - alpha_zero)
        # Tratto curvo vicino allo stallo
        cl_picco = cl_lin
        # Crollo dopo stallo
        out = np.where(a <= alpha_stallo - 4,
                       cl_lin,
                       np.where(a <= alpha_stallo,
                                slope * (alpha_stallo - 4 - alpha_zero) +
                                (cl_max - slope * (alpha_stallo - 4 - alpha_zero)) *
                                (1 - ((alpha_stallo - a) / 4) ** 2),
                                cl_max - 0.18 * (a - alpha_stallo)))
        return out

    cl_pulito = cl_curva(a, 1.4, 16, -2)
    cl_flap = cl_curva(a, 2.0, 14, -8)
    cl_flap_slat = cl_curva(a, 2.8, 22, -8)

    ax.plot(a, cl_pulito, color="#1976d2", linewidth=2.8, label="Pulito ($C_{L,max}$ = 1,4)")
    ax.plot(a, cl_flap, color="#43a047", linewidth=2.6, label="+ Flap ($C_{L,max}$ = 2,0)")
    ax.plot(a, cl_flap_slat, color="#d32f2f", linewidth=2.6,
            label="+ Flap + Slat ($C_{L,max}$ = 2,8)")

    # Annotazioni
    ax.scatter([16, 14, 22],
               [max(cl_pulito), max(cl_flap), max(cl_flap_slat)],
               color="black", s=50, zorder=5)

    ax.axhline(0, color="black", linewidth=0.6)
    ax.axvline(0, color="black", linewidth=0.6)

    ax.set_xlabel("Angolo di attacco α (gradi)")
    ax.set_ylabel("Coefficiente di portanza $C_L$")
    ax.set_title("Effetto di flap e slat sulla curva $C_L$–α")
    ax.set_xlim(-6, 28)
    ax.set_ylim(-0.5, 3.2)
    ax.legend(loc="upper left", fontsize=10)
    ax.grid(True, alpha=0.3)
    save(fig, "curva-cl-flap-slat")


# ─── 5. Polare 737 punto per punto (Esercizio 10) ────────────
def polare_737_punti():
    fig, ax = plt.subplots(figsize=(7, 5))
    pi_lambda_e = np.pi * 10 * 0.85
    cd_0 = 0.025
    cl_smooth = np.linspace(0, 1.4, 300)
    cd_smooth = cd_0 + cl_smooth ** 2 / pi_lambda_e

    # Punti tabulati
    cl_punti = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.82, 1.0, 1.2, 1.4])
    cd_punti = cd_0 + cl_punti ** 2 / pi_lambda_e
    e_punti = cl_punti / cd_punti

    ax.plot(cd_smooth, cl_smooth, color="#1976d2", linewidth=2.5, alpha=0.7, label="Polare $C_D = C_{D,0} + C_L^2/(πλe)$")
    ax.scatter(cd_punti, cl_punti, color="#1976d2", s=70, zorder=5,
               edgecolors="black", linewidths=1.2)

    # Etichette punti notevoli
    for cd, cl, e in zip(cd_punti, cl_punti, e_punti):
        if abs(cl - 0.5) < 0.01 or abs(cl - 0.82) < 0.01 or abs(cl - 1.4) < 0.01:
            ax.annotate(f"E={e:.1f}", xy=(cd, cl), xytext=(8, 5),
                        textcoords="offset points", fontsize=10)

    # Tangente E_max
    cl_star = 0.82
    cd_star = 2 * cd_0
    e_max = cl_star / cd_star
    cd_line = np.linspace(0, 0.13, 50)
    ax.plot(cd_line, e_max * cd_line, "--", color="#d32f2f",
            linewidth=1.6, label=f"$E_{{max}}$ = {e_max:.1f} (a $C_L^*$ = {cl_star})")

    # Crociera reale 737
    ax.scatter([0.0344], [0.5], color="#fb8c00", s=120, zorder=6,
               marker="*", edgecolors="black", linewidths=1)
    ax.annotate("Crociera 737\n(M=0,78)",
                xy=(0.0344, 0.5), xytext=(0.07, 0.3),
                fontsize=10, color="#e65100",
                arrowprops=dict(arrowstyle="->", color="#e65100"))

    ax.set_xlabel("Coefficiente di resistenza $C_D$")
    ax.set_ylabel("Coefficiente di portanza $C_L$")
    ax.set_title("Polare del Boeing 737-800 (modello del liceo)")
    ax.set_xlim(0, 0.16)
    ax.set_ylim(0, 1.6)
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(True, alpha=0.3)
    save(fig, "polare-737")


# ─── 6. Profilo alare schematico (Lezione 1) ──────────
def profilo_alare():
    fig, ax = plt.subplots(figsize=(8, 3.5))
    # Profilo NACA 2412 approssimato
    x = np.linspace(0, 1, 200)
    # Parametri NACA 2412: m=0.02, p=0.4, t=0.12
    m, p, t = 0.02, 0.4, 0.12
    # Camber line
    yc = np.where(x < p, m / p ** 2 * (2 * p * x - x ** 2),
                  m / (1 - p) ** 2 * ((1 - 2 * p) + 2 * p * x - x ** 2))
    # Thickness
    yt = 5 * t * (0.2969 * np.sqrt(x) - 0.1260 * x - 0.3516 * x ** 2 +
                  0.2843 * x ** 3 - 0.1015 * x ** 4)

    yu = yc + yt  # dorso
    yl = yc - yt  # ventre

    ax.fill_between(x, yu, yl, color="#bbdefb", alpha=0.7, edgecolor="#1976d2", linewidth=2)
    ax.plot(x, yc, "--", color="#d32f2f", linewidth=1.5, label="Linea media")
    ax.plot([0, 1], [0, 0], "-", color="black", linewidth=1, label="Corda (c)")

    # Annotazioni
    ax.annotate("Bordo d'attacco", xy=(0, 0), xytext=(-0.05, 0.06),
                fontsize=11, color="#1565c0",
                arrowprops=dict(arrowstyle="->", color="#1565c0"))
    ax.annotate("Bordo d'uscita", xy=(1, 0), xytext=(0.78, 0.06),
                fontsize=11, color="#1565c0",
                arrowprops=dict(arrowstyle="->", color="#1565c0"))

    # Spessore max (12% al ~30%)
    x_t = 0.30
    yt_at_xt = 5 * t * (0.2969 * np.sqrt(x_t) - 0.1260 * x_t - 0.3516 * x_t ** 2 +
                         0.2843 * x_t ** 3 - 0.1015 * x_t ** 4)
    yc_at_xt = m / p ** 2 * (2 * p * x_t - x_t ** 2)
    ax.annotate("", xy=(x_t, yc_at_xt + yt_at_xt), xytext=(x_t, yc_at_xt - yt_at_xt),
                arrowprops=dict(arrowstyle="<->", color="#7b1fa2", lw=1.5))
    ax.text(x_t + 0.02, 0.02, "spessore\nmax = 12%c", fontsize=9, color="#6a1b9a")

    # Curvatura max (al 40%)
    x_c = 0.40
    yc_at_xc = m / p ** 2 * (2 * p * x_c - x_c ** 2)
    ax.annotate("", xy=(x_c, yc_at_xc), xytext=(x_c, 0),
                arrowprops=dict(arrowstyle="<->", color="#388e3c", lw=1.2))
    ax.text(x_c - 0.18, -0.03, "freccia $f$\n= 2%c", fontsize=9, color="#1b5e20")

    ax.set_xlim(-0.15, 1.1)
    ax.set_ylim(-0.12, 0.18)
    ax.set_aspect("equal")
    ax.set_title("Profilo alare NACA 2412 (Cessna 172)")
    ax.legend(loc="upper right", fontsize=9)
    ax.axis("off")
    save(fig, "profilo-naca-2412")


# ─── 7. Schema forze in volo livellato (Esercizio 1) ──────
def schema_forze():
    fig, ax = plt.subplots(figsize=(7, 5))
    # Aereo (rettangolo arrotondato semplificato)
    from matplotlib.patches import FancyBboxPatch
    box = FancyBboxPatch((-0.5, -0.15), 1.0, 0.3,
                          boxstyle="round,pad=0.05",
                          edgecolor="#1976d2", facecolor="#e3f2fd", linewidth=2)
    ax.add_patch(box)
    ax.text(0, 0, "Cessna 172", ha="center", va="center", fontsize=12,
            fontweight="bold", color="#0d47a1")

    # Frecce delle 4 forze
    arrow_kw = dict(head_width=0.07, head_length=0.08, fc="#d32f2f", ec="#d32f2f",
                    linewidth=2.5, length_includes_head=True)

    # Portanza L (su)
    ax.arrow(0, 0.15, 0, 0.7, **arrow_kw)
    ax.text(0.05, 0.55, "L (portanza)", fontsize=12, color="#b71c1c", fontweight="bold")

    # Peso W (giù)
    ax.arrow(0, -0.15, 0, -0.7, fc="#388e3c", ec="#388e3c",
             head_width=0.07, head_length=0.08, linewidth=2.5, length_includes_head=True)
    ax.text(0.05, -0.55, "W = m·g (peso)", fontsize=12, color="#1b5e20", fontweight="bold")

    # Spinta T (avanti, →)
    ax.arrow(0.5, 0, 0.7, 0, fc="#fb8c00", ec="#fb8c00",
             head_width=0.07, head_length=0.08, linewidth=2.5, length_includes_head=True)
    ax.text(0.75, 0.08, "T (spinta)", fontsize=12, color="#e65100", fontweight="bold")

    # Resistenza D (indietro, ←)
    ax.arrow(-0.5, 0, -0.7, 0, fc="#7b1fa2", ec="#7b1fa2",
             head_width=0.07, head_length=0.08, linewidth=2.5, length_includes_head=True)
    ax.text(-1.15, 0.08, "D (resistenza)", fontsize=12, color="#4a148c", fontweight="bold")

    # Equilibrio
    ax.text(0, -1.3, "Volo livellato a velocità costante:",
            ha="center", fontsize=12, fontweight="bold")
    ax.text(0, -1.5, "L = W   (equilibrio verticale)", ha="center", fontsize=11)
    ax.text(0, -1.65, "T = D   (equilibrio orizzontale)", ha="center", fontsize=11)

    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.8, 1.0)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Sistema delle 4 forze sul velivolo")
    save(fig, "forze-volo-livellato")


# ─── 8. Atmosfera ISA: T, p, ρ vs quota (Lezione 5) ──────
def atmosfera_isa():
    fig, axes = plt.subplots(1, 3, figsize=(11, 5), sharey=True)
    # Tabella ISA fino a 11000 m (troposfera) + tratto stratosfera
    h = np.linspace(0, 20000, 500)
    T0 = 288.15
    T = np.where(h <= 11000, T0 - 0.0065 * h, 216.65)
    p0 = 101325
    p = np.where(h <= 11000, p0 * (T / T0) ** 5.256,
                  22632 * np.exp(-9.81 / (287 * 216.65) * (h - 11000)))
    rho = p / (287 * T)

    axes[0].plot(T - 273.15, h / 1000, color="#d32f2f", linewidth=2.5)
    axes[0].axhline(11, color="black", linestyle="--", linewidth=1, alpha=0.5)
    axes[0].text(-50, 11.4, "Tropopausa", fontsize=10)
    axes[0].set_xlabel("Temperatura T (°C)")
    axes[0].set_ylabel("Quota (km)")
    axes[0].set_title("T vs quota")
    axes[0].grid(True, alpha=0.3)
    axes[0].set_xlim(-80, 20)
    axes[0].set_ylim(0, 20)

    axes[1].plot(p / 1000, h / 1000, color="#1976d2", linewidth=2.5)
    axes[1].axhline(11, color="black", linestyle="--", linewidth=1, alpha=0.5)
    axes[1].set_xlabel("Pressione p (kPa)")
    axes[1].set_title("p vs quota (esponenziale)")
    axes[1].grid(True, alpha=0.3)

    axes[2].plot(rho, h / 1000, color="#43a047", linewidth=2.5)
    axes[2].axhline(11, color="black", linestyle="--", linewidth=1, alpha=0.5)
    axes[2].set_xlabel("Densità ρ (kg/m³)")
    axes[2].set_title("ρ vs quota")
    axes[2].grid(True, alpha=0.3)

    fig.suptitle("Atmosfera Standard ISA — Troposfera + Stratosfera inferiore",
                 fontsize=13, fontweight="bold", y=1.02)
    plt.tight_layout()
    save(fig, "atmosfera-isa")


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
    print("Fatto!")
