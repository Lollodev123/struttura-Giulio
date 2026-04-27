# Soluzione — Variante Esercizio 4

**Variante**: stesso aliante ASK-21 ma ora con un solo pilota: $m = 520$ kg invece di 600 kg.

### Passo 1 — Peso

$$W = m \cdot g = 520 \times 9{,}81 = 5\,101{,}2 \text{ N}$$

### Passo 2 — $C_L^*$ ed $E_{max}$ (invariati)

$$C_L^* = \sqrt{\pi \times 16{,}6 \times 0{,}95 \times 0{,}014} = 0{,}833$$

$$E_{max} = \dfrac{1}{2}\sqrt{\dfrac{\pi \times 16{,}6 \times 0{,}95}{0{,}014}} \approx 29{,}75$$

> 💡 Identici al problema base: questi parametri **dipendono SOLO dalla geometria**, NON dal peso.

### Passo 3 — Nuova velocità $V^*$

$$V^* = \sqrt{\dfrac{2W}{\rho S C_L^*}} = \sqrt{\dfrac{2 \times 5\,101{,}2}{1{,}225 \times 17{,}95 \times 0{,}833}}$$

Calcolo:

- Numeratore: $2 \times 5\,101{,}2 = 10\,202{,}4$
- Denominatore: $1{,}225 \times 17{,}95 \times 0{,}833 = 18{,}31$
- Rapporto: $10\,202{,}4 / 18{,}31 = 557{,}3$
- Radice: $\sqrt{557{,}3} = 23{,}61$ m/s

$$\boxed{V^*(520\,kg) \approx 23{,}6 \text{ m/s} = 45{,}9 \text{ kt}}$$

### Passo 4 — Distanza in planata da 2000 m (invariata)

$$\text{distanza} = E_{max} \times h = 29{,}75 \times 2\,000 = 59\,500 \text{ m} \approx 60 \text{ km}$$

### Confronto con problema base (600 kg)

| Massa | $V^*$ (m/s) | $V^*$ (kt) | $E_{max}$ | Distanza |
|---|---|---|---|---|
| 600 kg (base) | 25,4 | 49 | 29,75 | 60 km |
| 520 kg (variante) | 23,6 | 46 | **29,75** | **60 km** |
| Rapporto | $\sqrt{520/600} = 0{,}931$ | 0,931 | 1 | 1 |

**Lettura**: $V^* \propto \sqrt{W}$, quindi peso ridotto del 13% → $V^*$ ridotta del **6,9%**. Ma **$E_{max}$ e distanza di planata sono identiche** — non dipendono dal peso!

> 🎓 **Take-away controintuitivo ma fondamentale**: aliante più leggero **non vola più lontano**, vola solo più piano. La distanza percorsa per metro di quota persa è la stessa. È puramente geometria del profilo + ala. Il peso **non è una variabile** della formula della planata. Sembra strano ma è esattamente così, ed è una delle prime cose che insegnano alla scuola di volo a vela.
