(function () {
  var list = document.getElementById('reviews-list');
  var form = document.getElementById('review-form');
  if (!list || !form) return;

  var T = {
    ru: {
      empty: 'Пока здесь нет отзывов. Если мы работали вместе, будьте первым!',
      loadErr: 'Не удалось загрузить отзывы. Обновите страницу.',
      sending: 'Отправляю…', send: 'Отправить отзыв',
      ok: 'Спасибо! Отзыв появится на сайте после проверки.',
      err: 'Не получилось отправить. Попробуйте ещё раз или напишите мне в Telegram.',
      rate: 'Слишком много отзывов с вашего адреса за сутки. Попробуйте завтра.',
      name: 'Укажите имя (от 2 символов).', text: 'Напишите отзыв (от 20 символов).',
      consent: 'Нужно согласие на обработку данных.', links: 'Пожалуйста, без ссылок в отзыве.',
      projects: { morehleba: 'Море хлеба', vmr: 'ВМР ТРАНС', greymax: 'GREYMAX', calorieai: 'CalorieAI', other: 'Другой проект' },
      months: ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    },
    en: {
      empty: 'No reviews yet. If we\'ve worked together, be the first!',
      loadErr: 'Couldn\'t load reviews. Please refresh the page.',
      sending: 'Sending…', send: 'Send review',
      ok: 'Thank you! Your review will appear after moderation.',
      err: 'Couldn\'t send it. Please try again or message me on Telegram.',
      rate: 'Too many reviews from your address today. Please try tomorrow.',
      name: 'Please enter your name (2+ characters).', text: 'Please write a review (20+ characters).',
      consent: 'Please give your consent to data processing.', links: 'Please don\'t include links in the review.',
      projects: { morehleba: 'More Hleba bakery', vmr: 'VMR TRANS', greymax: 'GREYMAX', calorieai: 'CalorieAI', other: 'Other project' },
      months: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    }
  };
  function t() { return T[document.documentElement.lang === 'en' ? 'en' : 'ru']; }

  var data = null, loadFailed = false;
  var startedAt = Date.now();

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }

  function render() {
    list.innerHTML = '';
    if (loadFailed) { list.appendChild(el('p', 'rv-empty', t().loadErr)); return; }
    if (!data) return;
    if (!data.length) { list.appendChild(el('p', 'rv-empty', t().empty)); return; }
    data.forEach(function (r) {
      var card = el('article', 'rv');
      var stars = el('div', 'rv-stars', '★★★★★'.slice(0, r.rating) + '☆☆☆☆☆'.slice(0, 5 - r.rating));
      stars.setAttribute('aria-label', r.rating + '/5');
      card.appendChild(stars);
      card.appendChild(el('p', 'rv-text', r.text));
      var who = el('div', 'rv-who');
      who.appendChild(el('b', null, r.name));
      if (r.company) who.appendChild(el('span', null, r.company));
      card.appendChild(who);
      var d = r.date.split('-');
      card.appendChild(el('div', 'rv-meta', (t().projects[r.project] || '') + ' · ' + t().months[+d[1] - 1] + ' ' + d[0]));
      list.appendChild(card);
    });
  }

  fetch('api/reviews.php', { cache: 'no-store' })
    .then(function (r) { return r.json(); })
    .then(function (j) { data = j.reviews || []; render(); })
    .catch(function () { loadFailed = true; render(); });

  document.addEventListener('langchange', render);

  var status = document.getElementById('rv-status');
  var btn = form.querySelector('button[type=submit]');
  function setStatus(msg, ok) { status.textContent = msg; status.className = 'rv-status ' + (ok ? 'ok' : 'bad'); }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var f = form.elements;
    var payload = {
      name: f.name.value.trim(), company: f.company.value.trim(), project: f.project.value,
      rating: +(form.querySelector('input[name=rating]:checked') || { value: 5 }).value,
      text: f.text.value.trim(), consent: f.consent.checked, website: f.website.value,
      elapsed: Date.now() - startedAt, lang: document.documentElement.lang
    };
    if (payload.name.length < 2) return setStatus(t().name);
    if (payload.text.length < 20) return setStatus(t().text);
    if (!payload.consent) return setStatus(t().consent);

    btn.disabled = true; btn.lastChild.textContent = t().sending;
    fetch('api/reviews.php', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) })
      .then(function (r) { return r.json().then(function (j) { return { code: r.status, j: j }; }); })
      .then(function (res) {
        if (res.j.ok) { form.reset(); setStatus(t().ok, true); return; }
        if (res.code === 429) return setStatus(t().rate);
        var fl = (res.j.fields || [])[0];
        setStatus(fl && t()[fl] ? t()[fl] : t().err);
      })
      .catch(function () { setStatus(t().err); })
      .then(function () { btn.disabled = false; btn.lastChild.textContent = t().send; });
  });
})();
