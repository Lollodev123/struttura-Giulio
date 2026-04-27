# Esercizio 8 — Velocità di max efficienza e planata con vento (aliante DG-1000)

> 🔴 **Difficoltà: AVANZATO** — Combina efficienza, velocità ottima e effetto del vento sulla planata.
>
> 🎯 **Obiettivi didattici**: imparare a (a) calcolare $V^*$ ed $E_{max}$, (b) capire come un vento contrario riduce la distanza al suolo, (c) ragionare in termini di "velocità ottimale di MacCready" — un classico del volo a vela.

---

## 📋 Testo del problema

Un **aliante DG-1000** è in planata stabilizzata a **1 500 m** sopra l'aeroporto di destinazione, in atmosfera ISA. Soffia un **vento contrario** (head wind) costante di **20 kt** = $10{,}3$ m/s lungo tutta la traiettoria.

Dati DG-1000:

- Massa con due piloti: $m = 700$ kg
- Superficie alare: $S = 16{,}7$ m²
- Allungamento: $\lambda = 24$
- Resistenza parassita: $C_{R,0} = 0{,}012$
- Fattore di Oswald: $e = 0{,}95$

**Determina**:

1. L'efficienza massima $E_{max}$ in aria calma
2. La velocità di max efficienza $V^*$ (rispetto all'aria) al livello mare
3. La velocità al suolo (groundspeed) durante la planata, con vento contrario di 20 kt
4. La distanza al suolo realmente percorsa dall'aliante (rispetto al terreno)

---

## 🖼️ Diagramma del problema

![Planata con vento contrario: la distanza al suolo si riduce](../assets/img/grafici/planata-con-vento.svg)

Con vento contrario di 20 kt, l'aliante mantiene $V^* = 26{,}9$ m/s **rispetto all'aria**, ma la sua **velocità al suolo** è ridotta: $V_{ground} = V^* - V_{wind} = 16{,}6$ m/s. La distanza al suolo realmente percorsa scende del **38%** rispetto al caso senza vento.

---

## 📊 Dati noti / da trovare

| Grandezza | Simbolo | Valore | Unità |
|---|---|---|---|
| Massa | $m$ | 700 | kg |
| Superficie alare | $S$ | 16,7 | m² |
| Allungamento | $\lambda$ | 24 | — |
| Resistenza parassita | $C_{R,0}$ | 0,012 | — |
| Fattore Oswald | $e$ | 0,95 | — |
| Densità (mare ISA) | $\rho$ | 1,225 | kg/m³ |
| Quota | $h$ | 1 500 | m |
| Vento contrario | $V_w$ | 10,3 | m/s |
| **Da trovare** | $E_{max}$, $V^*$, $V_g$, distanza terreno | ? | — |

---

## 🧠 Strategia di risoluzione

1. **Cosa mi sta chiedendo?** Efficienza, velocità ottima, ground speed, e distanza effettiva con vento.
2. **Quale fenomeno?** Equilibrio aerodinamico in planata + composizione del moto con il vento (matematica vettoriale di base).
3. **Quali formule?**
   - $E_{max} = \frac{1}{2}\sqrt{\pi \lambda e / C_{R,0}}$
   - $C_p^* = \sqrt{\pi \lambda e \cdot C_{R,0}}$
   - $V^* = \sqrt{2W/(\rho S C_p^*)}$
   - $V_{ground} = V_{air} - V_{wind}$ (vento contrario)
   - distanza al suolo = $E \times h \times (V_g/V^*)$

4. **Dati e unità coerenti?** Sì, tutto SI.
5. **Algebra**: catena di calcoli, attenzione al rapporto velocità.

---

## ✏️ Risoluzione passo-passo

### Passo 1 — Peso

$$Q = m \cdot g = 700 \times 9{,}81 = 6\,867 \text{ N}$$

### Passo 2 — $E_{max}$

$$E_{max} = \dfrac{1}{2}\sqrt{\dfrac{\pi \lambda e}{C_{R,0}}} = \dfrac{1}{2}\sqrt{\dfrac{\pi \times 24 \times 0{,}95}{0{,}012}}$$

Calcolo:

- $\pi \times 24 \times 0{,}95 = 71{,}63$
- $71{,}63/0{,}012 = 5\,969$
- $\sqrt{5\,969} = 77{,}26$
- $E_{max} = 77{,}26/2 = 38{,}63$

$$\boxed{E_{max} \approx 38{,}6}$$

> ✅ Il manuale del DG-1000 dichiara $E_{max} = 50$. Il modello sottostima del 23% (errore tipico per alianti di alta classe — la realtà sfrutta effetti laminari avanzati che il modello non cattura). Per il liceo va comunque bene.

### Passo 3 — $C_p^*$ e $V^*$

$C_p^*$:
$$C_p^* = \sqrt{\pi \lambda e \cdot C_{R,0}} = \sqrt{71{,}63 \times 0{,}012} = \sqrt{0{,}860} \approx 0{,}927$$

$V^*$:
$$V^* = \sqrt{\dfrac{2Q}{\rho S C_p^*}} = \sqrt{\dfrac{2 \times 6\,867}{1{,}225 \times 16{,}7 \times 0{,}927}}$$

Calcolo:

- Numeratore: $2 \times 6\,867 = 13\,734$
- Denominatore: $1{,}225 \times 16{,}7 \times 0{,}927 = 18{,}96$
- Rapporto: $13\,734/18{,}96 = 724{,}4$
- Radice: $\sqrt{724{,}4} = 26{,}9$ m/s

$$V^* \approx 26{,}9 \text{ m/s} = 52{,}3 \text{ kt}$$

$$\boxed{V^* \approx 27 \text{ m/s} = 52 \text{ kt}}$$

### Passo 4 — Distanza in aria calma (riferimento)

In aria calma:
$$\text{distanza}_{calma} = E_{max} \times h = 38{,}6 \times 1\,500 = 57\,900 \text{ m} \approx 58 \text{ km}$$

### Passo 5 — Velocità al suolo con vento contrario

$$V_{ground} = V^* - V_{wind} = 26{,}9 - 10{,}3 = 16{,}6 \text{ m/s}$$

### Passo 6 — Distanza al suolo con vento

L'aliante perde quota a una **velocità verticale** $V_z = V^*/E_{max} = 26{,}9/38{,}6 = 0{,}697$ m/s. Tempo di volo per arrivare al suolo:
$$t = h/V_z = 1\,500/0{,}697 = 2\,152 \text{ s} \approx 35{,}9 \text{ minuti}$$

In 2152 s, l'aliante si sposta **al suolo** a $V_{ground}$:
$$\text{distanza}_{suolo} = V_{ground} \times t = 16{,}6 \times 2\,152 = 35\,723 \text{ m} \approx 35{,}7 \text{ km}$$

$$\boxed{\text{distanza con vento} \approx 35{,}7 \text{ km}}$$

### Passo 7 — Confronto e riduzione

$$\dfrac{\text{distanza con vento}}{\text{distanza calma}} = \dfrac{35{,}7}{58} = 0{,}616$$

→ Il vento contrario di 20 kt **riduce la distanza al suolo del ~38%**.

---

## ✅ Verifica di plausibilità

**Angolo di planata** in aria: $\tan(\gamma) = 1/E = 1/38{,}6 = 0{,}0259 \Rightarrow \gamma = 1{,}48°$. Coerente per aliante moderno.

**Tempo di volo** ~36 minuti per scendere da 1500 m: realistico (3 km/min in caduta libera, qui molto più lento).

**Riduzione del 38%**: notevole ma non insolita. È per questo che i piloti di alianti studiano la **teoria di MacCready** — esiste una velocità ottimale che dipende dal vento e dalla velocità di salita prevista nelle termiche. Volare a $V^*$ con forte vento contrario non è più ottimale: bisogna **aumentare la velocità** per ridurre il tempo di esposizione al vento.

> 💡 In termini operativi: con vento contrario forte, gli alianti volano a **$V^* + V_{wind}/2$** (regola pratica MacCready semplificata). Per il nostro caso: $V_{ottima} \approx 27 + 5 = 32$ m/s. Ma il calcolo completo di MacCready è oltre il programma del liceo.

---

## 🔄 Variante per autovalutazione

Stesso aliante, stessa quota, stesso vento, ma il pilota decide di **volare più veloce** a $V_2 = 32$ m/s per "tagliare" il vento. Calcola:

- La nuova velocità verticale $V_z$
- La nuova distanza al suolo

(Suggerimento: serve calcolare il nuovo $E$ a $V_2$, che NON è $E_{max}$. Per il liceo, accetta $E$ a $V_2 \approx 0{,}85 \cdot E_{max}$ — è una buona approssimazione.)

<details markdown="1">
<summary>👉 Solo il risultato (prima provaci da solo!)</summary>

- $E$ a $V_2 = 0{,}85 \cdot 38{,}6 = 32{,}8$
- $V_z = V_2 / E = 32/32{,}8 = 0{,}976$ m/s
- $t = 1500/0{,}976 = 1\,537$ s ≈ 25,6 minuti
- $V_{ground} = 32 - 10{,}3 = 21{,}7$ m/s
- distanza = $21{,}7 \times 1537 = 33\,353$ m ≈ **33,4 km**

→ **Volando più veloce con vento contrario, la distanza scende solo del 7% (33,4 vs 35,7 km) ma il tempo di volo si riduce del 30%**. Il pilota arriva a destinazione in 26 min invece di 36 — meno fatica, più tempo per termiche all'arrivo. Questa è MacCready in nuce: meglio "tagliare" il vento veloce che fare distanza massima lenta.

</details>

---

## 🎓 Cosa hai imparato

- **$E_{max}$ e $V^*$ si calcolano dalla geometria**: $E_{max}$ dipende solo da $\lambda$, $e$, $C_{R,0}$.
- Il **vento contrario** non cambia la velocità nell'aria, ma riduce la velocità al suolo → distanza ridotta.
- La **distanza al suolo** è proporzionale al rapporto $V_g/V_{air}$: con vento al 38% di $V^*$, la distanza scende al 62% di quella in aria calma.
- **MacCready** (volo a vela): non sempre $V^*$ è la velocità migliore. Con vento contrario, si vola più veloce per minimizzare l'effetto del vento.
- Il **modello del liceo** sottostima $E_{max}$ degli alianti di alta classe del 20%, ma cattura il comportamento qualitativo correttamente.

---

## ➡️ Prossimo

[Esercizio 9 — Decollo con flap (Airbus A320)](./09-avanzato-decollo-flap.md) — l'altro lato della velocità: come dispositivi di alta portanza permettono decolli sicuri.
