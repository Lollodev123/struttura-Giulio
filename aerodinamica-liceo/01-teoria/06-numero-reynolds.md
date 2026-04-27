# Lezione 6 — Numero di Reynolds

> **Obiettivo**: alla fine di questa lezione sai cos'è il numero di Reynolds, calcolarlo per qualsiasi corpo in un flusso, distinguere flusso laminare e turbolento, e capire perché un modellino in galleria del vento ha *un altro mondo* aerodinamico rispetto al Boeing 737 reale.

---

## 🎯 In una riga

Il **numero di Reynolds** $Re$ è un **numero adimensionale** che ti dice se in una situazione data l'aria si comporta da fluido "tranquillo" (laminare) o "agitato" (turbolento). È il rapporto tra forze d'inerzia e forze viscose.

$$Re = \frac{\rho V c}{\mu}$$

---

## ✈️ A cosa serve davvero

Il Reynolds determina **la natura stessa del flusso**:

- **Re basso** → forze viscose dominano → flusso **laminare** (strati ordinati di aria che scorrono uno sull'altro)
- **Re alto** → forze d'inerzia dominano → flusso **turbolento** (vortici caotici, mescolamento)

Da questa "natura" dipende **tutto** in aerodinamica:

- Il coefficiente di resistenza ($C_D$ varia anche del 50% tra laminare e turbolento)
- Il punto di stallo (a $Re$ basso, lo stallo arriva prima)
- L'aderenza del flusso al profilo
- L'efficacia di flap e slat

> 💡 **Vita reale**: una farfalla, un Cessna 172, e una pallina da ping pong vivono in regimi di Re completamente diversi. È per questo che le ali di una farfalla sono fatte come carta accartocciata e quelle del Cessna sono lisce — quello che funziona a un Re non funziona all'altro.

---

## 📐 La formula — un solo numero, quattro pezzi

$$Re = \frac{\rho V c}{\mu}$$

| Simbolo | Significato | Unità SI |
|---|---|---|
| $\rho$ | Densità del fluido | kg/m³ |
| $V$ | Velocità relativa | m/s |
| $c$ | **Lunghezza caratteristica** del corpo | m |
| $\mu$ | Viscosità dinamica del fluido | Pa·s (= kg/(m·s)) |

**Per l'aria a 15°C**: $\mu \approx 1{,}78 \times 10^{-5}$ Pa·s. Questo numero **lo memorizzi**, è quello che userai sempre.

### Cos'è "lunghezza caratteristica"?
Dipende da cosa stai studiando:

- Per un'**ala**: la **corda** (avanti-indietro)
- Per una **palla**: il **diametro**
- Per un **tubo**: il **diametro interno**
- Per un'**auto**: la lunghezza totale

Devi sempre chiarire qual è la lunghezza che usi, perché due Re calcolati con $c$ diverse non sono confrontabili.

> ⚠️ **Errore comune**: confondere la corda dell'ala con l'apertura alare. Per il Reynolds di un velivolo si usa **la corda media**, mai l'apertura.

---

## 🌊 Le 3 "zone" del Reynolds — laminare, transizione, turbolento

**Le 3 zone di Reynolds**, con esempi reali:

| Re tipico | Regime | Esempi reali |
|---|---|---|
| $10^4$ | **Laminare** | Insetti, aeromodelli piccoli |
| $10^5$ | **Transizione** | Modello in galleria del vento, ali piccole |
| $10^6$ | **Turbolento** | Cessna, ATR in volo |
| $10^7$ | **Turbolento sviluppato** | Liner in crociera (737, A320) |

**Soglie indicative** (per profilo alare):

| Regime | Range $Re$ | Caratteristiche |
|---|---|---|
| **Laminare** | $< 5 \cdot 10^5$ | Strati ordinati. Bassa resistenza. Ma: il flusso si stacca facilmente → stallo precoce |
| **Transizione** | $\sim 5 \cdot 10^5$ | Zona instabile, dove il flusso passa da laminare a turbolento. Punto di transizione si sposta avanti col $Re$ |
| **Turbolento** | $> 5 \cdot 10^5$ | Vortici, mescolamento. Resistenza maggiore ma flusso *aderisce meglio* al profilo → stallo più "morbido", $C_{L,max}$ più alto |

**Paradosso utile**: il flusso turbolento ha **più resistenza** ma anche **più portanza** (perché stalla più tardi). I profili moderni cercano un compromesso.

---

## ✈️ Calcolo del Reynolds per velivoli reali

### Cessna 172 in crociera al livello mare
- $\rho = 1{,}225$ kg/m³
- $V = 62{,}76$ m/s (122 kt)
- $c = 1{,}49$ m (corda media del Cessna)
- $\mu = 1{,}78 \cdot 10^{-5}$ Pa·s

$$Re = \frac{1{,}225 \cdot 62{,}76 \cdot 1{,}49}{1{,}78 \cdot 10^{-5}} = \frac{114{,}5}{1{,}78 \cdot 10^{-5}} \approx 6{,}4 \cdot 10^6$$

Re ~6 milioni: pienamente **turbolento**, regime tipico per aviazione generale.

### ATR 72 in crociera
- $V \approx 140$ m/s, $c \approx 2{,}3$ m, $\rho \approx 0{,}55$ kg/m³ (in quota 7000 m)
- $Re = (0{,}55 \cdot 140 \cdot 2{,}3) / (1{,}78 \cdot 10^{-5}) \approx 1{,}0 \cdot 10^7$ → 10 milioni, turbolento netto.

### Boeing 737 in crociera FL350
- $V \approx 230$ m/s, $c \approx 4$ m, $\rho \approx 0{,}38$ kg/m³
- $Re \approx (0{,}38 \cdot 230 \cdot 4) / (1{,}78 \cdot 10^{-5}) \approx 1{,}96 \cdot 10^7$ → 20 milioni!

### Modello del Cessna in galleria del vento (scala 1:10)
- $V = 30$ m/s (galleria a bassa velocità), $c = 0{,}15$ m (corda scalata)
- $Re \approx (1{,}225 \cdot 30 \cdot 0{,}15) / (1{,}78 \cdot 10^{-5}) \approx 3 \cdot 10^5$

→ Re del modello = **20 volte più piccolo** del velivolo reale. **Il modello vive in un regime quasi laminare**, mentre il vero Cessna è turbolento. **Questo è il dramma delle gallerie del vento a bassa velocità**: senza accorgimenti, i risultati del modello non rappresentano il vero velivolo.

> 💡 **Soluzioni reali**: gallerie pressurizzate (aumentano $\rho$ → aumentano $Re$), gallerie criogeniche (riducono $\mu$ con azoto liquido a -190°C), o accettare il limite e correggere a posteriori.

### Una farfalla
- $V = 2$ m/s, $c = 0{,}03$ m (3 cm di apertura alare)
- $Re \approx (1{,}225 \cdot 2 \cdot 0{,}03) / (1{,}78 \cdot 10^{-5}) \approx 4\,000$

→ $Re = 4000$, regime **fortemente laminare**. La farfalla è in un altro pianeta aerodinamico: per lei l'aria è "viscosa" come olio per noi. Per questo le sue ali non sono lisce ma "rugose" — funziona meglio così a quel $Re$.

---

## 🎯 Box "Da ricordare per l'interrogazione"

> 1. **$Re = \rho V c / \mu$**, adimensionale.
> 2. Per **aria a 15°C**: $\mu = 1{,}78 \cdot 10^{-5}$ Pa·s. Memorizza questo numero.
> 3. **$Re < 5 \cdot 10^5$** → laminare. **$> 5 \cdot 10^5$** → turbolento.
> 4. Velivoli reali sono **sempre** in turbolento ($Re$ tra $10^6$ e $10^8$).
> 5. **Lunghezza caratteristica** = corda dell'ala (per profili). Mai l'apertura.
> 6. **Il modello in galleria** ha $Re$ molto più basso del velivolo reale — non è confrontabile direttamente.
> 7. Turbolento = più resistenza MA stallo più morbido e $C_{L,max}$ maggiore.

---

## ⚠️ Errori comuni

❌ **Usare l'apertura alare invece della corda**. Sbagliato: per il Reynolds di un'ala, la lunghezza caratteristica è la **corda media**. Apertura non c'entra (quella entra in $\lambda$, allungamento).

❌ **Dimenticare l'unità di $\mu$**. $\mu$ ha le unità di **Pa·s**, equivalenti a **kg/(m·s)**. Se confondi $\mu$ con la viscosità cinematica $\nu = \mu/\rho$ (che ha unità m²/s), il Reynolds viene sballato di ~$\rho$ → tre ordini di grandezza errati.

❌ **Confondere viscosità dinamica e cinematica**. $\mu$ (dinamica) è una proprietà del solo fluido. $\nu$ (cinematica) dipende anche dalla densità: $\nu = \mu/\rho$. Per l'aria a 15°C, $\nu \approx 1{,}45 \cdot 10^{-5}$ m²/s. Si può scrivere anche $Re = V c/\nu$.

❌ **Pensare che il $Re$ critico sia esattamente $5 \cdot 10^5$**. È un valore **indicativo** per profili lisci. Su superfici rugose o con strato limite tripped (volutamente disturbato) la transizione avviene prima. Su profili laminari speciali, può ritardarsi fino a $Re = 2 \cdot 10^6$.

❌ **Trascurare l'effetto di $\rho$ in quota**. In alta quota $\rho$ scende, quindi $Re$ scende a parità di V e c. A 11 000 m il Reynolds di un'ala è circa **30%** di quello al livello mare alla stessa V → potresti uscire dal regime turbolento "comodo" in zone di transizione delicate.

❌ **Pensare che laminare = sempre meglio**. Non è vero: laminare ha meno resistenza, ma stallo precoce e meno tollerante a sporco. Per piccoli aerei e alianti laminari, una mosca schiacciata sul bordo d'attacco può ridurre $E_{max}$ del 20%.

---

## 🧠 Domande di autoverifica

1. Calcola il numero di Reynolds di un Piper PA-28 (corda 1,4 m) in volo a 110 kt al livello mare ISA.
2. A 10 000 m, lo stesso Cessna 172 a 122 kt: il suo Reynolds è maggiore o minore di quello al livello mare? Di quanto, percentualmente?
3. Una pallina da ping pong (diametro 4 cm) lanciata a 20 m/s: in che regime è? Laminare, transizione, turbolento?
4. Perché i profili NACA serie 6 (laminari, P-51 Mustang) richiedono superfici impeccabili?
5. Una galleria del vento ha velocità massima 50 m/s. Voglio testare un'ala di Cessna a $Re$ di volo ($6 \cdot 10^6$). Qual è la corda minima del modello, supponendo aria standard?

<details markdown="1">
<summary>👉 Risposte</summary>

1. $V = 110 \cdot 0{,}5144 = 56{,}6$ m/s. $Re = (1{,}225 \cdot 56{,}6 \cdot 1{,}4)/(1{,}78 \cdot 10^{-5}) = 97{,}1/(1{,}78 \cdot 10^{-5}) \approx 5{,}45 \cdot 10^6$. **Re ~5,5 milioni, turbolento**.

2. **Minore**, di circa il **66%**. A 10 000 m $\rho \approx 0{,}413$ vs 1,225 al mare: rapporto 0,34. Quindi $Re_{quota} \approx 0{,}34 \cdot Re_{mare}$. Per il Cessna: $Re_{mare} = 6{,}4 \cdot 10^6 \Rightarrow Re_{quota} \approx 2{,}2 \cdot 10^6$ (sempre turbolento, ma "meno"). Avere meno Re può significare un punto di transizione più avanti, performance leggermente diverse.

3. $Re = (1{,}225 \cdot 20 \cdot 0{,}04)/(1{,}78 \cdot 10^{-5}) = 0{,}98/(1{,}78 \cdot 10^{-5}) \approx 5{,}5 \cdot 10^4 = 55\,000$. **Regime in transizione bassa, tendente al laminare**. Una pallina da ping pong è notoriamente "instabile" in volo proprio perché vive nella zona di transizione: piccoli cambi di rugosità o scia possono cambiare drasticamente la sua resistenza. Ricerca "drag crisis" per approfondire.

4. Perché su un profilo laminare il **flusso resta laminare per gran parte del dorso** solo se la superficie è perfettamente liscia. Insetti, sporcizia, ghiaccio o gocce di pioggia "innescano" la transizione precoce a turbolento. Risultato: la resistenza sale di colpo (anche del 30%) e l'efficienza crolla. Per questo le squadriglie di P-51 lavavano e lucidavano le ali ogni missione.

5. $Re = \rho V c / \mu \Rightarrow c = Re \cdot \mu / (\rho V)$. Con $Re = 6 \cdot 10^6$, $\mu = 1{,}78 \cdot 10^{-5}$, $\rho = 1{,}225$, $V = 50$:
   $c = (6 \cdot 10^6 \cdot 1{,}78 \cdot 10^{-5}) / (1{,}225 \cdot 50) = 106{,}8 / 61{,}25 \approx 1{,}74$ m.
   **Corda del modello ≥ 1,74 m** — circa la stessa del Cessna reale (1,49 m)! In pratica significa che con questa galleria a 50 m/s puoi testare solo modelli quasi a grandezza naturale, oppure devi pressurizzare la galleria per aumentare $\rho$. È il classico problema delle gallerie a bassa velocità.

</details>

---

## ➡️ Prossimo passo

Vai a [Lezione 7 — Geometria alare](./07-geometria-alare.md) per vedere come l'allungamento (che hai già incontrato in resistenza ed efficienza) si combina con altri parametri 3D dell'ala.

Oppure [Esercizio 7 — Reynolds e regime di flusso](../03-esercizi/07-medio-reynolds.md) 🚧 per esercitarti.
