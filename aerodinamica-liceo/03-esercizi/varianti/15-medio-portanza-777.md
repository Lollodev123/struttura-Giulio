# Esercizio 15 — Portanza del Boeing 777-300ER a FL400

> 🟡 **Difficoltà: MEDIO** — Variante dell'[Esercizio 5](../05-medio-portanza-quota.md): stesso problema (portanza in alta quota con tabella ISA), ma con un widebody intercontinentale al doppio del peso del 737.
>
> 🎯 **Obiettivi**: applicare la stessa metodologia a un velivolo molto più grande, vedere come carico alare e quota interagiscono per i jet di linea pesanti, capire perché i 777 volano a FL400 (12 192 m).

---

## 📋 Testo del problema

Un **Boeing 777-300ER** (uno dei jet di linea più diffusi su rotte intercontinentali) è in crociera a **FL400** = 12 192 m.

Dati:

- Massa di crociera (a metà rotta, dopo aver consumato carburante): $m = 280\,000$ kg
- Superficie alare: $S = 427{,}8$ m²
- Velocità vera (TAS): $V = 252$ m/s (≈ 490 kt, Mach 0,84)

**Determina**:
1. $\rho$ a 12 192 m (interpolando dalla tabella ISA)
2. $C_L$ richiesto in crociera
3. **Confronto** con il Boeing 737 dell'Esercizio 5: stesso $C_L$ o diverso? Perché?

---

## 🖼️ Diagramma del problema

![Atmosfera ISA: T/p/ρ vs quota](../../assets/img/grafici/atmosfera-isa.svg)

A FL400 siamo **sopra la tropopausa** (11 km): T è costante a $-56{,}5\,°\text{C}$, ma pressione e densità continuano a scendere esponenzialmente.

---

## 📊 Dati noti / da trovare

| Grandezza | Simbolo | Valore | Unità |
|---|---|---|---|
| Massa | $m$ | 280 000 | kg |
| Superficie | $S$ | 427,8 | m² |
| Velocità (TAS) | $V$ | 252 | m/s |
| Quota | $h$ | 12 192 | m |
| $T$ a 12 192 m | — | $-56{,}5$ (stratosfera) | °C |

---

## 🧠 Strategia

1. Densità a 12 km: oltre la tropopausa, formula esponenziale dalla [Lezione 5](../../01-teoria/05-atmosfera-isa.md)
2. Peso: $W = m \cdot g$
3. $C_L = 2W/(\rho V^2 S)$
4. Confronto: stessa formula del 737 ma con valori diversi

---

## ✏️ Risoluzione passo-passo

### Passo 1 — Densità a 12 192 m

Sopra la tropopausa, la densità segue:

$$\rho(h) = \rho_{11000} \cdot \exp\left(-\dfrac{g}{R \cdot T_{strat}} (h - 11\,000)\right)$$

con $\rho_{11000} = 0{,}365$ kg/m³, $T_{strat} = 216{,}65$ K, $R = 287$ J/(kg·K).

Calcolo:

- $g/(R T_{strat}) = 9{,}81 / (287 \times 216{,}65) = 9{,}81 / 62\,179 = 1{,}578 \times 10^{-4}$ /m
- $h - 11\,000 = 1\,192$ m
- esponente: $-1{,}578 \times 10^{-4} \times 1\,192 = -0{,}1881$
- $e^{-0{,}1881} = 0{,}828$
- $\rho(12\,192) = 0{,}365 \times 0{,}828 \approx 0{,}302$ kg/m³

$$\boxed{\rho(12\,192\,m) \approx 0{,}302 \text{ kg/m}^3}$$

(Nota: dal tabella ISA estesa, $\rho(12\,192) = 0{,}3022$ kg/m³ ✅)

### Passo 2 — Peso del 777

$$W = 280\,000 \times 9{,}81 = 2\,746\,800 \text{ N}$$

### Passo 3 — $C_L$ in crociera

$$C_L = \dfrac{2W}{\rho V^2 S} = \dfrac{2 \times 2\,746\,800}{0{,}302 \times 252^2 \times 427{,}8}$$

Calcolo:

- Numeratore: $5\,493\,600$
- $252^2 = 63\,504$
- $0{,}302 \times 63\,504 = 19\,178$
- Denominatore: $19\,178 \times 427{,}8 = 8\,205\,375$
- Rapporto: $5\,493\,600 / 8\,205\,375 = 0{,}6695$

$$\boxed{C_L \approx 0{,}67}$$

