# Esercizio 3 — Resistenza in crociera (ATR 72-600)

> 🟢 **Difficoltà: BASE** — Applicazione della formula della resistenza con decomposizione parassita+indotta.
>
> 🎯 **Obiettivi didattici**: imparare a (a) calcolare $C_L$ in crociera in quota, (b) decomporre $C_D$ in parassita e indotta, (c) ottenere la spinta richiesta dal motore.

---

## 📋 Testo del problema

Un **ATR 72-600** (turboelica regionale) è in crociera livellata a **7 000 m** di quota in atmosfera standard ISA. Velocità di crociera vera (TAS) **140 m/s** (~272 kt). Dati:

- Massa di crociera: $m = 22\,000$ kg
- Superficie alare: $S = 61$ m²
- Allungamento alare: $\lambda = 12$
- Coefficiente di resistenza parassita: $C_{D,0} = 0{,}025$
- Fattore di Oswald: $e = 0{,}85$

**Determina**:
1. Il coefficiente di portanza $C_L$ richiesto
2. Il coefficiente di resistenza indotta $C_{D,i}$
3. La resistenza totale $D$ in newton
4. La spinta totale richiesta ai motori (per i due motori PW127M sommati)

---

## 🖼️ Diagramma del problema

```
   Crociera livellata, quota costante:
   
                    ↑ L (= W)
                    │
         ←────●─────────●──→ T (= D)
              D                              
                    │
                    ↓
                    W = m·g
                    
   Equazioni di equilibrio:
       L = W                (verticale)
       T = D                (orizzontale)
       
   Resistenza decomposta:
       C_D = C_D,0 + C_D,i
              ↑       ↑
         parassita   indotta = C_L²/(π λ e)
```

---

## 📊 Dati noti / da trovare

| Grandezza | Simbolo | Valore | Unità |
|---|---|---|---|
| Massa | $m$ | 22 000 | kg |
| Superficie alare | $S$ | 61 | m² |
| Allungamento alare | $\lambda$ | 12 | adim. |
| Resistenza parassita | $C_{D,0}$ | 0,025 | adim. |
| Fattore di Oswald | $e$ | 0,85 | adim. |
| Velocità (TAS) | $V$ | 140 | m/s |
| Quota | $h$ | 7 000 | m |
| Densità aria a 7000 m (ISA) | $\rho$ | 0,590 | kg/m³ |
| **Da trovare** | $C_L$, $C_{D,i}$, $D$, $T$ | ? | — |

