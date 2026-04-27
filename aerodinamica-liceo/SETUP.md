# 🚀 Setup — Mettere questo repo su GitHub

Tre opzioni in ordine di facilità. **Scegli UNA**.

---

## ✅ Opzione A — GitHub web UI (più semplice, no terminale)

1. Vai su [github.com/new](https://github.com/new) e crea un nuovo repository
   - **Nome**: `aerodinamica-liceo` (o quello che preferisci)
   - **Privacy**: 🔒 **Private** (importante: lo studente entra come collaborator)
   - **NON** spuntare "Add a README" — lo abbiamo già

2. Nella pagina del repo vuoto, clicca **"uploading an existing file"**
3. Trascina **tutti i file e cartelle** del .zip estratto
4. Scrivi messaggio commit: `Initial commit: scaffold + lezione 1 + esercizio 1`
5. Clicca **Commit changes**
6. Vai su **Settings → Collaborators → Add people** → email/username dello studente

⏱️ Tempo: 5 minuti. ✅ Pronto.

---

## ⚙️ Opzione B — GitHub CLI (1 minuto se hai `gh` installato)

```bash
cd aerodinamica-liceo
git init
git add .
git commit -m "Initial commit: scaffold + lezione 1 + esercizio 1"
gh repo create aerodinamica-liceo --private --source=. --remote=origin --push
gh repo edit --add-collaborator USERNAME_STUDENTE
```

Sostituisci `USERNAME_STUDENTE` con lo username GitHub dello studente.

Se non hai `gh`: `brew install gh` (macOS) o vai su [cli.github.com](https://cli.github.com).

---

## 🔧 Opzione C — Git classico

```bash
cd aerodinamica-liceo
git init
git branch -M main
git add .
git commit -m "Initial commit"
# Crea il repo vuoto su github.com PRIMA, poi:
git remote add origin git@github.com:TUO_USERNAME/aerodinamica-liceo.git
git push -u origin main
```

Poi aggiungi lo studente da **Settings → Collaborators**.

---

## 🌐 Upgrade opzionale: GitHub Pages (sito navigabile)

Se vuoi che il materiale diventi un **sito mobile-friendly** invece di un repo, dopo il push iniziale:

1. Installa [MkDocs Material](https://squidfunk.github.io/mkdocs-material/getting-started/):
   ```bash
   pip install mkdocs-material pymdown-extensions
   ```

2. Aggiungi un `mkdocs.yml` minimale (te lo posso generare quando vuoi).
3. Attiva GitHub Pages: **Settings → Pages → Source: GitHub Actions**.
4. Risultato: sito tipo `https://tuousername.github.io/aerodinamica-liceo/` con search, dark mode, navigazione ad albero.

> Per ora ignoralo. Funziona benissimo come repo. Se lo studente ti chiede "si può avere come sito?", torniamo qui.

---

## 🔄 Workflow per gli aggiornamenti futuri

Quando io ti consegno una nuova lezione/esercizio in chat:

1. Salvi il file `.md` nella cartella giusta del repo locale
2. ```bash
   git add . && git commit -m "Aggiunta lezione 2: portanza" && git push
   ```

3. Lo studente vede l'aggiornamento entro pochi secondi su GitHub

Oppure, se stai lavorando in browser: vai sul repo → **Add file → Upload files**.

---

## ❓ Domande frequenti

**Lo studente ha bisogno di un account GitHub?**
Sì, gratuito. Si crea su [github.com/signup](https://github.com/signup) in 30 secondi. Su mobile esiste anche l'app GitHub.

**Posso fare il repo pubblico?**
Tecnicamente sì, ma se contiene info personali dello studente (nome nelle issue, ecc.) tienilo privato. Si può sempre flippare dopo.

**Le formule LaTeX si vedono su GitHub mobile?**
Sì, sia su browser mobile che sull'app GitHub. Anche i diagrammi Mermaid.

**Come faccio se sbaglio qualcosa nel push?**
Tranquillo: git tiene tutta la cronologia. Si può sempre tornare indietro con `git revert` o ripristinare un file da una versione precedente direttamente dall'interfaccia GitHub.
