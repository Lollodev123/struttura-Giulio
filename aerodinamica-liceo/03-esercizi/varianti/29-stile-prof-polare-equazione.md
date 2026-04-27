# Esercizio 29 — Polare data come equazione: risultante delle forze

> 🔴 **Difficoltà: AVANZATO** — La polare è già fornita come equazione $C_R = a + b \cdot C_p^2$. Devi solo applicarla per trovare la risultante.
>
> 🎯 **Obiettivi**: usare una polare data direttamente, calcolare la **risultante** $\vec{F}$ delle forze aerodinamiche (modulo + direzione), interpretare i due coefficienti della polare in termini fisici.

---

## 📋 Testo del problema

Un'**ala a pianta rettangolare** vola con questi dati:

- Quota $h = 18\,000$ ft
- Velocità $V = 332$ kt
- Polare: $C_R = 0{,}031 + 0{,}058 \cdot C_p^2$
- Coefficiente angolare di portanza del profilo: $C'_{p\infty} = 2{,}91$ rad⁻¹
- Apertura alare: $b = 12{,}8$ m
- Angolo di portanza nulla: $\alpha_0 = -1{,}98°$
- Incidenza (assetto di volo): $\alpha = 1{,}78°$

**Determina** la **risultante** $\vec{F}$ delle forze aerodinamiche (modulo $|\vec{F}|$ e direzione $\theta$ rispetto a $\vec{V}$).

---

## 🖼️ Diagramma del problema

```
     V →
      ↗ Risultante F = √(P² + R²)
   P |
     |  ↑              θ
     | / 
     |/____________  R (resistenza, parallela a V)
```

La risultante delle forze aerodinamiche si ottiene componendo **portanza** (perpendicolare a $V$) e **resistenza** (parallela a $V$, opposta al moto):

$$|\vec{F}| = \sqrt{P^2 + R^2}, \quad \tan\theta = \dfrac{P}{R} = E$$

---

## 📊 Dati noti / da trovare

| Grandezza | Valore |
|---|---|
| $h$ | 18 000 ft |
| $V$ | 332 kt |
| Polare | $C_R = 0{,}031 + 0{,}058 C_p^2$ |
| $C'_{p\infty}$ | 2,91 rad⁻¹ |
| $b$ | 12,8 m |
| $\alpha_0$ | -1,98° |
| $\alpha$ | 1,78° |

> 💡 **Astuzia**: dal coefficiente "0,058" della polare si ricava $\pi\lambda e$. Sapendo $C_{R,i} = C_p^2/(\pi\lambda e) = 0{,}058 C_p^2$ → $\pi\lambda e = 1/0{,}058 = 17{,}24$.

---

## 🧠 Strategia

1. **Dal coefficiente della polare** ricavo $\pi\lambda e$ → posso calcolare $\lambda$ se conosco $e$ (assumo 0,85)
2. Conosciuto $\lambda$, ricavo $S$ e corda
3. Pendenza ala 3D
4. $C_p$ all'incidenza data
5. $C_R$ dalla polare
6. Forze $P$, $R$
7. Risultante = modulo + angolo

---

## ✏️ Risoluzione passo-passo

### Passo 1 — Estrarre $\lambda$ dalla polare

$$C_{R,i} = 0{,}058 C_p^2 = \dfrac{C_p^2}{\pi \lambda e}$$

$$\Rightarrow \pi \lambda e = \dfrac{1}{0{,}058} = 17{,}24$$

Assumendo $e = 0{,}85$:
$$\lambda = \dfrac{17{,}24}{\pi \times 0{,}85} = \dfrac{17{,}24}{2{,}671} = 6{,}45$$

$$\boxed{\lambda \approx 6{,}45}$$

### Passo 2 — Geometria

$$S = \dfrac{b^2}{\lambda} = \dfrac{12{,}8^2}{6{,}45} = \dfrac{163{,}84}{6{,}45} = 25{,}40 \text{ m}^2$$

$$c = \dfrac{S}{b} = \dfrac{25{,}40}{12{,}8} = 1{,}98 \text{ m}$$

### Passo 3 — Conversioni

$$h = 18\,000 \times 0{,}3048 = 5\,486 \text{ m}$$

$$V = 332 \times 0{,}5144 = 170{,}8 \text{ m/s}$$

### Passo 4 — Densità a 5 486 m

Tra 5 000 m (ρ=0,736) e 6 000 m (ρ ≈ 0,660):

$$\rho \approx 0{,}736 - (0{,}736 - 0{,}660) \times \dfrac{486}{1000} = 0{,}736 - 0{,}076 \times 0{,}486 = 0{,}699 \text{ kg/m}^3$$

### Passo 5 — Pendenza ala 3D

$$C'_p = \dfrac{2{,}91}{1 + 2{,}91/17{,}24} = \dfrac{2{,}91}{1 + 0{,}169} = \dfrac{2{,}91}{1{,}169} = 2{,}490 \text{ rad}^{-1}$$

