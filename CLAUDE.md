# CLAUDE.md — Memoria del progetto

> Questo file viene letto automaticamente da Claude Code all'apertura del progetto. Spiega contesto, convenzioni, stile e workflow. Tienilo aggiornato quando cambia qualcosa di strutturale.

---

## 🎯 Cos'è questo progetto

Pacchetto didattico di **Aerodinamica per Liceo Aeronautico** (2° e 3° anno italiano). Lo studente ha difficoltà specifica con la **parte pratica**: capisce la teoria a livello superficiale ma non sa risolvere gli esercizi (non sa leggere un problema, scegliere la formula, gestire le unità).

**Obiettivi del materiale:**
1. Lezioni teoriche chiare con diagrammi
2. Quiz di verifica (40 totali, 3 livelli di difficoltà)
3. **10 esercizi risolti passo-passo** (cuore del progetto, peso ~50% del lavoro)
4. Tutto in markdown, leggibile su mobile via GitHub

---

## 👤 Chi è lo studente

- Liceo aeronautico, 2°-3° anno (15-17 anni)
- Matematica disponibile: trigonometria, geometria analitica, derivate semplici. **Niente integrali, niente equazioni differenziali.**
- Lingua: italiano nativo
- Dispositivo principale: smartphone (mobile-first)
- Bloccato su: trasformare un testo di problema in passaggi di calcolo

---

## ✍️ Stile didattico — non negoziabile

1. **Spiega il "come pensare al problema" PRIMA dei calcoli.** Ogni esercizio deve avere una sezione "🧠 Strategia di risoluzione" con 3-5 bullet che insegnano la metodologia, non solo l'algebra.
2. **Tono paziente, mai intimidatorio.** Lo studente è bloccato — l'enfasi è sull'autostima e sul metodo, non sulla velocità.
3. **Velivoli reali con dati realistici** — Cessna 172, Piper PA-28, ATR 72, Boeing 737, Airbus A320, Eurofighter. Mai cifre tonde finte tipo "un aereo di 1000 kg".
4. **Sistema di unità SI primario.** Mostra conversioni a nodi/piedi/libbre quando rilevante per realismo aeronautico, ma i calcoli si fanno in SI.
5. **Verifica di plausibilità sempre**, ogni esercizio finisce confrontando il risultato con valori tipici (vedi `00-formulario/formulario.md` sezione "Coefficienti tipici").
6. **Variante per autovalutazione** alla fine di ogni esercizio: stesso problema con un dato cambiato, solo risultato finale.

---

## 📂 Struttura del repo

```
00-formulario/      # Formulario unico + glossario IT/EN
01-teoria/          # 9 lezioni (1 completa: profilo alare; 8 placeholder)
02-quiz/            # Quiz base/medio/avanzato (placeholder)
03-esercizi/        # 10 esercizi (1 completo: portanza Cessna; 9 placeholder)
03-esercizi/soluzioni/   # Soluzioni delle varianti autovalutative
.github/ISSUE_TEMPLATE/  # Template per domande studente e segnalazione errori
assets/img/         # Diagrammi raster (futuri)
README.md           # Indice navigabile con stato di completamento
SETUP.md            # Guida push GitHub
```

---

## 📝 Template e convenzioni

### Per nuove lezioni
Segui `01-teoria/_template-lezione.md`. Sezioni obbligatorie:
- 🎯 In una riga
- ✈️ A cosa serve davvero
- 📐 Concetti / Geometria / Formule
- ✈️ Esempi su velivoli reali
- 🎯 Box "Da ricordare per l'interrogazione"
- ⚠️ Errori comuni
- 🧠 Domande di autoverifica con risposte in `<details>`

**Riferimento di stile**: `01-teoria/01-profilo-alare.md` — completa al 100%, usala come benchmark.

### Per nuovi esercizi
Segui `03-esercizi/_template-esercizio.md`. Sezioni obbligatorie:
- 📋 Testo del problema
- 🖼️ Diagramma (ASCII art o Mermaid)
- 📊 Dati noti / da trovare (tabella)
- 🧠 Strategia di risoluzione (5 punti, prima dei calcoli)
- ✏️ Risoluzione passo-passo (numerata, sostituzioni numeriche visibili)
- ✅ Verifica di plausibilità
- 🔄 Variante per autovalutazione (con risultato in `<details>`)
- 🎓 Cosa hai imparato

**Riferimento di stile**: `03-esercizi/01-base-portanza-cessna.md` — completo al 100%, benchmark.

### Notazione matematica
- LaTeX inline: `$L = \frac{1}{2}\rho V^2 S C_L$`
- LaTeX display: `$$...$$`
- GitHub renderizza nativamente da .md (sia browser che app mobile)

### Diagrammi
- **Forme statiche** (profilo alare, polare): ASCII art con etichette
- **Flussi/decisioni/relazioni**: Mermaid
- **Grafici quantitativi** (curva CL-α): per ora descrittiva, futuri come SVG in `assets/img/`

