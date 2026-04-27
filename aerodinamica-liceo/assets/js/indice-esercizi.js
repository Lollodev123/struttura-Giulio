// Indice esercizi: filtri + ordinamento + ricerca testuale

(function() {
  'use strict';

  let esercizi = [];
  const URL = '/struttura-Giulio/assets/data/esercizi-indice.json';

  const COLORS = {
    BASE: { bg: '#43a047', label: '🟢 BASE' },
    MEDIO: { bg: '#fb8c00', label: '🟡 MEDIO' },
    AVANZATO: { bg: '#d32f2f', label: '🔴 AVANZATO' },
  };

  async function loadData() {
    try {
      const r = await fetch(URL);
      const data = await r.json();
      esercizi = data.esercizi || [];
      return true;
    } catch (e) {
      console.error('Errore caricamento indice:', e);
      return false;
    }
  }

  function getUniqueValues(field) {
    return Array.from(new Set(esercizi.map(e => e[field]))).sort();
  }

  function applyFilters() {
    const filtroLivello = document.getElementById('filtro-livello').value;
    const filtroArgomento = document.getElementById('filtro-argomento').value;
    const filtroTipo = document.getElementById('filtro-tipo').value;
    const ordine = document.getElementById('ordine').value;
    const ricerca = document.getElementById('ricerca').value.toLowerCase().trim();

    let filtered = esercizi.filter(e => {
      if (filtroLivello !== 'TUTTI' && e.difficolta !== filtroLivello) return false;
      if (filtroArgomento !== 'TUTTI' && e.argomento !== filtroArgomento) return false;
      if (filtroTipo !== 'TUTTI' && e.tipo !== filtroTipo) return false;
      if (ricerca && !(e.titolo.toLowerCase().includes(ricerca) ||
                       e.velivolo.toLowerCase().includes(ricerca) ||
                       e.argomento.toLowerCase().includes(ricerca))) return false;
      return true;
    });

    if (ordine === 'difficolta') {
      const order = { BASE: 1, MEDIO: 2, AVANZATO: 3 };
      filtered.sort((a, b) => order[a.difficolta] - order[b.difficolta] || a.id - b.id);
    } else if (ordine === 'argomento') {
      filtered.sort((a, b) => a.argomento.localeCompare(b.argomento) || a.id - b.id);
    } else if (ordine === 'velivolo') {
      filtered.sort((a, b) => a.velivolo.localeCompare(b.velivolo));
    } else {
      filtered.sort((a, b) => a.id - b.id);
    }

    renderTable(filtered);
    document.getElementById('contatore').textContent =
      `${filtered.length} esercizi su ${esercizi.length}`;
  }

  function renderTable(items) {
    const tbody = document.getElementById('tbody-esercizi');
    if (!tbody) return;
    if (items.length === 0) {
      tbody.innerHTML = '<tr><td colspan="5" style="text-align:center;padding:2em;color:#888;">Nessun esercizio corrisponde ai filtri.</td></tr>';
      return;
    }
    tbody.innerHTML = items.map(e => {
      const col = COLORS[e.difficolta];
      const isAlt = e.tipo === 'alternativo';
      const isProf = e.tipo === 'stile_prof';
      const altBadge = isAlt ? '<span style="background:#7b1fa2;color:white;padding:0.1em 0.4em;border-radius:6px;font-size:0.7em;margin-left:0.3em;font-weight:600;">ALT</span>' : '';
      const profBadge = isProf ? '<span style="background:#d32f2f;color:white;padding:0.1em 0.4em;border-radius:6px;font-size:0.7em;margin-left:0.3em;font-weight:600;">PROF</span>' : '';
      return `<tr>
        <td style="text-align:center;font-weight:600;">${e.id}</td>
        <td><span style="background:${col.bg};color:white;padding:0.15em 0.5em;border-radius:8px;font-size:0.75em;font-weight:600;">${col.label}</span></td>
        <td><a href="../${e.file.replace('.md','')}/" style="color:#1976d2;font-weight:500;">${e.titolo}</a>${altBadge}${profBadge}</td>
        <td><em style="color:#666;">${e.velivolo}</em></td>
        <td><span style="color:#888;font-size:0.9em;">${e.argomento}</span></td>
      </tr>`;
    }).join('');
  }

  function populateFilters() {
    const argSelect = document.getElementById('filtro-argomento');
    if (argSelect && argSelect.children.length <= 1) {
      getUniqueValues('argomento').forEach(arg => {
        const opt = document.createElement('option');
        opt.value = arg;
        opt.textContent = arg;
        argSelect.appendChild(opt);
      });
    }
  }

  async function init() {
    const root = document.getElementById('indice-esercizi');
    if (!root) return;
    if (esercizi.length === 0) {
      const ok = await loadData();
      if (!ok) {
        root.innerHTML = '<p style="color:#d32f2f;">⚠️ Errore caricamento indice esercizi.</p>';
        return;
      }
    }
    populateFilters();

    const inputs = ['filtro-livello', 'filtro-argomento', 'filtro-tipo', 'ordine', 'ricerca'];
    inputs.forEach(id => {
      const el = document.getElementById(id);
      if (el) el.addEventListener(el.tagName === 'INPUT' ? 'input' : 'change', applyFilters);
    });

    applyFilters();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
