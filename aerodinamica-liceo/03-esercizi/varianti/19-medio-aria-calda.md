# Esercizio 19 — Effetto della temperatura sulla portanza (giorno caldo vs ISA)

> 🟡 **Difficoltà: MEDIO** — **Esercizio nuovo** sull'**ISA deviata**: come cambia la performance di un velivolo in un giorno caldo (35°C) rispetto allo standard ISA (15°C)?
>
> 🎯 **Obiettivi**: calcolare la densità reale a temperatura non-ISA, vedere come la velocità di stallo aumenta in un giorno caldo, capire perché le compagnie aeree hanno restrizioni "hot day operations".

---

## 📋 Testo del problema

Stesso Cessna 172 ($m = 1\,043$ kg, $S = 16{,}2$ m², $C_{p,max} = 2{,}1$ con flap) deve atterrare al **livello mare** in due giorni diversi:

- **Giorno A — ISA standard**: $T = 15°C$, $\rho = 1{,}225$ kg/m³
- **Giorno B — giornata calda di luglio**: $T = 35°C$ (20°C sopra ISA), $p$ = standard 101 325 Pa

**Determina**:

1. La densità $\rho$ effettiva del giorno caldo (usando $\rho = p/(RT)$, $R = 287$ J/(kg·K))
2. $V_S$ in atterraggio per i due giorni
3. La differenza percentuale di $V_S$
4. L'aumento della **distanza di decollo** (indicativa) sulla giornata calda

---

## 🖼️ Diagramma del problema

Riferimento: [Lezione 5 — Atmosfera ISA](../../01-teoria/05-atmosfera-isa.md). In una giornata calda fuori standard:

- Pressione = standard (cambia poco con la temperatura)
- **Densità più bassa** (gas caldo si espande)
- Conseguenza: meno aria che genera portanza per ogni m² di ala → tutto si comporta come se fossi a quota maggiore

---

## 📊 Dati noti / da trovare

| Grandezza | Giorno A (ISA) | Giorno B (caldo) |
|---|---|---|
| $T$ | 15°C = 288,15 K | 35°C = 308,15 K |
| $p$ | 101 325 Pa | 101 325 Pa |
| $\rho$ | 1,225 kg/m³ | da calcolare |
| $C_{p,max}$ atterraggio | 2,1 | 2,1 (invariato) |

---

## 🧠 Strategia

1. Equazione di stato gas perfetto: $\rho = p/(RT)$
2. Calcolo $\rho_B$ a 308 K (mantenendo $p$ standard)
3. Applico $V_S = \sqrt{2W/(\rho S C_{p,max})}$ per i 2 casi
4. Confronto

---

## ✏️ Risoluzione passo-passo

### Passo 1 — Densità del giorno caldo

$$\rho_B = \dfrac{p}{R \cdot T} = \dfrac{101\,325}{287 \times 308{,}15} = \dfrac{101\,325}{88\,439} \approx 1{,}146 \text{ kg/m}^3$$

$$\boxed{\rho_B \approx 1{,}146 \text{ kg/m}^3}$$

→ Riduzione del **6,5%** rispetto a $\rho_0 = 1{,}225$.

> 💡 **Trucco veloce**: $\rho \propto 1/T$ (a $p$ costante). Rapporto: $T_A/T_B = 288{,}15/308{,}15 = 0{,}9351$. Quindi $\rho_B = \rho_A \times 0{,}9351 = 1{,}146$. Coerente.

### Passo 2 — Peso (invariato)

$$Q = 1\,043 \times 9{,}81 = 10\,232 \text{ N}$$

### Passo 3 — $V_S$ in atterraggio

**Giorno A (ISA standard)**:
$$V_{S,A} = \sqrt{\dfrac{2 \times 10\,232}{1{,}225 \times 16{,}2 \times 2{,}1}} = \sqrt{491{,}1} = 22{,}16 \text{ m/s} = $$ **43,1 kt**

**Giorno B (caldo)**:
$$V_{S,B} = \sqrt{\dfrac{2 \times 10\,232}{1{,}146 \times 16{,}2 \times 2{,}1}} = \sqrt{\dfrac{20\,464}{38{,}99}} = \sqrt{524{,}9} = 22{,}91 \text{ m/s} = $$ **44,5 kt**

