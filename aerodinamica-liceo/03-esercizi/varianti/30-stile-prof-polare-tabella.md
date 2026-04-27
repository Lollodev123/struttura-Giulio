# Esercizio 30 — Polare data come tabella: ricava $C_{R,0}$ e $\lambda$

> 🔴 **Difficoltà: AVANZATO** — La polare è data come tabella di valori sperimentali. Devi **regredire i parametri** e poi calcolare la velocità di stallo in quota.
>
> 🎯 **Obiettivi**: ricavare $C_{R,0}$ e $\lambda$ da una polare tabellare (regressione/interpolazione), usare i parametri ricavati per calcolare $V_S$ a quota assegnata.

---

## 📋 Testo del problema

Per un velivolo sono date queste caratteristiche:

- Peso $Q = 123\,000$ N
- Superficie alare $S = 49{,}2$ m²
- Caratteristiche aerodinamiche tabulate sperimentalmente:

| $C_p$ | $C_R$ |
|---|---|
| 0,2 | 0,022 |
| 0,4 | 0,029 |
| 0,6 | 0,040 |
| 0,8 | 0,056 |
| 1,0 | 0,076 |
| 1,2 | 0,100 |
| 1,4 | 0,155 |
| **1,35** | **0,183** |

(Ultima riga: dato anomalo, vicino allo stallo — non lo uso per la regressione.)

**Determina**:

1. Il **coefficiente di resistenza parassita** $C_{R,0}$ (regressione dalla tabella)
2. L'**allungamento alare** $\lambda$ (assumendo $e = 0{,}85$)
3. In ipotesi di **volo rettilineo uniforme**, la **velocità di stallo $V_S$** alla quota di $h = 4\,200$ m, sapendo che $C_{p,max} = 1{,}4$

---

## 🖼️ Diagramma del problema

![Polare con tangente per E_max](../../assets/img/grafici/polare-tangente-emax.svg)

I valori tabellati sono **punti sperimentali** della polare. La curva analitica $C_R = C_{R,0} + k C_p^2$ deve passare per loro (quasi). Devo trovare $C_{R,0}$ e $k = 1/(\pi\lambda e)$.

---

## 📊 Dati noti / da trovare

