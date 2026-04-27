# Esercizio 26 — Ala a freccia con polare e diagrammi (stile prof)

> 🔴 **Difficoltà: AVANZATO** — Esercizio in **stile compito tradizionale**: ala con dati realistici di profilo, calcolo di portanza/resistenza/efficienza, **polare richiesta come grafico** $(C_p, \alpha)$, $(C_R, \alpha)$ e $(C_p, C_R)$.
>
> 🎯 **Obiettivi**: applicare la teoria a un velivolo intero (non solo profilo), gestire la conversione **ft → m**, **kt → m/s**, calcolare $V$ in km/h e Mach, tracciare i tre diagrammi richiesti.

---

## 📋 Testo del problema

Un'**ala rettangolare** ha:

- Coefficiente angolare di portanza del profilo: $C'_{p\infty} = 5{,}2$ rad⁻¹
- Coefficiente di resistenza di profilo: $C_{R,0} = 0{,}03$
- Apertura alare: $b = 14$ m
- Corda: $c = 1{,}4$ m
- Angolo di portanza nulla: $\alpha_0 = 0{,}2°$

Il velivolo si trova a:

- Quota $h = 12\,000$ ft
- Velocità $V = 430$ kt
- Incidenza $\alpha = 5{,}3°$

**Determina**:

1. Superficie alare $S$ e allungamento $\lambda$
2. Densità $\rho$ alla quota di volo
3. Pendenza $C'_p$ dell'ala 3D (correzione per allungamento finito)
4. Coefficiente di portanza $C_p$ e di resistenza $C_R$ dell'ala
5. Portanza $P$, resistenza $R$ e efficienza $E$
6. Velocità in km/h e numero di Mach
7. Tracciare i diagrammi $(C_p, \alpha)$, $(C_R, \alpha)$, $(C_p, C_R)$ — la **polare**

---

## 🖼️ Diagramma del problema

L'ala rettangolare è caratterizzata da: profilo costante lungo l'apertura, $\tau = 1$ (corda costante), $\Lambda = 0°$ (no freccia).

![Polare con tangente per E_max](../../assets/img/grafici/polare-tangente-emax.svg)

La polare del nostro velivolo avrà la stessa forma (parabola) ma valori specifici di $C_{R,0}$ e fattore di Oswald.

---

## 📊 Dati noti / da trovare

| Grandezza | Simbolo | Valore | Unità |
|---|---|---|---|
| Pendenza profilo | $C'_{p\infty}$ | 5,2 | rad⁻¹ |
| Resistenza profilo | $C_{R,0}$ | 0,03 | adim. |
| Apertura | $b$ | 14 | m |
| Corda | $c$ | 1,4 | m |
| $\alpha_0$ | $-$ | 0,2 | gradi |
| Quota | $h$ | 12 000 | ft |
| Velocità | $V$ | 430 | kt |
| Incidenza | $\alpha$ | 5,3 | gradi |
| Fattore Oswald (assunto) | $e$ | 0,85 | adim. |

---

## 🧠 Strategia

