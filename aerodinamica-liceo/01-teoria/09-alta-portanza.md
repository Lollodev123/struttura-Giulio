# Lezione 9 — Dispositivi di alta portanza

> **Obiettivo**: alla fine di questa lezione sai a cosa servono flap e slat, distinguere i 4 tipi principali di flap, calcolare l'effetto sul $C_{L,max}$ e capire perché un Boeing 737 ha quel sistema complesso di superfici mobili sotto le ali.

---

## 🎯 In una riga

I **dispositivi di alta portanza** (flap, slat, slot) sono **superfici mobili dell'ala** che si dispiegano in decollo e atterraggio per **aumentare $C_{L,max}$** e permettere di volare a velocità più basse senza stallare.

---

## ✈️ A cosa serve davvero

Hai visto in [Lezione 4](./04-efficienza.md) che la velocità di stallo è:

$$V_S = \sqrt{\frac{2 W}{\rho \cdot S \cdot C_{L,max}}}$$

Per **atterrare in sicurezza** servono velocità basse: una pista standard è 1500–3000 m, e a 250 kt non frenerebbe nessun aereo. Ma ridurre la velocità troppo significa entrare in stallo.

**L'unico modo per ridurre $V_S$**, a parità di peso e densità (quindi stessa pista, stesso giorno):

- Aumentare $S$ (la superficie alare) → **flap Fowler** lo fanno scivolando indietro
- Aumentare $C_{L,max}$ → **flap, slat, slot** lo fanno aumentando la curvatura del profilo e ritardando lo stallo

Esempio: Boeing 737 al peso massimo di atterraggio.

- **Senza flap**: $C_{L,max} \approx 1{,}3$ → $V_S \approx 95$ m/s = 185 kt — pista enorme, frenata impossibile
- **Flap pieni (40°)**: $C_{L,max} \approx 2{,}8$ → $V_S \approx 65$ m/s = 126 kt — atterrabile

Senza flap, **non ci sarebbero aeroporti urbani**.

---

## 📐 I 4 tipi di flap — dal più semplice al più sofisticato

### 1. Flap semplice (plain flap)
La parte posteriore dell'ala ruota verso il basso, come un'aletta.

```
   ──────────────╲    ←── flap esteso
                  ╲___
   
   Effetto: aumenta curvatura → +20% C_L,max
   Aerei: ultraleggeri, primi modelli (anni '30)
```

- Aumento di $C_{L,max}$: ~$+0{,}3$ (da 1,2 a 1,5)
- Aumento di $C_D$: significativo (resistenza extra)
- **Cessna 172 → flap semplici a 3 posizioni** (10°, 20°, 30°)

### 2. Flap a doppia/tripla fessura (slotted flap)
Quando il flap si abbassa, **lascia una fessura** tra ala e flap. L'aria ad alta pressione del ventre passa attraverso, energizzando lo strato limite sul dorso del flap → **ritarda lo stallo**.

```
   ──────────────  ← apertura della fessura
                ╲___
                    ────  ← flap con fessura
   
   Effetto: +50-70% C_L,max
   Aerei: aviazione generale moderna, regionali
```

- Aumento di $C_{L,max}$: ~$+0{,}6$–$0{,}8$
- $C_D$ moderato

### 3. Flap Fowler (extended)
Il flap **scivola indietro** lungo binari prima di abbassarsi → **aumenta sia la superficie alare $S$ che la curvatura**.

```
   ──────────────              ──────────  ← flap retratto
                  ─────────
   
   ↓ in atterraggio:
   
   ───────                                ←── ala
                  ─────────────────────  ←── flap esteso, scivolato indietro
   
   Effetto: +80-100% C_L,max e aumento S del 15-25%
   Aerei: jet di linea (737, A320, 777)
```

- Aumento di $C_{L,max}$: ~$+1{,}0$–$1{,}2$ (da 1,4 a 2,4-2,6)
- **Aumenta anche $S$** → effetto cumulativo sulla portanza
- Sistema meccanico complesso (binari, attuatori), pesante

### 4. Sistema multi-flap (Fowler + multi-slot)
Combinazione di Fowler con due o tre flap consecutivi, ciascuno con la sua fessura. Massima sofisticazione.

```
   ───────                                     
              ────                            
                   ────                       
                        ────                  ← 3 flap a fessura tipo Fowler
   
   Effetto: +120% C_L,max, S +30%
   Aerei: 747, A380, alcuni AV (V-22, c-17)
```

- $C_{L,max}$ può raggiungere **2,8–3,5** in atterraggio
- Sistema mostruosamente complesso: A380 ha 6 superfici mobili per lato

---

## 🪶 Slat e slot — al bordo d'attacco

Mentre i flap stanno **al bordo d'uscita**, slat e slot stanno **al bordo d'attacco**:

### Slat
Una superficie mobile che si estende **avanti e in basso**, creando una fessura sopra il bordo d'attacco. **Energizza lo strato limite** sul dorso → l'ala può lavorare a $\alpha$ molto maggiori senza stallare.

