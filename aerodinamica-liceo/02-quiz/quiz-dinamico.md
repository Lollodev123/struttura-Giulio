# 🎲 Quiz dinamico — pesca casuale dalla banca

> **60 domande** in pool (BASE, MEDIO, AVANZATO). Ogni volta che clicchi "Genera nuovo quiz", **ne pesca 10 a caso**. Mai due volte uguale: ogni sessione è una verifica diversa.
>
> Idea: ti alleni 10 minuti al giorno con 10 domande nuove → in 2 settimane hai visto la quasi totalità del pool, mescolato in modi diversi.

---

<div id="quiz-dinamico">

<div style="display:flex;flex-wrap:wrap;gap:1em;align-items:center;margin:1.5em 0;padding:1em;background:#f0f7ff;border-radius:8px;border-left:4px solid #1976d2;">

<label><strong>Livello:</strong>
<select id="filtro-livello" style="padding:0.4em;border-radius:4px;border:1px solid #ccc;margin-left:0.5em;">
<option value="TUTTI">Tutti i livelli</option>
<option value="BASE">🟢 Solo BASE</option>
<option value="MEDIO">🟡 Solo MEDIO</option>
<option value="AVANZATO">🔴 Solo AVANZATO</option>
</select>
</label>

<label><strong>Numero domande:</strong>
<select id="numero-domande" style="padding:0.4em;border-radius:4px;border:1px solid #ccc;margin-left:0.5em;">
<option value="5">5</option>
<option value="10" selected>10</option>
<option value="15">15</option>
<option value="20">20</option>
</select>
</label>

<button id="genera-quiz" style="padding:0.6em 1.2em;background:#1976d2;color:white;border:none;border-radius:6px;font-weight:600;cursor:pointer;font-size:1em;">🎲 Genera nuovo quiz</button>

<span style="color:#666;font-size:0.9em;">Pool: <strong id="totale-domande">60</strong> domande</span>

</div>

<div id="quiz-container"></div>

</div>

---

## 💡 Vuoi più domande nel pool?

La banca cresce nel tempo. Per aggiungere nuove domande basta che chiedi a Claude nel Project di studio:

> *"Generami 10 nuove domande sull'argomento [X] in formato JSON come quelle in `assets/data/domande-pool.json`"*

Claude segue lo stile del pool esistente. Tu (papà) le aggiungi al file JSON e le nuove domande sono live al prossimo deploy.

**Per il file JSON e la documentazione**: vedi [`assets/data/COME-AGGIUNGERE-DOMANDE.md`](../assets/data/COME-AGGIUNGERE-DOMANDE.md).

## 📚 Quiz strutturati (i 3 originali)

Se vuoi domande in ordine fisso anziché random:

- [Quiz BASE](./quiz-base.md) — 15 domande Lezioni 1-2
- [Quiz MEDIO](./quiz-medio.md) — 15 domande Lezioni 3-6
- [Quiz AVANZATO](./quiz-avanzato.md) — 10 domande Lezioni 7-9
