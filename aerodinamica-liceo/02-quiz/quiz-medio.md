# Quiz MEDIO — Lezioni 3-6 (Resistenza, Efficienza, ISA, Reynolds)

> 🟡 **Difficoltà: MEDIO** — 15 domande con feedback immediato.
>
> 🎯 Studia [Lezione 3](../01-teoria/03-resistenza.md), [4](../01-teoria/04-efficienza.md), [5](../01-teoria/05-atmosfera-isa.md), [6](../01-teoria/06-numero-reynolds.md).
>
> ⏱️ Tempo: ~20 min

<div class="quiz-score">📊 Inizia il quiz</div>

---

<div class="quiz-q" data-correct="b" markdown="1">

**1. La resistenza totale di un velivolo si decompone in:**

<button class="quiz-opt" data-opt="a">A. Parassita + induzione + interferenza</button>
<button class="quiz-opt" data-opt="b">B. Parassita + indotta</button>
<button class="quiz-opt" data-opt="c">C. Forma + attrito + lift</button>
<button class="quiz-opt" data-opt="d">D. Stallo + viscosa + di pressione</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: B** — $C_D = C_{D,0} + C_{D,i}$. La parassita esiste anche senza portanza; l'indotta è il prezzo della portanza. Vedi [Lezione 3](../01-teoria/03-resistenza.md).
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="b" markdown="1">

**2. La resistenza indotta cresce proporzionalmente a:**

<button class="quiz-opt" data-opt="a">A. C_L</button>
<button class="quiz-opt" data-opt="b">B. C_L²</button>
<button class="quiz-opt" data-opt="c">C. V</button>
<button class="quiz-opt" data-opt="d">D. V²</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: B** — $C_{D,i} = C_L^2/(\pi \lambda e)$. Cresce col **quadrato** di $C_L$.
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="c" markdown="1">

**3. Ali lunghe e sottili (alianti) sono progettate per:**

<button class="quiz-opt" data-opt="a">A. Aumentare la velocità massima</button>
<button class="quiz-opt" data-opt="b">B. Ridurre la resistenza parassita</button>
<button class="quiz-opt" data-opt="c">C. Ridurre la resistenza indotta tramite alto allungamento alare</button>
<button class="quiz-opt" data-opt="d">D. Aumentare il C_L,max</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: C** — Allungamento $\lambda$ alto → $C_{D,i}$ basso → efficienza massima alta. Principio cardine degli alianti.
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="b" markdown="1">

**4. L'efficienza aerodinamica E è definita come:**

<button class="quiz-opt" data-opt="a">A. L/W</button>
<button class="quiz-opt" data-opt="b">B. C_L/C_D</button>
<button class="quiz-opt" data-opt="c">C. L · D</button>
<button class="quiz-opt" data-opt="d">D. C_D/C_L</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: B** — $E = C_L/C_D = L/D$, rapporto adimensionale tra portanza e resistenza.
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="b" markdown="1">

**5. In planata (motore spento), un aliante con E = 30 a 1500 m di quota può percorrere al massimo:**

<button class="quiz-opt" data-opt="a">A. 30 km</button>
<button class="quiz-opt" data-opt="b">B. 45 km</button>
<button class="quiz-opt" data-opt="c">C. 15 km</button>
<button class="quiz-opt" data-opt="d">D. 1500 m</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: B** — distanza = $E \times h = 30 \times 1{,}5\,$km = **45 km**. Formula della planata, [Lezione 4](../01-teoria/04-efficienza.md).
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="c" markdown="1">

**6. La formula di E_max dipende da:**

<button class="quiz-opt" data-opt="a">A. Solo dal peso</button>
<button class="quiz-opt" data-opt="b">B. Solo dalla velocità</button>
<button class="quiz-opt" data-opt="c">C. Allungamento, fattore di Oswald, e resistenza parassita</button>
<button class="quiz-opt" data-opt="d">D. Solo dal C_L,max</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: C** — $E_{max} = \frac{1}{2}\sqrt{\pi \lambda e / C_{D,0}}$. **Non** dipende dal peso! È un parametro puramente geometrico/aerodinamico.
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="c" markdown="1">

**7. A massima efficienza, qual è la relazione tra parassita e indotta?**

<button class="quiz-opt" data-opt="a">A. Parassita = doppio dell'indotta</button>
<button class="quiz-opt" data-opt="b">B. Indotta = zero</button>
<button class="quiz-opt" data-opt="c">C. Parassita = indotta</button>
<button class="quiz-opt" data-opt="d">D. Parassita = zero</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: C** — A massima efficienza, le due componenti sono **uguali**. Risultato matematico molto elegante: $C_{D,0} = C_{L^*}^2/(\pi\lambda e)$.
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="c" markdown="1">

**8. In atmosfera ISA standard, al livello del mare la temperatura è:**

