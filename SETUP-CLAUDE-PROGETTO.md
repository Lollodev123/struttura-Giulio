# 🤖 Setup del Project Claude.ai per Giulio

> Apri questo file sul Mac. Le istruzioni sono **per te (papà)**, da fare una volta sola in 5 minuti. Dopo, lasci il Mac in modalità "Claude pronto" e Giulio chatta da lì.

---

## 🎯 Cosa stiamo creando

Un **Project di Claude.ai** chiamato `Aerodinamica — Giulio`, pre-caricato con:
- Tutto il materiale del repo `Lollodev123/struttura-Giulio` (lezioni, esercizi, formulario, glossario) connesso direttamente da GitHub — si aggiorna da solo a ogni push
- Una "personalità" (system prompt) che fa ragionare Claude come **tutor paziente di liceo aeronautico italiano**, con tono adatto a Giulio e regole strette su unità SI, formule e metodo

Risultato: Giulio apre claude.ai sul tuo Mac → entra nel Project → chiede qualsiasi cosa, Claude risponde **ancorato al repo**.

---

## 📋 Step-by-step (5 minuti)

### Step 1 — Crea il Project

1. Vai su https://claude.ai sul Mac (sei già loggato con il tuo Max)
2. Sidebar a sinistra → **Projects** → bottone **`+ New Project`**
3. Nome: `Aerodinamica — Giulio`
4. Descrizione (opzionale): `Tutor di aerodinamica per liceo aeronautico, 2°-3° anno`
5. Crea

### Step 2 — Connetti il repo GitHub

Dentro il Project appena creato:

1. Cerca la sezione **`Project knowledge`** (di solito in alto a destra o sotto le impostazioni)
2. Clicca il bottone **`+`** → seleziona **`GitHub`**
3. Se è la prima volta: autorizza Claude ad accedere ai tuoi repo (OAuth GitHub)
4. Cerca o incolla `Lollodev123/struttura-Giulio` → seleziona il repo
5. Branch: **`main`** (default)
6. Path: lascia vuoto (importa tutto il repo)
7. **Save / Sync now**

> 💡 Da qui in poi, ogni volta che pusho un nuovo `.md` (es. Lezione 3, nuovo esercizio), Claude lo vede automaticamente entro pochi minuti. Niente da fare manualmente.

### Step 3 — Imposta la personalità (system prompt)

Sempre dentro il Project, cerca **`Project instructions`** o **`Custom instructions`** (campo grande di testo):

**Copia-incolla esattamente questo blocco:**

```
Sei un tutor di aerodinamica per Giulio, studente del 2°-3° anno di Liceo Aeronautico italiano (15-17 anni).

CONTESTO DELLO STUDENTE
- Capisce la teoria a livello superficiale ma è bloccato sulla parte pratica
- Difficoltà specifica: trasformare un testo problema in passaggi di calcolo (non sa scegliere la formula, gestire le unità)
- Matematica disponibile: trigonometria, geometria analitica, derivate semplici. NON usare integrali, NON usare equazioni differenziali, NON usare Navier-Stokes
- Lingua: italiano. Usa SEMPRE terminologia aeronautica italiana (portanza, resistenza, allungamento alare, ecc.) — vedi glossario nel repo per i termini

REGOLE NON-NEGOZIABILI
1. Spiega il "come pensare al problema" PRIMA dei calcoli, in 3-5 punti di strategia
2. Tono paziente, mai intimidatorio. Mai dire "è facile" — anche le cose semplici qui non lo sono
3. Velivoli reali con dati realistici (Cessna 172, Piper PA-28, ATR 72, Boeing 737, Airbus A320, Eurofighter, ASK-21). Mai cifre tonde finte
4. Sistema SI primario (m, s, N, Pa, kg/m³). Conversioni a nodi/piedi/libbre quando rilevanti, ma calcoli in SI
5. Verifica di plausibilità sempre — confronta il risultato con i valori tipici dal formulario del repo
6. Quando crei un esercizio, finisci con una "Variante per autovalutazione" (stesso problema, dato cambiato, solo risultato finale)

ERRORI DA NON FARE MAI
- Dimenticare il fattore ½ nella formula della portanza L = ½ρV²S·C_L
- Confondere massa (kg) e peso (N): sempre W = m·g
- Sostituire velocità in nodi senza convertire in m/s (× 0,5144)
- Usare ρ₀ = 1,225 kg/m³ in quota — usa la tabella ISA del formulario per altitudini diverse
- Mostrare solo la formula finale: ogni passaggio numerico va visibile
- Saltare il controllo unità

FORMATO DELLE RISPOSTE
- Formule in LaTeX con $...$ inline e $$...$$ per display
- Quando spieghi una lezione nuova, segui lo stile del file 01-teoria/01-profilo-alare.md (sezioni: 🎯 In una riga · ✈️ A cosa serve · 📐 Concetti · 🔢 Formule · ✈️ Esempi reali · 🎯 Box ricordare · ⚠️ Errori comuni · 🧠 Domande autoverifica)
- Quando crei un esercizio, segui lo stile del file 03-esercizi/01-base-portanza-cessna.md (sezioni: 📋 Testo · 🖼️ Diagramma · 📊 Dati · 🧠 Strategia · ✏️ Risoluzione passo-passo · ✅ Plausibilità · 🔄 Variante · 🎓 Cosa hai imparato)
- Per le risposte nascoste usa <details markdown="1">

SCOPO
Rispondi alle domande di Giulio sul materiale del repo. Se ti chiede di spiegare un argomento di una lezione ancora "🚧 In arrivo", crea una mini-lezione provvisoria nello stile del benchmark. Se ti chiede di creare un esercizio nuovo, fallo nello stile di 01-base-portanza-cessna.md.

NON fare:
- Argomenti fuori scope (propulsione, avionica, navigazione, meteorologia avanzata)
- Spiegazioni accademiche con terminologia universitaria
- Risposte secche tipo "la portanza è L = ½ρV²S·C_L. Bye." — Giulio ha bisogno del ragionamento intermedio.
```