> 💡 La densità a 7000 m si interpola dalla tabella ISA del [formulario](../00-formulario/formulario.md#7-atmosfera-standard-isa--valori-chiave): tra 5000 m (ρ=0,736) e 8000 m (ρ=0,526), a 7000 m è circa **0,590 kg/m³**.

---

## 🧠 Strategia di risoluzione

1. **Cosa mi sta chiedendo?** $C_L$, $C_{D,i}$, $D$, $T$ in crociera.
2. **Quale fenomeno è coinvolto?** Equilibrio in volo livellato: $L = W$ e $T = D$.
3. **Quali formule mi servono?**
   - $W = m \cdot g$
   - $L = \frac{1}{2}\rho V^2 S C_L$ → da cui $C_L = 2W/(\rho V^2 S)$
   - $C_{D,i} = C_L^2/(\pi \lambda e)$
   - $C_D = C_{D,0} + C_{D,i}$
   - $D = \frac{1}{2}\rho V^2 S C_D$
4. **Dati e unità sono coerenti?** Sì, tutti SI. Velocità già in m/s. Densità in quota da tabella.
5. **Algebra**: catena di sostituzioni. Calcolo intermedio: la pressione dinamica $q = \frac{1}{2}\rho V^2$ — utile da calcolare una volta sola.

---

## ✏️ Risoluzione passo-passo

### Passo 1 — Peso e pressione dinamica

$$W = m \cdot g = 22\,000 \times 9{,}81 = 215\,820 \text{ N}$$

$$q = \dfrac{1}{2}\rho V^2 = \dfrac{1}{2} \times 0{,}590 \times 140^2 = \dfrac{1}{2} \times 0{,}590 \times 19\,600 = 5\,782 \text{ Pa}$$

### Passo 2 — Coefficiente di portanza

$$C_L = \dfrac{W}{q \cdot S} = \dfrac{215\,820}{5\,782 \times 61} = \dfrac{215\,820}{352\,702} \approx 0{,}612$$

$$\boxed{C_L \approx 0{,}61}$$

> ✅ **Plausibilità**: nel formulario, "regionale/jet in crociera" → $C_L \in [0{,}4;\, 0{,}6]$. 0,61 è leggermente sopra, ma coerente per turboelica che vola a velocità inferiore al jet.

### Passo 3 — Coefficiente di resistenza indotta

$$C_{D,i} = \dfrac{C_L^2}{\pi \lambda e} = \dfrac{0{,}612^2}{\pi \times 12 \times 0{,}85} = \dfrac{0{,}3745}{32{,}04} \approx 0{,}01169$$

$$\boxed{C_{D,i} \approx 0{,}012}$$

### Passo 4 — Coefficiente di resistenza totale

$$C_D = C_{D,0} + C_{D,i} = 0{,}025 + 0{,}012 = 0{,}037$$

> 💡 In crociera, **parassita pesa il 68%** ($0{,}025/0{,}037$), **indotta il 32%**. Tipico per turboelica che vola a velocità moderate (più indotta che jet veloci).

### Passo 5 — Resistenza in newton

$$D = q \cdot S \cdot C_D = 5\,782 \times 61 \times 0{,}037$$

Calcolo:
- $5\,782 \times 61 = 352\,702$
- $352\,702 \times 0{,}037 = 13\,050{,}0$

$$\boxed{D \approx 13\,050 \text{ N}}$$

### Passo 6 — Spinta richiesta totale

In crociera livellata $T = D$:
$$T = D = 13\,050 \text{ N}$$

I due motori Pratt & Whitney PW127M devono erogare in totale **~13,05 kN di spinta** in crociera. Ciascun motore: ~6,5 kN.

> ✅ **Confronto realtà**: PW127M ha potenza di 2 050 kW. In crociera a 140 m/s la spinta = potenza/velocità = $2050000/140 = 14\,640$ N per due motori. Coerente entro il 12% (la differenza viene dall'efficienza dell'elica, ~80%, e da approssimazioni del modello).

---

## ✅ Verifica di plausibilità

**Efficienza** del velivolo nelle condizioni date:
$$E = \dfrac{C_L}{C_D} = \dfrac{0{,}612}{0{,}037} \approx 16{,}5$$

**Distanza in planata da 7000 m** (Lezione 4): $E \times 7000 = 16{,}5 \times 7\,000 = 115\,500$ m ≈ **115 km**.

Coerente: l'ATR ha autonomia di volo a vela ottima, paragonabile ai jet di linea. Se entrambi i motori si fermano a 7000 m, può raggiungere un aeroporto fino a 115 km di distanza.

---

## 🔄 Variante per autovalutazione

Stesso ATR 72, stesso peso e quota, ma in **discesa con motori al minimo a 110 m/s** (~213 kt). Calcola **$C_L$** e **$C_{D,i}$** in queste nuove condizioni.

<details markdown="1">
<summary>👉 Solo il risultato (prima provaci da solo!)</summary>

A 110 m/s:
- $q = \frac{1}{2} \cdot 0{,}590 \cdot 110^2 = 3\,570$ Pa
- $C_L = 215\,820 / (3\,570 \cdot 61) = 215\,820 / 217\,770 \approx 0{,}991$
- $C_{D,i} = 0{,}991^2 / (32{,}04) = 0{,}0306$

→ $C_L \approx 1{,}0$ (alto, vicino a stallo "sicuro") e $C_{D,i} \approx 0{,}031$ (raddoppia rispetto alla crociera!).

**Lettura**: a velocità più basse, l'aereo lavora con $C_L$ alti → la resistenza indotta esplode. Questo è il motivo per cui i piloti scendono *aumentando* la velocità (no, non si "tira il muso giù lentamente"): vanno più veloci, $C_L$ scende, l'aereo "cade" controllatamente.

</details>

---

## 🎓 Cosa hai imparato

- **Decomporre $C_D$** in parassita + indotta è il primo passo per ogni esercizio di resistenza.
- In **crociera ad alta velocità**, parassita domina; a **bassa velocità**, indotta domina.
- L'**efficienza E** del velivolo si trova quasi gratuitamente: $E = C_L/C_D$. È utile per stimare distanze di planata.
- La **densità in quota** (qui 0,59 kg/m³ a 7000 m) entra in TUTTE le formule — mai $\rho_0$ in quota.
- I conti tornano con la realtà: la spinta calcolata coincide entro il 10-15% con i dati ufficiali del motore.

---

## ➡️ Prossimo

[Esercizio 4 — Efficienza massima (aliante ASK-21)](./04-medio-efficienza-aliante.md) — passa al regime degli alianti, dove l'indotta è il problema principale.
