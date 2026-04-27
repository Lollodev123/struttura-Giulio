# Soluzione — Variante Esercizio 1

**Variante**: Cessna 172 con $m = 1\,043$ kg, $S = 16{,}2$ m², $\rho = 1{,}225$ kg/m³, ma $V = 140$ kt.

### Passo 1 — Conversione velocità
$$V = 140 \times 0{,}5144 = 72{,}02 \text{ m/s}$$

### Passo 2 — Peso (invariato rispetto al problema base)
$$W = 1\,043 \times 9{,}81 = 10\,231{,}83 \text{ N}$$

### Passo 3 — Calcolo $C_L$
$$C_L = \frac{2W}{\rho V^2 S} = \frac{2 \times 10\,231{,}83}{1{,}225 \times (72{,}02)^2 \times 16{,}2}$$

- $(72{,}02)^2 = 5\,186{,}88$
- Denominatore: $1{,}225 \times 5\,186{,}88 \times 16{,}2 = 102\,943{,}70$
- $C_L = 20\,463{,}66 / 102\,943{,}70 = 0{,}1988$

$$\boxed{C_L \approx 0{,}20}$$

### Confronto con il problema base

| | $V$ | $V^2$ | $C_L$ |
|---|---|---|---|
| Problema base | 62,76 m/s | 3 938,82 | 0,262 |
| Variante | 72,02 m/s | 5 186,88 | 0,199 |
| Rapporto | 1,148 | 1,317 | **0,759** |

**Lettura**: aumentare la velocità del 14,8% riduce $C_L$ del 24,1%. Conferma la dipendenza inversa quadratica: $C_L \propto 1/V^2$.

> 🎓 **Take-away didattico**: ogni volta che il vento sull'ala raddoppia, $V^2$ quadruplica, e a parità di peso $C_L$ si riduce a un quarto. Questo è il motivo per cui in crociera ad alta velocità si vola con $C_L$ piccoli e in fase di atterraggio (lenta) servono $C_L$ alti — da qui i flap.
