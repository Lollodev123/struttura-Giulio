# Esercizio 21 — Decollo A320 da Cuzco (3 399 m, alta quota tropicale)

> 🔴 **Difficoltà: AVANZATO** — Variante dell'[Esercizio 9](../09-avanzato-decollo-flap.md): "hot AND high" reale, non teorico. Cuzco è uno degli aeroporti più estremi al mondo per A320.
>
> 🎯 **Obiettivi**: combinare gli effetti di **alta quota** (densità ridotta) e **alta temperatura** (densità ulteriormente ridotta), calcolare $V_S$, $V_R$, $V_2$ in queste condizioni reali, e capire perché LATAM/Sky Airlines limitano il peso al decollo a Cuzco.

---

## 📋 Testo del problema

L'aeroporto **Alejandro Velasco Astete** di Cuzco (Perù, codice CUZ) si trova a **3 399 m** di quota. In una giornata di luglio (inverno australe ma temperatura tropicale): $T = 18°C$ (ISA standard a 3399 m sarebbe $T = 15 - 0{,}0065 \times 3399 = -7°C$, quindi siamo **+25°C sopra ISA**!).

Un **Airbus A320-200** decolla in queste condizioni a:

- Massa = $m = 70\,000$ kg (ridotta sotto MTOW = 78 000 kg per restrizioni operative)
- $S = 122{,}6$ m²
- $C_{L,max,T/O}$ con flap CONF 1+F = 2,00

**Determina**:

1. La densità $\rho$ effettiva a Cuzco in questa giornata
2. $V_S$ in configurazione di decollo
3. $V_R$ e $V_2$ (in m/s e in nodi)
4. Confronto con le stesse velocità in **Roma Fiumicino (livello mare ISA)**
5. Quanto è più lunga la pista necessaria a Cuzco?

---

## 🖼️ Diagramma del problema

![Sequenza decollo](../../assets/img/grafici/sequenza-decollo.svg)

Sequenza V_S → V_R → V_2 invariata. Cambiano i **valori** delle velocità per via di $\rho$ ridotta.

---

## 📊 Dati noti / da trovare

| | Roma (mare ISA) | Cuzco (3399 m, +25°C) |
|---|---|---|
| Quota | 0 m | 3 399 m |
| Temperatura | 15°C = 288,15 K | 18°C = 291,15 K |
| Pressione (ISA) | 101 325 Pa | ~67 000 Pa |
| Densità calcolata | 1,225 | da calcolare |

---

## 🧠 Strategia

