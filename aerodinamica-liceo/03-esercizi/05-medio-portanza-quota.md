# Esercizio 5 — Portanza in quota ISA (Boeing 737-800)

> 🟡 **Difficoltà: MEDIO** — Applicazione della formula di portanza in quota usando la tabella ISA.
>
> 🎯 **Obiettivi didattici**: imparare a (a) usare la tabella ISA per ricavare $\rho$, (b) calcolare $C_L$ a quote diverse, (c) confrontare il comportamento di un velivolo a livello mare e in crociera ad alta quota.

---

## 📋 Testo del problema

Un **Boeing 737-800** è in crociera livellata a **FL350** (Flight Level 350 = 10 670 m). Massa di crociera $m = 70\,000$ kg, velocità vera (TAS) $V = 230$ m/s.

- Superficie alare: $S = 124{,}6$ m²
- Allungamento: $\lambda = 10$
- Quota: $h = 10\,670$ m, atmosfera ISA

**Determina**:
1. La densità $\rho$ alla quota di volo (interpolando dalla tabella ISA)
2. Il coefficiente di portanza $C_L$ richiesto in crociera
3. **Confronto**: se lo stesso velivolo volasse al livello mare a 230 m/s, quale $C_L$ servirebbe? Cosa significa fisicamente?

---

## 🖼️ Diagramma del problema

```
   Crociera FL350 (10 670 m), aria rarefatta:
   
   ρ(0) = 1,225 kg/m³ ────────●──────  livello mare
                              │
                              │ ↑ portanza richiesta = peso
                              │ │   identica alle due quote
                              │ │
                              │ │   MA densità ≠
                              │ │
                              │ │
   ρ(10670) ≈ 0,38 kg/m³ ─────●────── FL350
                              ↓
                              W = m·g
   
   Conseguenza: a parità di V e S, in quota serve C_L MAGGIORE.
```

---

## 📊 Dati noti / da trovare

| Grandezza | Simbolo | Valore | Unità |
|---|---|---|---|
| Massa | $m$ | 70 000 | kg |
| Superficie alare | $S$ | 124,6 | m² |
| Velocità (TAS) | $V$ | 230 | m/s |
| Quota | $h$ | 10 670 | m |
| Allungamento | $\lambda$ | 10 | — |
| **Da trovare** | $\rho(h)$, $C_L$ | ? | — |

---

## 🧠 Strategia di risoluzione

1. **Cosa mi sta chiedendo?** $\rho$ in quota, $C_L$ in quota e $C_L$ al mare per confronto.
2. **Quale fenomeno?** Equilibrio in volo livellato $L = W$, ma con $\rho$ ridotta.
3. **Quali formule?**
   - Tabella ISA per $\rho$ (interpolazione lineare tra 10000 e 11000 m)
   - $C_L = 2W/(\rho V^2 S)$
4. **Dati e unità coerenti?** Sì, tutto SI.
5. **Algebra**: applicare la stessa formula a due densità diverse, confrontare.

---

## ✏️ Risoluzione passo-passo

### Passo 1 — Densità a 10 670 m (interpolazione)

