# Esercizio 17 — Reynolds di un modello in galleria del vento

> 🟡 **Difficoltà: MEDIO** — Variante dell'[Esercizio 7](../07-medio-reynolds.md): stesso fenomeno (Reynolds), problema diverso (modello vs velivolo reale e correzione di scala).
>
> 🎯 **Obiettivi**: capire perché un modello in galleria del vento NON ha lo stesso $Re$ del velivolo reale, calcolare il fattore di scala richiesto per "avere lo stesso $Re$", capire perché esistono gallerie pressurizzate.

---

## 📋 Testo del problema

Un'azienda di progettazione vuole testare in galleria del vento un **modello in scala 1:8 di un Piper PA-28** (corda alare reale 1,4 m). La galleria del vento è a livello mare ISA, velocità massima 80 m/s.

**Determina**:

1. Il $Re$ del Piper REALE in crociera (110 kt al livello mare)
2. Il $Re$ del modello in scala 1:8 in galleria a 80 m/s (massimo)
3. Il rapporto $Re_{modello}/Re_{reale}$ e la conseguenza
4. Quale velocità servirebbe nella galleria per avere lo **stesso $Re$** del Piper reale (e perché è impossibile)?

---

## 🖼️ Diagramma del problema

Riferimento: [Lezione 6 — Numero di Reynolds](../../01-teoria/06-numero-reynolds.md).

Formula chiave: $Re = \dfrac{\rho V c}{\mu}$, con:

- $\rho = 1{,}225$ kg/m³ (livello mare ISA)
- $\mu = 1{,}78 \times 10^{-5}$ Pa·s (aria a 15°C)

---

## 📊 Dati noti / da trovare

| Grandezza | Piper reale | Modello 1:8 |
|---|---|---|
| Corda $c$ | 1,4 m | $1{,}4/8 = 0{,}175$ m |
| Velocità $V$ | 110 kt = 56,6 m/s | fino a 80 m/s |
| Densità $\rho$ | 1,225 | 1,225 |
| Viscosità $\mu$ | $1{,}78 \times 10^{-5}$ | $1{,}78 \times 10^{-5}$ |

---

## 🧠 Strategia

1. Applico $Re = \rho V c / \mu$ al velivolo reale
2. Idem per il modello (stessa $\rho$, $\mu$; $c$ ridotta di 8; $V$ massima)
3. Confronto e calcolo rapporto
4. Inverto la formula per trovare $V_{richiesta}$ in galleria per pareggiare $Re_{reale}$

---

## ✏️ Risoluzione passo-passo

### Passo 1 — $Re$ del Piper reale in crociera

$V = 110 \times 0{,}5144 = 56{,}58$ m/s

$$Re_{reale} = \dfrac{1{,}225 \times 56{,}58 \times 1{,}4}{1{,}78 \times 10^{-5}} = \dfrac{97{,}03}{1{,}78 \times 10^{-5}} \approx 5{,}45 \times 10^6$$

$$\boxed{Re_{reale} \approx 5{,}5 \times 10^6}$$

→ **Pienamente turbolento** ($Re \gg 5 \times 10^5$).

### Passo 2 — $Re$ del modello in galleria (max V = 80 m/s)

$$Re_{mod} = \dfrac{1{,}225 \times 80 \times 0{,}175}{1{,}78 \times 10^{-5}} = \dfrac{17{,}15}{1{,}78 \times 10^{-5}} \approx 9{,}64 \times 10^5$$

$$\boxed{Re_{mod} \approx 0{,}96 \times 10^6}$$

→ **Appena nel turbolento**, vicino al $Re$ critico.

### Passo 3 — Rapporto

$$\dfrac{Re_{mod}}{Re_{reale}} = \dfrac{9{,}64 \times 10^5}{5{,}45 \times 10^6} \approx 0{,}177$$

→ Il modello "vede" un Reynolds del **17,7%** rispetto al velivolo reale (~6 volte minore).

**Conseguenza**: il flusso sul modello è **molto più "delicato"** (vicino alla transizione laminare-turbolento), mentre sul Piper reale è pienamente turbolento. **I dati di forza misurati sul modello NON sono direttamente trasferibili al velivolo reale** senza correzione.

### Passo 4 — Velocità richiesta in galleria per pareggiare $Re$

