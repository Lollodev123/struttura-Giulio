# Esercizio 7 — Numero di Reynolds e regime di flusso

> 🟡 **Difficoltà: MEDIO** — Calcolo di $Re$ per uno stesso velivolo in tre condizioni di volo diverse.
>
> 🎯 **Obiettivi didattici**: imparare a (a) calcolare $Re$ con la formula completa, (b) capire quanto $Re$ varia con quota e velocità, (c) identificare il regime (laminare/turbolento) corrispondente.

---

## 📋 Testo del problema

Un **Cessna 172** vola in tre condizioni diverse. Calcola il numero di Reynolds basato sulla **corda media** dell'ala in ciascun caso.

Dati comuni:

- Corda media: $c = 1{,}49$ m
- Viscosità dinamica aria a 15°C: $\mu = 1{,}78 \times 10^{-5}$ Pa·s
- Quota: livello mare ISA per i casi (a) e (c); 3000 m per il (b)

**Condizioni**:

1. **Crociera** al livello mare, $V = 122$ kt (velocità di crociera standard)
2. **Crociera** a 3000 m, stessa V (122 kt)
3. **Avvicinamento finale** al livello mare, $V = 60$ kt

Per ogni caso, calcola $Re$ e classifica il regime (laminare/transizione/turbolento).

---

## 🖼️ Diagramma del problema

$$Re = \dfrac{\rho V c}{\mu}$$

| Caso | Variazione rispetto a (a) | Effetto su Re |
|---|---|---|
| (a) Crociera mare, V alta | — | Re grande |
| (b) Quota, V invariata | $\rho$ scende | Re scende |
| (c) Mare, V bassa | $V$ scende | Re scende |

**Soglie del regime di flusso** (per profilo alare tipico):

| Re | Regime |
|---|---|
| $< 5 \cdot 10^5$ | **Laminare** (strati ordinati) |
| $\approx 5 \cdot 10^5$ | Transizione (instabile) |
| $> 5 \cdot 10^5$ | **Turbolento** (vortici, mescolamento) |

---

## 📊 Dati noti / da trovare

Per ogni caso, ricavo $\rho$ e $V$ in m/s:

| Caso | Quota (m) | $\rho$ (kg/m³) | $V$ (kt) | $V$ (m/s) |
|---|---|---|---|---|
| (a) crociera mare | 0 | 1,225 | 122 | 62,76 |
| (b) crociera 3000 m | 3 000 | 0,909 | 122 | 62,76 |
| (c) approccio mare | 0 | 1,225 | 60 | 30,86 |

