# Esercizio 14 — Efficienza dello Schweizer 2-33 (aliante didattico)

> 🟡 **Difficoltà: MEDIO** — Variante dell'[Esercizio 4](../04-medio-efficienza-aliante.md): stesso fenomeno (planata), aliante meno performante per capire come la geometria limita $E_{max}$.
>
> 🎯 **Obiettivi**: confrontare un aliante didattico (Schweizer 2-33) con uno moderno (ASK-21) e vedere come allungamento alare basso e profilo poco raffinato riducono drasticamente $E_{max}$.

---

## 📋 Testo del problema

Uno **Schweizer 2-33** (aliante biposto in metallo, anni '60, ancora usato per addestramento iniziale) sta planando al livello mare ISA.

Dati:

- Massa con due persone: $m = 410$ kg
- Superficie alare: $S = 20{,}06$ m²
- Apertura alare: $b = 15{,}24$ m → allungamento $\lambda = b^2/S = 11{,}6$ (più basso dell'ASK-21!)
- Resistenza parassita: $C_{D,0} = 0{,}019$ (peggiore di un aliante moderno — costruzione metallica meno pulita)
- Fattore Oswald: $e = 0{,}85$

**Determina**:
1. $C_L^*$ ed $E_{max}$
2. $V^*$ (velocità di max efficienza)
3. Distanza di planata da **1 000 m** AGL
4. Confronto numerico con l'ASK-21 dell'Esercizio 4 ($E_{max} = 33$)

---

## 🖼️ Diagramma del problema

![Planata stabilizzata di un aliante](../../assets/img/grafici/planata-aliante.svg)

Stesso schema dell'aliante ASK-21: equilibrio in planata, distanza = $E \times h$.

---

## 📊 Dati noti / da trovare

| Grandezza | Simbolo | Valore | Unità |
|---|---|---|---|
| Massa | $m$ | 410 | kg |
| Superficie | $S$ | 20,06 | m² |
| Apertura | $b$ | 15,24 | m |
| Allungamento | $\lambda$ | 11,6 | — |
| $C_{D,0}$ | — | 0,019 | — |
| $e$ | — | 0,85 | — |
| Quota | $h$ | 1 000 | m |

---

## 🧠 Strategia

Stessa dell'Esercizio 4. Le formule chiave:

- $C_L^* = \sqrt{\pi \lambda e \cdot C_{D,0}}$
- $E_{max} = \frac{1}{2}\sqrt{\pi \lambda e / C_{D,0}}$
- $V^* = \sqrt{2W/(\rho S C_L^*)}$
- distanza = $E_{max} \times h$

---

## ✏️ Risoluzione passo-passo

### Passo 1 — Peso

$$W = 410 \times 9{,}81 = 4\,022{,}1 \text{ N}$$

### Passo 2 — $\pi \lambda e$ (utile costante)

$$\pi \lambda e = \pi \times 11{,}6 \times 0{,}85 = 30{,}98$$

### Passo 3 — $C_L^*$

$$C_L^* = \sqrt{30{,}98 \times 0{,}019} = \sqrt{0{,}5886} \approx 0{,}767$$

### Passo 4 — $E_{max}$

$$E_{max} = \dfrac{1}{2}\sqrt{\dfrac{30{,}98}{0{,}019}} = \dfrac{1}{2}\sqrt{1\,631} = \dfrac{40{,}4}{2} \approx 20{,}2$$

$$\boxed{E_{max} \approx 20}$$

### Passo 5 — Velocità di max efficienza

$$V^* = \sqrt{\dfrac{2 \times 4\,022{,}1}{1{,}225 \times 20{,}06 \times 0{,}767}}$$

Calcolo:

- Numeratore: $8\,044{,}2$
- Denominatore: $1{,}225 \times 20{,}06 \times 0{,}767 = 18{,}85$
- Rapporto: $8\,044{,}2 / 18{,}85 = 426{,}8$
- $V^* = \sqrt{426{,}8} = 20{,}66$ m/s ≈ **40,2 kt**

### Passo 6 — Distanza di planata

$$\text{distanza} = E_{max} \times h = 20{,}2 \times 1\,000 = 20\,200 \text{ m} \approx 20 \text{ km}$$

---

## ✅ Verifica di plausibilità

Il manuale dello Schweizer 2-33 dichiara $E_{max} \approx 22$ a velocità di best glide ~40 kt. **Il nostro 20 sottostima del 9%** — coerente col fatto che il modello del liceo è ottimistico per i parassita reali a basso $Re$.

### Confronto Schweizer 2-33 vs ASK-21

| | Schweizer 2-33 (anni '60) | ASK-21 (moderno) | Rapporto |
|---|---|---|---|
| $\lambda$ | 11,6 | 16,6 | ASK 1,43× |
| $C_{D,0}$ | 0,019 | 0,014 | Sch +36% |
| $C_L^*$ | 0,77 | 0,83 | quasi uguali |
| **$E_{max}$** | 20 | 30 | **ASK 1,5× migliore!** |
| $V^*$ | 40 kt | 49 kt | ASK +20% (più pesante) |
| Planata da 1 km | 20 km | 30 km | ASK +50% |

**Lettura**: 30 anni di evoluzione (1960 → 1990) hanno aumentato l'efficienza degli alianti del **50%**. Le leve sono state due:

- Allungamento maggiore ($\lambda$ da 12 a 17)
- Profili più puliti, materiali compositi ($C_{D,0}$ da 0,019 a 0,014)

---

## 🔄 Variante per autovalutazione

Lo Schweizer 2-33 in **discesa più ripida** ($V = 30$ m/s, sopra $V^*$). L'efficienza scende a $E \approx 0{,}82 \cdot E_{max}$ (modello del liceo). Calcola:

a. La nuova efficienza $E$
b. La distanza di planata da 1000 m

<details markdown="1">
<summary>👉 Solo il risultato (prima provaci da solo!)</summary>

a. $E = 0{,}82 \cdot 20{,}2 = 16{,}6$
b. distanza = $E \cdot h = 16{,}6 \cdot 1\,000 = 16\,600$ m ≈ **16,6 km**

→ Volando il 45% più veloce di $V^*$ (30 m/s vs 20,6 m/s), perdi 18% di distanza in planata. **Lezione MacCready**: in aria calma, vola sempre a $V^*$ — chi accelera perde distanza per niente.

Ma se c'è vento contrario o forti termiche da raggiungere, **conviene accelerare** per ridurre il tempo di esposizione al vento (vedi Esercizio 8).

</details>

---

## 🎓 Cosa hai imparato

- **L'aliante didattico** ha $E_{max}$ "modesta" (~20) rispetto a uno moderno (~30-50).
- Le due leve fondamentali per migliorare $E_{max}$: **allungamento $\lambda$** e **resistenza parassita $C_{D,0}$**.
- Una pista di addestramento di 1000 m → 20 km di planata possibile = puoi facilmente provare le manovre senza paura.
- I **vecchi alianti metallici** restano didatticamente preziosi proprio perché meno performanti: insegnano a pilotare con margini più stretti, abituando il pilota a ottimizzare ogni manovra.

---

## ➡️ Prossimo

[Esercizio 15 — Portanza Boeing 777 a FL400](./15-medio-portanza-777.md) o l'[indice completo](../tutti.md).
