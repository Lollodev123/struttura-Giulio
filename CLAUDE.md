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
/                              # Root del repo
  CLAUDE.md                    # Memoria del progetto (questo file)
  mkdocs.yml                   # Config sito MkDocs Material
  SETUP-CLAUDE-PROGETTO.md     # Guida setup Claude.ai Project per lo studente
  .github/workflows/           # Deploy automatico sito su push a main
  .gitignore

/aerodinamica-liceo/           # Tutto il materiale didattico
  00-formulario/               # Formulario unico + glossario IT/EN
  01-teoria/                   # 9 lezioni
  02-quiz/                     # Quiz base/medio/avanzato (placeholder)
  03-esercizi/                 # 10 esercizi
  03-esercizi/soluzioni/       # Soluzioni delle varianti autovalutative
  .github/ISSUE_TEMPLATE/      # Solo errore-materiale (le domande vanno in chat)
  assets/img/                  # Diagrammi (futuri)
  assets/js/katex-init.js      # Render LaTeX sul sito
  README.md, SETUP.md, CONTRIBUTING.md, LICENSE
```

- **Repo pubblico** (deciso il 2026-04-27): https://github.com/Lollodev123/struttura-Giulio
- **Sito live**: https://lollodev123.github.io/struttura-Giulio/ — deploy automatico via GitHub Actions a ogni push su `main`

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
- GitHub renderizza nativamente da .md; il sito MkDocs usa KaTeX (configurato).

### Sezioni nascoste (`<details>`)
Per le risposte di autoverifica e le varianti, **usa SEMPRE** `<details markdown="1">` (NON solo `<details>`). L'attributo `markdown="1"` è necessario perché MkDocs (con `md_in_html`) processi il Markdown dentro l'elemento. Senza, le liste numerate, le formule LaTeX e i grassetti collassano in un unico paragrafo. GitHub ignora l'attributo silenziosamente — funziona da entrambe le parti.

```markdown
<details markdown="1">
<summary>👉 Risposte</summary>

1. Prima risposta con $V^2$ e **grassetto**.
2. Seconda risposta.

</details>
```

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

### Canali di interazione con lo studente
Lo studente ha **due canali**, con scopi diversi:

1. **Chat diretta su Claude.ai Project** (canale primario): per le **domande di comprensione** ("non capisco questo passaggio", "spiegami meglio X"). Il Project ha il connector GitHub al repo, quindi Claude.ai legge il materiale aggiornato. La conversazione resta nel Project — non passa da qui.
2. **GitHub Issue con label `errore-materiale`** (canale secondario): solo per **segnalare errori** trovati nel materiale (refusi, calcoli sbagliati, link rotti). C'è un solo template: `.github/ISSUE_TEMPLATE/correzione-errore.md`.

### Quando arriva una issue `errore-materiale`
1. Leggi la issue (`gh issue view <n>`)
2. Identifica file e passaggio
3. **Correggi il file**, commit `fix(teoria/esercizi): ...` su un branch fix/
4. Apri PR, mergia, commenta l'issue linkando il commit/PR e chiudila
5. Se l'errore era concettualmente importante, aggiungi anche la voce in `CLAUDE.md` → "Errori che NON devi rifare"

### Quando lo studente chiede di promuovere una chat a chiarimento permanente
Se l'utente ti dice "*la chat di Giulio sull'angolo di attacco era utile, integriamola*", aggiungi una sezione `💡 Chiarimento` al file della lezione/esercizio interessato. Non c'è un trigger automatico: avviene solo quando il padre lo chiede esplicitamente.

### Convenzioni Git
- Commit in italiano, formato conventional: `feat:`, `fix:`, `docs:`, `chore:`
- Branch per qualsiasi modifica: `feat/nome-breve`, `fix/nome-breve`
- **Niente push diretti a `main`**: sempre PR (anche per fix piccoli). Default branch resta `main`; `develop` esiste come branch di lavoro ma in pratica si usano feature branch.
- Dopo merge: il workflow `Deploy MkDocs site` deploya il sito automaticamente

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
- ❌ Non aggiungere informazioni personali dello studente nel repo (il repo è pubblico dal 2026-04-27)
- ❌ Non droppare emoji a caso: quelli che ci sono nei template sono intenzionali e creano gerarchia visiva. Mantienili coerenti.

---

## ✅ Status corrente (aggiorna man mano)

- [x] Scaffold completo del repo
- [x] Formulario + glossario
- [x] Sito MkDocs Material live su GitHub Pages
- [x] Lezione 1: Profilo alare
- [x] Lezione 2: Portanza
- [x] Esercizio 1: Portanza Cessna 172 + variante
- [ ] Lezione 3: Resistenza aerodinamica
- [ ] Lezione 4: Efficienza e polare
- [ ] Lezione 5: Atmosfera Standard ISA
- [ ] Lezione 6: Numero di Reynolds
- [ ] Lezione 7: Geometria alare
- [ ] Lezione 8: Momento e centraggio
- [ ] Lezione 9: Dispositivi di alta portanza
- [ ] Esercizi 2-10
- [ ] 3 quiz (base/medio/avanzato) con soluzioni
