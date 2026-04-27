# Soluzione — Variante Esercizio 6

**Variante**: $C_L = 0{,}9$ richiesto (per atterraggio lento). Quale $\alpha$ per profilo NACA 2412? E per NACA 0012?

### Passo 1 — Profilo A (NACA 2412): $\alpha_0 = -2°$

$$0{,}9 = 0{,}11 \times (\alpha + 2°)$$

Risolvendo:

$$\alpha + 2 = \dfrac{0{,}9}{0{,}11} = 8{,}18°$$

$$\boxed{\alpha^A = 6{,}18°}$$

### Passo 2 — Profilo B (NACA 0012): $\alpha_0 = 0°$

$$0{,}9 = 0{,}11 \times \alpha$$

$$\boxed{\alpha^B = 8{,}18°}$$

### Confronto

| Profilo | $\alpha_0$ | $\alpha$ richiesto per $C_L = 0{,}9$ | Margine fino allo stallo |
|---|---|---|---|
| A (2412 — Cessna) | $-2°$ | $6{,}18°$ | $16° - 6{,}18° = 9{,}82°$ |
| B (0012 — simmetrico) | $0°$ | $8{,}18°$ | $14° - 8{,}18° = 5{,}82°$ |

**Lettura**:

- Il profilo asimmetrico A ha bisogno di **2° in meno** per generare lo stesso $C_L$ → fusoliera più orizzontale in atterraggio → migliore visibilità sul muso, comfort passeggeri.
- Inoltre A ha **margine maggiore** prima dello stallo (9,8° vs 5,8°) — più sicuro per pilota meno esperto.

### Implicazione progettuale

L'esempio del Cessna 172 (NACA 2412 sull'ala, NACA 0012 sulla coda) è didatticamente perfetto:

- **Ala**: deve generare portanza in volo livellato → asimmetrico (curvato), $C_L$ "gratis" a $\alpha = 0$
- **Stabilizzatore di coda**: deve lavorare in entrambi i sensi (deportanza in crociera, portanza in atterraggio quando l'equilibratore è alzato) → simmetrico

> 🎓 **Take-away didattico**: la **scelta del profilo** è la prima decisione progettuale dopo aver definito la missione. Scegliere asimmetrico per un'ala da trasporto e simmetrico per una coda è "common sense aerodinamico" — anche oggi, dopo 90 anni di NACA, si fa così su quasi tutti i velivoli generali.