| Grandezza | Valore |
|---|---|
| $Q$ | 123 000 N |
| $S$ | 49,2 m² |
| $C_{p,max}$ (dato dall'ultimo punto) | 1,4 |
| $h$ | 4 200 m |
| $e$ | 0,85 (assunto) |

---

## 🧠 Strategia

1. **Estrarre $C_{R,0}$**: la polare è $C_R = C_{R,0} + k C_p^2$. Quando $C_p \to 0$, $C_R \to C_{R,0}$.
   - Usa due punti della tabella per impostare un sistema di 2 equazioni in 2 incognite.
2. **Estrarre $\lambda$**: dalla relazione $k = 1/(\pi\lambda e)$, isolando $\lambda$.
3. **Densità a 4 200 m**: dalla tabella ISA (interpolando).
4. **Velocità di stallo**: $V_S = \sqrt{2Q/(\rho S C_{p,max})}$.

---

## ✏️ Risoluzione passo-passo

### Passo 1 — Estrarre $C_{R,0}$ e $k$ dalla polare (sistema 2×2)

Uso i punti $C_p = 0{,}2$ e $C_p = 1{,}0$ (sono "puliti", non vicini allo stallo):

- A $C_p = 0{,}2$: $0{,}022 = C_{R,0} + k \times 0{,}04$
- A $C_p = 1{,}0$: $0{,}076 = C_{R,0} + k \times 1{,}00$

Sottraendo:

$$0{,}076 - 0{,}022 = k \times (1{,}00 - 0{,}04)$$
$$0{,}054 = k \times 0{,}96$$
$$k = 0{,}0563$$

Sostituendo nella prima:
$$C_{R,0} = 0{,}022 - 0{,}0563 \times 0{,}04 = 0{,}022 - 0{,}00225 = 0{,}0198$$

$$\boxed{C_{R,0} \approx 0{,}020 \quad k \approx 0{,}0563}$$

### Verifica con altri punti

| $C_p$ | $C_R$ tabellato | $C_R$ calcolato $0{,}020 + 0{,}0563 \, C_p^2$ | Errore |
|---|---|---|---|
| 0,4 | 0,029 | $0{,}020 + 0{,}0090 = 0{,}029$ | 0% ✅ |
| 0,6 | 0,040 | $0{,}020 + 0{,}0203 = 0{,}040$ | 0% ✅ |
| 0,8 | 0,056 | $0{,}020 + 0{,}0360 = 0{,}056$ | 0% ✅ |
| 1,2 | 0,100 | $0{,}020 + 0{,}0811 = 0{,}101$ | +1% ✅ |
| 1,4 | 0,155 | $0{,}020 + 0{,}1103 = 0{,}130$ | -16% ⚠️ |

→ Polare quadratica perfetta per $C_p \leq 1{,}2$. Per $C_p \geq 1{,}4$ ci sono effetti di stallo (la polare diventa più ripida) → coerente.

### Passo 2 — Estrarre $\lambda$

$$k = \dfrac{1}{\pi \lambda e} \Rightarrow \pi\lambda e = \dfrac{1}{k} = \dfrac{1}{0{,}0563} = 17{,}76$$

$$\lambda = \dfrac{17{,}76}{\pi \times 0{,}85} = \dfrac{17{,}76}{2{,}671} = 6{,}65$$

$$\boxed{\lambda \approx 6{,}65}$$

→ Allungamento medio, tipico aviazione generale o piccolo regionale.

### Passo 3 — Densità a 4 200 m

Interpolando tra 3 000 m (ρ=0,909) e 5 000 m (ρ=0,736):

$$\rho(4\,200) \approx 0{,}909 - (0{,}909 - 0{,}736) \times \dfrac{4\,200 - 3\,000}{5\,000 - 3\,000} = 0{,}909 - 0{,}173 \times 0{,}600 = 0{,}805 \text{ kg/m}^3$$

### Passo 4 — Velocità di stallo

In volo livellato, $P = Q$. Allo stallo, $C_p = C_{p,max}$:

$$V_S = \sqrt{\dfrac{2 Q}{\rho \cdot S \cdot C_{p,max}}}$$

$$V_S = \sqrt{\dfrac{2 \times 123\,000}{0{,}805 \times 49{,}2 \times 1{,}4}}$$

Calcolo:

- Numeratore: $2 \times 123\,000 = 246\,000$
- Denominatore: $0{,}805 \times 49{,}2 \times 1{,}4 = 55{,}45$
- Rapporto: $246\,000 / 55{,}45 = 4\,436$
- Radice: $\sqrt{4\,436} = 66{,}6$ m/s

In nodi: $66{,}6 / 0{,}5144 = 129{,}5$ kt
In km/h: $66{,}6 \times 3{,}6 = 240$ km/h

$$\boxed{V_S \approx 66{,}6 \text{ m/s} = 129 \text{ kt} = 240 \text{ km/h}}$$

---

## ✅ Verifica di plausibilità

- $C_{R,0} = 0{,}020$: tipico di velivolo aerodinamicamente pulito (jet regionale, business jet).
- $\lambda = 6{,}65$: medio, coerente con aviazione generale.
- Massa del velivolo: $m = Q/g = 123\,000/9{,}81 = 12\,540$ kg → categoria business jet (Cessna Citation Mustang, Embraer Phenom 100).
- $V_S = 240$ km/h a 4 200 m: alto perché la quota riduce la densità → un'atterraggio difficile a quota.

### Confronto col livello mare

A livello mare ($\rho = 1{,}225$):
$$V_{S,mare} = V_S(4\,200) \times \sqrt{\dfrac{0{,}805}{1{,}225}} = 66{,}6 \times 0{,}811 = 54{,}0 \text{ m/s} = 105 \text{ kt}$$

→ A livello mare, $V_S \approx 105$ kt — coerente con un Citation o Phenom (V_S manuale 100-110 kt).

---

## 🔄 Variante per autovalutazione

Lo stesso velivolo a $h = 8\,000$ m (quota di crociera tipica). Calcola $V_S$.

<details markdown="1">
<summary>👉 Risultato</summary>

A 8 000 m: $\rho = 0{,}526$ kg/m³

$V_S = \sqrt{2 \times 123000/(0{,}526 \times 49{,}2 \times 1{,}4)} = \sqrt{246000/36{,}24} = \sqrt{6\,790} \approx$ **82,4 m/s = 160 kt**

→ A 8 000 m la $V_S$ è del 24% superiore rispetto a 4 200 m. È il motivo per cui i velivoli **non scendono mai sotto una quota minima sicura** in caso di emergenza: la velocità di stallo a quota troppo alta diventa insostenibile.

</details>

---

## 🎓 Cosa hai imparato

- **Estrarre $C_{R,0}$ e $k$** da una polare tabellare: sistema 2×2 con 2 punti scelti.
- **$k$ contiene** $1/(\pi\lambda e)$ → permette di estrarre $\lambda$ se assumi $e$.
- **Polare quadratica** è valida solo nel regime lineare (lontano dallo stallo): a $C_p$ alti, deviazione del modello.
- **Velocità di stallo in quota**: cresce come $1/\sqrt{\rho}$. A 4 200 m è del 22% superiore al livello mare.
- **Stile compito prof**: data tabella → ricavare parametri → applicarli a calcolo specifico = è un esercizio di "lettura inversa" molto formativo.

---

## ➡️ Prossimo

[Esercizio 31 — Cambio assetto e VIAS vs TAS](./31-stile-prof-cambio-assetto.md) o l'[indice esercizi](../tutti.md).
