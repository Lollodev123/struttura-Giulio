# Esercizio 13 — Resistenza in crociera (Piper PA-28)

> 🟢 **Difficoltà: BASE** — Variante dell'[Esercizio 3](../03-base-resistenza-atr.md): stessa metodologia (decomposizione $C_R = C_{R,0} + C_{R,i}$), ma su un velivolo di aviazione generale invece di un turboelica regionale.
>
> 🎯 **Obiettivi**: applicare la decomposizione della resistenza a un velivolo "scuola", confrontare i pesi relativi di parassita e indotta in un GA, calcolare la potenza richiesta dal motore.

---

## 📋 Testo del problema

Un **Piper PA-28-181 Archer** è in crociera livellata al livello mare ISA. Dati:

- Massa: $m = 1\,000$ kg
- Superficie alare: $S = 15{,}8$ m²
- Velocità di crociera: $V = 116$ kt
- Allungamento alare: $\lambda = 7{,}6$
- Resistenza parassita: $C_{R,0} = 0{,}033$ (un po' alta, è un velivolo poco aerodinamico)
- Fattore di Oswald: $e = 0{,}80$

**Determina**:
1. $C_p$ in crociera
2. $C_{R,i}$ (resistenza indotta)
3. $C_R$ totale
4. $D$ in newton
5. La **potenza richiesta** in kW (notare che è uguale a $D \cdot V$)

---

## 🖼️ Diagramma del problema

![Sistema delle 4 forze sul velivolo](../../assets/img/grafici/forze-volo-livellato.svg)

In crociera livellata: $P = Q$ e $T = R$. La spinta del motore eguaglia la resistenza totale.

---

## 📊 Dati noti / da trovare

| Grandezza | Simbolo | Valore | Unità |
|---|---|---|---|
| Massa | $m$ | 1 000 | kg |
| Superficie | $S$ | 15,8 | m² |
| Velocità | $V$ | 116 kt → 59,67 | m/s |
| Allungamento | $\lambda$ | 7,6 | — |
| $C_{R,0}$ | — | 0,033 | — |
| $e$ | — | 0,80 | — |
| Densità (mare ISA) | $\rho$ | 1,225 | kg/m³ |

---

## 🧠 Strategia

1. Calcola pressione dinamica $q = \frac{1}{2}\rho V^2$
2. Calcola $C_p = W/(qS)$
3. Calcola $C_{R,i} = C_p^2 / (\pi \lambda e)$
4. Somma $C_R = C_{R,0} + C_{R,i}$
5. Calcola $R = q \cdot S \cdot C_R$
6. Potenza: $P = D \cdot V$

---

## ✏️ Risoluzione passo-passo

### Passo 1 — Conversione + peso + pressione dinamica

$$V = 116 \times 0{,}5144 = 59{,}67 \text{ m/s}$$
$$Q = 1\,000 \times 9{,}81 = 9\,810 \text{ N}$$
$$q = \dfrac{1}{2} \times 1{,}225 \times 59{,}67^2 = \dfrac{1}{2} \times 1{,}225 \times 3\,560{,}5 = 2\,180{,}8 \text{ Pa}$$

### Passo 2 — Coefficiente di portanza

$$C_p = \dfrac{W}{q \cdot S} = \dfrac{9\,810}{2\,180{,}8 \times 15{,}8} = \dfrac{9\,810}{34\,457} \approx 0{,}285$$

### Passo 3 — Resistenza indotta

$$C_{R,i} = \dfrac{C_p^2}{\pi \lambda e} = \dfrac{0{,}285^2}{\pi \times 7{,}6 \times 0{,}80} = \dfrac{0{,}0812}{19{,}10} \approx 0{,}00425$$

$$\boxed{C_{R,i} \approx 0{,}0043}$$

### Passo 4 — Resistenza totale

$$C_R = C_{R,0} + C_{R,i} = 0{,}033 + 0{,}00425 = 0{,}0373$$

→ **Parassita pesa l'88,6%, indotta solo l'11,4%** in crociera. Tipico GA.

### Passo 5 — Resistenza in newton

$$R = q \cdot S \cdot C_R = 2\,180{,}8 \times 15{,}8 \times 0{,}0373 = 1\,285 \text{ N}$$

### Passo 6 — Potenza richiesta

$$P_{req} = D \cdot V = 1\,285 \times 59{,}67 = 76\,675 \text{ W} = 76{,}7 \text{ kW}$$

In cavalli (per confronto col motore reale):
$$P_{req} = 76{,}7 / 0{,}735 \approx 104 \text{ CV}$$

### Passo 7 — Confronto col motore reale

Il Piper PA-28 monta un Lycoming **O-360 da 180 CV**. La potenza richiesta in crociera (104 CV) è solo il **58% della potenza massima** — coerente: i motori GA in crociera lavorano al 60-75% della potenza nominale per non consumare troppo e durare di più.

---

## ✅ Verifica di plausibilità

**Efficienza** del Piper:

$$E = \dfrac{C_p}{C_R} = \dfrac{0{,}285}{0{,}0373} \approx 7{,}6$$

Confronto col Cessna 172 dell'[Esercizio 3 originale](../03-base-resistenza-atr.md): l'ATR ha $E \approx 16{,}5$, perché ha $\lambda = 12$ e profili ottimizzati. Il Piper è "domestico", costruzione semplice, $E$ modesta.

**Distanza di planata** del Piper da 1000 m: $E \times 1{,}0 = 7{,}6$ km. **In caso di avaria motore a 1000 m, hai 7,6 km di raggio per scegliere dove atterrare.**

---

## 🔄 Variante per autovalutazione

Stesso Piper, ma il pilota installa **gambali aerodinamici sulle ruote** (carenature che riducono la resistenza). Nuovo $C_{R,0} = 0{,}028$ invece di 0,033. **Calcola la nuova potenza richiesta**.

<details markdown="1">
<summary>👉 Solo il risultato (prima provaci da solo!)</summary>

$C_R$ nuovo = $0{,}028 + 0{,}0043 = 0{,}0323$
$D$ = $2\,180{,}8 \cdot 15{,}8 \cdot 0{,}0323 = 1\,113$ N
$P$ = $1113 \cdot 59{,}67 = 66\,400$ W = **66,4 kW (90 CV)**

→ Risparmio potenza del **13,4%** → autonomia +13% in crociera. Le carenature ruote costano ~$3000 ma si ripagano in qualche centinaio di ore di volo.

</details>

---

## 🎓 Cosa hai imparato

- In **GA in crociera**, parassita domina (~85-90%), indotta minoritaria (~10-15%). Per ridurre consumi: ridurre parassita (carenature, pulizia).
- $E_{Piper} \approx 7{,}6$ è sotto l'ATR ($E \approx 16{,}5$) perché ha $\lambda$ minore e $C_{R,0}$ maggiore.
- **Potenza richiesta** = $D \cdot V$. Cresce col cubo della velocità: raddoppi V → potenza × 8.
- I motori GA in crociera lavorano **al 60-75% della potenza nominale** — mai al massimo (consumo eccessivo, usura motore).

---

## ➡️ Prossimo

Continua con il livello MEDIO: [Esercizio 14 — Efficienza Schweizer 2-33](./14-medio-efficienza-schweizer.md) o vedi tutti nell'[indice](../tutti.md).
