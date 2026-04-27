# Esercizio 18 — Confronto carico alare 3 velivoli

> 🟡 **Difficoltà: MEDIO** — **Esercizio nuovo** (non variante diretta) sul concetto di carico alare $W/S$ — il "DNA" del velivolo che determina velocità di stallo, comportamento in turbolenza, lunghezza pista.
>
> 🎯 **Obiettivi**: calcolare $W/S$ per Cessna 172, ATR 72, Boeing 737, capire la relazione $V_S \propto \sqrt{W/S}$, vedere come carico alare diversi giustificano disegni e missioni diverse.

---

## 📋 Testo del problema

Confronta tre velivoli al loro MTOW:

| Velivolo | MTOW (kg) | $S$ (m²) | $C_{p,max}$ atterraggio (con flap) |
|---|---|---|---|
| **Cessna 172** | 1 043 | 16,2 | 2,1 |
| **ATR 72** | 22 500 | 61,0 | 2,5 |
| **Boeing 737-800** | 79 000 | 124,6 | 2,8 |

**Determina** per ciascuno:
1. Carico alare $W/S$ (in kg/m² e in N/m²)
2. $V_S$ in atterraggio (al livello mare ISA, con flap)
3. $V_{atterraggio}$ standard (= $1{,}3 \cdot V_S$, regola FAA)
4. Velocità di approccio in nodi
5. **Trend**: come cresce il carico alare e la velocità di approccio dal Cessna al 737?

---

## 🖼️ Diagramma del problema

I tre velivoli **occupano scale di dimensione e peso completamente diverse**. Eppure tutti applicano la stessa formula $V_S = \sqrt{2W/(\rho S C_{p,max})}$. La leva fondamentale che li differenzia è il **carico alare**.

---

## 📊 Dati noti / da trovare

| | Cessna 172 | ATR 72 | Boeing 737 |
|---|---|---|---|
| $m$ (kg) | 1 043 | 22 500 | 79 000 |
| $S$ (m²) | 16,2 | 61,0 | 124,6 |
| $C_{p,max}$ con flap | 2,1 | 2,5 | 2,8 |
| $\rho$ mare ISA | 1,225 | 1,225 | 1,225 |

---

## 🧠 Strategia

1. $Q = m \cdot g$
2. $W/S$ in N/m² e in kg/m² (= $m/S$)
3. $V_S = \sqrt{2W/(\rho S C_{p,max})}$
4. $V_{atterraggio} = 1{,}3 V_S$ (standard FAA per atterraggio sicuro)

---

## ✏️ Risoluzione passo-passo

### Cessna 172

$W = 1\,043 \times 9{,}81 = 10\,232$ N
$W/S = 10\,232/16{,}2 = $ **632 N/m² = 64 kg/m²**
$V_S = \sqrt{2 \cdot 10232/(1{,}225 \cdot 16{,}2 \cdot 2{,}1)} = \sqrt{20464/41{,}67} = \sqrt{491{,}1} = 22{,}16$ m/s = **43 kt**
$V_{atterraggio} = 1{,}3 \cdot 43 = $ **56 kt**

### ATR 72

$W = 22\,500 \times 9{,}81 = 220\,725$ N
$W/S = 220\,725/61 = $ **3 619 N/m² = 369 kg/m²**
$V_S = \sqrt{2 \cdot 220725/(1{,}225 \cdot 61 \cdot 2{,}5)} = \sqrt{441450/186{,}81} = \sqrt{2363} = 48{,}6$ m/s = **94 kt**
$V_{atterraggio} = 1{,}3 \cdot 94 = $ **122 kt**

### Boeing 737-800

$W = 79\,000 \times 9{,}81 = 774\,990$ N
$W/S = 774\,990/124{,}6 = $ **6 220 N/m² = 634 kg/m²**
$V_S = \sqrt{2 \cdot 774990/(1{,}225 \cdot 124{,}6 \cdot 2{,}8)} = \sqrt{1549980/427{,}3} = \sqrt{3627} = 60{,}2$ m/s = **117 kt**
$V_{atterraggio} = 1{,}3 \cdot 117 = $ **152 kt**