1. **Pressione a Cuzco**: dalla [tabella ISA](../../00-formulario/formulario.md#7-atmosfera-standard-isa--valori-chiave), interpolando a 3399 m
2. **Densità con T reale**: $\rho = p/(R T)$, con $T = 291{,}15$ K (NON quella ISA)
3. $V_S = \sqrt{2W/(\rho S C_{L,max})}$ per Roma e Cuzco
4. $V_R = 1{,}1 V_S$, $V_2 = 1{,}2 V_S$
5. Distanza decollo $\propto V_R^2 / \rho$ (energia + spinta motore minore)

---

## ✏️ Risoluzione passo-passo

### Passo 1 — Pressione a 3399 m (ISA)

Tabella ISA: a 3000 m $p = 70\,109$ Pa, a 5000 m $p = 54\,020$ Pa.
Interpolazione lineare a 3399 m:
$$p(3399) \approx 70\,109 - (70\,109 - 54\,020) \times \dfrac{3399 - 3000}{5000 - 3000}$$
$$= 70\,109 - 16\,089 \times 0{,}1995 = 70\,109 - 3\,210 = 66\,899 \text{ Pa}$$

(Esatto da formula barometrica: 66 906 Pa. Accurato.)

### Passo 2 — Densità a Cuzco

$T = 18°C = 291{,}15$ K, $R = 287$ J/(kg·K):

$$\rho = \dfrac{p}{R T} = \dfrac{66\,899}{287 \times 291{,}15} = \dfrac{66\,899}{83\,560} \approx 0{,}801 \text{ kg/m}^3$$

→ Densità Cuzco (caldo) = **65% di Roma livello mare**!

(Per confronto, $\rho$ ISA standard a 3399 m sarebbe ~0,890 kg/m³ → giornata calda riduce ulteriormente del 10%.)

### Passo 3 — Peso

$$W = 70\,000 \times 9{,}81 = 686\,700 \text{ N}$$

### Passo 4 — $V_S$, $V_R$, $V_2$ a Cuzco

$$V_S^{Cuzco} = \sqrt{\dfrac{2 \times 686\,700}{0{,}801 \times 122{,}6 \times 2{,}00}} = \sqrt{\dfrac{1\,373\,400}{196{,}40}} = \sqrt{6\,993} \approx 83{,}6 \text{ m/s}$$

In nodi: $83{,}6 / 0{,}5144 \approx $ **162 kt**

$V_R = 1{,}1 \times 83{,}6 = 91{,}96$ m/s = **179 kt**
$V_2 = 1{,}2 \times 83{,}6 = 100{,}32$ m/s = **195 kt**

### Passo 5 — Confronto con Roma livello mare ISA

Da [Esercizio 9](../09-avanzato-decollo-flap.md), peso 78 000 kg → $V_S = 71{,}4$ m/s. **Riproporziono per 70 000 kg** (rapporto $\sqrt{70/78} = 0{,}947$): $V_S^{Roma} = 71{,}4 \times 0{,}947 = 67{,}6$ m/s = **131 kt**.

| Velocità | Roma (mare) | Cuzco (3399 m, +25°C) | Aumento % |
|---|---|---|---|
| $V_S$ | 131 kt | **162 kt** | **+24%** |
| $V_R$ | 144 kt | 179 kt | +24% |
| $V_2$ | 158 kt | 195 kt | +24% |

→ Tutte le V-speeds aumentano del **24%** a Cuzco rispetto a Roma.

### Passo 6 — Lunghezza pista necessaria

Distanza decollo $\propto V_R^2 / \rho \cdot 1/\text{spinta}$. La spinta motori a Cuzco scende per via di $\rho$ ridotta (~ -25% per turbofan a 3400 m caldo) e velocità di ingresso ridotta.

| | Roma | Cuzco |
|---|---|---|
| $V_R$ | 144 kt | 179 kt |
| $V_R^2$ | 20 736 | 32 041 |
| Rapporto $V_R^2$ | 1 | × 1,55 |
| Rapporto 1/$\rho$ | 1 | × 1,53 |
| Rapporto spinta | 1 | × 1,33 |
| **Cumulativo distanza** | × 1 | **× 3,1** |

→ Pista necessaria a Cuzco è **~3 volte** quella di Roma.

A Roma A320 a 70 t: pista decollo ~1700 m. **A Cuzco**: ~5300 m teorici!

**Cuzco ha pista di 3400 m**. → A320 può decollare SOLO a peso ridotto (sotto 65 000 kg per stare nei margini di sicurezza FAA).

---

## ✅ Verifica di plausibilità

LATAM, Sky Airlines, Avianca operano A320 da Cuzco con queste **restrizioni reali**:

- Peso decollo massimo: **62-65 t** (vs 78 t MTOW) → 17% in meno
- Solo voli regionali brevi (Lima, Arequipa, La Paz)
- **Decolli solo al mattino presto** (T più bassa = $\rho$ più alta)
- Spesso operano A319 (più leggero) invece di A320
- Boeing 757 (più potente) può decollare a peso pieno; A320 no

**El Alto (La Paz, 4061 m, +30°C estivo)** è ancora peggio: alcuni voli internazionali sono cancellati nelle ore più calde dell'estate.

### Effetto ulteriore: salita

Dopo decollo, l'A320 deve **salire dell'altimetro 35 ft AGL** in 11 secondi (regolamento FAA). A Cuzco, con motori ridotti del 25%, la **rate of climb** scende del 50%! Alcuni A320 anziani ($V_2$ insufficiente) potrebbero non riuscire a salire abbastanza in caso di motore in avaria.

---

## 🔄 Variante per autovalutazione

L'aeroporto **Lhasa Gonggar** (Cina, Tibet) è a **3 569 m** di quota. Su A320 con $m = 65\,000$ kg in giornata invernale ($T = -10°C$), calcola:

a. Densità (NB: aria fredda, opposta del problema)
b. $V_S$
c. È più o meno problematico di Cuzco?

<details markdown="1">
<summary>👉 Solo il risultato (prima provaci da solo!)</summary>

a. Pressione a 3569 m ISA: ~64 700 Pa (interpolando)
$T = -10°C = 263{,}15$ K
$\rho = 64700/(287 \cdot 263{,}15) = 64700/75524 \approx$ **0,857 kg/m³** (-30% rispetto a livello mare)

→ **Più alta** della densità di Cuzco (0,801)! L'aria fredda compensa parzialmente la quota.

b. $W = 65000 \cdot 9{,}81 = 637\,650$ N
$V_S = \sqrt{(2 \cdot 637650)/(0{,}857 \cdot 122{,}6 \cdot 2)} = \sqrt{1275300/210{,}14} = \sqrt{6\,068} \approx$ **77,9 m/s = 151 kt**

c. **Lhasa è meno problematico di Cuzco** (151 kt vs 162 kt) GRAZIE all'aria fredda. Per questo le compagnie cinesi/tibetane operano A320 a Lhasa senza grandi restrizioni in inverno, mentre in estate (T = 25°C) il problema diventa serio.

</details>

---

## 🎓 Cosa hai imparato

- **Hot AND high** è un problema cumulativo: alta quota + alta T → densità minorissima.
- Tutte le **V-speeds aumentano del ~25%** a 3400 m caldo rispetto al livello mare ISA.
- La **distanza decollo triplica** per effetto cumulato di velocità + densità + spinta motori.
- Le compagnie aeree applicano **restrizioni di peso** ai aeroporti d'alta quota — calcolate dal CAA/FAA con simulatori certificati.
- La **temperatura** è una variabile altrettanto importante della quota: La Paz a -10°C in inverno è OK, a +30°C in estate è critica.

---

## ➡️ Prossimo

[Esercizio 22 — Polare del Concorde](./22-avanzato-concorde.md) o l'[indice](../tutti.md).
