# Esercizio 24 — Effetto winglet su Boeing 737NG vs MAX

> 🔴 **Difficoltà: AVANZATO** — **Esercizio nuovo** sul **fattore di Oswald $e$**: come i winglet (alette di estremità) lo migliorano e quanto si traduce in risparmio carburante.
>
> 🎯 **Obiettivi**: capire fisicamente cosa fanno i winglet, calcolare la riduzione di resistenza indotta tra 737 Classic (no winglet), 737NG (blended winglet), 737 MAX (split scimitar), e quantificare il risparmio carburante annuo.

---

## 📋 Testo del problema

Confronta lo stesso Boeing 737-800 (peso = 70 t, $S = 124{,}6$ m², crociera FL350 $\rho = 0{,}38$ kg/m³, $V = 230$ m/s) in 3 versioni:

| Versione | Tipo winglet | $\lambda$ effettivo | $e$ effettivo |
|---|---|---|---|
| **737-800 Classic (anni '90)** | Nessuno | 9,5 | 0,80 |
| **737-800 NG con blended winglet** (2003+) | Inclinato 60°, 2,4 m alto | 9,8 | 0,86 |
| **737 MAX 8 (2017+)** | Split scimitar (a forcella) | 10,2 | 0,89 |

$C_{D,0} = 0{,}025$ (invariato).

**Determina**:

1. $C_L$ in crociera (uguale per tutte: $L = W$)
2. $C_{D,i}$ per le 3 versioni
3. $C_D$ totale e $E$ in crociera per le 3 versioni
4. Resistenza $D$ in newton e potenza richiesta $P$
5. **Risparmio carburante annuo** (assumendo 3000 ore di volo/anno e che il consumo sia proporzionale a $D$)

---

## 🖼️ Diagramma del problema

Il **vortice di estremità alare** (wingtip vortex) si forma perché l'aria del ventre (alta pressione) "scappa" sopra il dorso (bassa pressione) all'estremità. Questo vortice si porta via energia → resistenza indotta.

**Winglet** = aletta verticale al tip che **ostacola la fuga d'aria** → vortice più piccolo → **$e$ effettivo aumenta** (l'ala "vede" un allungamento maggiore di quello geometrico).

---

## 📊 Dati noti / da trovare

| | Classic | NG (blended) | MAX (split) |
|---|---|---|---|
| $\lambda$ effettivo | 9,5 | 9,8 | 10,2 |
| $e$ effettivo | 0,80 | 0,86 | 0,89 |
| $\pi \lambda e$ | $\pi \cdot 9{,}5 \cdot 0{,}80 = 23{,}88$ | $\pi \cdot 9{,}8 \cdot 0{,}86 = 26{,}48$ | $\pi \cdot 10{,}2 \cdot 0{,}89 = 28{,}51$ |

---

## 🧠 Strategia

$C_L$ uguale per le 3 versioni (stessi $W$, $V$, $\rho$, $S$). Cambia $C_{D,i}$ per via di $\pi \lambda e$ diverso.

---

## ✏️ Risoluzione passo-passo

### Passo 1 — Pressione dinamica e $C_L$ (uguali per tutte)

$q = \frac{1}{2} \cdot 0{,}38 \cdot 230^2 = 0{,}5 \cdot 0{,}38 \cdot 52\,900 = 10\,051$ Pa
$W = 70\,000 \cdot 9{,}81 = 686\,700$ N
$C_L = W/(qS) = 686\,700/(10\,051 \cdot 124{,}6) = 686\,700/1\,252\,355 \approx 0{,}548$

### Passo 2 — $C_{D,i}$ per ciascuna versione

$$C_{D,i} = \dfrac{C_L^2}{\pi \lambda e} = \dfrac{0{,}548^2}{\pi \lambda e}$$

$0{,}548^2 = 0{,}3003$

| Versione | $\pi \lambda e$ | $C_{D,i}$ |
|---|---|---|
| Classic | 23,88 | $0{,}3003/23{,}88 = 0{,}01258$ |
| NG (blended) | 26,48 | $0{,}3003/26{,}48 = 0{,}01134$ |
| MAX (split) | 28,51 | $0{,}3003/28{,}51 = 0{,}01054$ |

### Passo 3 — $C_D$ totale ed efficienza

| Versione | $C_{D,0}$ | $C_{D,i}$ | $C_D$ totale | $E = C_L/C_D$ |
|---|---|---|---|---|
| Classic | 0,025 | 0,01258 | 0,03758 | **14,58** |
| NG | 0,025 | 0,01134 | 0,03634 | **15,08** |
| MAX | 0,025 | 0,01054 | 0,03554 | **15,42** |

**Miglioramento**: $E$ +3,4% da Classic a NG, +5,8% da Classic a MAX.

### Passo 4 — Resistenza in newton e potenza