---

## 🔑 Costanti e valori standard del progetto

| Quantità | Valore | Quando usare |
|---|---|---|
| ρ₀ (densità ISA livello mare) | 1,225 kg/m³ | Tutti gli esercizi base |
| g | 9,81 m/s² | Sempre |
| 1 kt | 0,5144 m/s | Conversione velocità |
| Viscosità dinamica aria a 15°C | 1,78 × 10⁻⁵ Pa·s | Reynolds |

Per quote diverse dal livello mare, usa la tabella ISA in `00-formulario/formulario.md` sezione 7.

---

## 🚫 Errori che NON devi rifare

1. **Mai dimenticare il fattore ½** nella formula della portanza (errore frequente quando si copia da memoria).
2. **Mai usare massa al posto del peso**: $W = m \cdot g$ sempre.
3. **Mai sostituire velocità in nodi senza convertirla** in m/s prima.
4. **Mai usare ρ₀ in quota**: la densità diminuisce con l'altitudine. Tabella ISA è obbligatoria.
5. **Mai mostrare solo la formula finale**: ogni passaggio numerico deve essere visibile (lo studente ne ha bisogno per imparare).
6. **Mai semplificare unità nelle conversioni**: scrivi "× 0,5144 m/s/kt" non "× 0,5144".

---

## 🔄 Workflow operativo

### Quando l'utente chiede una nuova lezione/esercizio
1. Leggi il template corrispondente per assicurarti della struttura
2. Scrivi il file nuovo nella cartella giusta con la naming convention esistente
3. **Aggiorna il README.md**: cambia 🚧 → ✅ nell'indice, aggiungi link nella tabella
4. Commit con messaggio descrittivo: `feat(teoria): lezione 2 - portanza`
5. Push (se richiesto, o conferma prima)

### Quando arriva una issue dallo studente
1. Leggi la issue via GitHub MCP
2. Identifica il file/passaggio coinvolto
3. **Se è una domanda di chiarimento**: aggiungi una sezione "💡 Chiarimento" al file della lezione/esercizio (NON rispondere solo nell'issue: integra nel materiale per i futuri studenti)
4. Commenta sull'issue con link al chiarimento aggiunto
5. Chiudi la issue

### Convenzioni Git
- Commit in italiano, formato conventional: `feat:`, `fix:`, `docs:`, `chore:`
- Branch per modifiche grandi (>3 file): `feat/nome-breve`
- Push sempre su `main` per cambi piccoli, PR per cambi strutturali

---

## 🌐 Lingua

**Tutto in italiano**, terminologia aeronautica italiana corretta. Vedi `00-formulario/glossario.md` per traduzioni IT/EN. Ricorda:
- "Portanza" non "Lift" nel testo italiano
- "Resistenza aerodinamica" non "Drag"
- "Allungamento alare" non "Aspect ratio"
- Mantieni i simboli matematici standard ($L$, $D$, $C_L$, $\alpha$, $\lambda$, ecc.)

---

## 📚 Fonti di riferimento

- Flaccavento — *Aerotecnica e Costruzioni Aeronautiche* (testo standard liceo aeronautico IT)
- Anderson — *Fundamentals of Aerodynamics* (per approfondimenti tecnici)
- NACA Report TR-824 (catalogo profili)
- Tabella ISA: documento standard internazionale, valori già in `formulario.md`

---

## 🎚️ Cose da NON fare

- ❌ Non aggiungere argomenti fuori scope (es. propulsione, avionica): il progetto è strettamente aerodinamica + cenni strutturali base
- ❌ Non cambiare lo stile dei template senza confrontarti con l'utente
- ❌ Non spingere oltre la matematica del liceo (no integrali, no Navier-Stokes)
- ❌ Non rendere pubblico il repo senza esplicita richiesta (info sullo studente)
- ❌ Non droppare emoji a caso: quelli che ci sono nei template sono intenzionali e creano gerarchia visiva. Mantienili coerenti.

---

## ✅ Status corrente (aggiorna man mano)

- [x] Scaffold completo del repo
- [x] Formulario + glossario
- [x] Lezione 1: Profilo alare
- [x] Esercizio 1: Portanza Cessna 172 + variante
- [ ] Lezione 2: Portanza
- [ ] Lezione 3: Resistenza aerodinamica
- [ ] Lezione 4: Efficienza e polare
- [ ] Lezione 5: Atmosfera Standard ISA
- [ ] Lezione 6: Numero di Reynolds
- [ ] Lezione 7: Geometria alare
- [ ] Lezione 8: Momento e centraggio
- [ ] Lezione 9: Dispositivi di alta portanza
- [ ] Esercizi 2-10
- [ ] 3 quiz (base/medio/avanzato) con soluzioni
