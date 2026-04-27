# Soluzione — Variante Esercizio 10

**Variante**: calcolare la velocità di **massima efficienza** $V^*$ del Boeing 737 (peso 65 000 kg, $S = 124{,}6$ m², $C_L^* = 0{,}817$) in **crociera FL350** (10 670 m), $\rho = 0{,}38$ kg/m³.

### Passo 1 — Peso

$$W = m \cdot g = 65\,000 \times 9{,}81 = 637\,650 \text{ N}$$

### Passo 2 — Applicazione della formula $V^*$

$$V^* = \sqrt{\dfrac{2W}{\rho S C_L^*}} = \sqrt{\dfrac{2 \times 637\,650}{0{,}38 \times 124{,}6 \times 0{,}817}}$$

Calcolo:

- Numeratore: $2 \times 637\,650 = 1\,275\,300$
- $0{,}38 \times 124{,}6 = 47{,}35$
- Denominatore: $47{,}35 \times 0{,}817 = 38{,}68$
- Rapporto: $1\,275\,300 / 38{,}68 = 32\,966$
- Radice: $\sqrt{32\,966} = 181{,}57$ m/s

$$\boxed{V^* \approx 181{,}6 \text{ m/s} = 353 \text{ kt}}$$

### Passo 3 — Confronto con velocità di crociera

| | Velocità (m/s) | Velocità (kt) | Mach |
|---|---|---|---|
| Crociera 737 a FL350 | 230 | 447 | 0,78 |
| $V^*$ (max efficienza) | 181,6 | 353 | 0,62 |
| Rapporto | 0,789 | 0,789 | — |

**In crociera, il 737 vola al 27% sopra la sua $V^*$**.

### Calcolo dell'efficienza in crociera vs $V^*$

A $V^* = 181{,}6$ m/s con $C_L = C_L^* = 0{,}817$ → $E_{max} = 16{,}34$ (vedi [Esercizio 10](../10-avanzato-polare-completa.md)).

A $V_{cruise} = 230$ m/s, calcoliamo $C_L$ con la stessa formula:

$$C_L = \dfrac{2W}{\rho V^2 S} = \dfrac{1\,275\,300}{0{,}38 \times 230^2 \times 124{,}6}$$

- $230^2 = 52\,900$
- $0{,}38 \times 52\,900 = 20\,102$
- Denominatore: $20\,102 \times 124{,}6 = 2\,504\,675$
- $C_L = 1\,275\,300 / 2\,504\,675 = 0{,}509$

$$C_D = 0{,}025 + \dfrac{0{,}509^2}{\pi \times 10 \times 0{,}85} = 0{,}025 + 0{,}00972 = 0{,}03472$$

$$E_{cruise} = \dfrac{0{,}509}{0{,}03472} = 14{,}66$$

**Riassunto**:

| | $C_L$ | $C_D$ | $E$ | % di $E_{max}$ |
|---|---|---|---|---|
| $V^*$ | 0,817 | 0,050 | **16,34** | 100% |
| Crociera reale | 0,509 | 0,035 | 14,66 | **89,7%** |

### Implicazione operativa

In crociera commerciale **si sacrifica il 10% dell'efficienza** per andare il **27% più veloce**. È un compromesso economico:

- $E$ minore → più carburante per km
- Ma velocità maggiore → meno tempo di volo → minor costo equipaggio + parcheggio gate + manutenzione + benessere passeggeri

In **emergenza** (avaria motori, spegnimento totale a 11 000 m), il pilota:

1. Spegne i motori funzionanti per minimizzare turbolenza
2. Rallenta a $V^*$ (~353 kt al peso del 737)
3. Plana a $E = 16{,}34$
4. Distanza al suolo: $E \cdot h = 16{,}34 \times 10{,}67$ km = **174 km**

Questa è la "sfera di scelta" del pilota in caso di avaria a FL350: ogni aeroporto entro 174 km è raggiungibile.

> 🎓 **Take-away didattico**: a velocità di crociera commerciale, l'aereo NON è al massimo della sua efficienza. È un **compromesso operativo consapevole**. In situazioni anomale (planata, ferry flight per riposizionare), il pilota cambia gioco e vola a $V^*$ — lì il velivolo dà il meglio di sé.
>
> Il **Gimli Glider** del 1983 (Boeing 767 senza carburante) volò a $V^*$ del 767, planando 100+ km da FL350 fino a una pista militare abbandonata di Gimli, Manitoba. Il pilota Bob Pearson era un appassionato di volo a vela e applicò la teoria della planata in tempo reale. Caso di studio dell'aviazione: la teoria del liceo che salva 69 vite.