$D = q \cdot S \cdot C_D = 10\,051 \cdot 124{,}6 \cdot C_D = 1\,252\,355 \cdot C_D$

| Versione | $D$ (N) | Riduzione % | $P = D \cdot V$ (kW) |
|---|---|---|---|
| Classic | $1\,252\,355 \cdot 0{,}03758 = 47\,063$ | — | $47063 \cdot 230 = 10\,824$ |
| NG | $1\,252\,355 \cdot 0{,}03634 = 45\,491$ | **-3,3%** | $10\,463$ |
| MAX | $1\,252\,355 \cdot 0{,}03554 = 44\,489$ | **-5,5%** | $10\,233$ |

### Passo 5 — Risparmio carburante annuo

Consumo motore $\propto P$. **Riduzione consumo**:

- NG vs Classic: **-3,3%**
- MAX vs Classic: **-5,5%**

Per **3000 h di volo/anno** (utilizzo medio compagnia low-cost):

Consumo nominale 737 (Classic): ~2 700 kg/h × 3000 h = **8 100 t carburante/anno**.

| Versione | Consumo annuo | Risparmio annuo |
|---|---|---|
| Classic | 8 100 t | — |
| NG | 7 833 t | **267 t** |
| MAX | 7 654 t | **446 t** |

**A prezzo carburante** ~$0,80/kg: risparmio NG = $214 000/anno per aereo. Per una flotta di 100 aerei: $21,4 milioni/anno.

**MAX vs Classic**: risparmio **$357 000/anno per aereo** = $35,7M per flotta di 100.

→ **Per questo Boeing/Airbus aggiungono winglet a OGNI nuovo modello**: il ROI (return on investment) è di pochi mesi.

---

## ✅ Verifica di plausibilità

Boeing dichiara ufficialmente:

- 737 NG con blended winglet: **risparmio carburante 3-5% rispetto al senza winglet** ✅
- 737 MAX con split scimitar: **risparmio aggiuntivo 1,5-2% rispetto a NG** ✅

I nostri 3,3% e 5,5% (NG e MAX vs Classic) coincidono coi valori certificati. Il modello del liceo conferma i numeri reali del business aviation.

### Aspetti reali aggiuntivi non coperti

- I winglet aumentano leggermente il **peso** (~200 kg per coppia) → riduce parte del beneficio
- Aumentano **resistenza parassita** in atterraggio (a piccoli angoli di attacco) → -0,5% di $C_D$ in cruise
- **Vibrazioni in turbolenza** = attenuate con winglet (sicurezza extra)

---

## 🔄 Variante per autovalutazione

Una compagnia low-cost ha 200 aerei Classic (no winglet). Calcola:

a. Consumo carburante annuo totale (200 aerei × 3000 h × 2,7 t/h)
b. Costo carburante annuo (a $0,80/kg)
c. Risparmio annuo se **converte tutta la flotta a NG** (retrofit possibile per ~$1,5M ad aereo, costo totale $300M)
d. Tempo di rientro dell'investimento

<details markdown="1">
<summary>👉 Solo il risultato (prima provaci da solo!)</summary>

a. Consumo annuo: $200 \cdot 3000 \cdot 2{,}7 = 1\,620\,000$ t = **1,62 Mt**

b. Costo: $1{,}62 \times 10^9$ kg × $0{,}80 = $ **$1,3 miliardi/anno**

c. Risparmio 3,3% = $1{,}3 \times 10^9 \cdot 0{,}033 = $ **$43 milioni/anno**

d. Tempo rientro: $300M / 43M/anno = $ **7 anni**.

→ Se la flotta volerà ancora 7+ anni, conviene. Se è in dismissione tra 5 anni, non conviene. Per questo American Airlines (flotta giovane) ha messo winglet a tutti i 737NG, mentre alcune compagnie regionali con 737 Classic anziani li dismettono senza retrofit.

</details>

---

## 🎓 Cosa hai imparato

- I **winglet** aumentano il **fattore di Oswald $e$** ostacolando i vortici di estremità.
- $C_{D,i} \propto 1/(\pi \lambda e)$: aumentare $e$ del 10% riduce indotta del 9%.
- Il guadagno in **efficienza totale** è 3-6% (a seconda della percentuale di indotta in crociera).
- Su un aereo che vola 3000 h/anno, **3-6% di risparmio = $200-400 mila/anno**.
- Per questo i winglet sono diventati **standard** su tutti i jet moderni (737NG/MAX, 757-Winglet retrofit, A320 sharklets, A330 winglet, 787 raked tip).
- Boeing/Airbus calcolano questi numeri con simulazioni CFD complesse — ma il **modello del liceo** dà la risposta giusta entro l'1%.

---

## ➡️ Prossimo

[Esercizio 25 — Atterraggio short-field Pilatus PC-6](./25-avanzato-stol.md) o l'[indice](../tutti.md).
