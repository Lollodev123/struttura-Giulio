# Soluzioni Quiz — BASE + MEDIO + AVANZATO

> Risposte corrette con **spiegazione** per tutte e 40 le domande.
> Studia le spiegazioni anche se hai risposto giusto: ogni risposta sbagliata è un'occasione per fissare un concetto chiave.

---

## 🟢 Quiz BASE (Lezioni 1-2)

### 1. **B** — Il segmento rettilineo dal bordo d'attacco al bordo d'uscita
La corda è la "lunghezza" del profilo, riferimento per tutto. L'apertura alare invece è la lunghezza tra le due estremità dell'ala (tip a tip). Vedi [Lezione 1](../../01-teoria/01-profilo-alare.md#geometria-le-6-parti-che-devi-conoscere).

### 2. **B** — Lo spessore massimo al 12% della corda
Nel codice NACA `MPXX`, le ultime due cifre sono lo spessore massimo in % della corda. M=2 (curvatura), P=4 (posizione curvatura), 12 (spessore).

### 3. **C** — NACA 0012
Le prime due cifre `00` indicano curvatura zero → profilo simmetrico. Tutti gli altri (2412, 4412, 23012) sono asimmetrici.

### 4. **B** — $L = \frac{1}{2} \rho V^2 S C_L$
Mai dimenticare il fattore ½ e il quadrato di V. Vedi [Lezione 2](../../01-teoria/02-portanza.md).

### 5. **B** — Quadruplica
$L \propto V^2$, quindi raddoppi V → $L$ × 4. Errore classico: pensare che raddoppi.

### 6. **B** — $L = W$ e $T = D$
Equilibrio in volo livellato: forze a coppie. Vedi [Esercizio 1](../../03-esercizi/01-base-portanza-cessna.md).

### 7. **C** — La portanza dipende solo dalla forma, non dall'angolo
SBAGLIATA: la portanza dipende sia dalla forma del profilo che dall'angolo di attacco. Anche un profilo simmetrico genera portanza se inclinato.

### 8. **C** — L'angolo di attacco
Lo stallo arriva quando $\alpha$ supera il valore critico (~16° per profili tipici). La velocità di stallo è una conseguenza, non la causa.

### 9. **C** — Profilo laminare sensibile alla contaminazione
Il P-51 Mustang aveva profilo NACA serie 6 (laminare). Una mosca o sporcizia sul bordo d'attacco innesca transizione precoce a turbolento → resistenza maggiore, prestazioni crollano.

### 10. **B** — Al 40% della corda (NACA 2412 → P=4 = 4 decimi = 40%)
La cifra P (seconda) di NACA 4-cifre indica la posizione in **decimi** della corda.

### 11. **B** — L'ala deflette aria verso il basso → reazione verso l'alto
La vista di Newton è quella della reazione (downwash). La vista di Bernoulli (pressione) è complementare ma diversa. Entrambe sono corrette.

### 12. **B** — Simmetrico
Linea media = corda = profilo simmetrico, portanza zero a $\alpha = 0$.

### 13. **C** — Il fattore ½
È l'errore più comune, mai dimenticarlo. Sta dentro il termine di pressione dinamica $\frac{1}{2}\rho V^2$.

### 14. **C** — 10 232 N
$W = m \cdot g = 1043 \times 9{,}81 = 10\,231{,}83$ N. Le altre risposte confondono kg con N (errore di unità).

### 15. **C** — Crolla bruscamente
Allo stallo, il flusso si separa dal dorso → $C_L$ scende drasticamente. Non resta costante né cresce.

---

## 🟡 Quiz MEDIO (Lezioni 3-6)

### 1. **B** — Parassita + indotta
$C_D = C_{D,0} + C_{D,i}$. La parassita esiste anche senza portanza; l'indotta è il prezzo della portanza. Vedi [Lezione 3](../../01-teoria/03-resistenza.md).

### 2. **B** — $C_L^2$
$C_{D,i} = C_L^2/(\pi \lambda e)$. Cresce col **quadrato** di $C_L$.

### 3. **C** — Ridurre la resistenza indotta tramite alto allungamento
Allungamento $\lambda$ alto → $C_{D,i}$ basso → efficienza massima alta. È il principio cardine degli alianti.

### 4. **B** — $C_L/C_D$ (o equivalentemente $L/D$)
È il rapporto adimensionale tra portanza e resistenza, anch'esso adimensionale.

### 5. **B** — 45 km
distanza = $E \times h = 30 \times 1{,}5\,km = 45$ km. Formula della planata, [Lezione 4](../../01-teoria/04-efficienza.md).

### 6. **C** — Allungamento, Oswald, parassita
$E_{max} = \frac{1}{2}\sqrt{\pi \lambda e / C_{D,0}}$. Non dipende dal peso!

### 7. **C** — Parassita = indotta
A massima efficienza, le due componenti di resistenza sono uguali. Risultato matematico molto elegante.

### 8. **C** — 15 °C (= 288,15 K)
Vedi [Lezione 5](../../01-teoria/05-atmosfera-isa.md). $\rho_0 = 1{,}225$ kg/m³, $p_0 = 101325$ Pa, $T_0 = 15$°C.

### 9. **B** — -6,5 °C ogni 1000 m
Gradiente standard troposferico ISA. Da memorizzare.

### 10. **C** — 0,413 kg/m³
Dalla tabella ISA. A 10 km, densità ridotta a circa un terzo del livello mare.

### 11. **B** — Aumenta
$V_S = \sqrt{2W/(\rho S C_{L,max})}$: $\rho$ scende → $V_S$ sale. Per questo gli aeroporti d'alta quota hanno piste più lunghe.

### 12. **B** — Rapporto adimensionale tra forze inerziali e viscose
$Re = \rho V c / \mu$, numero puro. Vedi [Lezione 6](../../01-teoria/06-numero-reynolds.md).

### 13. **B** — Turbolento
Cessna in crociera: $Re \approx 6 \times 10^6$ — pienamente turbolento. Tutti i velivoli convenzionali vivono in regime turbolento.

### 14. **A** — $1{,}78 \times 10^{-5}$ Pa·s
Da memorizzare. Confondere con altre potenze di 10 è un errore frequente.

### 15. **B** — Si sacrifica efficienza per arrivare prima
A $V^*$ (~70 kt) si va più "economici" ma arrivare a destinazione ci vorrebbe il doppio del tempo. La crociera è un compromesso operativo.

---

## 🔴 Quiz AVANZATO (Lezioni 7-9)

### 1. **B** — $b^2/S$
Allungamento = apertura al quadrato fratto superficie. Memorizza la formula.

### 2. **B** — Resistenza indotta molto maggiore
$C_{D,i} \propto 1/\lambda$. Un caccia con $\lambda = 3$ ha indotta quasi 8 volte quella di un aliante con $\lambda = 25$, a parità di $C_L$.

### 3. **C** — Stabilità laterale
Diedro positivo = ala più bassa "vede" più aria = più portanza = aereo torna dritto. È uno dei meccanismi base di stabilità di volo.

### 4. **A** — Il CG è davanti al CP / centro aerodinamico
Vedi [Lezione 8](../../01-teoria/08-momento-centraggio.md). CG davanti = momento di richiamo = stabilità.

### 5. **B** — 25% della corda
Punto canonico per profili convenzionali a bassa velocità. Memorizza questo numero — è il riferimento per tutti i calcoli di centraggio.

### 6. **B** — Piccola deportanza per equilibrare il momento dell'ala
Errore comune: pensare che la coda spinga verso l'alto. In realtà fa una deportanza correttiva.

### 7. **B** — Aumentano contemporaneamente curvatura E superficie alare
Caratteristica unica dei Fowler: scivolano indietro lungo binari. Massimo aumento di $C_{L,max}$ disponibile.

### 8. **B** — Sul bordo d'attacco
Slat e flap stanno in punti opposti dell'ala: slat avanti, flap dietro.

### 9. **C** — Possibili danni strutturali
Il flap ha un limite di velocità ($V_{FE}$) oltre il quale il sistema strutturale può cedere. Pericoloso e tipicamente vietato dai sistemi di protezione.

### 10. **B** — Aumenta l'agilità in manovra
Velivolo intenzionalmente instabile = reazioni rapidissime, ma richiede fly-by-wire computerizzato. È il paradigma dei caccia moderni post-anni '80.

---

## 📊 Punteggio finale

Conta le risposte corrette su 40:

- **35-40**: Eccellente. Sei pronto per l'interrogazione e per applicare le formule a problemi nuovi.
- **28-34**: Buono. Rivedi i concetti delle domande sbagliate prima dell'interrogazione.
- **20-27**: Sufficiente. Devi ripassare almeno una lezione per ogni gruppo di domande in cui hai sbagliato.
- **<20**: Insufficiente. Riprendi il programma dall'inizio, focalizzandoti sulle Lezioni e poi ripeti il quiz.

> 💡 **Consiglio**: gli errori sono **più informativi** delle risposte giuste. Ogni domanda sbagliata = una rispolverata mirata.

---

## ➡️ Cosa fare adesso

1. **Errori sui concetti delle Lezioni 1-2**: ripassa [Profilo alare](../../01-teoria/01-profilo-alare.md) e [Portanza](../../01-teoria/02-portanza.md), poi rifai gli [Esercizi 1-2](../../03-esercizi/01-base-portanza-cessna.md).
2. **Errori su resistenza/efficienza**: ripassa [Lezione 3](../../01-teoria/03-resistenza.md) e [4](../../01-teoria/04-efficienza.md), poi gli [Esercizi 3-4](../../03-esercizi/03-base-resistenza-atr.md).
3. **Errori su ISA/Reynolds**: ripassa [Lezione 5](../../01-teoria/05-atmosfera-isa.md) e [6](../../01-teoria/06-numero-reynolds.md).
4. **Errori su geometria/centraggio/flap**: ripassa [Lezioni 7-9](../../01-teoria/07-geometria-alare.md).
5. **Per mettere alla prova**: chiedi a Claude nel Project di **generare 5 nuove domande** sull'argomento più debole.

> 🎓 **Memoria spaziata**: ripeti questo quiz tra 1 settimana, poi tra 2 settimane, poi tra 1 mese. È il modo dimostrato per fissare i concetti a lungo termine.