> 💡 $V$ in m/s: $V_{kt} \times 0{,}5144$. Densità a 3000 m dalla [tabella ISA](../00-formulario/formulario.md#7-atmosfera-standard-isa--valori-chiave): 0,909 kg/m³.

---

## 🧠 Strategia di risoluzione

1. **Cosa mi sta chiedendo?** Tre $Re$ e relativi regimi.
2. **Quale fenomeno?** Numero di Reynolds: rapporto tra forze inerziali e viscose, decide laminare/turbolento.
3. **Quali formule?** $Re = \rho V c / \mu$. Una sola, applicata 3 volte.
4. **Dati e unità coerenti?** Sì: $\rho$ kg/m³, $V$ m/s, $c$ m, $\mu$ Pa·s = kg/(m·s) → $Re$ adimensionale.
5. **Algebra**: ripeti il calcolo con gli input diversi.

---

## ✏️ Risoluzione passo-passo

### Caso (a) — Crociera al livello mare

$$Re_a = \dfrac{\rho \cdot V \cdot c}{\mu} = \dfrac{1{,}225 \times 62{,}76 \times 1{,}49}{1{,}78 \times 10^{-5}}$$

Numeratore:

- $1{,}225 \times 62{,}76 = 76{,}88$
- $76{,}88 \times 1{,}49 = 114{,}55$

Rapporto:
$$Re_a = \dfrac{114{,}55}{1{,}78 \times 10^{-5}} = 6{,}43 \times 10^6$$

$$\boxed{Re_a \approx 6{,}4 \times 10^6 \text{ — TURBOLENTO}}$$

### Caso (b) — Crociera a 3000 m

Stessa V e c, ma $\rho = 0{,}909$ kg/m³:

$$Re_b = \dfrac{0{,}909 \times 62{,}76 \times 1{,}49}{1{,}78 \times 10^{-5}}$$

Numeratore:

- $0{,}909 \times 62{,}76 = 57{,}05$
- $57{,}05 \times 1{,}49 = 85{,}01$

Rapporto:
$$Re_b = \dfrac{85{,}01}{1{,}78 \times 10^{-5}} = 4{,}77 \times 10^6$$

$$\boxed{Re_b \approx 4{,}8 \times 10^6 \text{ — TURBOLENTO}}$$

> 📊 Rapporto $Re_b/Re_a = 4{,}77/6{,}43 = 0{,}742 = \rho_b/\rho_a$. Coerente: a parità di V e c, $Re \propto \rho$.

### Caso (c) — Approccio finale al livello mare

$\rho = 1{,}225$, $V = 30{,}86$ m/s, $c = 1{,}49$ m:

$$Re_c = \dfrac{1{,}225 \times 30{,}86 \times 1{,}49}{1{,}78 \times 10^{-5}}$$

Numeratore:

- $1{,}225 \times 30{,}86 = 37{,}80$
- $37{,}80 \times 1{,}49 = 56{,}33$

Rapporto:
$$Re_c = \dfrac{56{,}33}{1{,}78 \times 10^{-5}} = 3{,}16 \times 10^6$$

$$\boxed{Re_c \approx 3{,}2 \times 10^6 \text{ — TURBOLENTO}}$$

### Riassunto e classificazione

| Caso | $Re$ | Regime |
|---|---|---|
| (a) crociera mare | $6{,}4 \times 10^6$ | Turbolento netto |
| (b) crociera 3000 m | $4{,}8 \times 10^6$ | Turbolento |
| (c) approccio mare | $3{,}2 \times 10^6$ | Turbolento (vicino transizione su superfici lisce) |

**Tutti e tre i casi sono in regime turbolento** ($Re > 5 \times 10^5$). Le variazioni operative del Cessna non lo portano mai vicino alla zona laminare.

---

## ✅ Verifica di plausibilità

Dal [formulario, sezione 5](../00-formulario/formulario.md#5-numero-di-reynolds):

> Aviazione generale in crociera: $Re \sim 10^6$ – $10^7$.

I tuoi calcoli (3,2 – 6,4 × 10⁶) rientrano perfettamente. ✅

**Implicazione fisica**: il flusso sul Cessna è sempre turbolento → il punto di transizione è quasi sul bordo d'attacco. Non vale la pena progettare profili NACA serie 6 (laminari) per questo velivolo: a Re così alti la transizione avviene comunque presto, e il vantaggio aerodinamico del laminare è perso.

> 💡 È per questo che il Cessna usa NACA 2412 (profilo "sociale" turbolento robusto), non NACA 64-212 (profilo laminare delicato come quelli del P-51 Mustang).

---

## 🔄 Variante per autovalutazione

Calcola $Re$ per la **coda orizzontale** del Cessna 172 (corda media $c_{coda} = 0{,}82$ m) in crociera al livello mare. Confronta con quello dell'ala. È in regime laminare o turbolento?

<details markdown="1">
<summary>👉 Solo il risultato (prima provaci da solo!)</summary>

$Re_{coda} = (1{,}225 \times 62{,}76 \times 0{,}82) / (1{,}78 \times 10^{-5}) = 63{,}05 / (1{,}78 \times 10^{-5}) \approx 3{,}54 \times 10^6$

→ **Re ~3,5 milioni, turbolento**. Inferiore al Re dell'ala ($6{,}4 \times 10^6$) di un fattore $c_{coda}/c_{ala} = 0{,}82/1{,}49 \approx 0{,}55$ — coerente: $Re \propto c$ a parità di altri parametri.

**Lettura**: la coda lavora a Re inferiore ma sempre nel turbolento. Non ci sono "sorprese" laminari. Per questo i progettisti dimensionano la coda con criteri standard turbolenti.

</details>

---

## 🎓 Cosa hai imparato

- **$Re$ varia molto con la condizione di volo**: stesso aereo, da 3,2 a 6,4 milioni a seconda della velocità e quota.
- **$Re \propto V$**: dimezzi V, dimezzi Re.
- **$Re \propto \rho$**: in quota Re scende perché l'aria si rarefà.
- **$Re \propto c$**: ali grandi → Re grande. La coda ha Re inferiore dell'ala, ma sempre turbolento.
- I velivoli convenzionali (Cessna, ATR, 737) **vivono sempre in turbolento**. Il regime laminare riguarda alianti raffinati, modellini, insetti.
- Conoscere il $Re$ permette di **scegliere il profilo giusto**: a Re alti i profili turbolenti robusti sono migliori; a Re bassi (~10⁵) servono profili laminari speciali.

---

## ➡️ Prossimo

[Esercizio 8 — Velocità di max efficienza in planata (aliante avanzato)](./08-avanzato-planata-aliante.md) — combina più concetti per un calcolo completo.