Dalla tabella ISA del [formulario](../00-formulario/formulario.md#7-atmosfera-standard-isa--valori-chiave):

| Quota (m) | $\rho$ (kg/m³) |
|---|---|
| 10 000 | 0,413 |
| 11 000 | 0,365 |

Differenza di densità per 1000 m: $0{,}413 - 0{,}365 = 0{,}048$ kg/m³.
Per ogni metro: $0{,}048/1000 = 4{,}8 \cdot 10^{-5}$ kg/m³ persi.

A 10 670 m, salgo di 670 m sopra i 10 000:
$$\rho(10\,670) \approx 0{,}413 - 670 \times 4{,}8 \cdot 10^{-5} = 0{,}413 - 0{,}032 = 0{,}381 \text{ kg/m³}$$

$$\boxed{\rho \approx 0{,}381 \text{ kg/m³}}$$

### Passo 2 — Peso

$$W = m \cdot g = 70\,000 \times 9{,}81 = 686\,700 \text{ N}$$

### Passo 3 — $C_L$ in crociera FL350

$$C_L = \dfrac{2W}{\rho V^2 S}$$

Sostituisco:
$$C_L = \dfrac{2 \times 686\,700}{0{,}381 \times 230^2 \times 124{,}6}$$

Calcolo a tappe:
- Numeratore: $2 \times 686\,700 = 1\,373\,400$
- $230^2 = 52\,900$
- $0{,}381 \times 52\,900 = 20\,155$
- Denominatore: $20\,155 \times 124{,}6 = 2\,511\,313$
- Rapporto: $1\,373\,400 / 2\,511\,313 = 0{,}547$

$$\boxed{C_L \approx 0{,}55}$$

### Passo 4 — Confronto: $C_L$ al livello mare a stessa V

Stesso peso, stessa $S$, stessa $V$, ma $\rho_0 = 1{,}225$:

$$C_L^{mare} = \dfrac{1\,373\,400}{1{,}225 \times 52\,900 \times 124{,}6}$$

Calcolo:
- $1{,}225 \times 52\,900 = 64\,803$
- $64\,803 \times 124{,}6 = 8\,074\,447$
- $1\,373\,400 / 8\,074\,447 = 0{,}170$

$$C_L^{mare} \approx 0{,}17$$

### Passo 5 — Lettura del confronto

| Quota | $\rho$ (kg/m³) | $C_L$ richiesto |
|---|---|---|
| Livello mare | 1,225 | 0,17 |
| FL350 (10 670 m) | 0,381 | 0,55 |

**Rapporto** $C_L^{quota}/C_L^{mare} = 0{,}55/0{,}17 = 3{,}24 \approx \rho_0/\rho = 1{,}225/0{,}381 = 3{,}21$ ✓

→ **A parità di V e di geometria, $C_L \propto 1/\rho$**. Sopra di 10 km il velivolo lavora con un $C_L$ **3 volte maggiore** che al livello mare.

> 💡 **Significato fisico**: l'aria è "rarefatta" → ogni m² di ala riceve meno massa d'aria al secondo → per generare la stessa portanza, l'ala deve "lavorare di più" (angolo di attacco maggiore, ovvero $C_L$ maggiore). Il pilota lo gestisce automaticamente con il pitch del velivolo.

---

## ✅ Verifica di plausibilità

Dal [formulario, sezione 9](../00-formulario/formulario.md#9-coefficienti-tipici-ordine-di-grandezza):
- "Crociera, jet di linea" → $C_L \in [0{,}4;\, 0{,}6]$.

Il nostro $C_L = 0{,}55$ rientra perfettamente. ✅

Il $C_L = 0{,}17$ al livello mare (con la stessa V) sarebbe **bassissimo** per un 737 — significherebbe che l'aereo sta volando "troppo veloce per il suo peso" e potrebbe addirittura scendere senza voler ridurre quota. In realtà al livello mare il 737 vola a velocità minori per restare in $C_L$ ragionevole.

---

## 🔄 Variante per autovalutazione

Stesso 737 in crociera FL350, ma a **peso più basso** (50 000 kg, fine volo dopo aver consumato carburante). **Ricalcola $C_L$**.

<details markdown="1">
<summary>👉 Solo il risultato (prima provaci da solo!)</summary>

$W = 50000 \times 9{,}81 = 490\,500$ N

$C_L = 2 \cdot 490500 / (0{,}381 \cdot 230^2 \cdot 124{,}6) = 981000 / 2511313 \approx 0{,}391$

→ Con peso ridotto del 28,6%, anche $C_L$ scende del 28,6% (è proporzionale a $W$). Coerente.

**Implicazione operativa**: a fine volo (quando l'aereo è leggero), il pilota può:
- Salire di quota (FL370, FL390): la $\rho$ scende ma il $C_L$ richiesto è già basso
- Risparmiare carburante grazie a parassita ridotta

Si chiama "step climb" — il jet sale gradualmente man mano che brucia carburante.

</details>

---

## 🎓 Cosa hai imparato

- **Tabella ISA è imprescindibile**: per qualsiasi calcolo in quota, $\rho \neq \rho_0$.
- **A parità di V e geometria, $C_L \propto 1/\rho$**: in alta quota il velivolo lavora con $C_L$ molto maggiore.
- **Il jet di linea vola alto perché**: la parassita (proporzionale a $\rho$) scende → meno consumo carburante. Anche se l'indotta è maggiore (alti $C_L$), il bilancio è positivo per voli lunghi.
- **Lo "step climb"** sfrutta il calo di peso per salire progressivamente — un pilota commerciale lo richiede al controllo del traffico aereo a metà rotta.

---

## ➡️ Prossimo

[Esercizio 6 — Confronto profili NACA (Cessna 172 vs caccia)](./06-medio-confronto-naca.md) — l'effetto della scelta del profilo a parità di altre condizioni.
