# Soluzione — Variante Esercizio 2

**Variante**: stesso Piper PA-28 ($m = 1\,157$ kg, $S = 15{,}8$ m², $C_{L,max} = 1{,}5$ ala pulita), ma in volo a **2 000 m** di quota ISA invece che al livello mare.

### Passo 1 — Densità a 2000 m (tabella ISA)

Dalla [tabella ISA del formulario](../../00-formulario/formulario.md#7-atmosfera-standard-isa--valori-chiave):

$$\rho(2000) = 1{,}007 \text{ kg/m}^3$$

### Passo 2 — Peso (invariato)

$$W = m \cdot g = 1\,157 \times 9{,}81 = 11\,350{,}17 \text{ N}$$

### Passo 3 — Velocità di stallo a 2000 m

$$V_S(2000) = \sqrt{\dfrac{2W}{\rho S C_{L,max}}} = \sqrt{\dfrac{2 \times 11\,350{,}17}{1{,}007 \times 15{,}8 \times 1{,}5}}$$

Calcolo:

- Numeratore: $2 \times 11\,350{,}17 = 22\,700{,}34$
- Denominatore: $1{,}007 \times 15{,}8 \times 1{,}5 = 23{,}87$
- Rapporto: $22\,700{,}34 / 23{,}87 = 951{,}1$
- Radice: $\sqrt{951{,}1} = 30{,}84$ m/s

$$\boxed{V_S(2000) \approx 30{,}8 \text{ m/s} = 59{,}9 \text{ kt}}$$

### Confronto con il livello mare

| | $\rho$ (kg/m³) | $V_S$ (m/s) | $V_S$ (kt) |
|---|---|---|---|
| Livello mare | 1,225 | 28,0 | 54,4 |
| 2000 m | 1,007 | 30,8 | 59,9 |
| Rapporto | 0,822 | **1,099** | 1,099 |

**Lettura**: $V_S$ aumenta del **9,9%** salendo da livello mare a 2000 m. Coerente con la formula $V_S \propto 1/\sqrt{\rho}$: rapporto $\sqrt{\rho_0/\rho_{2000}} = \sqrt{1{,}225/1{,}007} = \sqrt{1{,}216} = 1{,}103$ ✅.

> 🎓 **Take-away didattico**: in alta quota stalli prima. Ecco perché aeroporti d'alta quota (Cuzco 3399 m, Lhasa 3570 m, La Paz 4061 m) richiedono velocità di approccio significativamente maggiori di un aeroporto al mare. Se sei abituato a "atterrare a 50 kt" con un Piper, a quota dovrai farlo a 60+ kt — e la pista deve essere più lunga.