In gradi: 2,490 × π/180 = 0,0435 /°

### Passo 6 — $C_p$ all'incidenza data

$\Delta\alpha = 1{,}78 - (-1{,}98) = 3{,}76° = 0{,}0656$ rad

$$C_p = 2{,}490 \times 0{,}0656 = 0{,}1634$$

### Passo 7 — $C_R$ dalla polare

$$C_R = 0{,}031 + 0{,}058 \times 0{,}1634^2 = 0{,}031 + 0{,}058 \times 0{,}02670 = 0{,}031 + 0{,}001549 = 0{,}0325$$

### Passo 8 — Forze e risultante

$$q = \dfrac{1}{2} \times 0{,}699 \times 170{,}8^2 = \dfrac{1}{2} \times 0{,}699 \times 29\,173 = 10\,196 \text{ Pa}$$

$$P = q \cdot S \cdot C_p = 10\,196 \times 25{,}40 \times 0{,}1634 = 42\,310 \text{ N}$$

$$R = q \cdot S \cdot C_R = 10\,196 \times 25{,}40 \times 0{,}0325 = 8\,418 \text{ N}$$

**Risultante** (componendo P perpendicolare a V e R parallela a V):

$$|\vec{F}| = \sqrt{P^2 + R^2} = \sqrt{42\,310^2 + 8\,418^2} = \sqrt{1{,}79 \times 10^9 + 7{,}09 \times 10^7} = \sqrt{1{,}86 \times 10^9} = 43\,140 \text{ N}$$

**Angolo $\theta$ rispetto a $\vec{V}$**:

$$\tan\theta = \dfrac{P}{R} = \dfrac{42\,310}{8\,418} = 5{,}03 = E$$

$$\theta = \arctan(5{,}03) = 78{,}8°$$

$$\boxed{|\vec{F}| \approx 43{,}1 \text{ kN}, \quad \theta \approx 78{,}8° \text{ (quasi perpendicolare a V)}}$$

### Passo 9 — Significato

- L'efficienza $E \approx 5$ è bassa (parassita relativamente alta nella polare).
- L'angolo $\theta = 78{,}8°$ significa che la risultante è quasi perpendicolare alla velocità (12° rispetto alla portanza pura, dovuto a R).
- La risultante è di poco superiore alla sola portanza (43,1 kN vs 42,3 kN) — l'effetto di R è piccolo ma non trascurabile.

---

## ✅ Verifica di plausibilità

- $C_p = 0{,}163$ a $\alpha = 1{,}78°$: basso ma coerente con un velivolo veloce in crociera.
- $\lambda = 6{,}45$: tipico di aviazione generale o piccoli velivoli regionali.
- $E = 5$: modesta — il velivolo ha parassita alta (probabilmente non aerodinamicamente pulito).

---

## 🔄 Variante per autovalutazione

Stesso velivolo, stessa polare, ma a incidenza $\alpha = 5°$ (al posto di 1,78°). Calcola $|\vec{F}|$ e $\theta$.

<details markdown="1">
<summary>👉 Risultato</summary>

$\Delta\alpha = 5 - (-1{,}98) = 6{,}98° = 0{,}1219$ rad
$C_p = 2{,}490 \times 0{,}1219 = 0{,}3035$
$C_R = 0{,}031 + 0{,}058 \times 0{,}0921 = 0{,}031 + 0{,}00534 = 0{,}0363$
$P = 10196 \cdot 25{,}40 \cdot 0{,}3035 = 78\,608$ N
$R = 10196 \cdot 25{,}40 \cdot 0{,}0363 = 9\,397$ N
$|\vec{F}| = \sqrt{78608^2 + 9397^2} = \sqrt{6{,}18 \times 10^9 + 8{,}83 \times 10^7} = \sqrt{6{,}27 \times 10^9} = $ **79,2 kN**
$\theta = \arctan(78608/9397) = \arctan(8{,}36) = $ **83,2°**

→ Aumentando l'incidenza, la risultante cresce (78 → 79 kN ovvero **+85%** ↑) e l'angolo si avvicina a 90° (più "verticale").

</details>

---

## 🎓 Cosa hai imparato

- **Polare data come equazione**: il coefficiente del termine $C_p^2$ contiene $1/(\pi\lambda e)$ — leggibile per ricavare $\lambda$.
- **Risultante** delle forze aerodinamiche = vettore con $|\vec{F}| = \sqrt{P^2 + R^2}$ e $\tan\theta = P/R = E$.
- L'angolo $\theta$ è **quasi 90°** (perpendicolare a V) per velivoli con E alta. Per E bassa (caccia veloci), $\theta$ scende verso 80°.
- **Astuzia**: estrarre informazioni dai dati apparentemente "compressi" (in questo caso la polare).

---

## ➡️ Prossimo

[Esercizio 30 — Polare data come tabella](./30-stile-prof-polare-tabella.md) o l'[indice esercizi](../tutti.md).
