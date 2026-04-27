// Banca quiz dinamica — pesca random N domande dal pool e le mostra interattive

(function() {
  'use strict';

  let pool = [];
  const POOL_URL = '/struttura-Giulio/assets/data/domande-pool.json';

  async function loadPool() {
    try {
      const r = await fetch(POOL_URL);
      const data = await r.json();
      pool = data.domande || [];
      return true;
    } catch (e) {
      console.error('Errore caricamento pool domande:', e);
      return false;
    }
  }

  function shuffle(array) {
    const a = array.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  function pickQuestions(filter, n) {
    let candidates = pool;
    if (filter && filter !== 'TUTTI') {
      candidates = pool.filter(q => q.livello === filter);
    }
    return shuffle(candidates).slice(0, n);
  }

  function renderQuiz(container, questions) {
    if (questions.length === 0) {
      container.innerHTML = '<p>Nessuna domanda disponibile per il filtro selezionato.</p>';
      return;
    }

    let answeredCorrect = 0;
    let answeredTotal = 0;

    const scoreEl = document.createElement('div');
    scoreEl.className = 'quiz-score';
    scoreEl.innerHTML = `📊 Quiz dinamico (${questions.length} domande) — clicca le risposte`;
    container.appendChild(scoreEl);

    questions.forEach((q, idx) => {
      const qDiv = document.createElement('div');
      qDiv.className = 'quiz-q';
      qDiv.dataset.correct = q.correct;
      qDiv.dataset.qid = `dyn-${idx}`;

      const livelloChip = `<span style="display:inline-block;padding:0.15em 0.6em;border-radius:10px;background:${q.livello === 'BASE' ? '#43a047' : q.livello === 'MEDIO' ? '#fb8c00' : '#d32f2f'};color:white;font-size:0.75em;font-weight:600;margin-right:0.5em;">${q.livello}</span>`;
      const argChip = `<span style="font-size:0.85em;color:#666;">${q.argomento}</span>`;

      let html = `<p>${livelloChip}${argChip}</p>`;
      html += `<p><strong>${idx + 1}. ${q.domanda}</strong></p>`;
      q.opzioni.forEach((opt, i) => {
        const letter = ['a', 'b', 'c', 'd'][i];
        html += `<button class="quiz-opt" data-opt="${letter}">${opt}</button>`;
      });
      html += `<div class="quiz-explanation"><strong>Risposta corretta: ${q.correct.toUpperCase()}</strong> — ${q.spiegazione}</div>`;
      html += `<button class="quiz-retry">↻ Riprova</button>`;

      qDiv.innerHTML = html;
      container.appendChild(qDiv);
    });

    // Update score live
    const updateScore = () => {
      scoreEl.innerHTML = `📊 Quiz dinamico — <strong>${answeredCorrect}/${questions.length}</strong> giuste (${answeredTotal} risposte date)`;
    };

    // Click handler local to this quiz
    container.addEventListener('click', e => {
      const btn = e.target.closest('.quiz-opt');
      if (btn) {
        const q = btn.closest('.quiz-q');
        if (q.dataset.answered === '1') return;
        q.dataset.answered = '1';
        const correct = q.dataset.correct;
        const chosen = btn.dataset.opt;
        q.querySelectorAll('.quiz-opt').forEach(b => b.classList.add('disabled'));
        if (chosen === correct) {
          btn.classList.add('correct');
          answeredCorrect++;
        } else {
          btn.classList.add('wrong');
          const corr = q.querySelector(`.quiz-opt[data-opt="${correct}"]`);
          if (corr) corr.classList.add('correct');
          q.querySelector('.quiz-retry').classList.add('show');
        }
        answeredTotal++;
        const exp = q.querySelector('.quiz-explanation');
        if (exp) exp.classList.add('show');
        updateScore();
      }
      const retry = e.target.closest('.quiz-retry');
      if (retry) {
        const q = retry.closest('.quiz-q');
        delete q.dataset.answered;
        q.querySelectorAll('.quiz-opt').forEach(b => b.classList.remove('correct', 'wrong', 'disabled'));
        q.querySelector('.quiz-explanation').classList.remove('show');
        retry.classList.remove('show');
        answeredTotal--;
        updateScore();
      }
    });
  }

  async function init() {
    const dyn = document.getElementById('quiz-dinamico');
    if (!dyn) return;

    if (pool.length === 0) {
      const ok = await loadPool();
      if (!ok) {
        dyn.innerHTML = '<p style="color:#d32f2f;">⚠️ Errore caricamento banca domande. Verifica la connessione.</p>';
        return;
      }
    }

    const totaleEl = document.getElementById('totale-domande');
    if (totaleEl) totaleEl.textContent = pool.length;

    const generaBtn = document.getElementById('genera-quiz');
    const filtroSel = document.getElementById('filtro-livello');
    const numeroSel = document.getElementById('numero-domande');
    const containerEl = document.getElementById('quiz-container');

    if (!generaBtn || !containerEl) return;

    const generate = () => {
      const filtro = filtroSel ? filtroSel.value : 'TUTTI';
      const n = numeroSel ? parseInt(numeroSel.value, 10) : 10;
      containerEl.innerHTML = '';
      const qs = pickQuestions(filtro, n);
      renderQuiz(containerEl, qs);
    };

    generaBtn.addEventListener('click', generate);

    // Auto-genera al primo caricamento
    generate();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
