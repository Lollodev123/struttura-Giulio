# Soluzione — Variante Esercizio 3

**Variante**: stesso ATR 72 ($m = 22\,000$ kg, $S = 61$ m², $\lambda = 12$, $C_{R,0} = 0{,}025$, $e = 0{,}85$), in **discesa** a 7 000 m con motori al minimo, velocità ridotta a $V = 110$ m/s.

### Passo 1 — Pressione dinamica nuova

$$q = \dfrac{1}{2}\rho V^2 = \dfrac{1}{2} \times 0{,}590 \times 110^2 = \dfrac{1}{2} \times 0{,}590 \times 12\,100 = 3\,569{,}5 \text{ Pa}$$

### Passo 2 — $C_p$ richiesto

$$C_p = \dfrac{W}{q \cdot S} = \dfrac{215\,820}{3\,569{,}5 \times 61} = \dfrac{215\,820}{217\,740} \approx 0{,}991$$

$$\boxed{C_p \approx 0{,}99}$$

### Passo 3 — $C_{R,i}$

$$C_{R,i} = \dfrac{C_p^2}{\pi \lambda e} = \dfrac{0{,}991^2}{\pi \times 12 \times 0{,}85} = \dfrac{0{,}982}{32{,}04} \approx 0{,}0307$$

$$\boxed{C_{R,i} \approx 0{,}031}$$

### Confronto crociera (140 m/s) vs discesa (110 m/s)

| | $V$ (m/s) | $q$ (Pa) | $C_p$ | $C_{R,i}$ | Quota indotta su $C_R$ |
|---|---|---|---|---|---|
| Crociera | 140 | 5 782 | 0,612 | 0,012 | ~32% |
| Discesa | 110 | 3 570 | 0,991 | 0,031 | ~55% |

**Lettura**: a velocità ridotta, $C_p$ aumenta (da 0,61 a 0,99 = +62%) e $C_{R,i}$ aumenta col **quadrato** (da 0,012 a 0,031 = +160%). L'indotta passa da minore della parassita a **dominante**.

> 🎓 **Take-away didattico**: i piloti commerciali in discesa NON rallentano lentamente lasciando galleggiare l'aereo a $C_p$ alti. Strategy operativa: scendono a velocità di crociera o appena sotto, gestendo l'angolo di traiettoria con i throttle. Rallentare troppo presto = $C_{R,i}$ esplode = l'aereo "galleggia" e arriva alto sopra l'aeroporto. Si chiama **"high & fast"**: l'errore più comune dei voli simulati o dei piloti junior.
