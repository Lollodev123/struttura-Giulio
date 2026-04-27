# Esercizio 23 — Numero di Mach critico (Boeing 737 vs Concorde)

> 🔴 **Difficoltà: AVANZATO** — **Esercizio nuovo** sul numero di Mach: il "Mach critico" che separa subsonico dal transonico, e perché determina la velocità massima dei jet.
>
> 🎯 **Obiettivi**: calcolare il numero di Mach a quota di crociera, capire il concetto di Mach critico ($M_{cr}$) e Mach di divergenza ($M_{DD}$), e capire perché Boeing 737 vola a Mach 0,78 e non Mach 0,9.

---

## 📋 Testo del problema

Il **Boeing 737-800** vola in crociera a 230 m/s a FL350 (10 670 m). Il **Concorde** volava a 600 m/s a FL590 (18 000 m).

In atmosfera ISA:

- A 10 670 m: $T = 218{,}8$ K = $-54{,}3$°C
- A 18 000 m (stratosfera): $T = 216{,}65$ K = $-56{,}5$°C

La **velocità del suono** in aria si calcola come:
$$a = \sqrt{\gamma R T}$$

con $\gamma = 1{,}4$ (gas perfetto biatomico), $R = 287$ J/(kg·K), $T$ in kelvin.

**Determina**:

1. La velocità del suono $a$ alle 2 quote
2. Il numero di Mach $M = V/a$ per i 2 velivoli
3. Cos'è il **Mach critico** $M_{cr}$ e perché il 737 NON può volare a Mach 0,9
4. Spiega come il Concorde "passava" il Mach critico (perché lo poteva fare)

---

## 🖼️ Diagramma del problema

In aerodinamica subsonica, il flusso d'aria sull'ala accelera SEMPRE oltre la velocità del velivolo (a causa della curvatura). A un certo $M_{velivolo}$, il flusso locale sull'ala raggiunge $M = 1$ → si forma un'**onda d'urto**.

- $M_{cr}$ = numero di Mach del velivolo a cui PRIMA volta il flusso locale arriva a $M = 1$
- $M_{DD}$ = "drag divergence Mach", ~0,02 sopra $M_{cr}$, dove $C_D$ esplode (+50%)

Per profili subsonici tipici (NACA 23012, profili Boeing): $M_{cr} \approx 0{,}72-0{,}78$.

---

## 📊 Dati noti / da trovare

| Velivolo | Quota | T | V |
|---|---|---|---|
| Boeing 737 | 10 670 m | 218,8 K | 230 m/s |
| Concorde | 18 000 m | 216,65 K | 600 m/s |

---

## 🧠 Strategia

1. $a = \sqrt{1{,}4 \cdot 287 \cdot T}$
2. $M = V/a$
3. Confronto con $M_{cr}$ tipico (~0,75 per profili convenzionali)

---

## ✏️ Risoluzione passo-passo

### Passo 1 — Velocità del suono a FL350 (737)

$$a_{737} = \sqrt{1{,}4 \times 287 \times 218{,}8} = \sqrt{401{,}8 \times 218{,}8} = \sqrt{87\,914} \approx 296{,}5 \text{ m/s}$$

### Passo 2 — Velocità del suono a FL590 (Concorde)

$$a_{Concorde} = \sqrt{1{,}4 \times 287 \times 216{,}65} = \sqrt{87\,049} \approx 295{,}0 \text{ m/s}$$

> 💡 La velocità del suono dipende **SOLO da T**! In stratosfera (T costante a -56,5°C), $a$ resta circa **295 m/s** a tutte le quote sopra 11 km.

### Passo 3 — Numeri di Mach

$$M_{737} = \dfrac{230}{296{,}5} \approx 0{,}776$$

$$M_{Concorde} = \dfrac{600}{295{,}0} \approx 2{,}03$$

→ **737 vola a Mach 0,78, Concorde a Mach 2**, esattamente i valori dichiarati nei manuali ✅.

### Passo 4 — Mach critico del 737

Il profilo del 737 (NACA 230xx famiglia, modificato per high-Mach) ha $M_{cr} \approx 0{,}74$ con angolo di attacco di crociera. A Mach 0,78 il velivolo è a **+5% sopra il Mach critico** → si forma un'onda d'urto sul dorso dell'ala, ma debole.

$M_{DD}$ del 737 (drag divergence) ≈ 0,82-0,84. **Sopra di questo, $C_D$ esplode**:

| $M$ del 737 | $C_D$ relativo | Note |
|---|---|---|
| 0,70 | 1,00 | Subsonico pulito |
| 0,76 | 1,05 | Crociera economica |
| **0,78** | **1,10** | Crociera nominale (sweet spot) |
| 0,80 | 1,18 | Crociera "high" |
| 0,82 | 1,35 | Inizio drag divergence |
| 0,85 | 1,80 | **VIETATO** — strutturale + consumo |

