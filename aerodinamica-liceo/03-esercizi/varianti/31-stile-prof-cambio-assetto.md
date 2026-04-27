# Esercizio 31 — Cambio assetto: due condizioni di volo a confronto

> 🔴 **Difficoltà: AVANZATO** — Il **più tosto** del set: due condizioni di volo successive, calcolo della resistenza indotta in entrambe, scrittura della polare, rappresentazione grafica.
>
> 🎯 **Obiettivi**: gestire un velivolo che **cambia assetto** (e quindi $C_p$ e $E$), calcolare resistenze indotte prima/dopo, scrivere la polare a partire dai dati operativi.

---

## 📋 Testo del problema

Un velivolo ha:

- Carico alare $Q/S = 2\,500$ N/m²
- Superficie alare $S = 19$ m²
- Allungamento $\lambda = 9{,}6$
- Vola con **efficienza $E = 8$** alla velocità di **360 km/h**

A un certo punto il pilota cambia assetto **abbassando il muso** (riduce l'incidenza). Nelle nuove condizioni di volo, l'**anemometro** (che misura $V_{IAS}$, indicated airspeed) segna $V_{IAS} = 510$ km/h.

> 💡 **Ipotesi semplificativa**: si vola al livello del mare ISA, quindi $V_{IAS} = V_{TAS}$ (vera). In quota i due differiscono per il fattore $\sqrt{\rho_0/\rho}$, ma a livello mare coincidono.

**Determina**:

1. Resistenza totale $R_1$ nelle condizioni iniziali (E = 8, V = 360 km/h)
2. Coefficienti $C_p$ e $C_R$ iniziali, e quindi $C_{R,0}$ del velivolo (assumi $e = 0{,}85$)
3. $C_p$ nelle nuove condizioni (V = 510 km/h, stesso peso)
4. **Resistenza indotta** $R_i$ prima e dopo la manovra
5. Resistenza totale $R_2$ e nuova efficienza $E_2$
6. Scrivere l'**equazione della polare** e rappresentarla graficamente, evidenziando i 2 punti di volo

---

## 🖼️ Diagramma del problema

![Polare con tangente per E_max](../../assets/img/grafici/polare-tangente-emax.svg)

Le **due condizioni di volo** sono due punti distinti sulla stessa polare (stesso velivolo, stesso peso, solo $V$ diversa → $C_p$ diverso → punto operativo si sposta).

---

## 📊 Dati noti / da trovare

| Grandezza | Valore |
|---|---|
| Carico alare $Q/S$ | 2 500 N/m² |
| Superficie $S$ | 19 m² |
| Allungamento $\lambda$ | 9,6 |
| $e$ (assunto) | 0,85 |
| $\rho$ (livello mare) | 1,225 kg/m³ |
| **Condizione 1** | $V_1 = 360$ km/h, $E_1 = 8$ |
| **Condizione 2** | $V_2 = 510$ km/h |

---

## 🧠 Strategia

1. Calcolo $Q$ dalla relazione $Q/S$
2. Conversioni V in m/s
3. **Condizione 1**: da $V_1$ e $Q$ ricavo $C_{p,1}$, da $E_1$ ricavo $C_{R,1}$, da $C_{p,1}$ e $\lambda$ ricavo $C_{R,i,1}$, e quindi $C_{R,0}$ per differenza.
4. **Condizione 2**: stesso $Q$, nuova V → $C_{p,2}$. Polare → $C_{R,2}$. Forze.
5. Polare: $C_R = C_{R,0} + C_p^2/(\pi\lambda e)$. Tabulazione su 5-6 punti.

---

## ✏️ Risoluzione passo-passo

### Passo 1 — Peso, conversioni

$$Q = (Q/S) \times S = 2\,500 \times 19 = 47\,500 \text{ N}$$

$$V_1 = 360/3{,}6 = 100 \text{ m/s}$$
$$V_2 = 510/3{,}6 = 141{,}67 \text{ m/s}$$

### Passo 2 — Condizione 1: $C_{p,1}$ e $C_{R,1}$

Pressione dinamica:
$$q_1 = \dfrac{1}{2} \times 1{,}225 \times 100^2 = 6\,125 \text{ Pa}$$

In volo livellato, $P = Q$:
$$C_{p,1} = \dfrac{Q}{q_1 \cdot S} = \dfrac{47\,500}{6\,125 \times 19} = \dfrac{47\,500}{116\,375} = 0{,}408$$

Da $E_1 = C_{p,1}/C_{R,1}$:
$$C_{R,1} = \dfrac{C_{p,1}}{E_1} = \dfrac{0{,}408}{8} = 0{,}0510$$

### Passo 3 — Resistenza totale prima

$$R_1 = q_1 \cdot S \cdot C_{R,1} = 6\,125 \times 19 \times 0{,}0510 = 5\,936 \text{ N}$$

$$\boxed{R_1 \approx 5{,}9 \text{ kN}}$$

### Passo 4 — Estrarre $C_{R,0}$ dalla condizione 1

$$\pi\lambda e = \pi \times 9{,}6 \times 0{,}85 = 25{,}64$$

$$C_{R,i,1} = \dfrac{C_{p,1}^2}{\pi\lambda e} = \dfrac{0{,}408^2}{25{,}64} = \dfrac{0{,}1664}{25{,}64} = 0{,}00649$$

$$C_{R,0} = C_{R,1} - C_{R,i,1} = 0{,}0510 - 0{,}00649 = 0{,}0445$$

$$\boxed{C_{R,0} \approx 0{,}0445}$$

### Passo 5 — Condizione 2: $C_{p,2}$, $C_{R,i,2}$, $C_{R,2}$

$$q_2 = \dfrac{1}{2} \times 1{,}225 \times 141{,}67^2 = \dfrac{1}{2} \times 1{,}225 \times 20\,070 = 12\,293 \text{ Pa}$$

$$C_{p,2} = \dfrac{Q}{q_2 \cdot S} = \dfrac{47\,500}{12\,293 \times 19} = \dfrac{47\,500}{233\,567} = 0{,}2034$$

> 💡 **Lettura**: aumentando V del 41,7% (100 → 141,67 m/s), $C_p$ scende del 50% (0,408 → 0,203). Coerente: $C_p \propto 1/V^2$.

$$C_{R,i,2} = \dfrac{0{,}2034^2}{25{,}64} = \dfrac{0{,}0414}{25{,}64} = 0{,}001613$$

$$C_{R,2} = C_{R,0} + C_{R,i,2} = 0{,}0445 + 0{,}001613 = 0{,}0461$$

### Passo 6 — Resistenza totale e efficienza dopo

$$R_2 = q_2 \cdot S \cdot C_{R,2} = 12\,293 \times 19 \times 0{,}0461 = 10\,772 \text{ N}$$

$$E_2 = \dfrac{C_{p,2}}{C_{R,2}} = \dfrac{0{,}2034}{0{,}0461} = 4{,}41$$

$$\boxed{R_2 \approx 10{,}8 \text{ kN}, \quad E_2 \approx 4{,}41}$$

### Passo 7 — Confronto resistenze indotte

$$R_{i,1} = q_1 \cdot S \cdot C_{R,i,1} = 6\,125 \times 19 \times 0{,}00649 = 755 \text{ N}$$

$$R_{i,2} = q_2 \cdot S \cdot C_{R,i,2} = 12\,293 \times 19 \times 0{,}001613 = 377 \text{ N}$$

| | Condizione 1 (V=360 km/h) | Condizione 2 (V=510 km/h) | Variazione |
|---|---|---|---|
| $C_p$ | 0,408 | 0,203 | -50% |
| $C_R$ | 0,051 | 0,046 | -10% |
| $R$ totale | 5,9 kN | 10,8 kN | **+82%** |
| $R_i$ (indotta) | 755 N | 377 N | -50% |
| $E$ | 8,0 | **4,4** | -45% |

**Lettura del confronto**:

- $R$ totale **aumenta** nonostante $C_R$ scenda — perché $q$ raddoppia.
- $R_i$ scende come $C_p^2$.
- L'efficienza **crolla** perché ci si allontana dal punto ottimo (a velocità troppo alta, parassita domina).

### Passo 8 — Equazione della polare

$$\boxed{C_R = 0{,}0445 + \dfrac{C_p^2}{25{,}64}}$$

Tabulazione e rappresentazione:

| $C_p$ | $C_R$ |
|---|---|
| 0 | 0,0445 |
| 0,2 | 0,0461 |
| **0,203** (Cond. 2) | **0,0461** |
| 0,4 | 0,0507 |
| **0,408** (Cond. 1) | **0,0510** |
| 0,6 | 0,0585 |
| 0,8 | 0,0695 |
| 1,0 | 0,0835 |

Sulla **polare**, le due condizioni si rappresentano come due punti distinti:

- **Condizione 1**: $(0{,}0510; 0{,}408)$ — più in alto (più $C_p$, quindi $\alpha$ maggiore)
- **Condizione 2**: $(0{,}0461; 0{,}203)$ — più in basso (meno $C_p$, $\alpha$ ridotto)

La distanza fra i due punti rappresenta il **cambiamento di assetto** (il pilota ha abbassato il muso → $\alpha$ → $C_p$ scendono).

---

## ✅ Verifica di plausibilità

- $C_{R,0} = 0{,}0445$ è **alto** (tipico velivolo non aerodinamicamente pulito, forse turboelica o aircraft con carrello fisso).
- $E_1 = 8$ è efficienza modesta — coerente con $C_{R,0}$ alto.
- Il velivolo pesa $47\,500/9{,}81 = 4\,842$ kg → categoria small business jet o turboelica.
- A $V = 510$ km/h ($\sim 280$ kt), efficienza scende del 45% → grande costo carburante in crociera veloce.

---

## 🔄 Variante per autovalutazione

Lo stesso velivolo, ma il pilota cambia assetto **alzando il muso** invece di abbassarlo. La nuova velocità è $V_3 = 250$ km/h. Calcola $C_{p,3}$, $C_{R,3}$, $E_3$.

<details markdown="1">
<summary>👉 Risultato</summary>

$V_3 = 250/3{,}6 = 69{,}44$ m/s
$q_3 = \frac{1}{2} \cdot 1{,}225 \cdot 69{,}44^2 = 2\,953$ Pa
$C_{p,3} = 47500/(2953 \cdot 19) = 47500/56\,107 = 0{,}847$
$C_{R,i,3} = 0{,}847^2/25{,}64 = 0{,}0280$
$C_{R,3} = 0{,}0445 + 0{,}0280 = 0{,}0725$
$E_3 = 0{,}847/0{,}0725 = $ **11,7**

→ Rallentando, l'efficienza **migliora del 46%** (da 8 a 11,7). Il velivolo si avvicina al $C_p^* = \sqrt{25{,}64 \cdot 0{,}0445} = 1{,}07$, dove $E_{max} = (1/2)\sqrt{25{,}64/0{,}0445} = 12{,}0$. **Quasi a max efficienza!**

</details>

---

## 🎓 Cosa hai imparato

- **Cambio assetto** = stesso velivolo, due punti diversi sulla stessa polare. La polare resta la curva del velivolo, cambia solo il punto operativo.
- **Estrazione di $C_{R,0}$**: con un punto noto ($C_p$ + E) e $\lambda$ noto, è una sottrazione.
- **Resistenza totale aumenta** con velocità anche se $C_R$ scende (il fattore $q = \frac{1}{2}\rho V^2$ pesa il doppio).
- **Efficienza ottimale** si trova a $C_p^*$: a velocità diverse, l'efficienza è inferiore.
- **VIAS vs TAS** (in questo esercizio assunti uguali): in quota, il pilota legge VIAS sull'anemometro ma per i calcoli aerodinamici serve la TAS, calcolata dalla densità.

---

## ➡️ Prossimo

Hai completato i 5 esercizi in stile prof! Torna all'[indice esercizi](../tutti.md) per vedere tutti i 31 disponibili, oppure prova [Esercizio 32 — Polare cambio assetto a quota] (in arrivo).
