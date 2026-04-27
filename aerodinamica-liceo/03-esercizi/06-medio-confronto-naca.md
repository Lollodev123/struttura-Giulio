# Esercizio 6 — Confronto profili NACA (asimmetrico vs simmetrico)

> 🟡 **Difficoltà: MEDIO** — Confronta due profili NACA usando la curva $C_L$–$\alpha$ linearizzata.
>
> 🎯 **Obiettivi didattici**: imparare a (a) usare la pendenza della curva $C_L$–$\alpha$, (b) capire l'effetto della curvatura sul coefficiente di portanza a $\alpha = 0$, (c) decidere quale profilo conviene per quale missione.

---

## 📋 Testo del problema

Confronta due profili NACA in **regime lineare** (lontano dallo stallo, $\alpha < 12°$):

- **Profilo A**: NACA 2412 (asimmetrico, ala del **Cessna 172**). Angolo di portanza nulla $\alpha_0 = -2°$.
- **Profilo B**: NACA 0012 (simmetrico, **stabilizzatore** di molti velivoli). Angolo di portanza nulla $\alpha_0 = 0°$.
- Pendenza della curva $C_L$–$\alpha$ per entrambi: $a = 0{,}11$ per grado (vicino al valore teorico $2\pi$ rad/rad).
- $C_{L,max}$ A: 1,55 (a $\alpha_{stallo} = 16°$). $C_{L,max}$ B: 1,40 (a $\alpha_{stallo} = 14°$).

**Determina**:
1. Il $C_L$ di ciascun profilo a $\alpha = 0°, 5°, 10°$
2. Per generare $C_L = 0{,}5$ (crociera tipica), a quale $\alpha$ ciascun profilo deve operare?
3. Quale profilo è più adatto per un Cessna 172 in crociera, e perché?

---

## 🖼️ Diagramma del problema

```
   C_L
    │
 1,5│   ╱──────╲       ←── stallo
    │  ╱        ╲___
    │ ╱
 1,0│╱──── 2412 (asimm)
    │
    │     ╱──── 0012 (simm)
 0,5│   ╱
    │ ╱
 0,0│●──────●─────────── α
    │ ↑    ↑
   α₀=-2°  α₀=0°
    │
   -0,5
   
   In regime lineare:
       Profilo A (2412):  C_L = 0,11 (α + 2°)
       Profilo B (0012):  C_L = 0,11 (α - 0°)
   
   Differenza: A "parte avanti" di 2° rispetto a B → genera già C_L = 0,22 a α = 0°.
```

---

## 📊 Dati noti / da trovare

| Grandezza | Profilo A (NACA 2412) | Profilo B (NACA 0012) |
|---|---|---|
| Angolo portanza nulla $\alpha_0$ | $-2°$ | $0°$ |
| Pendenza $a$ | 0,11 /° | 0,11 /° |
| $C_{L,max}$ | 1,55 | 1,40 |
| $\alpha_{stallo}$ | 16° | 14° |

---

## 🧠 Strategia di risoluzione

1. **Cosa mi sta chiedendo?** Tabulare $C_L$ in funzione di $\alpha$ per i due profili e confrontarli.
2. **Quale fenomeno?** La curva $C_L$–$\alpha$ in regime lineare: $C_L = a(\alpha - \alpha_0)$.
3. **Quali formule?** Solo la formula lineare. Sostituire diversi $\alpha$.
4. **Dati e unità coerenti?** Sì, $\alpha$ in gradi, $a$ in /°. Risultato adimensionale.
5. **Algebra**: tabulare 3 valori per 2 profili. Per la 2ª domanda, isolare $\alpha$.

---

## ✏️ Risoluzione passo-passo

### Passo 1 — Formula della curva linearizzata

In regime lineare (lontano dallo stallo):
$$C_L = a \cdot (\alpha - \alpha_0)$$

con $\alpha$ e $\alpha_0$ in gradi, $a$ in /°. Per il liceo, **niente derivate**: si usa direttamente questa retta.

### Passo 2 — Tabulazione $C_L$ a tre angoli

**Profilo A (NACA 2412)**: $\alpha_0 = -2°$
$$C_L^A(\alpha) = 0{,}11 \times (\alpha - (-2°)) = 0{,}11 \times (\alpha + 2°)$$

**Profilo B (NACA 0012)**: $\alpha_0 = 0°$
$$C_L^B(\alpha) = 0{,}11 \times \alpha$$

| $\alpha$ | $C_L^A$ (2412) | $C_L^B$ (0012) | Differenza |
|---|---|---|---|
| $0°$ | $0{,}11 \times 2 = 0{,}22$ | $0{,}11 \times 0 = 0{,}00$ | +0,22 |
| $5°$ | $0{,}11 \times 7 = 0{,}77$ | $0{,}11 \times 5 = 0{,}55$ | +0,22 |
| $10°$ | $0{,}11 \times 12 = 1{,}32$ | $0{,}11 \times 10 = 1{,}10$ | +0,22 |