```
   ●───────  ←── ala normale
   
   ↓ con slat estesa:
   
       ●─────  ←── slat avanti
        ↓ fessura
   ●───────   ←── ala
```

**Effetto principale**: aumenta l'angolo di stallo $\alpha_{stallo}$ da ~16° a ~22-25°.

**Aerei**: tutti i jet di linea moderni hanno slat. Cessna 172 NO (non gli serve, atterra già lentamente).

### Slot fisso
Versione **non mobile**: un'apertura permanente al bordo d'attacco. Storica, oggi rara perché aumenta $C_D$ in crociera.

**Aerei famosi con slot fissi**: Fieseler Storch (Fi-156, decollo in 60 m), Helio Courier.

---

## 📊 Effetto cumulativo — la curva $C_L$-$\alpha$ con flap

![Curva CL-alpha confronto: ala pulita, con flap, con flap+slat](../assets/img/grafici/curva-cl-flap-slat.svg)

**Lettura**: flap aumentano il $C_L$ a ogni $\alpha$ (sposta la curva in alto, da blu a verde a rosso), slat estendono $\alpha$ di stallo (sposta il picco a destra: da 16° pulito a 22° con slat). Insieme, **multiplicano l'effetto**: $C_{L,max}$ raddoppia, da 1,4 (pulito) a 2,8 (flap+slat).

---

## 🏗️ Configurazioni tipiche di volo

| Fase | Flap | Slat | Velocità tipica (737) |
|---|---|---|---|
| Crociera | Retratto (0°) | Retratti | 230 m/s (Mach 0,78) |
| Decollo | 5°–15° (T/O setting) | Estesi | 80 m/s (155 kt) |
| Salita iniziale | 5° | Estesi | 100 m/s (195 kt) |
| Approccio | 25°–30° | Estesi | 75 m/s (145 kt) |
| Atterraggio | **40° (full flaps)** | Estesi | 65 m/s (126 kt) |
| Go-around (riattaccata) | 15° | Estesi | 80 m/s (155 kt) |

> ⚠️ **Velocità massima con flap (V_FE)**: tutti i flap hanno una velocità massima oltre la quale **si rompono**. Per il Cessna 172, $V_{FE}$ flap pieni = 85 kt. Per il 737, $V_{FE}$ flap 40° = 158 kt. Estendere flap ad alta velocità = danno strutturale immediato.

---

## ✈️ Esempi reali

### Cessna 172 in atterraggio
- Flap a 30° (massimo): $C_{L,max}$ passa da 1,5 (pulita) a ~2,1
- $V_S$ scende da 51 kt a 41 kt (–20%)
- Velocità di approccio standard $V_{ref}$ = 1,3 × $V_S$ ≈ 53 kt

### Boeing 737-800 in atterraggio (peso 65 t)
- Flap 40° + slat: $C_{L,max} \approx 2{,}8$
- $\rho_0 = 1{,}225$, $S = 124{,}6$ m², $W = 65000 \cdot 9{,}81 = 637\,650$ N
- $V_S = \sqrt{(2 \cdot 637\,650)/(1{,}225 \cdot 124{,}6 \cdot 2{,}8)} = \sqrt{2987} \approx 54{,}7$ m/s ≈ 106 kt
- $V_{ref}$ = 1,3 × $V_S$ ≈ 138 kt — coerente con i tipici 130-145 kt all'atterraggio.

### A380 — il pesce d'aprile dei flap
Sistema più complesso al mondo: flap multi-fessura su 3 superfici per lato + slat su 8 superfici per lato. Permette al gigante (peso atterraggio 390 t!) di toccare a 145 kt.

---

## 🎯 Box "Da ricordare per l'interrogazione"