**Perché Boeing limita il 737 a M_MO = 0,82?**

- Sopra M = 0,82, $C_D$ aumenta del 30-40% → consumo carburante esplode
- Vibrazioni Mach buffet (l'onda d'urto oscilla)
- Stress sulla struttura
- Comfort passeggeri

→ Il 737 vola a **Mach 0,78 di crociera** = compromesso ottimale tra velocità e consumo.

### Passo 5 — Concorde e il Mach critico

Il Concorde NON ha "passato" il Mach critico nel modo del 737. Era progettato con **profilo specificatamente supersonico** (delta sottile, freccia 75°) → l'onda d'urto si forma **avanti** del bordo d'attacco (oblique shock) e non "rovina" il flusso sull'ala.

In altre parole: il Concorde ha **due regimi separati** di funzionamento ottimale:
- Subsonico fino a Mach 0,9 (decolli, atterraggi, voli sopra terra)
- Supersonico Mach 2,0 (crociera oceanica)

In mezzo, **Mach 0,9 - 1,5** = transonic, **inefficiente** (drag picco). Il Concorde "passava" rapidamente questa zona accelerando con post-bruciatore.

→ **Boeing 737 = "limitato" da $M_{cr}$**, Concorde = **progettato per superarlo**.

---

## ✅ Verifica di plausibilità

Manuali Boeing 737-800:
- $V_{MO}$ (max operating speed) = 340 KIAS = ~230 m/s a FL350 = **Mach 0,82**
- Crociera economica = Mach **0,78**
- Crociera "high speed" = Mach **0,79-0,80**

Manuali Concorde (storici):
- Velocità di crociera supersonica = **Mach 2,02**
- Velocità transonica massimale = Mach 1,2 (passaggio veloce)
- Velocità subsonica massimale = Mach 0,93 (per voli sopra terra)

I nostri valori coincidono perfettamente.

### Effetto della temperatura sulla velocità del suono

A livello mare ISA ($T = 15°C = 288{,}15$ K):
$a_0 = \sqrt{1{,}4 \cdot 287 \cdot 288{,}15} = \sqrt{115\,762} \approx 340{,}3$ m/s = **661 kt**.

A FL350 (T = 218,8 K): $a = 296{,}5$ m/s = **576 kt**.

→ La velocità del suono **scende dell'13%** con la quota (per via della T più bassa). Mach 1 al livello mare = 1226 km/h, Mach 1 a FL350 = 1067 km/h. Per questo i jet "passano Mach 1" a quote diverse a velocità diverse in km/h.

---

## 🔄 Variante per autovalutazione

Un **F-35 Lightning II** (caccia di 5ª generazione) vola a Mach 1,6 a FL400 (12 192 m, $T \approx 216{,}65$ K). Calcola:

a. La velocità del suono a quota
b. La velocità vera del F-35 in m/s e in km/h
c. Confronta con la velocità di crociera del 737 (Mach 0,78) — quante volte più veloce è l'F-35?

<details markdown="1">
<summary>👉 Solo il risultato (prima provaci da solo!)</summary>

a. $a = \sqrt{1{,}4 \cdot 287 \cdot 216{,}65} = $ **295 m/s** (stratosfera, indipendente da quota)

b. $V = M \cdot a = 1{,}6 \cdot 295 = $ **472 m/s = 1700 km/h** (Mach 1,6)

c. F-35: 472 m/s. 737: 230 m/s. **Rapporto: 472/230 = 2,05**.
→ F-35 in supersonico vola **2 volte più veloce** di un 737. New York-Londra in 3 ore (vs 7 ore con 737). Ma con consumo carburante × 5.

</details>

---

## 🎓 Cosa hai imparato

- **Velocità del suono** $a = \sqrt{\gamma R T}$, dipende solo dalla temperatura.
- **In stratosfera (sopra 11 km)**, $a$ è costante (~295 m/s, ~574 kt).
- **Mach critico $M_{cr}$**: il velivolo a cui il flusso sull'ala raggiunge Mach 1 → onda d'urto.
- I **jet di linea subsonici** sono progettati per volare **sotto $M_{DD}$** (~Mach 0,82-0,85), tipico crociera 0,78.
- Il **Concorde** era progettato per **superare** il Mach critico e operare in regime supersonico — design fondamentalmente diverso.
- La **velocità in km/h** corrispondente a Mach 1 dipende dalla quota (1226 km/h al mare, 1067 km/h a FL350).

---

## ➡️ Prossimo

[Esercizio 24 — Effetto winglet su Boeing 737](./24-avanzato-winglet.md) o l'[indice](../tutti.md).