### Passo 4 — Differenza percentuale

$$\Delta V_S = \dfrac{44{,}5 - 43{,}1}{43{,}1} \times 100 \approx 3{,}3\%$$

→ $V_S$ aumenta del **3,3%** in giornata calda. Sembra poco, ma è solo l'inizio dei problemi.

### Passo 5 — Distanza di decollo (regola di proporzionalità)

La distanza di decollo è proporzionale a $V_R^2 \cdot 1/\rho \cdot 1/$(spinta motore). I motori a pistoni e turbine **perdono spinta in giornata calda** ($\sim$ -3% per ogni 10°C sopra ISA):

| Effetto | Variazione | Cumulativa |
|---|---|---|
| $V_R^2$ (proporzionale a $W/\rho$) | × 1,068 | × 1,068 |
| Spinta motore | × 0,94 (−6% per 20°C) | × 1,136 |
| 1/ρ (densità minore) | × 1,068 | × 1,21 |

→ Distanza di decollo aumenta del **~21%** in una giornata a 35°C.

Cessna 172 a livello mare ISA: pista decollo ~250 m. A 35°C: **~302 m**. Su una pista di 280 m → potresti **non riuscire a decollare**!

---

## ✅ Verifica di plausibilità

I manuali POH dei velivoli forniscono **tabelle di correzione** per temperatura non-ISA. Per il Cessna 172, la "Performance correction" indica:

- Aumento distanza decollo del **+10% per ogni 10°C sopra ISA**
- A 35°C (=ISA + 20°C): **+20%** rispetto allo standard

**Coincide con il nostro 21% calcolato** ✅.

### Implicazioni reali

**Hot day operations** è un problema reale per:

- Aeroporti del deserto in estate (Las Vegas, Phoenix, Dubai): le compagnie talvolta cancellano voli quando T > 50°C perché alcuni velivoli non rientrano nelle certificazioni
- Aeroporti d'alta quota in estate (Aspen, Denver in luglio): combinazione **hot AND high** = doppio problema
- Cessna a Roma in luglio (T ~ 38°C, quota 0): pista decollo aumenta del 25% rispetto a inverno

---

## 🔄 Variante per autovalutazione

Lo stesso Cessna in **giornata fredda** (winter operations a Helsinki): $T = -25°C$. **Ricalcola**:

a. Densità
b. $V_S$ in atterraggio
c. Distanza di decollo (rispetto a ISA standard)

<details markdown="1">
<summary>👉 Solo il risultato (prima provaci da solo!)</summary>

a. $T = -25°C = 248{,}15$ K
$\rho = 101325/(287 \cdot 248{,}15) = 101325/71218 \approx$ **1,423 kg/m³** (+16% rispetto a ISA!)

b. $V_S = \sqrt{2 \cdot 10232/(1{,}423 \cdot 16{,}2 \cdot 2{,}1)} = \sqrt{20464/48{,}40} = \sqrt{422{,}8} = 20{,}56$ m/s = **40,0 kt** (-7% rispetto a ISA)

c. Distanza decollo:

- $V_R^2 \propto 1/\rho$: × 0,861
- Spinta motore: +6% in giornata fredda (× 0,944 sull'invertito)
- Cumulato: × 0,82 → **distanza ridotta del 18%**

→ Ecco perché i pochi voli aerei "performance test" si fanno in giornate fredde: si misurano i numeri "best case". E per questo le compagnie di linea che operano in Scandinavia in inverno hanno meno problemi di restrizioni di peso al decollo.

</details>

---

## 🎓 Cosa hai imparato

- $\rho = p/(RT)$: a pressione costante, **densità inverso alla temperatura**. Ogni 20°C sopra ISA → densità -6,5%.
- $V_S$ aumenta del 3-4% in giornata calda — sembra poco
- MA la **distanza di decollo aumenta del 20-25%** per effetto cumulato su $V$, motore, densità
- I manuali POH hanno tabelle "non-standard atmosphere" obbligatorie per qualsiasi calcolo di performance
- **Hot day operations** = problema reale, soprattutto in deserto/montagna estate

---

## ➡️ Prossimo

[Esercizio 20 — Boeing 787 con vento al traverso](./20-avanzato-787-traverso.md) o l'[indice](../tutti.md).
