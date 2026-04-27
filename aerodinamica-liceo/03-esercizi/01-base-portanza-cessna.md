# Esercizio 1 — Coefficiente di portanza in crociera (Cessna 172)

> 🟢 **Difficoltà: BASE** — Applicazione diretta della formula della portanza.
>
> 🎯 **Obiettivi didattici**: imparare a (a) impostare l'equilibrio in volo livellato, (b) ricavare $C_p$ dalla formula della portanza, (c) verificare la plausibilità del risultato.

---

## 📋 Testo del problema

Un **Cessna 172 Skyhawk** vola in **crociera livellata** al livello del mare in atmosfera standard. I dati del velivolo e della crociera sono:

- Massa totale: $m = 1\,043$ kg (peso al decollo MTOW)
- Superficie alare: $S = 16{,}2$ m²
- Velocità di crociera: $V = 122$ kt (nodi)

**Determinare il coefficiente di portanza $C_p$ richiesto** per mantenere il volo livellato.

---

## 🖼️ Diagramma del problema

![Sistema delle 4 forze sul velivolo in volo livellato](../assets/img/grafici/forze-volo-livellato.svg)

Il velivolo è in equilibrio sotto **quattro forze**: portanza $P$ (verso l'alto, in rosso), peso $Q$ (verso il basso, in verde), spinta $T$ (in avanti, in arancione), resistenza $R$ (all'indietro, in viola). In **volo livellato a velocità costante**, queste forze si bilanciano a coppie.

---

## 📊 Dati noti / da trovare

| Grandezza | Simbolo | Valore | Unità |
|---|---|---|---|
| Massa | $m$ | 1 043 | kg |
| Superficie alare | $S$ | 16,2 | m² |
| Velocità | $V$ | 122 | kt |
| Densità aria (livello del mare ISA) | $\rho$ | 1,225 | kg/m³ |
| Accelerazione di gravità | $g$ | 9,81 | m/s² |
| **Da trovare** | $C_p$ | ? | adimensionale |

---

## 🧠 Strategia di risoluzione

Prima di scrivere una formula, ragiona così:

1. **Cosa mi sta chiedendo?** Il coefficiente di portanza $C_p$ in una specifica condizione di volo.
2. **Quale fenomeno è coinvolto?** La portanza in volo livellato. La portanza deve uguagliare il peso.
3. **Quali formule mi servono?**
   - Equilibrio verticale: $P = Q = m \cdot g$
   - Definizione di portanza: $P = \frac{1}{2}\rho V^2 S C_p$

4. **Dati e unità sono coerenti?** Quasi: la velocità è in **nodi**, devo convertirla in **m/s** prima di sostituirla.
5. **Algebra**: combino le due equazioni, isolo $C_p$, sostituisco i numeri.

---

## ✏️ Risoluzione passo-passo

### Passo 1 — Convertire la velocità in m/s

$$V = 122 \text{ kt} \times 0{,}5144 \, \frac{\text{m/s}}{\text{kt}} = 62{,}76 \text{ m/s}$$

> 💡 **Memo**: 1 nodo ≈ 0,5144 m/s. Per stime al volo: 1 kt ≈ ½ m/s.

### Passo 2 — Calcolare il peso del velivolo

$$Q = m \cdot g = 1\,043 \text{ kg} \times 9{,}81 \, \frac{\text{m}}{\text{s}^2} = 10\,231{,}83 \text{ N}$$

### Passo 3 — Imporre l'equilibrio verticale

In volo livellato a velocità costante:
$$P = Q = 10\,231{,}83 \text{ N}$$

### Passo 4 — Isolare $C_p$ dalla formula della portanza

Partendo da $P = \frac{1}{2}\rho V^2 S C_p$, isolo $C_p$:

$$C_p = \frac{2 L}{\rho V^2 S}$$

### Passo 5 — Sostituire i valori numerici

$$C_p = \frac{2 \times 10\,231{,}83}{1{,}225 \times (62{,}76)^2 \times 16{,}2}$$

Calcolo a tappe per evitare errori:

- Numeratore: $2 \times 10\,231{,}83 = 20\,463{,}66$
- $(62{,}76)^2 = 3\,938{,}82$
- Denominatore: $1{,}225 \times 3\,938{,}82 \times 16{,}2$
  - $1{,}225 \times 3\,938{,}82 = 4\,825{,}05$
  - $4\,825{,}05 \times 16{,}2 = 78\,165{,}81$

- Quindi: $C_p = 20\,463{,}66 / 78\,165{,}81 = 0{,}2618$

### Passo 6 — Risultato

$$\boxed{C_p \approx 0{,}26}$$

---

## ✅ Verifica di plausibilità

Il valore ha senso? Confrontiamo con quanto dice il [formulario](../00-formulario/formulario.md):

> Crociera, velivolo GA: $C_p$ tipico = **0,2 – 0,4**

Il nostro $C_p \approx 0{,}26$ rientra **perfettamente** in questo intervallo, posizionandosi sul lato basso — coerente con una velocità di crociera relativamente alta (122 kt è la crociera standard del Cessna 172).

**Lettura fisica**: l'ala lavora "tranquilla", lontana dallo stallo (che avverrebbe intorno a $C_{p,max} \approx 1{,}5$). C'è ampio margine per manovre e per rallentare in atterraggio. ✈️

---

## 🔄 Variante per autovalutazione

Stesso Cessna, stesso peso, stessa superficie. Ma ora vola a **140 kt** invece di 122 kt.
**Calcola il nuovo $C_p$ richiesto.**

<details markdown="1">
<summary>👉 Solo il risultato (prima provaci da solo!)</summary>

$V = 140 \times 0{,}5144 = 72{,}02$ m/s
$C_p \approx 0{,}199 \approx 0{,}20$

> Più velocità ⇒ meno $C_p$ serve per generare lo stesso peso. Conferma: a velocità maggiori, l'ala "lavora meno". Per i dettagli del calcolo, vedi [`soluzioni/01-soluzione.md`](./soluzioni/01-soluzione.md).

</details>

---

## 🎓 Cosa hai imparato

- In volo livellato, **portanza = peso**, sempre.
- Il **coefficiente di portanza non è una proprietà fissa** del velivolo: dipende dalle condizioni di volo (velocità, peso, densità).
- A parità di velivolo: **più veloce → $C_p$ minore**, perché la portanza cresce con $V^2$ e basta meno "aiuto" dall'angolo di attacco.
- Il **controllo delle unità** è metà del lavoro: 122 kt sostituiti come "122" dentro la formula avrebbero dato un $C_p$ assurdo (~70).

---

## ➡️ Prossimo

[Esercizio 2 — Velocità di stallo (Piper PA-28)](./02-base-velocita-stallo.md) 🚧
