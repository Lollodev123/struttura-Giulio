# Esercizio 2 — Velocità di stallo (Piper PA-28 Archer)

> 🟢 **Difficoltà: BASE** — Applicazione diretta della formula della velocità di stallo.
>
> 🎯 **Obiettivi didattici**: imparare a (a) calcolare $V_S$ a partire da $C_{L,max}$, (b) capire l'effetto dei flap sulla velocità di stallo, (c) verificare la coerenza con i dati del manuale di volo.

---

## 📋 Testo del problema

Un **Piper PA-28-181 Archer** vola in atmosfera standard al livello del mare. I suoi dati di progetto sono:

- Massa massima al decollo (MTOW): $m = 1\,157$ kg
- Superficie alare: $S = 15{,}8$ m²
- Coefficiente di portanza massimo, **ala pulita** (senza flap): $C_{L,max} = 1{,}5$
- Coefficiente di portanza massimo, **flap pieni** (40°): $C_{L,max,flap} = 2{,}1$

**Determina**:

1. La velocità di stallo $V_S$ con ala pulita
2. La velocità di stallo $V_{S,0}$ con flap pieni
3. La percentuale di riduzione di $V_S$ ottenuta estraendo i flap

---

## 🖼️ Diagramma del problema

```
   Allo stallo, l'aereo mantiene equilibrio verticale appena
   sopra la velocità minima:
   
          L_max = ½ ρ V_S² S C_L,max  ──→ uguagliata a W
          
                  ↑ L_max
                  │
              ●──────●  Piper PA-28
                  │
                  ↓
                  W = m·g
                  
   Stallo: oltre questo angolo (~16°), C_L crolla → portanza
   non basta più a sostenere il peso → l'aereo scende.
```

---

## 📊 Dati noti / da trovare

| Grandezza | Simbolo | Valore | Unità |
|---|---|---|---|
| Massa | $m$ | 1 157 | kg |
| Superficie alare | $S$ | 15,8 | m² |
| $C_{L,max}$ ala pulita | $C_{L,max}$ | 1,5 | adim. |
| $C_{L,max}$ flap pieni | $C_{L,max,flap}$ | 2,1 | adim. |
| Densità aria (livello mare ISA) | $\rho$ | 1,225 | kg/m³ |
| Accelerazione gravità | $g$ | 9,81 | m/s² |
| **Da trovare** | $V_S$, $V_{S,0}$ | ? | m/s e kt |

---

## 🧠 Strategia di risoluzione

1. **Cosa mi sta chiedendo?** Due velocità di stallo (con e senza flap), e il rapporto tra le due.
2. **Quale fenomeno è coinvolto?** Lo stallo: il punto in cui l'ala genera la massima portanza possibile, oltre il quale crolla. Per restare in volo livellato a $C_{L,max}$, occorre che $L_{max} = W$.
3. **Quali formule mi servono?**
   - Equilibrio verticale: $L = W$
   - Portanza: $L = \frac{1}{2}\rho V^2 S C_L$
   - Allo stallo: $L_{max} = \frac{1}{2}\rho V_S^2 S C_{L,max}$
   - Da cui: $V_S = \sqrt{\dfrac{2 W}{\rho S C_{L,max}}}$

4. **Dati e unità sono coerenti?** Sì, tutti SI. Il risultato sarà in m/s; converto in nodi alla fine.
5. **Algebra**: stessa formula due volte, con $C_{L,max}$ diverso. Confronto i risultati.

---

## ✏️ Risoluzione passo-passo

### Passo 1 — Calcolare il peso del velivolo
$$W = m \cdot g = 1\,157 \times 9{,}81 = 11\,350{,}17 \text{ N}$$

### Passo 2 — Velocità di stallo con ala pulita
Applicando la formula:
$$V_S = \sqrt{\dfrac{2 W}{\rho S C_{L,max}}}$$

Sostituisco:
$$V_S = \sqrt{\dfrac{2 \times 11\,350{,}17}{1{,}225 \times 15{,}8 \times 1{,}5}}$$

Calcolo a tappe:

