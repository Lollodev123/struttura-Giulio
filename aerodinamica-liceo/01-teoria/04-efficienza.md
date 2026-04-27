# Lezione 4 — Efficienza aerodinamica e polare

> **Obiettivo**: alla fine di questa lezione sai cos'è $E = C_L/C_D$, perché esiste un valore massimo $E_{max}$, come leggere la polare di un velivolo, e come calcolare la distanza in planata di un aliante.

---

## 🎯 In una riga

L'**efficienza aerodinamica** $E$ è il rapporto tra portanza e resistenza: misura **quanti newton di portanza ottieni per ogni newton di resistenza pagato**. Più alta è $E$, più il velivolo "vola economico".

$$E = \frac{L}{D} = \frac{C_L}{C_D}$$

---

## ✈️ A cosa serve davvero

L'efficienza è il **parametro singolo più importante** del progetto aeronautico. Da sola ti dice:

- Quanti chilometri puoi percorrere con un litro di carburante (autonomia)
- Quanto in alto puoi salire (tangenza pratica)
- A che velocità ti conviene volare per consumare meno
- **In planata (motore spento), quanto sei lontano dall'aeroporto** quando perdi 1000 m di quota

> 💡 **Numero da ricordare**: efficienza tipica di un Cessna 172 ≈ **10**. Significa che in planata, da 1000 m di quota, puoi percorrere **10 km** prima di toccare terra. Per un aliante moderno ($E \approx 40$), **40 km**.

---

## 📐 La formula della planata — cuore di tutto

In **planata stabilizzata** (motore spento, discesa a velocità costante), il velivolo si muove lungo una traiettoria inclinata di un angolo $\gamma$ (gamma) rispetto all'orizzontale. Le forze in gioco sono solo tre: portanza, resistenza, peso.

```
      ←── distanza percorsa (orizzontale) ───→
                                                
       ╲                                          
        ╲ ←── traiettoria di planata               ↑
         ╲                                          │
          ╲                                          │ quota
           ╲                                          │ persa
            ╲                                          │
              ●  velivolo                              ↓
              
                  γ = angolo di planata (rispetto all'orizzontale)
```

La matematica del liceo arriva a questa relazione:

$$\tan(\gamma) = \frac{1}{E}$$

→ **se $E$ è grande, $\gamma$ è piccolo, planata "lunga"**.

E direttamente:

$$\boxed{\text{distanza orizzontale} = E \times \text{quota persa}}$$