> 💡 **Osservazione importante**: la differenza $C_L^A - C_L^B$ è **costante** (= 0,22), pari a $a \cdot |\alpha_0^A - \alpha_0^B|$. È l'effetto della curvatura del profilo asimmetrico: una "spinta gratis" di $C_L = 0{,}22$ a qualsiasi $\alpha$.

### Passo 3 — Quale $\alpha$ serve per $C_L = 0{,}5$?

**Profilo A (2412)**:
$$0{,}5 = 0{,}11 \times (\alpha + 2°) \Rightarrow \alpha + 2 = \dfrac{0{,}5}{0{,}11} = 4{,}55°$$

$$\alpha^A = 2{,}55°$$

**Profilo B (0012)**:
$$0{,}5 = 0{,}11 \times \alpha \Rightarrow \alpha^B = \dfrac{0{,}5}{0{,}11} = 4{,}55°$$

| Profilo | $\alpha$ richiesto per $C_L = 0{,}5$ |
|---|---|
| A (2412) | $2{,}55°$ |
| B (0012) | $4{,}55°$ |

→ Il profilo asimmetrico A ha bisogno di **2° in meno** di angolo di attacco per generare lo stesso $C_L$.

### Passo 4 — Conclusione: quale per il Cessna 172?

Per **crociera del Cessna** ($C_L \approx 0{,}26$, dall'[Esercizio 1](./01-base-portanza-cessna.md)):

- **Profilo A**: $\alpha = (0{,}26/0{,}11) - 2° = 2{,}36 - 2 = 0{,}36°$ (quasi orizzontale, comodissimo)
- **Profilo B**: $\alpha = 0{,}26/0{,}11 = 2{,}36°$ (deve cabrare di 2° rispetto al simmetrico)

Il **profilo A (NACA 2412 asimmetrico)** è preferibile per il Cessna in crociera perché:

1. **Genera $C_L$ già a $\alpha = 0°$** → il velivolo può volare in crociera con la fusoliera quasi orizzontale (passeggeri comodi, visibilità migliore).
2. **$C_{L,max}$ maggiore** (1,55 vs 1,40) → atterra a velocità leggermente più bassa.
3. **$\alpha_{stallo}$ leggermente maggiore** (16° vs 14°) → margine di sicurezza.

**Profilo B (simmetrico)** è preferibile per:
- **Stabilizzatori e timoni di coda**: serve generare portanza in entrambi i sensi (cabrata e picchiata).
- **Acrobatica**: il profilo simmetrico vola identico a testa in giù.
- **Caccia in volo invertito**: nessuna penalità di portanza in volo capovolto.

---

## ✅ Verifica di plausibilità

Il Cessna 172 monta NACA 2412 sull'**ala** (asimmetrico, missione = trasporto). Lo stesso Cessna ha un **profilo simmetrico (NACA 0012 o simile)** sullo **stabilizzatore di coda** — perché la coda deve generare deportanza variabile.

Il Pitts S-2 (acrobatico) ha NACA 0006 simmetrico su ala E coda — nato per volare anche capovolto.

Cessna stallato a $\alpha = 16°$: testato in galleria del vento e confermato dal manuale.

---

## 🔄 Variante per autovalutazione

Un velivolo ha bisogno di un $C_L = 0{,}9$ per atterrare a velocità ridotta. Quale **angolo di attacco** deve mantenere il pilota se l'ala è NACA 2412? E se fosse NACA 0012?

<details markdown="1">
<summary>👉 Solo il risultato (prima provaci da solo!)</summary>

**Profilo 2412**: $0{,}9 = 0{,}11 (\alpha + 2°) \Rightarrow \alpha = (0{,}9/0{,}11) - 2 = 8{,}18 - 2 = $ **6,18°**

**Profilo 0012**: $0{,}9 = 0{,}11 \alpha \Rightarrow \alpha = $ **8,18°**

> Differenza: profilo simmetrico richiede 2° in più di "muso alto" per fare la stessa portanza. In atterraggio questo significa visibilità inferiore (l'aereo è più "cabrato"). Un altro motivo per cui i velivoli da addestramento usano profili asimmetrici.

</details>

---

## 🎓 Cosa hai imparato

- La **curva $C_L$–$\alpha$** è lineare in regime non-stallato, con pendenza $a \approx 0{,}11$/° per la maggior parte dei profili sottili.
- L'**$\alpha_0$ (angolo di portanza nulla)** è la "leva di curvatura": più curvo è il profilo, più $\alpha_0$ è negativo, più portanza si ha "gratis" a $\alpha = 0$.
- I **profili asimmetrici** sono ottimali per missioni di trasporto/turismo (volo livellato, comfort).
- I **profili simmetrici** sono per acrobatica, code orizzontali e velivoli che devono lavorare bene "in entrambi i sensi".
- A parità di altri parametri, **profilo asimmetrico = stesso $C_L$ con $\alpha$ minore** → fusoliera più orizzontale, comfort migliore.

---

## ➡️ Prossimo

[Esercizio 7 — Numero di Reynolds e regime](./07-medio-reynolds.md) — passa a come la viscosità determina la fisica del flusso.