Salva.

### Step 4 — Test

Apri una nuova chat dentro il Project e prova queste 3 domande:

1. *"Spiegami in 30 secondi cos'è il numero di Reynolds, in modo che lo capisca."*
   → Aspettati: spiegazione semplice, terminologia italiana, esempio su un Cessna o un aliante, riferimento al formulario del repo.

2. *"Creami un esercizio sulla velocità di stallo del Piper PA-28 in stile [01-base-portanza-cessna.md](./aerodinamica-liceo/03-esercizi/01-base-portanza-cessna.md)"*
   → Aspettati: esercizio completo con strategia, risoluzione passo-passo, verifica plausibilità, variante.

3. *"Nell'esercizio 1 (Cessna 172) non capisco perché serve convertire i nodi in m/s. Non posso lasciarli così?"*
   → Aspettati: spiegazione paziente, esempio numerico di cosa succederebbe sbagliando, conferma del fattore di conversione.

Se le 3 risposte sono buone, il Project è pronto.

---

## 👦 Come Giulio lo userà

- Usa il **tuo Mac** (account Max già loggato)
- Apre il browser → claude.ai → sidebar → Projects → `Aerodinamica — Giulio`
- Bottone **`Start new chat`** ogni volta che ha una domanda nuova
- Le sue chat **restano nel tuo account** (le vedi se vuoi controllare)

> ⚠️ **Privacy**: il Max è il tuo. Tutte le chat appaiono nella tua cronologia. Se non vuoi vedere ogni cosa che chiede, non aprire la sezione `Recents`. Se vuoi proprio separare, l'unica strada pulita è fargli un account Free suo (Free dal Feb 2026 supporta Projects + GitHub connector — funziona anche se più limitato).

---

## 🔄 Quando il repo cambia

Quando aggiungo (o tu aggiungi) una nuova lezione/esercizio e fai push su `main`:

- Il **sito** (https://lollodev123.github.io/struttura-Giulio/) si aggiorna in 1-2 minuti via GitHub Action
- Il **Project di Claude** si sincronizza automaticamente. Se vuoi forzare l'aggiornamento, vai nel Project → Knowledge → trova il GitHub source → bottone `Sync` (o icona di refresh). Tipicamente non serve.

---

## ❓ FAQ

**"Posso aggiungere altri file al Project?"**
Sì. Oltre al GitHub source puoi droppare PDF (es. capitoli del Flaccavento), foto del compito di Giulio per farglielo correggere, slide. Project knowledge accetta tutto.

**"E se Claude inventa una formula sbagliata?"**
Apri una Issue su GitHub con label `errore-materiale` o dimmelo direttamente. Aggiungiamo l'errore alla lista in CLAUDE.md così non si ripete.

**"Giulio può chiedere a Claude di scrivere lezioni nuove al posto tuo?"**
Funzionalmente sì, ma non finiscono nel repo automaticamente. La pipeline ufficiale resta: tu mi chiedi una lezione → io la scrivo nel formato del benchmark → commit → push → arriva nel Project di Giulio.

**"Quanto costa?"**
Zero in più. Il tuo Max è già attivo. Il GitHub connector e i Project sono inclusi su Pro+ (e ora anche su Free).

**"Posso esportare le chat di Giulio per archiviarle?"**
Sì, da claude.ai → impostazioni profilo → Export data. Esporta tutto in JSON.

---

## 📞 Quando serve me (Claude Code)

Mi chiami quando vuoi:
- Aggiungere una nuova lezione o esercizio nel repo (così entra anche nel Project di Giulio)
- Correggere un errore segnalato via Issue
- Cambiare lo stile/struttura del materiale
- Cambiare le regole del Project (basta riaprire questo file e dirti cosa modificare nel system prompt)

Per le **domande di studio quotidiane di Giulio** non servo: ci pensa il Project Claude.ai.
