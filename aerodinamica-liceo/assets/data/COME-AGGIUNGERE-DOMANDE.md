# 📝 Come aggiungere nuove domande al pool

Il file `domande-pool.json` contiene tutte le domande della banca quiz dinamica. Per aggiungerne di nuove, basta seguire il formato esistente.

## Format di una domanda

Ogni domanda è un oggetto JSON con questi campi:

```json
{
  "id": 61,
  "livello": "BASE",
  "argomento": "Profilo alare",
  "domanda": "Testo della domanda?",
  "opzioni": [
    "A. Prima opzione",
    "B. Seconda opzione",
    "C. Terza opzione",
    "D. Quarta opzione"
  ],
  "correct": "b",
  "spiegazione": "Perché B è la risposta corretta. Eventuale riferimento alla lezione."
}
```

### Regole
- `id`: numero progressivo (incrementare dall'ultimo `id` esistente)
- `livello`: `"BASE"` | `"MEDIO"` | `"AVANZATO"`
- `argomento`: breve etichetta (es. "Portanza", "Resistenza", "ISA")
- `correct`: `"a"` | `"b"` | `"c"` | `"d"` (tutto minuscolo)
- `opzioni`: sempre 4, con prefisso `A.`, `B.`, `C.`, `D.`

## Workflow rapido per Giulio (chat con Claude.ai)

Nel Project di studio Claude.ai, copia/incolla questo prompt:

> *"Generami 5 nuove domande sull'argomento [X] in formato JSON, seguendo lo stesso schema delle domande esistenti in domande-pool.json. Le risposte devono essere coerenti con le lezioni del repo. Restituiscimi solo il JSON."*

Claude risponde con un blocco JSON pronto da copiare. Tu (papà) lo apri in un editor:

1. Apri `aerodinamica-liceo/assets/data/domande-pool.json`
2. Incolla le nuove domande nell'array `"domande"` (prima della parentesi chiusa `]`)
3. Verifica gli `id` siano progressivi
4. Aggiorna `_meta.totale_domande` col nuovo totale
5. Salva, commit, push: `git add . && git commit -m "feat(quiz): +N domande sul pool" && git push`

Al prossimo deploy le domande sono live.

## Validazione prima del commit

Per verificare che il JSON sia valido:

```bash
python3 -c "import json; print(len(json.load(open('aerodinamica-liceo/assets/data/domande-pool.json'))['domande']))"
```

Se stampa il numero di domande senza errore, il JSON è valido.

## Statistiche pool attuale

Per vedere quante domande hai per livello/argomento:

```bash
python3 -c "
import json
from collections import Counter
d = json.load(open('aerodinamica-liceo/assets/data/domande-pool.json'))['domande']
print('Per livello:', Counter(q['livello'] for q in d))
print('Per argomento:', Counter(q['argomento'] for q in d).most_common())
"
```
