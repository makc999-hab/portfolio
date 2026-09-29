(function () {
  var EN = {
    'nav.home': 'Home', 'nav.about': 'About', 'nav.projects': 'Projects', 'nav.reviews': 'Reviews', 'nav.services': 'Services', 'nav.contact': 'Contact',
    'status': 'Available for freelance work',
    'footer.art': 'avatar art by Nemo', 'footer.privacy': 'Privacy policy',
    'hero.cv': 'Download CV',
    'cta.title': 'Have a project in mind?',
    'cta.text': 'Message me on Telegram. I usually reply within a couple of hours.',
    'cta.btn': 'Message me',

    // home
    'title.home': 'Max Perepelitsa | Web & Telegram Developer',
    'hero.hi': 'Hi, I\'m Max<br>Perepelitsa',
    'hero.lead': 'I build fast websites, Telegram bots and apps that bring clients to businesses. I\'m 24, based in Vladivostok, and I handle everything myself, from the first idea to launch on a live server.',
    'hero.city': 'Vladivostok, Primorsky Krai',
    'hero.now': 'Available now',
    'hero.hire': 'Hire me',
    'hero.works': 'View projects',
    'hero.follow': 'Follow me:',

    // about
    'title.about': 'About | Max Perepelitsa',
    'about.eyebrow': 'About me',
    'about.h1': 'A developer who takes a project <em>from idea to launch</em>',
    'about.p1': 'I\'m Max, 24, from Vladivostok. I make websites, Telegram bots, Mini Apps and iOS apps for small businesses and startups.',
    'about.p2': 'I don\'t just hand over a design mockup. I build a working product: the layout, the backend, payments, a server, a domain and SSL. The client gets a finished result they can use from day one.',
    'about.p3': 'I care about speed and details. My bakery website scores 99/100 in Google Lighthouse on mobile, and every project is tested on real phones.',
    'about.s1': 'launched projects', 'about.s2': 'Lighthouse score', 'about.s3': 'full cycle', 'about.s4': 'years old',
    'about.stack': 'Tools and technologies',
    'about.how': 'How I work',
    'about.st1h': 'Brief', 'about.st1p': 'We discuss your goals, the structure, the design and the budget before I write any code.',
    'about.st2h': 'Design', 'about.st2p': 'I build the visual style and show you a prototype to approve.',
    'about.st3h': 'Development', 'about.st3p': 'I write the code and send you progress updates, so you always know where things stand.',
    'about.st4h': 'Launch', 'about.st4p': 'I set up the domain, hosting and SSL, and support the project after launch.',

    // projects
    'title.projects': 'Projects | Max Perepelitsa',
    'proj.eyebrow': 'Portfolio',
    'proj.h1': 'Selected <em>projects</em>',
    'proj.lead': 'Real products for real businesses: an online store, an investor presentation, a Telegram service and a mobile app.',
    'proj.mh.p': 'An online store for a craft bakery in Vladivostok. It has a catalog with calories and nutrition info, a cart, phone-call login, a customer account, YooKassa payments and a CRM for orders. It scores 99/100 on Lighthouse for mobile.',
    'proj.vmr.p': 'A cinematic video presentation for investors in an aquaculture company in the Russian Far East. It has 16 fullscreen slides with video and lazy loading, so it opens fast even on mobile data.',
    'proj.gm.p': 'A Telegram bot with paid subscriptions, plus a Mini App with its own mascot. Access is granted automatically after payment through YooKassa or SBP, users get a personal account, and it runs 24/7 on my own server.',
    'proj.nda': 'Commercial project · demo on request',
    'proj.cal.p': 'An iOS nutrition tracker similar to FatSecret. It has a food diary, calorie and macro counting, hybrid food search (a local database plus an API through my own server) and weight and progress reports.',
    'proj.mh.t': 'More Hleba bakery', 'proj.vmr.t': 'VMR TRANS',
    'tag.shop': 'Online store', 'tag.pres': 'Presentation', 'tag.video': 'Video', 'tag.inv': 'Investors', 'tag.bot': 'Telegram bot',
    'proj.case': 'Read the case study', 'proj.open': 'Open', 'proj.bot': 'Open bot', 'proj.ios': 'iOS app · demo on request',

    // services
    'title.services': 'Services & Prices | Max Perepelitsa',
    'svc.eyebrow': 'Services',
    'svc.h1': 'What I can <em>build for you</em>',
    'svc.lead': 'The prices below are starting points. The final cost depends on the scope, so after a short conversation I\'ll send you an exact estimate and timeline.',
    'svc.from': 'from',
    'svc.1h': 'Landing page', 'svc.1p': 'A one-page website for a business, service or event that turns visitors into leads.',
    'svc.1a': 'Custom design', 'svc.1b': 'Mobile version and SEO', 'svc.1c': 'Hosting, domain and SSL setup', 'svc.1t': '5–10 days',
    'svc.2h': 'Online store', 'svc.2p': 'A catalog, cart, online payment, customer account and an admin panel for orders.',
    'svc.2a': 'YooKassa / SBP payments', 'svc.2b': 'SMS or phone-call login', 'svc.2c': 'CRM for orders', 'svc.2t': '3–5 weeks',
    'svc.3h': 'Presentation website', 'svc.3p': 'A striking presentation for investors or partners with video and animation.',
    'svc.3a': 'Fullscreen slides', 'svc.3b': 'Video and animation', 'svc.3c': 'Fast loading', 'svc.3t': '1–2 weeks',
    'svc.4h': 'Telegram bot', 'svc.4p': 'A bot for orders, bookings, subscriptions or support that works 24/7.',
    'svc.4a': 'Payments inside Telegram', 'svc.4b': 'Admin panel and notifications', 'svc.4c': 'Deployment to a server', 'svc.4t': '1–3 weeks',
    'svc.5h': 'Telegram Mini App', 'svc.5p': 'A full web app inside Telegram: a store, a service or a personal account.',
    'svc.5a': 'Native-feeling UI', 'svc.5b': 'Sign in with Telegram', 'svc.5c': 'Payments and backend', 'svc.5t': '3–6 weeks',
    'svc.6h': 'iOS app (first version)',
    'svc.oferta': 'Prices are for reference only and are not a public offer.', 'svc.6p': 'A mobile app in SwiftUI to test an idea or give your customers a handy tool.',
    'svc.6a': 'SwiftUI, native look', 'svc.6b': 'API and server', 'svc.6c': 'App Store release help', 'svc.6t': '4–8 weeks',
    'svc.note': 'I also offer support and updates for existing projects, server setup (VPS, Docker, Nginx) and domain moves. Just write to me and we\'ll discuss it.',
    'svc.btn': 'Discuss a project',

    // contact
    'title.contact': 'Contact | Max Perepelitsa',
    'ct.eyebrow': 'Contact',
    'ct.h1': 'Let\'s <em>talk</em>',
    'ct.lead': 'The fastest way to reach me is Telegram. Tell me a bit about your project and I\'ll reply with ideas, a timeline and a price.',
    'ct.card': 'Message me on Telegram. It\'s the fastest way to start a project',
    'ct.cardp': 'No forms and no waiting. Your message comes straight to me.',
    'ct.btn': 'Message on Telegram',
    'ct.i1': 'Location', 'ct.i1v': 'Vladivostok, Russia (UTC+10)',
    'ct.i2': 'Reply time', 'ct.i2v': 'Usually within 1–2 hours',
    'title.privacy': 'Privacy Policy | Max Perepelitsa',
    'pv.eyebrow': 'Legal', 'pv.h1': 'Privacy policy', 'pv.date': 'Version of 25 September 2026 (reviews section added)',
    'pv.body': '<h2>1. Who I am</h2><p>maxperepelitsa.store is the personal portfolio of Max Perepelitsa (the site owner). Contact: Telegram <a href="https://t.me/xxxtentac1onxx">@xxxtentac1onxx</a>.</p>'
      + '<h2>2. What data this site collects</h2><p>When you just browse, this site <b>does not collect personal data</b>. It has no sign-ups, analytics (such as Yandex Metrica or Google Analytics), ad pixels or cookies. Fonts and all other files load from this server, with no requests to third-party services. The only form on the site is the review form (see section 4).</p><p>Your browser\'s local storage keeps only your interface language (ru or en). This setting is never sent to the site owner and cannot identify you. You can remove it by clearing this site\'s data in your browser.</p>'
      + '<h2>3. Hosting logs</h2><p>Like any web server, the hosting provider (Timeweb LLC, servers in Russia) automatically keeps technical request logs: IP address, date and time, the requested page and browser data. These logs keep the site running and protected. The owner does not use them to identify visitors, and they are stored under the provider\'s rules.</p>'
      + '<h2>4. Reviews</h2><p>If you leave a review, I process your name, company or job title (optional), the selected project, your rating and the review text. The purpose is to publish the review on the Reviews page after moderation. This is based on your <a href="consent.html">consent</a>, and the data is stored on the hosting provider\'s server in Russia until you withdraw it. To prevent spam, a one-way hash of your IP address is kept for 24 hours. It cannot be used to identify you. To edit or remove your review, message me on Telegram.</p>'
      + '<h2>5. Telegram and other websites</h2><p>Buttons such as “Hire me” lead to Telegram, and links on the Projects page lead to other websites. If you message me on Telegram, you decide what to share. I use it only to reply and discuss your project, and I never pass it to third parties. Telegram and other websites handle data under their own policies.</p>'
      + '<h2>6. Your rights</h2><p>You can withdraw your consent at any time, or ask me to delete your review, our conversation and anything you shared, by writing to me on Telegram. Send any questions about this policy there too.</p>'
      + '<h2>7. Changes</h2><p>If the data this site collects changes, I will update this policy first. Personal data is processed under Russian Federal Law No. 152-FZ.</p>',
    'title.reviews': 'Client Reviews | Max Perepelitsa',
    'rv.eyebrow': 'Reviews', 'rv.h1': 'What <em>clients</em> say',
    'rv.lead': 'Clients write these reviews themselves. I only check them for spam before they go live.',
    'rv.formh': 'Leave a review', 'rv.formp': 'Have we worked together? Tell me how it went. Your review will appear after moderation.',
    'rv.name': 'Your name *', 'rv.company': 'Company or job title', 'rv.project': 'Project',
    'rv.p1': 'More Hleba bakery', 'rv.p2': 'VMR TRANS', 'rv.p5': 'Other project', 'rv.rating': 'Rating', 'rv.text': 'Review *',
    'rv.consent': 'I give my <a href="consent.html" target="_blank">consent to the processing and publication</a> of my name, company and review on this site and accept the <a href="privacy.html" target="_blank">privacy policy</a>.',
    'rv.send': 'Send review',
    'title.consent': 'Consent to Personal Data Processing | Max Perepelitsa',
    'cs.h1': 'Consent to personal data processing', 'cs.date': 'For the review form · version of 25 September 2026',
    'cs.body': '<p>By submitting a review on maxperepelitsa.store, I freely and in my own interest consent to Maksim Viktorovich Perepelitsa (the operator, contact: Telegram <a href="https://t.me/xxxtentac1onxx">@xxxtentac1onxx</a>) processing my personal data on the following terms.</p>'
      + '<h2>1. Data</h2><p>Name, company or job title (if given), the selected project, rating and review text.</p>'
      + '<h2>2. Purpose</h2><p>Publishing a review of the operator\'s work at maxperepelitsa.store/reviews.html.</p>'
      + '<h2>3. Actions</h2><p>Collection, recording, storage, correction, use, dissemination (publication on the site) and deletion. The data is not passed to third parties and is stored on a server in Russia.</p>'
      + '<h2>4. Data allowed for dissemination</h2><p>The following may be shown to anyone on that page: name, company or job title, project, rating, review text and the month it was published. I do not allow third parties to pass on or otherwise process this data.</p>'
      + '<h2>5. Term and withdrawal</h2><p>This consent is valid until withdrawn. You can withdraw it and ask to delete your review at any time by messaging the operator on Telegram. The review will be removed within 3 business days.</p>',
    'ct.i3': 'Format', 'ct.i3v': 'Remote, working with clients across Russia'
  };
  var ROLES = {
    ru: ['Веб-разработчик', 'Разработчик Telegram-ботов', 'Создатель Mini Apps', 'iOS-разработчик'],
    en: ['Web Developer', 'Telegram Bot Developer', 'Mini App Creator', 'iOS Developer']
  };

  var nodes = document.querySelectorAll('[data-i18n]');
  nodes.forEach(function (n) { n.dataset.ru = n.innerHTML; });
  var titleNode = document.querySelector('title');

  if (window.EN_EXTRA) for (var ek in window.EN_EXTRA) EN[ek] = window.EN_EXTRA[ek]; // тексты кейсов из build.py
  function getLang() {
    try { var s = localStorage.getItem('lang'); if (s) return s; } catch (e) {}
    return (navigator.language || 'ru').toLowerCase().indexOf('ru') === 0 ? 'ru' : 'en';
  }
  var lang = getLang();

  function apply(l) {
    lang = l;
    document.documentElement.lang = l;
    nodes.forEach(function (n) {
      var k = n.getAttribute('data-i18n');
      n.innerHTML = l === 'en' && EN[k] ? EN[k] : n.dataset.ru;
    });
    document.title = titleNode.textContent;
    document.querySelectorAll('.lang button').forEach(function (b) {
      b.classList.toggle('on', b.dataset.lang === l);
      b.setAttribute('aria-pressed', b.dataset.lang === l);
    });
    document.querySelectorAll('.js-cv').forEach(function (a) { a.href = 'assets/resume-' + l + '.pdf'; });
    try { localStorage.setItem('lang', l); } catch (e) {}
    restartTyping();
    document.dispatchEvent(new Event('langchange'));
  }

  document.querySelectorAll('.lang button').forEach(function (b) {
    b.addEventListener('click', function () { apply(b.dataset.lang); });
  });

  // typing effect
  var el = document.getElementById('role-text');
  var timer;
  function restartTyping() {
    if (!el) return;
    clearTimeout(timer);
    var list = ROLES[lang], i = 0, pos = 0, del = false;
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) { el.textContent = list[0]; return; }
    (function tick() {
      var word = list[i];
      pos += del ? -1 : 1;
      el.textContent = word.slice(0, pos);
      var d = del ? 40 : 85;
      if (!del && pos === word.length) { del = true; d = 1800; }
      else if (del && pos === 0) { del = false; i = (i + 1) % list.length; d = 350; }
      timer = setTimeout(tick, d);
    })();
  }

  apply(lang);
})();
