# Soluzione — Variante Esercizio 5

**Variante**: stesso Boeing 737 ($S = 122{,}6$ m², $\lambda = 10$, FL350 $\rho = 0{,}381$ kg/m³, $V = 230$ m/s), ma a fine volo con peso ridotto: $m = 50\,000$ kg invece di 70 000 kg (carburante consumato e meno passeggeri/bagagli).

### Passo 1 — Nuovo peso

$$Q = m \cdot g = 50\,000 \times 9{,}81 = 490\,500 \text{ N}$$

### Passo 2 — Nuovo $C_p$ richiesto

Densità e velocità invariate, cambia solo $W$:

$$C_p = \dfrac{2Q}{\rho V^2 S} = \dfrac{2 \times 490\,500}{0{,}381 \times 230^2 \times 122{,}6}$$

Calcolo:

- Numeratore: $2 \times 490\,500 = 981\,000$
- $230^2 = 52\,900$
- $0{,}381 \times 52\,900 = 20\,155$
- Denominatore: $20\,155 \times 122{,}6 = 2\,471\,003$
- Rapporto: $981\,000 / 2\,471\,003 = 0{,}3970$

$$\boxed{C_p \approx 0{,}40}$$

### Confronto con peso base (70 000 kg)

| Peso | $W$ (N) | $C_p$ | Variazione |
|---|---|---|---|
| 70 000 kg (base) | 686 700 | 0,55 | — |
| 50 000 kg (variante) | 490 500 | 0,40 | **−27,3%** |
| Rapporto | 0,714 | 0,727 | $C_p \propto W$ ✅ |

**Lettura**: $C_p$ è proporzionale a $W$ (a parità di tutto il resto). Riduci il peso del 28,6%, riduci $C_p$ del 27,3% (coerente entro arrotondamenti).

### Implicazione operativa: lo "step climb"

Con $C_p = 0{,}40$, il jet è abbondantemente sotto $C_p^* \approx 0{,}82$ (vedi [Esercizio 10](../10-avanzato-polare-completa.md)). È più lontano dall'efficienza massima.

**Soluzione operativa dei piloti commerciali**: salire di quota man mano che il peso scende. A FL370 o FL390:

- $\rho$ scende ulteriormente → $C_p$ richiesto risale verso $C_p^*$
- L'aereo lavora più vicino all'efficienza massima
- Il consumo $\downarrow$

Questo si chiama **step climb**: il pilota richiede ATC quote più alte ogni 1-2 ore di volo. Tipico transatlantico: parti FL340 a peso pieno, finisci FL400 dopo 7-8 ore di volo.

> 🎓 **Take-away didattico**: la quota di crociera non è fissa. Cambia col peso. È una delle differenze più importanti tra "volare per turismo" (Cessna sempre a 1000 m) e "volare per business" (jet che ottimizzano dinamicamente).
