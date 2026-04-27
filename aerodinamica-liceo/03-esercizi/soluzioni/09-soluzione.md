# Soluzione — Variante Esercizio 9

**Variante**: stesso A320 con configurazione decollo (CONF 1+F, $C_{p,max} = 2{,}00$, $S = 122{,}6$ m²), ma a peso ridotto $m = 65\,000$ kg invece di 78 000 kg (volo a corto raggio, meno carburante e meno passeggeri).

### Passo 1 — Peso

$$Q = m \cdot g = 65\,000 \times 9{,}81 = 637\,650 \text{ N}$$

### Passo 2 — $V_S$ a livello mare

$$V_S = \sqrt{\dfrac{2Q}{\rho_0 S C_{p,max,TO}}} = \sqrt{\dfrac{2 \times 637\,650}{1{,}225 \times 122{,}6 \times 2{,}00}}$$

Calcolo:

- Numeratore: $2 \times 637\,650 = 1\,275\,300$
- Denominatore: $1{,}225 \times 122{,}6 \times 2{,}00 = 300{,}37$
- Rapporto: $1\,275\,300 / 300{,}37 = 4\,245{,}8$
- Radice: $\sqrt{4\,245{,}8} = 65{,}16$ m/s

$$\boxed{V_S = 65{,}2 \text{ m/s} = 126{,}7 \text{ kt}}$$

### Passo 3 — $V_R$ e $V_2$

$$V_R = 1{,}1 \cdot V_S = 1{,}1 \times 65{,}16 = 71{,}68 \text{ m/s} \approx 139 \text{ kt}$$

$$V_2 = 1{,}2 \cdot V_S = 1{,}2 \times 65{,}16 = 78{,}19 \text{ m/s} \approx 152 \text{ kt}$$

### Confronto con MTOW (78 000 kg)

| Velocità | MTOW (78 t) | Variante (65 t) | Differenza |
|---|---|---|---|
| $V_S$ | 71,4 m/s = 139 kt | 65,2 m/s = 127 kt | $-8{,}7\%$ |
| $V_R$ | 78,5 m/s = 153 kt | 71,7 m/s = 139 kt | $-8{,}7\%$ |
| $V_2$ | 85,7 m/s = 167 kt | 78,2 m/s = 152 kt | $-8{,}7\%$ |

**Lettura**: con peso ridotto del **17%**, le velocità scendono dell'**8,7%** (come $\sqrt{0{,}833} = 0{,}913 \Rightarrow$ riduzione del 8,7%). Coerente con $V \propto \sqrt{W}$.

### Implicazione operativa: corsa di decollo

L'energia cinetica al momento del decollo è $\frac{1}{2}m V_R^2$. Confrontiamo:

| Peso | $V_R$ (m/s) | $\frac{1}{2}mV_R^2$ (J) | Rapporto |
|---|---|---|---|
| MTOW (78 t) | 78,5 | $2{,}40 \times 10^8$ | 1 (riferimento) |
| Variante (65 t) | 71,7 | $1{,}67 \times 10^8$ | **0,696** |

Energia cinetica scende del **30%**. Considerando che la pista converte spinta motori in energia cinetica con efficienza ~costante, **la corsa di decollo si riduce del 30%**.

| | MTOW | Variante |
|---|---|---|
| Corsa decollo (~) | 2 100 m | **1 470 m** |

### Implicazioni reali

Un A320 leggero a metà pista è completamente normale. Un Cessna 172 può fare lo stesso.

I **manuali di volo** danno tabelle V-speeds per peso (in genere 4-5 livelli di peso preimpostati). Il pilota:

1. Pesa il velivolo (passeggeri + carburante + bagagli)
2. Trova il peso reale del decollo
3. Legge $V_S$, $V_R$, $V_2$ corrispondenti dalla tabella

Per A320, scarto tipico tra MTOW e peso minimo operativo: 30-35 kt sulle V-speeds. Significativo!

> 🎓 **Take-away didattico**: peso e velocità sono accoppiati. Un pilota commerciale che non controlla il peso prima del decollo (o usa V-speeds sbagliate) rischia un decollo abortito o un avvio che si stacca a velocità troppo bassa = pericolo. È **obbligatorio** ricalcolare le V-speeds per ogni volo.
