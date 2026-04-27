# Esercizio 28 — Ala a freccia caccia leggero (con $C_{R,p}$ basso)

> 🔴 **Difficoltà: AVANZATO** — Stile prof con dati "anomali" (alta quota, bassa velocità) per testare la comprensione concettuale.
>
> 🎯 **Obiettivi**: gestire dati anomali (alta quota MA bassa velocità — tipico decollo/salita ad alta quota), riconoscere quando il velivolo è in fase di salita non di crociera.

---

## 📋 Testo del problema

Un'**ala a freccia** ha:

- Coefficiente angolare di portanza del profilo: $C'_{p\infty} = 1{,}09$ rad⁻¹
- Coefficiente di resistenza di profilo: $C_{R,p} = 0{,}0022$
- Apertura alare: $b = 7{,}6$ m
- Superficie alare: $S = 25$ m²
- Angolo di portanza nulla: $\alpha_0 = 1{,}67°$

In condizioni di volo:

- Quota $h = 16\,398$ ft
- Velocità $V = 20{,}5$ kt
- Incidenza $\alpha = 0{,}432°$

**Determina**:

1. Allungamento $\lambda$ e geometria dell'ala
2. Densità $\rho$ alla quota di volo
3. Pendenza ala 3D, $C_p$ e $C_R$
4. Portanza $P$, resistenza $R$, efficienza $E$
5. Tracciare la polare punto per punto

---

## 🖼️ Diagramma del problema

![Polare con tangente per E_max](../../assets/img/grafici/polare-tangente-emax.svg)