1. Geometria: $S = b \times c$, $\lambda = b^2/S$
2. Conversioni: ft → m, kt → m/s
3. Densità a 12 000 ft (3 658 m) dalla tabella ISA
4. Pendenza ala 3D: $C'_p = \dfrac{C'_{p\infty}}{1 + C'_{p\infty}/(\pi \lambda e)}$ (formula di Helmbold/Prandtl)
5. $C_p = C'_p \cdot (\alpha - \alpha_0)$ con $\alpha$ in radianti
6. $C_R = C_{R,0} + C_p^2/(\pi \lambda e)$
7. Pressione dinamica $q = \frac{1}{2}\rho V^2$, poi $P = q S C_p$, $R = q S C_R$
8. $E = P/R = C_p/C_R$
9. Mach: $M = V/a$, $a = 20{,}05\sqrt{T}$, $T$ a 12 000 ft

---

## ✏️ Risoluzione passo-passo

### Passo 1 — Geometria

$$S = b \cdot c = 14 \times 1{,}4 = 19{,}6 \text{ m}^2$$

$$\lambda = \dfrac{b^2}{S} = \dfrac{14^2}{19{,}6} = \dfrac{196}{19{,}6} = 10$$

### Passo 2 — Conversioni

$$h = 12\,000 \text{ ft} \times 0{,}3048 = 3\,658 \text{ m}$$

$$V = 430 \text{ kt} \times 0{,}5144 = 221{,}19 \text{ m/s}$$

### Passo 3 — Densità a 3 658 m (ISA)

Interpolazione dalla tabella ISA (3 000 m → 0,909; 5 000 m → 0,736):

$$\rho(3\,658) \approx 0{,}909 - (0{,}909 - 0{,}736) \times \dfrac{3\,658 - 3\,000}{5\,000 - 3\,000} = 0{,}909 - 0{,}173 \times 0{,}329 = 0{,}852 \text{ kg/m}^3$$

(Da formula esatta: $\rho \approx 0{,}849$ kg/m³ — coerente entro 0,4%.)

### Passo 4 — Pendenza dell'ala 3D

Per $\lambda = 10$ ed $e = 0{,}85$:

$$C'_p = \dfrac{C'_{p\infty}}{1 + \dfrac{C'_{p\infty}}{\pi \lambda e}} = \dfrac{5{,}2}{1 + \dfrac{5{,}2}{\pi \times 10 \times 0{,}85}}$$

Calcolo:

- $\pi \times 10 \times 0{,}85 = 26{,}70$
- $5{,}2/26{,}70 = 0{,}195$
- Denominatore: $1 + 0{,}195 = 1{,}195$
- $C'_p = 5{,}2/1{,}195 = 4{,}352$ rad⁻¹

$$\boxed{C'_p \approx 4{,}35 \text{ rad}^{-1}}$$

In gradi: $4{,}35 \times \pi/180 = 0{,}0759$ /°.

### Passo 5 — $C_p$ e $C_R$

$\Delta\alpha = \alpha - \alpha_0 = 5{,}3 - 0{,}2 = 5{,}1°$ in radianti: $5{,}1 \times \pi/180 = 0{,}0890$ rad.

$$C_p = C'_p \cdot \Delta\alpha = 4{,}352 \times 0{,}0890 = 0{,}387$$

$$C_{R,i} = \dfrac{C_p^2}{\pi \lambda e} = \dfrac{0{,}387^2}{26{,}70} = \dfrac{0{,}1498}{26{,}70} = 0{,}00561$$

$$C_R = C_{R,0} + C_{R,i} = 0{,}03 + 0{,}00561 = 0{,}0356$$

$$\boxed{C_p \approx 0{,}387 \quad C_R \approx 0{,}036}$$

### Passo 6 — Forze e efficienza

Pressione dinamica:
$$q = \dfrac{1}{2}\rho V^2 = \dfrac{1}{2} \times 0{,}852 \times 221{,}19^2 = \dfrac{1}{2} \times 0{,}852 \times 48\,925 = 20\,841 \text{ Pa}$$

**Portanza**:
$$P = q \cdot S \cdot C_p = 20\,841 \times 19{,}6 \times 0{,}387 = 158\,063 \text{ N}$$

$$\boxed{P \approx 158\,000 \text{ N} = 158 \text{ kN}}$$

**Resistenza**:
$$R = q \cdot S \cdot C_R = 20\,841 \times 19{,}6 \times 0{,}0356 = 14\,540 \text{ N}$$

$$\boxed{R \approx 14\,500 \text{ N} = 14{,}5 \text{ kN}}$$

**Efficienza**:
$$E = \dfrac{P}{R} = \dfrac{C_p}{C_R} = \dfrac{0{,}387}{0{,}0356} = 10{,}87$$

$$\boxed{E \approx 10{,}9}$$

### Passo 7 — Velocità in km/h e Mach

In km/h:
$$V_{km/h} = 221{,}19 \times 3{,}6 = 796{,}3 \text{ km/h}$$

Velocità del suono a 12 000 ft (3 658 m), $T \approx -8{,}8°C = 264{,}3$ K:
$$a = 20{,}05 \sqrt{264{,}3} = 20{,}05 \times 16{,}26 = 326{,}0 \text{ m/s}$$

Numero di Mach:
$$M = \dfrac{V}{a} = \dfrac{221{,}19}{326{,}0} = 0{,}679$$

$$\boxed{V = 796 \text{ km/h}, \quad M = 0{,}68 \text{ (subsonico)}}$$

### Passo 8 — I tre diagrammi

**(a) Diagramma $C_p$ vs $\alpha$** (regime lineare):

| $\alpha$ (gradi) | $C_p$ |
|---|---|
| 0 | $4{,}352 \times (-0{,}2) \times \pi/180 = -0{,}015$ |
| 2 | $4{,}352 \times (1{,}8) \times \pi/180 = 0{,}137$ |
| 5,3 | **0,387** ← punto di lavoro |
| 8 | $4{,}352 \times (7{,}8) \times \pi/180 = 0{,}592$ |
| 12 | $4{,}352 \times (11{,}8) \times \pi/180 = 0{,}896$ |

Retta lineare con $C_p = 0$ a $\alpha = 0{,}2°$ e pendenza 0,0759 /°.

**(b) Diagramma $C_R$ vs $\alpha$** (parabola crescente):

| $\alpha$ | $C_p$ | $C_R = 0{,}03 + C_p^2/26{,}7$ |
|---|---|---|
| 0 | -0,015 | 0,0300 |
| 2 | 0,137 | 0,0307 |
| 5,3 | **0,387** | **0,0356** ← punto di lavoro |
| 8 | 0,592 | 0,0431 |
| 12 | 0,896 | 0,0601 |

**(c) Polare $C_p$ vs $C_R$**:
La polare classica (forma parabolica). Vedi figura sopra. Costruita riportando $(C_R, C_p)$ dalle due tabelle precedenti.

> 💡 **Su carta millimetrata** (richiesto dal prof): scala consigliata 1 cm = 0,1 per $C_p$, 1 cm = 0,01 per $C_R$. Marcare il punto di lavoro $(0{,}0356; 0{,}387)$.

---

## ✅ Verifica di plausibilità

- $E \approx 11$: coerente per ala rettangolare con $\lambda = 10$ e $C_{R,0}$ alto (0,03). Caccia/turismo veloce.
- $V = 796$ km/h $\approx 430$ kt: alta velocità, M = 0,68 (subsonico, prima del Mach critico tipico ~0,72).
- $P \approx 158$ kN: corrispondente a un velivolo di massa $P/g = 16\,100$ kg (non in volo livellato a $\alpha = 5{,}3°$ — l'incidenza dichiarata produce portanza maggiore del peso a parità di $V$, quindi il velivolo sta salendo).

---

## 🔄 Variante per autovalutazione

Stessi dati ma $\alpha = 1{,}5°$ invece di 5,3°. Ricalcola $C_p$, $C_R$, $E$, $P$, $R$.

<details markdown="1">
<summary>👉 Risultati</summary>

$\Delta\alpha = 1{,}5 - 0{,}2 = 1{,}3° = 0{,}0227$ rad
$C_p = 4{,}352 \times 0{,}0227 = 0{,}0987$
$C_R = 0{,}03 + 0{,}0987^2/26{,}7 = 0{,}0304$
$E = 0{,}0987/0{,}0304 = 3{,}25$
$P = 20841 \times 19{,}6 \times 0{,}0987 = 40\,310$ N
$R = 20841 \times 19{,}6 \times 0{,}0304 = 12\,420$ N

→ A $\alpha$ basso, **$E$ molto bassa** (3,25): il velivolo è inefficiente perché ha troppa parassita rispetto a poca portanza. Conferma: la efficienza massima è a $C_p^* = \sqrt{\pi \lambda e \cdot C_{R,0}} = \sqrt{26{,}7 \cdot 0{,}03} = 0{,}895$, corrispondente a $\alpha^* \approx 12°$ — **molto sopra** la nostra incidenza di 5,3°.

</details>

---

## 🎓 Cosa hai imparato

- L'**ala 3D** ha pendenza $C'_p$ **inferiore** al profilo isolato ($C'_{p\infty}$) per via dell'effetto della finitezza alare (allungamento limitato).
- Formula di Helmbold/Prandtl: $C'_p = C'_{p\infty}/(1 + C'_{p\infty}/(\pi \lambda e))$.
- **Conversioni essenziali**: ft → m (× 0,3048), kt → m/s (× 0,5144), m/s → km/h (× 3,6).
- **Numero di Mach**: $M = V/a$, $a = 20{,}05\sqrt{T}$ con $T$ in K. Subsonico, transonico, supersonico.
- I **3 diagrammi richiesti** (polare nei suoi 3 modi) sono il modo standard di presentare l'aerodinamica di un velivolo nei testi italiani.
- Stile compito prof: **molteplici richieste**, conversioni multiple, costruzione grafica obbligatoria.

---

## ➡️ Esercizi simili

Vedi [Esercizio 10 — Polare completa](../10-avanzato-polare-completa.md) per il caso del Boeing 737 senza i fattori di profilo. Oppure [indice esercizi](../tutti.md) per tutti i 26.