- Numeratore: $2 \times 11\,350{,}17 = 22\,700{,}34$
- Denominatore: $1{,}225 \times 15{,}8 \times 1{,}5 = 1{,}225 \times 23{,}7 = 29{,}03$
- Rapporto: $22\,700{,}34 / 29{,}03 = 781{,}96$
- Radice: $\sqrt{781{,}96} = 27{,}96$ m/s

$$\boxed{V_S \approx 28{,}0 \text{ m/s} = 54{,}4 \text{ kt}}$$

### Passo 3 — Velocità di stallo con flap pieni
Stessa formula, ma con $C_{L,max} = 2{,}1$:
$$V_{S,0} = \sqrt{\dfrac{2 \times 11\,350{,}17}{1{,}225 \times 15{,}8 \times 2{,}1}}$$

Calcolo:

- Denominatore: $1{,}225 \times 15{,}8 \times 2{,}1 = 40{,}64$
- Rapporto: $22\,700{,}34 / 40{,}64 = 558{,}54$
- Radice: $\sqrt{558{,}54} = 23{,}63$ m/s

$$\boxed{V_{S,0} \approx 23{,}6 \text{ m/s} = 45{,}9 \text{ kt}}$$

### Passo 4 — Riduzione percentuale di $V_S$ con flap
$$\text{Riduzione} = \dfrac{V_S - V_{S,0}}{V_S} \times 100 = \dfrac{28{,}0 - 23{,}6}{28{,}0} \times 100$$

$$\text{Riduzione} = \dfrac{4{,}4}{28{,}0} \times 100 \approx 15{,}7\%$$

I flap fanno scendere $V_S$ del **~16%**.

> 💡 Trucco rapido: $V_S \propto 1/\sqrt{C_{L,max}}$, quindi il rapporto è $\sqrt{1{,}5/2{,}1} = \sqrt{0{,}714} = 0{,}845$. Coerente.

---

## ✅ Verifica di plausibilità

Il manuale POH (Pilot's Operating Handbook) del Piper PA-28-181 Archer dichiara:

| | Manuale | Calcolato |
|---|---|---|
| $V_S$ pulita | 53 kt | 54 kt ✅ |
| $V_S$ flap pieni | 47 kt | 46 kt ✅ |

Differenza < 2% → modello eccellente. La piccola differenza è dovuta a:

- $C_{L,max}$ effettivo dipende da Reynolds e finitura superficiale
- Il manuale considera condizioni reali (non ISA pura)

**Il risultato è coerente con la realtà operativa del velivolo**.

---

## 🔄 Variante per autovalutazione

Stesso Piper PA-28, stessa configurazione (ala pulita), ma in volo a **2000 m di quota** ISA (anziché al livello mare). **Ricalcola $V_S$**.

Suggerimento: a 2000 m, $\rho = 1{,}007$ kg/m³ (formulario, sezione 7).

<details markdown="1">
<summary>👉 Solo il risultato (prima provaci da solo!)</summary>

$V_S(2000\,m) = \sqrt{\dfrac{2 \times 11350}{1{,}007 \times 15{,}8 \times 1{,}5}} = \sqrt{\dfrac{22700}{23{,}87}} = \sqrt{951{,}1} \approx 30{,}8$ m/s ≈ **59,9 kt**.

> Aumento del 10% rispetto al livello mare: $V_S$ in quota è **maggiore** perché $\rho$ è minore. È una delle ragioni per cui i decolli/atterraggi in alta quota richiedono piste più lunghe.

</details>

---

## 🎓 Cosa hai imparato

- La **velocità di stallo** dipende da $W$, $\rho$, $S$, $C_{L,max}$ — tutti e quattro.
- I **flap** servono a **ridurre $V_S$** per atterrare in sicurezza: aumentano $C_{L,max}$ → $V_S$ scende come $1/\sqrt{C_{L,max}}$.
- A parità di velivolo e configurazione, **$V_S$ aumenta in quota** perché $\rho$ scende.
- Il calcolo da formulario coincide entro il 2% con il dato del manuale di volo → **fidati delle formule che hai imparato**.

---

## ➡️ Prossimo

[Esercizio 3 — Resistenza in crociera (ATR 72)](./03-base-resistenza-atr.md) — applica la formula della resistenza a un velivolo regionale.
