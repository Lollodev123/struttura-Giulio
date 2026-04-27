# Soluzione — Variante Esercizio 8

**Variante**: stesso aliante DG-1000, stessa quota (1500 m), stesso vento contrario (10,3 m/s), ma il pilota decide di volare **più veloce** a $V_2 = 32$ m/s invece di $V^* = 26{,}9$ m/s per "tagliare" il vento.

> 💡 **Approssimazione del liceo**: a velocità diversa da $V^*$, l'efficienza scende. Per un aliante di alta classe, possiamo stimare $E$ a $V_2$ usando il valore tipico $E(V_2) \approx 0{,}85 \cdot E_{max}$.

### Passo 1 — Efficienza a $V_2$

$$E(V_2) = 0{,}85 \cdot E_{max} = 0{,}85 \times 38{,}63 = 32{,}84$$

### Passo 2 — Velocità verticale (ratea di discesa)

$$V_z = \dfrac{V_2}{E(V_2)} = \dfrac{32}{32{,}84} = 0{,}974 \text{ m/s}$$

### Passo 3 — Tempo di volo fino al suolo

$$t = \dfrac{h}{V_z} = \dfrac{1\,500}{0{,}974} = 1\,540 \text{ s} \approx 25{,}7 \text{ minuti}$$

### Passo 4 — Velocità al suolo con vento

$$V_{ground} = V_2 - V_{wind} = 32 - 10{,}3 = 21{,}7 \text{ m/s}$$

### Passo 5 — Distanza al suolo

$$\text{distanza} = V_{ground} \times t = 21{,}7 \times 1\,540 = 33\,418 \text{ m} \approx 33{,}4 \text{ km}$$

### Confronto: $V^*$ vs $V_2$

| | $V^* = 26{,}9$ m/s | $V_2 = 32$ m/s | Differenza |
|---|---|---|---|
| Efficienza $E$ | 38,63 | 32,84 | $-15{,}0\%$ |
| Velocità verticale $V_z$ | 0,697 m/s | 0,974 m/s | $+39{,}7\%$ |
| Tempo di volo | 35,9 min | 25,7 min | $-28{,}4\%$ |
| Velocità al suolo | 16,6 m/s | 21,7 m/s | $+30{,}7\%$ |
| Distanza al suolo | 35,7 km | **33,4 km** | $-6{,}4\%$ |

### Lettura del confronto

Volando più veloce ($V_2$) con vento contrario:

- **Distanza percorsa al suolo**: scende solo del **6,4%** (33,4 km vs 35,7 km)
- **Tempo di volo**: scende del **28,4%** (10 minuti meno!)
- **Esposizione al vento**: meno tempo → vento "ti porta indietro" meno

In altre parole: **per soli 2,3 km di distanza in meno, arrivi 10 minuti prima**. Spesso conviene.

### MacCready in nuce

Questa è l'idea base della **teoria di Paul MacCready** (anni '50, fondamentale nel volo a vela competitivo):

> Con vento contrario: vola **più veloce** di $V^*$.
> Con vento in coda: vola **più lento** di $V^*$.
> In aria calma: vola a $V^*$.

Regola pratica semplificata: $V_{ottima} \approx V^* + V_{wind}/2$.

Per il nostro caso: $V_{ottima} \approx 26{,}9 + 10{,}3/2 = 32{,}05$ m/s ≈ **i 32 m/s del problema**!

> 🎓 **Take-away didattico**: piloti professionisti di alianti hanno questo concetto **interiorizzato**. Vedono il vento sul GPS, leggono il manuale del loro aliante, e regolano la velocità di crociera. Per noi, la lezione è che $V^*$ NON è sempre la velocità ottima operativa — solo in aria calma.
