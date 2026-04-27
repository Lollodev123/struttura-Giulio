// Quiz interattivi — gestione click, feedback e contatore punteggio

(function() {
  'use strict';

  let totalQuestions = 0;
  let answeredCorrect = 0;
  let answeredWrong = 0;
  let answeredQs = new Set();

  function updateScore() {
    const scoreEl = document.querySelector('.quiz-score');
    if (!scoreEl) return;
    const answered = answeredCorrect + answeredWrong;
    const pct = totalQuestions > 0 ? Math.round((answeredCorrect / totalQuestions) * 100) : 0;
    scoreEl.innerHTML =
      `📊 Punteggio: <strong>${answeredCorrect}/${totalQuestions}</strong> ` +
      `(${pct}%) — Risposte date: ${answered}, Sbagliate: ${answeredWrong}`;
  }

  function handleClick(e) {
    const btn = e.target.closest('.quiz-opt');
    if (!btn) return;
    const q = btn.closest('.quiz-q');
    if (!q) return;

    const qid = q.dataset.qid || q.id;
    if (answeredQs.has(qid)) return;

    const correct = q.dataset.correct;
    const chosen = btn.dataset.opt;

    // Disable all options
    q.querySelectorAll('.quiz-opt').forEach(b => b.classList.add('disabled'));

    if (chosen === correct) {
      btn.classList.add('correct');
      answeredCorrect++;
    } else {
      btn.classList.add('wrong');
      // Show the correct one
      const correctBtn = q.querySelector(`.quiz-opt[data-opt="${correct}"]`);
      if (correctBtn) correctBtn.classList.add('correct');
      answeredWrong++;

      // Show retry button only if first attempt was wrong
      const retryBtn = q.querySelector('.quiz-retry');
      if (retryBtn) retryBtn.classList.add('show');
    }

    answeredQs.add(qid);

    // Show explanation
    const exp = q.querySelector('.quiz-explanation');
    if (exp) exp.classList.add('show');

    updateScore();

    // Re-render KaTeX in newly shown explanation
    if (typeof renderMathInElement === 'function' && exp) {
      try {
        renderMathInElement(exp, {
          delimiters: [
            { left: '$$', right: '$$', display: true },
            { left: '$',  right: '$',  display: false }
          ],
          throwOnError: false
        });
      } catch (e) {}
    }
  }

  function handleRetry(e) {
    const btn = e.target.closest('.quiz-retry');
    if (!btn) return;
    const q = btn.closest('.quiz-q');
    if (!q) return;

    const qid = q.dataset.qid || q.id;
    // Reset state
    answeredQs.delete(qid);
    q.querySelectorAll('.quiz-opt').forEach(b => {
      b.classList.remove('correct', 'wrong', 'disabled');
    });
    const exp = q.querySelector('.quiz-explanation');
    if (exp) exp.classList.remove('show');
    btn.classList.remove('show');

    // Adjust score: was wrong, now allow new attempt
    answeredWrong = Math.max(0, answeredWrong - 1);
    updateScore();
  }

  function init() {
    // Count total questions and assign IDs
    document.querySelectorAll('.quiz-q').forEach((q, i) => {
      if (!q.dataset.qid) q.dataset.qid = 'q' + i;
    });
    totalQuestions = document.querySelectorAll('.quiz-q').length;

    if (totalQuestions === 0) return;

    document.addEventListener('click', handleClick);
    document.addEventListener('click', handleRetry);
    updateScore();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