<button class="quiz-opt" data-opt="a">A. 0 °C</button>
<button class="quiz-opt" data-opt="b">B. 10 °C</button>
<button class="quiz-opt" data-opt="c">C. 15 °C</button>
<button class="quiz-opt" data-opt="d">D. 25 °C</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: C** — $T_0 = 15$ °C = 288,15 K. Da memorizzare. Vedi [Lezione 5](../01-teoria/05-atmosfera-isa.md).
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="b" markdown="1">

**9. Il gradiente termico in troposfera è approssimativamente:**

<button class="quiz-opt" data-opt="a">A. -10 °C ogni 1000 m</button>
<button class="quiz-opt" data-opt="b">B. -6,5 °C ogni 1000 m</button>
<button class="quiz-opt" data-opt="c">C. -1 °C ogni 1000 m</button>
<button class="quiz-opt" data-opt="d">D. +6,5 °C ogni 1000 m</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: B** — Gradiente standard troposferico ISA. Da memorizzare. La temperatura sale solo nella stratosfera (oltre 11 km).
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="c" markdown="1">

**10. A 10 000 m di quota ISA, la densità dell'aria è circa:**

<button class="quiz-opt" data-opt="a">A. 1,225 kg/m³</button>
<button class="quiz-opt" data-opt="b">B. 0,909 kg/m³</button>
<button class="quiz-opt" data-opt="c">C. 0,413 kg/m³</button>
<button class="quiz-opt" data-opt="d">D. 0,150 kg/m³</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: C** — Dalla tabella ISA: a 10 km, densità ridotta a circa **un terzo** del livello mare. È il motivo per cui i jet volano alti: meno parassita.
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="b" markdown="1">

**11. La velocità di stallo V_S in alta quota:**

<button class="quiz-opt" data-opt="a">A. Diminuisce rispetto al livello mare</button>
<button class="quiz-opt" data-opt="b">B. Aumenta rispetto al livello mare</button>
<button class="quiz-opt" data-opt="c">C. Resta uguale</button>
<button class="quiz-opt" data-opt="d">D. Dipende solo dal peso</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: B** — $V_S = \sqrt{2W/(\rho S C_{L,max})}$: $\rho$ scende → $V_S$ sale. Per questo gli aeroporti d'alta quota (La Paz 4000 m) hanno piste più lunghe.
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="b" markdown="1">

**12. Il numero di Reynolds è:**

<button class="quiz-opt" data-opt="a">A. Una velocità in m/s</button>
<button class="quiz-opt" data-opt="b">B. Un rapporto adimensionale tra forze inerziali e viscose</button>
<button class="quiz-opt" data-opt="c">C. Una grandezza con unità di Pa·s</button>
<button class="quiz-opt" data-opt="d">D. Il quadrato della velocità divisa per la densità</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: B** — $Re = \rho V c / \mu$, numero **puro**. Determina il regime laminare vs turbolento. Vedi [Lezione 6](../01-teoria/06-numero-reynolds.md).
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="b" markdown="1">

**13. Per un Cessna 172 in crociera, il regime di flusso sull'ala è tipicamente:**

<button class="quiz-opt" data-opt="a">A. Laminare</button>
<button class="quiz-opt" data-opt="b">B. Turbolento</button>
<button class="quiz-opt" data-opt="c">C. In transizione</button>
<button class="quiz-opt" data-opt="d">D. Inversione di flusso</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: B** — Cessna in crociera: $Re \approx 6 \times 10^6$ — pienamente turbolento. **Tutti** i velivoli convenzionali vivono in turbolento.
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="a" markdown="1">

**14. La viscosità dinamica μ dell'aria a 15 °C è circa:**

<button class="quiz-opt" data-opt="a">A. 1,78 × 10⁻⁵ Pa·s</button>
<button class="quiz-opt" data-opt="b">B. 1,78 × 10⁻³ Pa·s</button>
<button class="quiz-opt" data-opt="c">C. 1,78 Pa·s</button>
<button class="quiz-opt" data-opt="d">D. 1,78 × 10⁵ Pa·s</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: A** — Da memorizzare. Confondere la potenza di 10 è un errore frequente che porta a $Re$ sballato di milioni di volte.
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="b" markdown="1">

**15. La velocità di max efficienza V* del Cessna 172 è circa 70 kt, mentre la crociera è 122 kt. Perché si vola in crociera, non a V*?**

<button class="quiz-opt" data-opt="a">A. Perché V* è il limite minimo strutturale</button>
<button class="quiz-opt" data-opt="b">B. Perché si sacrifica un po' di efficienza per arrivare prima</button>
<button class="quiz-opt" data-opt="c">C. Perché a V* l'aereo stallerebbe</button>
<button class="quiz-opt" data-opt="d">D. Per via dell'effetto Coanda</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: B** — A $V^*$ (~70 kt) si va più "economici" ma il tempo di volo raddoppia → crociera è un compromesso tra consumo e velocità.
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

---

## ➡️ Hai finito?

Vai al [Quiz AVANZATO](./quiz-avanzato.md) sulle Lezioni 7-9.
