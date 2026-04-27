# Quiz BASE — Lezioni 1-2 (Profilo alare e Portanza)

> 🟢 **Difficoltà: BASE** — 15 domande a risposta multipla con feedback immediato.
>
> 🎯 Studia prima [Lezione 1](../01-teoria/01-profilo-alare.md) e [Lezione 2](../01-teoria/02-portanza.md).
>
> ⏱️ Tempo: ~15 min · clicca la risposta che ritieni giusta, vedrai subito se è corretta.

<div class="quiz-score">📊 Inizia il quiz cliccando sulle risposte</div>

---

<div class="quiz-q" data-correct="b" markdown="1">

**1. Cosa rappresenta la "corda" di un profilo alare?**

<button class="quiz-opt" data-opt="a">A. La distanza tra le due estremità dell'ala (tip a tip)</button>
<button class="quiz-opt" data-opt="b">B. Il segmento rettilineo dal bordo d'attacco al bordo d'uscita</button>
<button class="quiz-opt" data-opt="c">C. La linea curva che separa dorso e ventre del profilo</button>
<button class="quiz-opt" data-opt="d">D. La distanza massima tra dorso e ventre</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: B** — La corda è la "lunghezza" del profilo, riferimento per tutto. L'opzione A è l'**apertura alare** (parametro 3D dell'ala). L'opzione D è lo **spessore**. Vedi [Lezione 1](../01-teoria/01-profilo-alare.md#geometria-le-6-parti-che-devi-conoscere).
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="b" markdown="1">

**2. Nel codice NACA 2412, cosa indica la cifra "12"?**

<button class="quiz-opt" data-opt="a">A. La curvatura massima al 12% della corda</button>
<button class="quiz-opt" data-opt="b">B. Lo spessore massimo al 12% della corda</button>
<button class="quiz-opt" data-opt="c">C. La posizione della curvatura al 12% della corda</button>
<button class="quiz-opt" data-opt="d">D. Il numero di Reynolds critico × 10⁵</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: B** — In NACA `MPXX`, le ultime due cifre sono lo spessore in % della corda. M=2 (curvatura), P=4 (posizione curvatura in decimi), 12 (spessore).
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="c" markdown="1">

**3. Quale dei seguenti profili è simmetrico?**

<button class="quiz-opt" data-opt="a">A. NACA 2412</button>
<button class="quiz-opt" data-opt="b">B. NACA 4412</button>
<button class="quiz-opt" data-opt="c">C. NACA 0012</button>
<button class="quiz-opt" data-opt="d">D. NACA 23012</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: C** — Le prime due cifre `00` indicano curvatura zero → profilo simmetrico. Tutti gli altri sono asimmetrici (cambered).
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="b" markdown="1">

**4. La formula della portanza è:**

<button class="quiz-opt" data-opt="a">A. L = ρ V S C_L</button>
<button class="quiz-opt" data-opt="b">B. L = ½ ρ V² S C_L</button>
<button class="quiz-opt" data-opt="c">C. L = ρ V² S C_L</button>
<button class="quiz-opt" data-opt="d">D. L = ½ ρ V S C_L</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: B** — Mai dimenticare il fattore **½** (sta nella pressione dinamica $q = \frac{1}{2}\rho V^2$) e il **quadrato** della velocità. Vedi [Lezione 2](../01-teoria/02-portanza.md).
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="b" markdown="1">

**5. Se raddoppi la velocità del velivolo, mantenendo C_L e ρ costanti, la portanza:**

<button class="quiz-opt" data-opt="a">A. Raddoppia</button>
<button class="quiz-opt" data-opt="b">B. Quadruplica</button>
<button class="quiz-opt" data-opt="c">C. Resta uguale</button>
<button class="quiz-opt" data-opt="d">D. Si dimezza</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: B** — $L \propto V^2$, quindi raddoppi V → $L \times 4$. Errore classico: pensare che raddoppi.
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="b" markdown="1">

**6. In volo livellato a velocità costante, quale relazione vale?**

<button class="quiz-opt" data-opt="a">A. L > W e T > D</button>
<button class="quiz-opt" data-opt="b">B. L = W e T = D</button>
<button class="quiz-opt" data-opt="c">C. L < W e T = D</button>
<button class="quiz-opt" data-opt="d">D. L = W e T > D</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: B** — Equilibrio in volo livellato: forze a coppie (verticale e orizzontale). Vedi [Esercizio 1](../03-esercizi/01-base-portanza-cessna.md).
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="c" markdown="1">

**7. Quale di queste affermazioni sulla portanza è SBAGLIATA?**

<button class="quiz-opt" data-opt="a">A. La portanza è perpendicolare alla velocità</button>
<button class="quiz-opt" data-opt="b">B. Per un profilo simmetrico a α = 0°, la portanza è zero</button>
<button class="quiz-opt" data-opt="c">C. La portanza dipende solo dalla forma del profilo, non dall'angolo di attacco</button>
<button class="quiz-opt" data-opt="d">D. In virata inclinata, la portanza non è verso l'alto in senso assoluto</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: C (è SBAGLIATA)** — La portanza dipende **sia** dalla forma del profilo **sia** dall'angolo di attacco. Anche un profilo simmetrico genera portanza se inclinato.
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="c" markdown="1">

**8. Lo stallo di un'ala dipende principalmente da:**

<button class="quiz-opt" data-opt="a">A. La velocità del velivolo</button>
<button class="quiz-opt" data-opt="b">B. La densità dell'aria</button>
<button class="quiz-opt" data-opt="c">C. L'angolo di attacco</button>
<button class="quiz-opt" data-opt="d">D. Il peso del velivolo</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: C** — Lo stallo arriva quando $\alpha$ supera il valore critico (~16° per profili tipici). La velocità di stallo è una **conseguenza**, non la causa.
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="c" markdown="1">

**9. Perché il P-51 Mustang viene "lavato" prima di ogni missione di precisione?**

<button class="quiz-opt" data-opt="a">A. Per estetica, era importante per la propaganda</button>
<button class="quiz-opt" data-opt="b">B. Per ridurre il peso dovuto a sporcizia</button>
<button class="quiz-opt" data-opt="c">C. Il profilo alare laminare è sensibile a contaminazione che innesca turbolenza precoce</button>
<button class="quiz-opt" data-opt="d">D. Per evitare ossidazione dell'alluminio</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: C** — Il P-51 ha profilo NACA serie 6 (laminare). Una mosca o sporcizia sul bordo d'attacco innesca **transizione precoce a turbolento** → resistenza maggiore, $E_{max}$ crolla del 20%.
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="b" markdown="1">

**10. Nel Cessna 172 (NACA 2412), la curvatura massima si trova:**

<button class="quiz-opt" data-opt="a">A. Al 20% della corda</button>
<button class="quiz-opt" data-opt="b">B. Al 40% della corda</button>
<button class="quiz-opt" data-opt="c">C. Al 24% della corda</button>
<button class="quiz-opt" data-opt="d">D. Al 50% della corda</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: B** — In NACA `MPXX`, la cifra P (seconda) indica la posizione della curvatura max in **decimi** della corda. P=4 → 40%.
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="b" markdown="1">

**11. La "vista di Newton" della portanza si basa su:**

<button class="quiz-opt" data-opt="a">A. La differenza di pressione tra dorso e ventre</button>
<button class="quiz-opt" data-opt="b">B. L'ala deflette aria verso il basso → reazione verso l'alto</button>
<button class="quiz-opt" data-opt="c">C. La velocità maggiore sopra che sotto l'ala</button>
<button class="quiz-opt" data-opt="d">D. L'effetto Coanda</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: B** — La vista di Newton è quella della **reazione** (downwash). La vista di Bernoulli (pressione, opzione A o C) è complementare e altrettanto valida — descrivono lo stesso fenomeno da angolazioni diverse.
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="b" markdown="1">

**12. Un profilo alare con linea media coincidente con la corda è:**

<button class="quiz-opt" data-opt="a">A. Asimmetrico</button>
<button class="quiz-opt" data-opt="b">B. Simmetrico</button>
<button class="quiz-opt" data-opt="c">C. Laminare</button>
<button class="quiz-opt" data-opt="d">D. Cambered</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: B** — Linea media = corda → profilo simmetrico. La portanza è zero a $\alpha = 0$.
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="c" markdown="1">

**13. Quale fattore matematico NON deve essere dimenticato nella formula della portanza?**

<button class="quiz-opt" data-opt="a">A. Il fattore ρ (densità)</button>
<button class="quiz-opt" data-opt="b">B. Il fattore S (superficie alare)</button>
<button class="quiz-opt" data-opt="c">C. Il fattore ½</button>
<button class="quiz-opt" data-opt="d">D. Il fattore C_L</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: C** — Il fattore **½** è l'errore più comune, sta dentro il termine di pressione dinamica $\frac{1}{2}\rho V^2$. Mai dimenticarlo.
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="c" markdown="1">

**14. Per un Cessna 172 (massa 1043 kg) in volo livellato, il peso W è approssimativamente:**

<button class="quiz-opt" data-opt="a">A. 1043 N</button>
<button class="quiz-opt" data-opt="b">B. 5215 N</button>
<button class="quiz-opt" data-opt="c">C. 10232 N</button>
<button class="quiz-opt" data-opt="d">D. 20464 N</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: C** — $W = m \cdot g = 1043 \times 9{,}81 = 10\,231{,}83$ N. L'opzione A confonde **kg con N** (errore di unità grave).
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

<div class="quiz-q" data-correct="c" markdown="1">

**15. Allo stallo di un profilo, cosa succede al C_L?**

<button class="quiz-opt" data-opt="a">A. Continua a crescere indefinitamente</button>
<button class="quiz-opt" data-opt="b">B. Resta costante</button>
<button class="quiz-opt" data-opt="c">C. Crolla bruscamente</button>
<button class="quiz-opt" data-opt="d">D. Diventa negativo</button>

<div class="quiz-explanation" markdown="1">
**Risposta corretta: C** — Allo stallo, il flusso si separa dal dorso → $C_L$ scende drasticamente. È il motivo per cui lo stallo è pericoloso: la portanza non basta più a sostenere il peso.
</div>
<button class="quiz-retry">↻ Riprova</button>

</div>

---

## ➡️ Hai finito?

Vai al [Quiz MEDIO](./quiz-medio.md) sulle Lezioni 3-6 (resistenza, efficienza, ISA, Reynolds).

> 💡 Punteggio sotto il 70%? **Ripassa** [Lezione 1](../01-teoria/01-profilo-alare.md) e [Lezione 2](../01-teoria/02-portanza.md), poi rifai il quiz tra qualche giorno.