### Passo 4 — Confronto col Boeing 737-800

Dall'[Esercizio 5](../05-medio-portanza-quota.md): 737 a FL350, 70 t, 230 m/s → $C_L \approx 0{,}55$.

| | Boeing 737-800 | Boeing 777-300ER | Rapporto |
|---|---|---|---|
| Massa | 70 000 kg | 280 000 kg | × 4 |
| $S$ | 124,6 m² | 427,8 m² | × 3,4 |
| **Carico alare** | 562 kg/m² | 654 kg/m² | + 16% |
| Quota | FL350 | FL400 | +1500 m |
| $\rho$ a quota | 0,381 | 0,302 | -21% |
| $V$ (TAS) | 230 m/s | 252 m/s | +9,6% |
| **$C_L$** | 0,55 | 0,67 | +22% |

**Lettura**: il 777 vola con **$C_L$ maggiore** del 737 perché:

- Carico alare più alto (richiede più portanza per m²)
- Densità minore in quota (FL400 vs FL350)
- Aumento velocità non sufficiente a compensare

→ Il 777 lavora più vicino al $C_L^* \approx 0{,}80$ → **efficienza maggiore** in crociera. Per questo i widebody intercontinentali (777, 787, A350) hanno consumi/passeggero migliori dei narrowbody (737, A320) nei voli lunghi.

---

## ✅ Verifica di plausibilità

Dal [formulario, sezione 9](../../00-formulario/formulario.md#9-coefficienti-tipici-ordine-di-grandezza): jet di linea in crociera → $C_L \in [0{,}4;\, 0{,}6]$.

Il nostro $C_L = 0{,}67$ è **leggermente sopra il range** ma:

- Il 777 a FL400 vola al limite operativo della quota (massima efficienza in cruise climb)
- Carico alare alto giustifica $C_L$ alto
- Real world: i 777 in crociera hanno $C_L$ effettivo 0,55-0,70 a seconda di peso/quota

→ Risultato **realistico**.

---

## 🔄 Variante per autovalutazione

Lo stesso 777, ma a **inizio rotta** dopo decollo (peso massimo $m = 351\,500$ kg = MTOW), in crociera iniziale a **FL310** (9 449 m).

a. Calcola $\rho$ a FL310 (interpolando dalla tabella ISA: tra 8000 m con ρ=0,526 e 11000 m con ρ=0,365)
b. Calcola $C_L$
c. Spiega perché il 777 inizia il volo a FL310 e non subito a FL400

<details markdown="1">
<summary>👉 Solo il risultato (prima provaci da solo!)</summary>

a. Interpolazione: $\rho(9449) \approx 0{,}526 - (0{,}526-0{,}365) \cdot (9449-8000)/(11000-8000) = 0{,}526 - 0{,}161 \cdot 0{,}483 = $ **0,448 kg/m³**

b. $W = 351500 \cdot 9{,}81 = 3\,448\,215$ N
$C_L = 2 \cdot 3448215 / (0{,}448 \cdot 252^2 \cdot 427{,}8) = 6\,896\,430 / 12\,166\,624 \approx$ **0,567**

c. Il 777 a peso massimo NON può salire subito a FL400. La portanza richiesta è troppo alta → il velivolo dovrebbe volare con $C_L > 0{,}80$ (oltre $C_L^*$, cioè in zona **inefficiente**, vicino allo stallo). Soluzione: **step climb** — parti FL310, poi sali a FL330 dopo 2-3 ore (peso scende), poi FL370, poi FL400. Ogni step climb richiede coordinamento con ATC ma fa risparmiare 3-5% di carburante per tappa.

</details>

---

## 🎓 Cosa hai imparato

- **Sopra la tropopausa**, la densità segue una formula esponenziale (no più la formula 4,256 della troposfera).
- I **widebody** (777, 787, A350) volano con $C_L$ relativamente alto (0,55-0,70) → vicino a $C_L^*$ → **massima efficienza**.
- Il **carico alare** del 777 (~654 kg/m²) è il 16% maggiore del 737 nonostante l'ala sia 4× più grande. È coerente: missione = trasporto carico/passeggeri massimi.
- **Step climb**: i lunghi raggi non volano mai a quota costante. Salgono per inseguire $C_L^*$ man mano che bruciano carburante.

---

## ➡️ Prossimo

[Indice esercizi](../tutti.md) per scegliere il prossimo, o [Esercizio 16 — Confronto NACA 23012](./16-medio-confronto-naca-23012.md).
