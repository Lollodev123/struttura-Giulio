# Soluzione — Variante Esercizio 7

**Variante**: calcolare $Re$ della **coda orizzontale** del Cessna 172 (corda media $c_{coda} = 0{,}82$ m) in crociera al livello mare ISA, $V = 62{,}76$ m/s.

### Passo 1 — Applicazione della formula

$$Re_{coda} = \dfrac{\rho V c_{coda}}{\mu} = \dfrac{1{,}225 \times 62{,}76 \times 0{,}82}{1{,}78 \times 10^{-5}}$$

### Passo 2 — Calcolo a tappe

- Numeratore parziale: $1{,}225 \times 62{,}76 = 76{,}88$
- Numeratore finale: $76{,}88 \times 0{,}82 = 63{,}04$
- Rapporto: $63{,}04 / (1{,}78 \times 10^{-5}) = 3{,}54 \times 10^6$

$$\boxed{Re_{coda} \approx 3{,}5 \times 10^6 \text{ — TURBOLENTO}}$$

### Confronto con l'ala

| Parte | Corda (m) | $Re$ | Regime |
|---|---|---|---|
| Ala principale | 1,49 | $6{,}4 \times 10^6$ | Turbolento |
| Coda orizzontale | 0,82 | $3{,}5 \times 10^6$ | Turbolento |
| Rapporto | $0{,}82/1{,}49 = 0{,}55$ | $3{,}5/6{,}4 = 0{,}55$ | $Re \propto c$ ✅ |

**Lettura**: il rapporto dei $Re$ è esattamente il rapporto delle corde, come previsto dalla formula. Entrambi sono nel regime turbolento, ma la coda lavora a $Re$ inferiore.

### Implicazione progettuale

La coda è **più piccola** dell'ala in due dimensioni:

- Corda minore (~55%) → $Re$ minore
- Apertura minore → momento applicato comunque sufficiente perché ha braccio lungo

A $Re$ minore di ~$10^6$, la coda è ancora pienamente turbolenta — niente sorprese laminari, niente bisogno di profili speciali. Il profilo della coda del Cessna è semplice (NACA 0009 o simile, simmetrico, sottile).

> 🎓 **Take-away didattico**: ogni superficie aerodinamica del velivolo ha **il suo $Re$**. Ala, coda orizzontale, timone verticale, eliche, prese d'aria: ognuno con la sua corda caratteristica. Il progettista deve calcolare ciascuno e verificare che sia in un regime "comodo" per il profilo scelto.
>
> Aeromodellini volano a $Re$ di $10^4$–$10^5$ → richiedono profili sottili specifici (Eppler, Wortmann), non i NACA "robusti" della 172.
