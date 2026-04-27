# 📚 Tutti gli esercizi — indice interattivo

> **25 esercizi totali**: 10 esercizi originali (numerati 1-10) + 15 esercizi alternativi (numerati 11-25, contrassegnati con badge **ALT**).
>
> Filtra per **livello**, **argomento** o **tipo**, ordina come preferisci, o cerca per nome/velivolo.

---

<div id="indice-esercizi">

<div style="display:flex;flex-wrap:wrap;gap:1em;align-items:center;margin:1.5em 0;padding:1em;background:#f0f7ff;border-radius:8px;border-left:4px solid #1976d2;">

<label><strong>Livello:</strong>
<select id="filtro-livello" style="padding:0.4em;border-radius:4px;border:1px solid #ccc;margin-left:0.5em;">
<option value="TUTTI">Tutti</option>
<option value="BASE">🟢 BASE</option>
<option value="MEDIO">🟡 MEDIO</option>
<option value="AVANZATO">🔴 AVANZATO</option>
</select>
</label>

<label><strong>Argomento:</strong>
<select id="filtro-argomento" style="padding:0.4em;border-radius:4px;border:1px solid #ccc;margin-left:0.5em;">
<option value="TUTTI">Tutti</option>
</select>
</label>

<label><strong>Tipo:</strong>
<select id="filtro-tipo" style="padding:0.4em;border-radius:4px;border:1px solid #ccc;margin-left:0.5em;">
<option value="TUTTI">Tutti</option>
<option value="originale">Originali (10)</option>
<option value="alternativo">Alternativi (15)</option>
<option value="stile_prof">Stile prof (6) 🔴</option>
</select>
</label>

<label><strong>Ordina:</strong>
<select id="ordine" style="padding:0.4em;border-radius:4px;border:1px solid #ccc;margin-left:0.5em;">
<option value="id">Numero</option>
<option value="difficolta">Difficoltà</option>
<option value="argomento">Argomento</option>
<option value="velivolo">Velivolo</option>
</select>
</label>

<label><strong>Cerca:</strong>
<input id="ricerca" type="text" placeholder="es. Boeing, stallo..." style="padding:0.4em;border-radius:4px;border:1px solid #ccc;margin-left:0.5em;width:180px;">
</label>

<span id="contatore" style="color:#666;font-size:0.9em;margin-left:auto;">25 esercizi</span>

</div>

<table style="width:100%;border-collapse:collapse;margin-top:1em;">
<thead>
<tr style="background:#1976d2;color:white;">
<th style="padding:0.6em;text-align:center;width:50px;">#</th>
<th style="padding:0.6em;text-align:left;width:120px;">Livello</th>
<th style="padding:0.6em;text-align:left;">Esercizio</th>
<th style="padding:0.6em;text-align:left;width:160px;">Velivolo</th>
<th style="padding:0.6em;text-align:left;width:130px;">Argomento</th>
</tr>
</thead>
<tbody id="tbody-esercizi">
<tr><td colspan="5" style="text-align:center;padding:2em;color:#888;">Caricamento...</td></tr>
</tbody>
</table>

</div>

---

## 💡 Come usarli

- **Cerchi un esercizio specifico**? Filtra per argomento (es. "Portanza", "Reynolds").
- **Vuoi allenarti su un velivolo specifico**? Cerca "Cessna" o "Boeing" nella casella di ricerca.
- **Stai studiando un livello**? Filtra "BASE" → "MEDIO" → "AVANZATO" in sequenza.
- **Solo gli alternativi**? Filtra Tipo = Alternativi (esercizi nuovi mai visti).

> 💬 Vuoi un esercizio nuovo che non c'è? **Chiedilo a Claude nel Project**: *"creami un esercizio sul [argomento] in stile [01-base-portanza-cessna.md]"* e te lo genera. Poi se vuoi che entri nell'indice, dimmelo e lo aggiungo qui.