Voglio $Re_{mod} = Re_{reale} = 5{,}45 \times 10^6$. Stessa $\rho, \mu, c_{mod}$, isolo $V$:

$$V = \dfrac{Re \cdot \mu}{\rho \cdot c_{mod}} = \dfrac{5{,}45 \times 10^6 \times 1{,}78 \times 10^{-5}}{1{,}225 \times 0{,}175}$$

$$V = \dfrac{96{,}99}{0{,}2144} \approx 452 \text{ m/s}$$

→ **452 m/s** (Mach 1,3, **supersonico**!)

**Ma è impossibile**: a Mach 1+ entrano in gioco effetti di compressibilità che cambiano completamente la fisica del flusso. Il modello andrebbe in onde d'urto e i risultati non sarebbero confrontabili col Piper subsonico.

---

## ✅ Verifica di plausibilità

Il problema della **similitudine di Reynolds** è uno dei più classici della fluidodinamica sperimentale. Soluzioni reali nel mondo industriale:

| Tecnica | Cosa fa | Esempio |
|---|---|---|
| **Galleria pressurizzata** | Aumenta $\rho$ (ariad alta pressione) → $Re$ × N | NASA Langley, Boeing |
| **Galleria criogenica** | Aria fredda → $\mu$ scende → $Re$ × ~3 | NASA TDT |
| **Modello più grande** | $c$ × 2 → $Re$ × 2 | Modelli 1:4 invece di 1:10 |
| **Strato limite trippato** | Inneschi turbolenza con strisce ruvide sul bordo d'attacco → simula alto Re | Tecnica universale |

Il modellino del Piper in galleria standard a $Re = 10^6$ → simulazione **decente** (turbolento sì, ma in transizione delicata) → si applica correzione strato limite trippato + correzione "scaling rules" + analisi numerica CFD.

---

## 🔄 Variante per autovalutazione

Per testare correttamente un modello del **Boeing 737** (corda media 4 m, crociera $V = 230$ m/s, $\rho = 0{,}38$ a FL350 → $Re_{reale} \approx 2 \times 10^7$), si vuole una galleria **pressurizzata** che riproduca lo stesso $Re$ con un modello 1:20 a $V = 50$ m/s.

a. Calcola $Re$ del modello 1:20 in galleria standard ($\rho = 1{,}225$) a 50 m/s
b. A che pressione (in atmosfere) bisogna pressurizzare la galleria per pareggiare $Re_{reale}$?

<details markdown="1">
<summary>👉 Solo il risultato (prima provaci da solo!)</summary>

a. $c_{mod} = 4/20 = 0{,}2$ m
$Re_{mod\_std} = (1{,}225 \cdot 50 \cdot 0{,}2)/(1{,}78 \times 10^{-5}) = 12{,}25/(1{,}78 \times 10^{-5}) \approx$ **6,9 × 10⁵**

→ $Re$ del modello = 6,9×10⁵, mentre quello reale è 2×10⁷ → rapporto ~30× troppo basso.

b. Per pareggiare $Re$, devo aumentare $\rho$ di un fattore 30:
$\rho_{required} = 30 \cdot 1{,}225 = 36{,}75$ kg/m³

In atmosfere (basato su $\rho \propto p$ a temperatura costante): $p = 36{,}75/1{,}225 \approx$ **30 atm**.

→ La galleria dovrebbe essere pressurizzata a 30 atmosfere, valore tecnicamente raggiungibile (gallerie come NTF a Langley arrivano a 9 atm + criogenia, equivalente a ~30 atm "atmosferiche"). Costo: enorme. Tipico di programmi come 787, 777X.

</details>

---

## 🎓 Cosa hai imparato

- I **modelli in galleria standard** non hanno lo stesso $Re$ del velivolo reale: solitamente $Re$ del modello = 10-30% di quello reale.
- **Pareggiare $Re$ in galleria standard** richiede velocità supersoniche → impossibile (nuovi effetti fisici entrano in gioco).
- **Soluzioni industriali**: gallerie pressurizzate (Boeing, NASA), criogeniche, modelli grandi (1:4-1:8), strato limite trippato.
- La **similitudine** è il fondamento della modellistica sperimentale: senza, i risultati di galleria sono "indicativi", non quantitativi.

---

## ➡️ Prossimo

[Esercizio 18 — Carico alare 3 velivoli](./18-medio-carico-alare.md) o l'[indice](../tutti.md).