| Velivolo | $E_{max}$ | Distanza in planata da 1000 m |
|---|---|---|
| Cessna 172 | ~10 | 10 km |
| Boeing 737 (motori spenti) | ~17 | 17 km |
| ATR 72 | ~14 | 14 km |
| Aliante ASK-21 | ~33 | 33 km |
| Aliante moderno (DG-1000, ASG-29) | 50–60 | 50–60 km |
| Albatros (uccello — sì, è meglio dell'ASK-21) | ~25 | 25 km |

---

## 📊 La polare di velivolo — l'identikit aerodinamico

La **polare** è il grafico $C_L$ vs $C_D$. Ogni punto rappresenta una specifica condizione di volo (quindi specifica $\alpha$, velocità, etc.).

```
   C_L
    │                      
 1,5│              ╱╲   ←─── stallo
    │            ╱   ╲___
 1,0│         ╱           ●  ←── massima C_L (atterraggio)
    │      ╱
 0,5│  ●─── tangente passa qui  ←── E_max (planata ottima)
    │ ╱
 0,0●────────────────────────── C_D
    │   0,02  0,04   0,06
```

**Lettura**: la **tangente alla polare passante per l'origine** tocca la curva nel punto di **massima efficienza** $E_{max}$. È il punto da cui la pendenza $C_L/C_D$ è massima.

> 💡 **Trucco grafico**: per trovare $E_{max}$ su una polare, traccia una retta dall'origine e ruotala verso la curva. Quando "tocca" la curva (tangenza), quello è il punto di efficienza massima. Il $C_L$ corrispondente si chiama $C_L^*$.

---

## 🔢 Calcolo di $E_{max}$ — formula del liceo

Dalla lezione precedente, $C_D = C_{D,0} + \dfrac{C_L^2}{\pi \lambda e}$. L'efficienza è $E = C_L/C_D$. Massimizzare $E$ rispetto a $C_L$ porta a:

$$C_L^* = \sqrt{\pi \lambda e \cdot C_{D,0}}$$

$$\boxed{E_{max} = \frac{1}{2} \sqrt{\frac{\pi \lambda e}{C_{D,0}}}}$$

A questo punto **resistenza parassita = resistenza indotta** (entrambe valgono $C_{D,0}$). Il $C_D$ totale è $2 \, C_{D,0}$.

> ⚠️ **Niente derivate per il liceo** — ma la formula $E_{max}$ è da tenere a mente, è di una semplicità impressionante: dipende solo da **allungamento alare**, **fattore di Oswald**, e **resistenza parassita**.

---

## ✈️ Calcoli su velivoli reali

### Cessna 172
- $\lambda = 7{,}5$, $e = 0{,}8$, $C_{D,0} = 0{,}028$
- $C_L^* = \sqrt{\pi \cdot 7{,}5 \cdot 0{,}8 \cdot 0{,}028} = \sqrt{0{,}528} \approx 0{,}73$
- $E_{max} = \frac{1}{2}\sqrt{\dfrac{\pi \cdot 7{,}5 \cdot 0{,}8}{0{,}028}} = \frac{1}{2}\sqrt{673} \approx 12{,}96$

→ massima efficienza ~13. Il manuale di volo del Cessna 172 dichiara $E_{max}$ effettivo ~10 (la formula sovrastima perché trascura interferenze e attrito a bassa Re). **Velocità di max efficienza** ≈ 65 kt.

### Aliante ASK-21
- $\lambda = 23$, $e = 0{,}9$, $C_{D,0} = 0{,}015$
- $C_L^* = \sqrt{\pi \cdot 23 \cdot 0{,}9 \cdot 0{,}015} = \sqrt{0{,}975} \approx 0{,}99$
- $E_{max} = \frac{1}{2}\sqrt{\dfrac{\pi \cdot 23 \cdot 0{,}9}{0{,}015}} = \frac{1}{2}\sqrt{4335} \approx 33$

→ efficienza massima ~33. **Distanza in planata da 1000 m: 33 km**. Velocità di max efficienza ≈ 50 kt.

### Boeing 737 (in caso di doppia avaria motori — ipotesi rara ma analizzabile)
- $\lambda = 9$, $e = 0{,}85$, $C_{D,0} = 0{,}025$
- $E_{max} \approx \frac{1}{2}\sqrt{\dfrac{\pi \cdot 9 \cdot 0{,}85}{0{,}025}} = \frac{1}{2}\sqrt{961} \approx 15{,}5$

→ a livello mare, dichiarato ~17 (il modello ideale sottostima questa volta). **Da 10 000 m, 737 può planare ~170 km** in caso di doppia avaria. Esempio reale: il *Gimli Glider* (Air Canada 143, 1983), un Boeing 767 rimasto senza carburante a 12 000 m, planò 100+ km e atterrò su una pista abbandonata.

---

## 📐 Velocità di massima efficienza ($V^*$)

A $C_L^*$ corrisponde una specifica velocità di volo:

$$V^* = \sqrt{\dfrac{2 W}{\rho S C_L^*}}$$

(stessa formula della $V_S$ ma con $C_L^*$ invece di $C_{L,max}$).

**Per il Cessna 172** in crociera al livello mare:
$V^* = \sqrt{\dfrac{2 \cdot 10\,232}{1{,}225 \cdot 16{,}2 \cdot 0{,}73}} \approx \sqrt{1\,413} \approx 37{,}6$ m/s ≈ **73 kt**.

→ Il Cessna è "più economico" se vola a 73 kt, non a 122 kt (la velocità di crociera). La crociera nominale a 122 kt è scelta per **arrivare prima**, non per consumare meno. Se devi affrontare un volo di emergenza con poco carburante, riduci a 70-75 kt.

---

## 🎯 Box "Da ricordare per l'interrogazione"

> 1. **$E = C_L/C_D = L/D$** — efficienza è un **rapporto adimensionale**, non una forza.
> 2. **In planata: distanza = $E \times$ quota persa**. È la formula più utile della lezione.
> 3. **Velocità di max efficienza ≠ velocità di crociera**. Quasi sempre la prima è più bassa (~70 kt per Cessna, ~50 kt per aliante).
> 4. **$E_{max} = \frac{1}{2}\sqrt{\pi \lambda e / C_{D,0}}$** — dipende SOLO da geometria alare (λ), distribuzione portanza (e), e parassita.
> 5. **A $E_{max}$**, parassita = indotta. Significa: minore parassita o maggiore allungamento → efficienza maggiore.
> 6. **Polari diverse = velivoli diversi**: confronta i grafici per capire l'identità aerodinamica.

---

## ⚠️ Errori comuni

❌ **Pensare che efficienza = velocità**. Sono cose distinte. Un caccia ha $E_{max} \approx 8$ ma $V_{max} \approx 2000$ km/h; un aliante ha $E_{max} \approx 50$ ma $V_{max} \approx 250$ km/h. L'efficienza non c'entra con quanto vai veloce, ma con quanto sei *economico*.

❌ **Calcolare la distanza di planata col $V_{max}$**. La formula `dist = E × quota` vale a $E_{max}$ — quindi alla velocità $V^*$, NON al $V_{max}$. Se vai più veloce o più lento di $V^*$, planari di meno.

❌ **Dimenticare che $E$ varia con la configurazione**. Flap fuori = $E$ crolla (5–6 invece di 10). Carrello fuori = $E$ scende. La $E_{max}$ è "ala pulita".

❌ **Confondere $E_{max}$ con efficienza in crociera**. In crociera reale (alta velocità) il velivolo NON è a $E_{max}$. Vola a un compromesso tra velocità e consumo.

❌ **Pensare che il fattore di Oswald $e$ sia sempre 1**. Vale 1 solo per l'ala ideale ellittica (Spitfire). Per la maggior parte degli aerei è 0,7–0,9.

---

## 🧠 Domande di autoverifica

1. Un aliante con $E_{max} = 40$ vola a 1500 m sopra il punto di atterraggio. Senza vento e in aria calma, quanti km può percorrere prima di toccare terra?
2. Un Cessna 172 ha $E_{max} \approx 10$. In caso di avaria motore a 600 m sopra l'aeroporto, può raggiungere una pista a 7 km di distanza? E a 5 km?
3. Tra due velivoli identici tranne l'allungamento alare ($\lambda_A = 8$, $\lambda_B = 16$), quale ha efficienza massima più alta? Di che fattore, approssimativamente?
4. Perché il pilota di Gimli Glider (B767 senza carburante) ha pianificato di volare a circa **220 kt**, non alla velocità di crociera del 767 (~480 kt)?
5. Per un Cessna 172 con $C_L^* = 0{,}73$ in volo livellato al livello mare, calcola la velocità di massima efficienza in nodi.

<details markdown="1">
<summary>👉 Risposte</summary>

1. **60 km**. Distanza = $E \times$ quota = $40 \times 1{,}5$ km = 60 km. (Se c'è vento contrario, di meno; se in coda, di più — la formula vale in aria calma.)

2. **A 7 km, no**: il Cessna ha portata massima in planata da 600 m = $10 \times 0{,}6 = 6$ km. **A 5 km, sì**, con margine. Da qui il consiglio dei manuali: in caso di motore in avaria, *cerca subito la pista più vicina dentro un cerchio di raggio = quota × E*. Conoscere $E$ è una **questione di vita o morte**.

3. **B ha $E_{max}$ maggiore**, di un fattore $\sqrt{\lambda_B/\lambda_A} = \sqrt{2} \approx 1{,}41$. Raddoppi l'allungamento → efficienza × 1,41. È il motivo per cui gli alianti hanno $\lambda$ enorme: è la leva più potente per aumentare $E_{max}$ a parità di tutto il resto.

4. Perché 480 kt è la velocità di **crociera** (alta), in cui parassita domina e $E$ è inferiore al massimo. La velocità di **massima efficienza** del 767 è circa 220-240 kt (a peso medio). Volando a $V^*$, il pilota ha massimizzato la distanza percorribile per ogni metro di quota persa — esattamente quello che serviva per arrivare a Gimli da 12 000 m senza propulsione.

5. $V^* = \sqrt{\dfrac{2W}{\rho S C_L^*}} = \sqrt{\dfrac{2 \cdot 10232}{1{,}225 \cdot 16{,}2 \cdot 0{,}73}} = \sqrt{1413} \approx 37{,}6$ m/s. Conversione: $37{,}6 / 0{,}5144 \approx 73$ kt. **Risposta: ~73 kt**, ben sotto i 122 kt di crociera. Il manuale POH del Cessna 172 dichiara $V_{best\,glide}$ = **68 kt** (a peso medio), molto vicino al nostro calcolo.

</details>

---

## ➡️ Prossimo passo

Vai a [Lezione 5 — Atmosfera Standard ISA](./05-atmosfera-isa.md) per capire come la densità $\rho$ (presente in tutte le formule fin qui) cambia con la quota.

Oppure prova [Esercizio 4 — Efficienza massima (aliante ASK-21)](../03-esercizi/04-medio-efficienza-aliante.md) 🚧.