> ⚠️ **Attenzione**: i dati sono inusuali. Velocità di 20,5 kt = ~10 m/s è vicina alla velocità di stallo (al limite). Quota molto alta (16 400 ft = 5 km) con bassa V suggerisce un velivolo molto particolare (drone d'alta quota, aliante stratosferico) o un esercizio di stress sui valori limite.

---

## 📊 Dati noti / da trovare

| Grandezza | Simbolo | Valore | Unità |
|---|---|---|---|
| Pendenza profilo | $C'_{p\infty}$ | 1,09 | rad⁻¹ |
| Resistenza profilo | $C_{R,p}$ | 0,0022 | adim. |
| Apertura | $b$ | 7,6 | m |
| Superficie | $S$ | 25 | m² |
| $\alpha_0$ | — | 1,67 | gradi |
| Quota | $h$ | 16 398 | ft |
| Velocità | $V$ | 20,5 | kt |
| Incidenza | $\alpha$ | 0,432 | gradi |
| Fattore Oswald (assunto) | $e$ | 0,85 | adim. |

---

## 🧠 Strategia

1. Geometria: $\lambda$, corda media $c = S/b$
2. Conversioni
3. Densità ISA a 5 000 m
4. Pendenza ala 3D
5. **Attenzione**: $\Delta\alpha = \alpha - \alpha_0 = 0{,}432 - 1{,}67 = -1{,}24°$ → **NEGATIVO**! Significa $C_p < 0$ (deportanza)
6. Calcolo forze
7. Polare

---

## ✏️ Risoluzione passo-passo

### Passo 1 — Geometria

$$\lambda = \dfrac{b^2}{S} = \dfrac{7{,}6^2}{25} = \dfrac{57{,}76}{25} = 2{,}31$$

$$c_{media} = \dfrac{S}{b} = \dfrac{25}{7{,}6} = 3{,}29 \text{ m}$$

> 💡 **Allungamento bassissimo** (2,31): caccia delta o ala molto tozza. Coerente con la freccia accentuata.

### Passo 2 — Conversioni

$$h = 16\,398 \times 0{,}3048 = 4\,998 \text{ m} \approx 5\,000 \text{ m}$$

$$V = 20{,}5 \times 0{,}5144 = 10{,}55 \text{ m/s}$$

### Passo 3 — Densità a 5 000 m

Dalla tabella ISA: $\rho(5\,000) = 0{,}736$ kg/m³

### Passo 4 — Pendenza ala 3D

$$\pi\lambda e = \pi \times 2{,}31 \times 0{,}85 = 6{,}17$$

$$C'_p = \dfrac{1{,}09}{1 + 1{,}09/6{,}17} = \dfrac{1{,}09}{1 + 0{,}177} = \dfrac{1{,}09}{1{,}177} = 0{,}926 \text{ rad}^{-1}$$

In gradi: $0{,}926 \times \pi/180 = 0{,}0162$ /°

### Passo 5 — $C_p$ e $C_R$ (attenzione: angolo negativo!)

$\Delta\alpha = 0{,}432 - 1{,}67 = -1{,}24° = -0{,}0216$ rad

$$C_p = 0{,}926 \times (-0{,}0216) = -0{,}0200$$

$$\boxed{C_p = -0{,}020 \text{ (deportanza!)}}$$

> ⚠️ **$C_p$ negativo**: l'ala genera **deportanza** (forza verso il basso) perché l'incidenza è SOTTO l'angolo di portanza nulla. Configurazione assurda per un velivolo che vuole volare normalmente.

$$C_{R,i} = \dfrac{C_p^2}{\pi\lambda e} = \dfrac{0{,}0200^2}{6{,}17} = \dfrac{4{,}0 \times 10^{-4}}{6{,}17} = 6{,}48 \times 10^{-5}$$

$$C_R = 0{,}0022 + 0{,}0001 \approx 0{,}00226$$

$$\boxed{C_R \approx 0{,}00226}$$

### Passo 6 — Forze

$$q = \dfrac{1}{2} \times 0{,}736 \times 10{,}55^2 = \dfrac{1}{2} \times 0{,}736 \times 111{,}3 = 41{,}0 \text{ Pa}$$

$$P = q \cdot S \cdot C_p = 41{,}0 \times 25 \times (-0{,}020) = -20{,}5 \text{ N}$$

$$R = 41{,}0 \times 25 \times 0{,}00226 = 2{,}32 \text{ N}$$

$$\boxed{P \approx -20 \text{ N (deportanza)} \quad R \approx 2{,}3 \text{ N}}$$

### Passo 7 — Lettura del risultato

**Il velivolo NON sta volando** in queste condizioni:

- Portanza negativa = ala spinge verso il basso → l'aereo cade come un sasso
- Velocità 20,5 kt è 10,5 m/s, molto sotto la velocità di stallo tipica di qualsiasi velivolo (V_S minima ~25 m/s anche per ultraleggeri)
- L'incidenza 0,432° è SOTTO $\alpha_0 = 1,67°$ → l'ala non porta

**Conclusione**: questo è un esercizio "limite" del prof per insegnare a **leggere criticamente i dati**. La risposta è "il velivolo non sta volando in equilibrio".

### Passo 8 — Polare

| $\alpha$ (°) | $\Delta\alpha$ (°) | $C_p$ | $C_R$ |
|---|---|---|---|
| 0,432 (problema) | -1,24 | **-0,020** | **0,00226** |
| 1,67 ($\alpha_0$) | 0 | 0 | 0,00220 |
| 5 | 3,33 | 0,054 | 0,00267 |
| 10 | 8,33 | 0,135 | 0,00516 |
| 15 | 13,33 | 0,216 | 0,00978 |

Polare **molto schiacciata** verso l'asse $C_R$ (parassita molto bassa, indotta domina ad alti $C_p$).

---

## ✅ Verifica di plausibilità

I dati di questo esercizio sono **inverosimili per un velivolo reale**:

- $V = 20{,}5$ kt = 10,5 m/s → un Cessna stalla a 25 m/s
- Quota 5 km a velocità così bassa = velivolo specializzato (drone stratosferico, aliante alta quota)
- $C_{R,p} = 0{,}0022$ è incredibilmente basso (alianti hanno 0,015)

**Lezione didattica**: il professore probabilmente vuole testare se lo studente:

1. Esegue meccanicamente i calcoli
2. **O nota che il risultato è non-fisico** ($C_p < 0$, $V < V_S$) e lo segnala

La risposta corretta in compito sarebbe: "Calcoli formalmente eseguiti: $C_p = -0,020$, $P = -20$ N. **In queste condizioni il velivolo non vola in equilibrio**: l'incidenza è sotto $\alpha_0$, generando deportanza, e la velocità è insufficiente per qualsiasi configurazione."

---

## 🔄 Variante per autovalutazione

Stesso velivolo, ma incidenza $\alpha = 5°$ (al posto di 0,432°). Ricalcola $C_p$, $C_R$, $E$.

<details markdown="1">
<summary>👉 Risultato</summary>

$\Delta\alpha = 5 - 1{,}67 = 3{,}33° = 0{,}0581$ rad
$C_p = 0{,}926 \times 0{,}0581 = 0{,}0538$
$C_{R,i} = 0{,}0538^2/6{,}17 = 4{,}69 \times 10^{-4}$
$C_R = 0{,}0022 + 0{,}000469 = 0{,}00267$
$E = 0{,}0538/0{,}00267 = 20{,}1$

→ Ora $E$ alta (20!) per via di $C_{R,p}$ minimo. Possibile velivolo da record di efficienza o aliante alta quota. Resta il problema $V$ insufficiente.

</details>

---

## 🎓 Cosa hai imparato

- **Leggere criticamente i dati** prima di calcolare meccanicamente: $\Delta\alpha < 0$ significa deportanza.
- **Allungamento basso** (2,3) → grande riduzione della pendenza ala (Helmbold).
- **$C_{R,p}$ molto basso** (0,002) implica un velivolo speciale (record, drone, aliante).
- **Portanza negativa** = velivolo che precipita: in compito segnalalo, non eseguire ciecamente.
- **Verifica di plausibilità** = parte fondamentale dell'esercizio, non opzionale.

---

## ➡️ Prossimo

[Esercizio 29 — Polare data come equazione](./29-stile-prof-polare-equazione.md) o l'[indice esercizi](../tutti.md).