> 1. **Flap = bordo d'uscita; slat = bordo d'attacco**.
> 2. **4 tipi di flap**: plain, split, slotted, Fowler. Ognuno aumenta $C_{L,max}$ di ~$+0{,}3$, $+0{,}5$, $+0{,}7$, $+1{,}0$ rispettivamente.
> 3. **Fowler aumenta anche la superficie alare $S$** (scivola indietro), oltre alla curvatura.
> 4. **Slat ritarda lo stallo** (estende l'angolo critico da 16° a 22-25°).
> 5. **Tutto questo costa resistenza**: i flap aumentano molto il $C_D$. Volare con flap fuori in crociera = consumo +30-50%.
> 6. **Velocità massima con flap ($V_{FE}$)** è un limite strutturale assoluto. Mai superarlo.
> 7. **Cessna 172 ha solo flap semplici** (basta per atterrare a ~50 kt). **Liner ha flap+slat sofisticati** perché vola pesante.

---

## ⚠️ Errori comuni

❌ **Pensare che flap = stallo evitato**. Falso: i flap **abbassano la velocità di stallo** ma se voli sotto la nuova $V_S$ stalli comunque. Lo stallo dipende sempre dall'angolo di attacco.

❌ **Estendere flap ad alta velocità**. Conseguenze: strappi strutturali, fessurazioni, perdita di controllo. È uno degli errori più gravi che un pilota possa fare. Su jet di linea c'è il "flap warning system" che bloccare il movimento se la velocità è troppo alta.

❌ **Confondere flap e ipersostentatori in generale**. "Ipersostentatori" è il termine italiano per high-lift devices, che include flap, slat E slot. Flap = solo quelli al bordo d'uscita.

❌ **Pensare che i flap aumentino solo la portanza**. Aumentano sia $C_L$ che $C_D$. Il rapporto $C_L/C_D$ (efficienza) **scende**. Per questo non si usano in crociera.

❌ **Dimenticare di estrarre i flap in atterraggio**. Conseguenza: velocità di toccata troppo alta, pista insufficiente. Un classico nei voli delle scuole di volo: piloti distratti che atterrano "puliti".

❌ **Estrarre flap senza compensare il trim**. I flap modificano il momento dell'ala → l'aereo cabra o picchia improvvisamente. Va dosato il trim simultaneamente.

---

## 🧠 Domande di autoverifica

1. Senza flap, $C_{L,max} = 1{,}4$. Con flap pieni, $C_{L,max} = 2{,}5$. Di quanto si riduce la velocità di stallo, in percentuale?
2. Un pilota di Cessna 172 si ricorda di estrarre i flap solo a 100 kt (limite $V_{FE}$ = 85 kt). Cosa rischia?
3. Perché i jet di linea hanno **slat** ma il Cessna 172 no?
4. Con flap pieni e slat estesi, l'angolo di stallo passa da 16° a 23°. È un vantaggio in atterraggio?
5. Calcola la velocità di stallo $V_S$ di un ATR 72 al peso massimo (22500 kg, $S = 61$ m²) in atterraggio con flap pieni ($C_{L,max} = 2{,}5$) al livello mare.

<details markdown="1">
<summary>👉 Risposte</summary>

1. $V_S \propto 1/\sqrt{C_{L,max}}$. Rapporto: $\sqrt{1{,}4/2{,}5} = \sqrt{0{,}56} \approx 0{,}748$. La velocità di stallo con flap è il **74,8%** di quella pulita → riduzione del **25,2%**.

2. **Strappo strutturale**: l'aereo è progettato per un certo carico aerodinamico sui flap fino a 85 kt. A 100 kt le forze sono $(100/85)^2 \approx 1{,}38$ → **38% in più di carico** sui flap rispetto al limite. Possibili: deformazione permanente, fessurazione del cassone alare, distacco totale del flap. Un Cessna 172 in fase di estensione flap a velocità eccessiva può perdere un flap → asimmetria di portanza → cappottamento immediato. Esistono casi documentati di NTSB.

3. Perché il Cessna **non vola pesante e non vola veloce**. La sua $V_S$ pulita è già ~50 kt (atterrabile su qualsiasi pista). Il jet di linea ha $V_S$ pulita di 100+ kt: per atterrare a 130 kt serve aumentare $C_{L,max}$ a 2,8+ → flap Fowler + slat sono necessari. Inoltre i jet hanno profili sottili ottimizzati per crociera ad alto Mach: questi profili stallano facilmente, lo slat compensa estendendo l'angolo critico.

4. **Sì, enorme**: il pilota può atterrare a un angolo di attacco maggiore (~20° invece di ~12°), il che significa che a parità di velocità di toccata, il muso è più alto e la traiettoria è più "ripida" → più controllo, frenata aerodinamica naturale. Inoltre la posizione "muso alto" allinea meglio il carrello con la pista. Senza slat, gli aerei militari moderni a volte usano "leading edge extension" (LEX) per ottenere un effetto simile.

5. $W = 22500 \cdot 9{,}81 = 220\,725$ N.
   $V_S = \sqrt{2W/(\rho S C_{L,max})} = \sqrt{(2 \cdot 220725)/(1{,}225 \cdot 61 \cdot 2{,}5)} = \sqrt{441450/186{,}8} = \sqrt{2363} \approx 48{,}6$ m/s.
   In nodi: $48{,}6/0{,}5144 \approx 94{,}5$ kt.
   $V_{ref} = 1{,}3 \cdot V_S \approx 126$ kt — coerente con i 110-130 kt di approccio dichiarati per ATR 72.

</details>

---

## 🎓 Hai finito le lezioni!

Le 9 lezioni di teoria sono complete. Ora il modo migliore per **fissare i concetti** è risolvere [gli esercizi](../03-esercizi/), specialmente l'[Esercizio 1 (Cessna 172)](../03-esercizi/01-base-portanza-cessna.md) come allenamento canonico.

Quando hai finito un esercizio, fai i [quiz](../02-quiz/) per autovalutarti prima dell'interrogazione.

> 💡 **Consiglio finale**: la teoria si impara, ma l'aerodinamica si **capisce solo facendo gli esercizi**. Non saltarli.