### Tabella riepilogativa

| | $W/S$ (kg/m²) | $V_S$ (kt) | $V_{atterraggio}$ (kt) | $V$ (km/h) |
|---|---|---|---|---|
| Cessna 172 | **64** | 43 | **56** | 104 |
| ATR 72 | 369 | 94 | 122 | 226 |
| Boeing 737 | **634** | 117 | **152** | 281 |

---

## ✅ Verifica di plausibilità

| Velivolo | $V_{atterraggio}$ calcolata | $V_{ref}$ manuale (POH) |
|---|---|---|
| Cessna 172 | 56 kt | 60 kt |
| ATR 72 | 122 kt | 120-125 kt |
| Boeing 737 | 152 kt | 145-160 kt |

**Tutte e tre coincidono entro il 5%** col manuale di volo certificato. Eccellente.

### Trend del carico alare e velocità

- $W/S$ **decuplica** dal Cessna al 737 (64 → 634 kg/m²)
- $V_S$ **circa triplica** (43 → 117 kt) — coerente con $V_S \propto \sqrt{W/S} \approx \sqrt{10} \approx 3{,}16$
- $V_{atterraggio}$ stessa proporzione (56 → 152 kt)

→ **Velivoli più "pesanti" rispetto all'ala** atterrano molto più veloci. Ecco perché:

- Cessna su pista d'erba di 400 m → OK
- ATR su pista di 1500 m → OK
- 737 richiede pista di 1900-2400 m

---

## 🔄 Variante per autovalutazione

Quale lunghezza minima di pista serve per atterrare ciascuno dei tre velivoli? Usa la regola empirica: pista atterraggio ≈ $V_{atterraggio}^2 / (2 \cdot a_{frenata})$, con $a_{frenata} = 3$ m/s² (decelerazione media tipica con freni + spoiler).

<details markdown="1">
<summary>👉 Solo il risultato (prima provaci da solo!)</summary>

Pista atterraggio = $V^2/(2 a)$:

| Velivolo | $V$ (m/s) | $V^2$ | Pista (m) |
|---|---|---|---|
| Cessna | 28,8 | 829 | 138 m |
| ATR | 62,8 | 3 944 | **657 m** |
| 737 | 78,2 | 6 115 | **1 019 m** |

Aggiungi ~50% per "margine di sicurezza FAA + flare + rotolamento":

| Velivolo | Pista atterraggio totale |
|---|---|
| Cessna | 138 × 1,5 ≈ **210 m** ✅ |
| ATR | 657 × 1,5 ≈ **985 m** ✅ |
| 737 | 1019 × 1,5 ≈ **1530 m** ✅ |

Confronta con piste reali: piste regionali italiane (Trento 1067 m → solo Cessna+ATR; Bolzano 1294 m → ATR sì, 737 al limite).

</details>

---

## 🎓 Cosa hai imparato

- Il **carico alare $W/S$** è il **parametro più importante** per definire la "personalità" di un velivolo: bassa $W/S$ = lento, agile, atterra ovunque; alta $W/S$ = veloce, pesante, richiede piste lunghe.
- $V_S \propto \sqrt{W/S}$: decuplichi $W/S$ → triplichi $V_S$. Relazione fondamentale.
- I **flap** servono ad alzare $C_{p,max}$ → ridurre $V_S$ a parità di $W/S$. Senza flap, il 737 atterrerebbe a ~200 kt → impossibile su qualsiasi pista commerciale.
- I **dati POH** (Pilot's Operating Handbook) si possono **ricostruire al 5%** con la matematica del liceo.

---

## ➡️ Prossimo

[Esercizio 19 — Effetto temperatura](./19-medio-aria-calda.md) o l'[indice](../tutti.md).
