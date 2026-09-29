(function () {
  var root = document.documentElement;
  var M = window.Motion;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!M || reduce) { root.classList.remove('anim'); return; }
  window.__animOk = true;

  var animate = M.animate, stagger = M.stagger, inView = M.inView;
  var ease = [0.22, 1, 0.36, 1];

  // Первый экран и заголовки страниц: каскад при загрузке
  var intro = document.querySelectorAll('.hero > div:first-child > *, .page-head > *');
  if (intro.length) {
    animate(intro, { opacity: [0, 1], y: [24, 0] },
      { duration: 0.7, delay: stagger(0.08, { startDelay: 0.05 }), ease: ease });
  }
  var avatar = document.querySelector('.avatar');
  if (avatar) {
    animate(avatar, { opacity: [0, 1], scale: [0.92, 1], rotate: [6, 1.5] },
      { duration: 0.9, delay: 0.25, ease: ease });

    // Лёгкий наклон аватара за курсором (только мышь, не тач)
    if (matchMedia('(hover: hover)').matches) {
      avatar.addEventListener('pointermove', function (e) {
        var r = avatar.getBoundingClientRect();
        var x = (e.clientX - r.left) / r.width - 0.5;
        var y = (e.clientY - r.top) / r.height - 0.5;
        animate(avatar, { rotateY: x * 10, rotateX: -y * 10, rotate: 0, scale: 1.02, transformPerspective: 800 },
          { type: 'spring', stiffness: 200, damping: 20 });
      });
      avatar.addEventListener('pointerleave', function () {
        animate(avatar, { rotateY: 0, rotateX: 0, rotate: 1.5, scale: 1, transformPerspective: 800 },
          { type: 'spring', stiffness: 150, damping: 18 });
      });
    }
  }
  root.classList.remove('anim'); // стартовые стили больше не нужны — дальше управляет Motion

  // Блоки ниже первого экрана: появляются при прокрутке, группой с задержкой
  var groups = ['.projects', '.services', '.steps', '.stats', '.chips', '.info',
                '.about-grid > div:first-child', '.contact-card', '.cta', '.rv-form-wrap'];
  groups.forEach(function (sel) {
    document.querySelectorAll(sel).forEach(function (group) {
      var items = group.children.length > 1 && !group.matches('.contact-card, .cta, .rv-form-wrap, .about-grid > div')
        ? Array.prototype.slice.call(group.children) : [group];
      items.forEach(function (el) { el.style.opacity = '0'; });
      inView(group, function () {
        animate(items, { opacity: [0, 1], y: [28, 0] },
          { duration: 0.6, delay: stagger(0.07), ease: ease });
      }, { amount: 0.15 });
    });
  });

  // Отзывы подгружаются с сервера позже — анимируем их при появлении
  var rv = document.getElementById('reviews-list');
  if (rv && window.MutationObserver) {
    new MutationObserver(function () {
      var cards = rv.querySelectorAll('.rv');
      if (cards.length) animate(cards, { opacity: [0, 1], y: [20, 0] }, { duration: 0.5, delay: stagger(0.06), ease: ease });
    }).observe(rv, { childList: true });
  }
})();
