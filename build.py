#!/usr/bin/env python3
"""Собирает 5 страниц портфолио с общей шапкой/футером. Запуск: python3 build.py"""
from pathlib import Path

ROOT = Path(__file__).parent / "dist"
SITE = "https://maxperepelitsa.store"
TG = "https://t.me/xxxtentac1onxx"
GH = "https://github.com/makc999-hab"
V = "13"  # cache-buster для css/js

def ico(d, extra=""):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"{extra}>{d}</svg>'

I = {
    "home": ico('<path d="M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6h-6v6H4a1 1 0 0 1-1-1z"/>'),
    "about": ico('<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="11" r="2"/><path d="M6 16c.6-1.5 1.7-2.2 3-2.2s2.4.7 3 2.2M14 10h4M14 13h3"/>'),
    "projects": ico('<path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>'),
    "services": ico('<path d="m8 8-4 4 4 4M16 8l4 4-4 4M13.5 5l-3 14"/>'),
    "contact": ico('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>'),
    "pin": ico('<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>'),
    "case": ico('<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 13h18"/>'),
    "arrow": ico('<path d="M5 12h14M13 6l6 6-6 6"/>'),
    "ext": ico('<path d="M7 17 17 7M8 7h9v9"/>'),
    "grid": ico('<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>'),
    "layout": ico('<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/>'),
    "cart": ico('<circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h3l2.7 12.4a2 2 0 0 0 2 1.6h7.6a2 2 0 0 0 2-1.5L21 8H6"/>'),
    "play": ico('<rect x="2" y="4" width="20" height="16" rx="3"/><path d="m10 9 5 3-5 3z"/>'),
    "bot": ico('<rect x="4" y="8" width="16" height="12" rx="3"/><path d="M12 4v4M9 13v1M15 13v1M2 14h2M20 14h2"/>'),
    "app": ico('<rect x="4" y="4" width="16" height="16" rx="3"/><path d="M4 9h16M9 20V9"/>'),
    "tgapp": ico('<rect x="5" y="2" width="14" height="20" rx="3"/><path d="m9 11 6-3-2 7-1.5-2.5z"/>'),
    "down": ico('<path d="M12 3v12M7 10l5 5 5-5M4 21h16"/>'),
    "reviews": ico('<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/><path d="m12 7 1.1 2.2 2.4.3-1.8 1.7.5 2.4-2.2-1.2-2.2 1.2.5-2.4-1.8-1.7 2.4-.3z"/>'),
    "phone": ico('<rect x="6" y="2" width="12" height="20" rx="3"/><path d="M11 18h2"/>'),
}
TG_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M21.9 4.3 18.7 19.4c-.2 1.1-.9 1.3-1.8.8l-4.9-3.6-2.4 2.3c-.3.3-.5.5-1 .5l.3-5 9.1-8.2c.4-.4-.1-.6-.6-.2L6.2 13 1.4 11.5c-1-.3-1.1-1 .2-1.5L20.6 2.8c.9-.3 1.6.2 1.3 1.5z"/></svg>'
GH_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 .5a11.5 11.5 0 0 0-3.6 22.4c.6.1.8-.3.8-.6v-2c-3.2.7-3.9-1.5-3.9-1.5-.5-1.3-1.3-1.7-1.3-1.7-1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1 1.8 2.8 1.3 3.4 1 .1-.8.4-1.3.8-1.6-2.6-.3-5.3-1.3-5.3-5.7 0-1.3.5-2.3 1.2-3.1-.1-.3-.5-1.5.1-3.1 0 0 1-.3 3.2 1.2a11 11 0 0 1 5.8 0C17.3 4.8 18.3 5.1 18.3 5.1c.6 1.6.2 2.8.1 3.1.8.8 1.2 1.8 1.2 3.1 0 4.4-2.7 5.4-5.3 5.7.4.4.8 1.1.8 2.2v3.2c0 .3.2.7.8.6A11.5 11.5 0 0 0 12 .5z"/></svg>'

NAV = [("home", "index.html", "Главная"), ("about", "about.html", "Обо мне"),
       ("projects", "projects.html", "Проекты"), ("reviews", "reviews.html", "Отзывы"),
       ("services", "services.html", "Услуги"),
       ("contact", "contact.html", "Контакты")]

def page(key, file, title, desc, body, cta=True, scripts=()):
    act = ' class="active" aria-current="page"'
    links = "".join(
        f'<a href="{f if f != "index.html" else "./"}"{act if k == key else ""}>'
        f'{I[k]}<span data-i18n="nav.{k}">{label}</span></a>' for k, f, label in NAV)
    url = SITE + "/" + ("" if file == "index.html" else file)
    cta_html = f'''
<div class="wrap"><section><div class="cta">
  <div><h3 data-i18n="cta.title">Есть идея проекта?</h3><p data-i18n="cta.text">Напишите мне в Telegram — обычно отвечаю в течение пары часов.</p></div>
  <a class="btn btn-dark" href="{TG}" target="_blank" rel="noopener">{TG_SVG}<span data-i18n="cta.btn">Написать</span></a>
</div></section></div>''' if cta else ""
    return f'''<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title data-i18n="title.{key}">{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Max Perepelitsa">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/og.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#100904">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="stylesheet" href="assets/style.css?v={V}">
<script>document.documentElement.classList.add('anim');setTimeout(function(){{if(!window.__animOk)document.documentElement.classList.remove('anim')}},2500)</script>
</head>
<body>
<header class="topbar"><a class="logo" href="./">Max Perepelitsa</a><nav class="nav" aria-label="Навигация">{links}</nav>
<div class="lang" role="group" aria-label="Language"><button data-lang="ru">RU</button><button data-lang="en">EN</button></div></header>
<div class="side-label" aria-hidden="true">Max Perepelitsa · Portfolio 2026 · Vladivostok</div>
<main>{body}{cta_html}</main>
<footer><div class="wrap"><span>© 2026 Max Perepelitsa · <span data-i18n="footer.art">аватар — арт Nemo</span></span><a href="privacy.html" data-i18n="footer.privacy">Политика конфиденциальности</a></div></footer>
<script src="assets/app.js?v={V}"></script>
<script src="assets/motion.js?v={V}"></script>
<script src="assets/anim.js?v={V}"></script>{"".join(f'<script src="assets/{js}?v={V}"></script>' for js in scripts)}
</body>
</html>
'''

HOME = f'''
<div class="wrap"><section class="hero">
  <div>
    <span class="badge"><i class="dot"></i><span data-i18n="status">Открыт для заказов</span></span>
    <h1 data-i18n="hero.hi">Привет, я Max<br>Perepelitsa</h1>
    <div class="role" aria-live="polite"><span id="role-text">Веб-разработчик</span><i class="caret"></i></div>
    <p class="lead" data-i18n="hero.lead">Создаю быстрые сайты, Telegram-ботов и приложения, которые приводят бизнесу клиентов. Мне 24, я из Владивостока — делаю всё сам: от идеи и дизайна до запуска на боевом сервере.</p>
    <div class="meta">
      <span>{I["pin"]}<span data-i18n="hero.city">Владивосток, Приморский край</span></span>
      <span>{I["case"]}<span data-i18n="hero.now">Свободен сейчас</span></span>
    </div>
    <div class="actions">
      <a class="btn btn-dark" href="{TG}" target="_blank" rel="noopener">{I["arrow"]}<span data-i18n="hero.hire">Нанять меня</span></a>
      <a class="btn btn-light js-cv" href="assets/resume-ru.pdf" download>{I["down"]}<span data-i18n="hero.cv">Скачать резюме</span></a>
    </div>
    <div class="follow"><span data-i18n="hero.follow">Я в сети:</span>
      <a href="{TG}" target="_blank" rel="noopener" aria-label="Telegram">{TG_SVG}</a>
      <a href="{GH}" target="_blank" rel="noopener" aria-label="GitHub">{GH_SVG}</a>
    </div>
  </div>
  <div class="avatar"><img src="assets/avatar.webp" width="736" height="736" alt="Max Perepelitsa — аватар" fetchpriority="high"></div>
</section></div>'''

STACK = ["HTML / CSS / JavaScript", "PHP", "Python", "aiogram", "FastAPI", "SwiftUI", "Telegram Bot API",
         "Telegram Mini Apps", "ЮKassa / СБП", "SQLite", "Docker", "Nginx", "Linux VPS", "Figma", "Git"]
ABOUT = f'''
<div class="wrap">
<div class="page-head"><div class="eyebrow" data-i18n="about.eyebrow">Обо мне</div>
<h1 data-i18n="about.h1">Разработчик, который доводит проект <em>от идеи до запуска</em></h1></div>
<section class="about-grid">
  <div>
    <p data-i18n="about.p1">Меня зовут Максим, мне 24 года, я из Владивостока. Делаю сайты, Telegram-ботов, Mini Apps и iOS-приложения для малого бизнеса и стартапов.</p>
    <p data-i18n="about.p2">Я не просто рисую макет — я собираю работающий продукт: вёрстка, бэкенд, оплата, сервер, домен и SSL. Клиент получает готовый результат, которым можно пользоваться с первого дня.</p>
    <p data-i18n="about.p3">Люблю скорость и детали: сайт пекарни, который я сделал, набирает 99/100 в Google Lighthouse на мобильных, а каждый проект я проверяю на реальных телефонах.</p>
  </div>
  <div class="stats">
    <div class="stat"><b>4+</b><span data-i18n="about.s1">запущенных проекта</span></div>
    <div class="stat"><b>99</b><span data-i18n="about.s2">баллов Lighthouse</span></div>
    <div class="stat"><b>100%</b><span data-i18n="about.s3">полный цикл</span></div>
    <div class="stat"><b>24</b><span data-i18n="about.s4">года</span></div>
  </div>
</section>
<section><h2 data-i18n="about.stack">Инструменты и технологии</h2>
<div class="chips">{"".join(f'<span class="chip">{s}</span>' for s in STACK)}</div></section>
<section><h2 data-i18n="about.how">Как я работаю</h2>
<div class="steps">
  <div class="step"><h3 data-i18n="about.st1h">Бриф</h3><p data-i18n="about.st1p">Обсуждаем цели, структуру, дизайн и бюджет — до первой строчки кода.</p></div>
  <div class="step"><h3 data-i18n="about.st2h">Дизайн</h3><p data-i18n="about.st2p">Собираю визуальный стиль и показываю прототип на согласование.</p></div>
  <div class="step"><h3 data-i18n="about.st3h">Разработка</h3><p data-i18n="about.st3p">Пишу код и присылаю промежуточные результаты — вы всегда в курсе.</p></div>
  <div class="step"><h3 data-i18n="about.st4h">Запуск</h3><p data-i18n="about.st4p">Настраиваю домен, хостинг и SSL, поддерживаю проект после запуска.</p></div>
</div></section>
</div>'''

TAGKEYS = {'Интернет-магазин': 'tag.shop', 'Презентация': 'tag.pres', 'Видео': 'tag.video', 'Инвесторы': 'tag.inv', 'Telegram-бот': 'tag.bot'}

def card(shot, title, tags, pkey, ptext, link=None, lkey="proj.open", ltext="Открыть"):
    tk = TAGKEYS
    tag_html = "".join(f'<span data-i18n="{tk[t]}">{t}</span>' if t in tk else f"<span>{t}</span>" for t in tags)
    if link:
        a = f'<a class="card-link" href="{link}" target="_blank" rel="noopener"><span data-i18n="{lkey}">{ltext}</span>{I["ext"]}</a>'
    else:
        a = f'<span class="card-link off" data-i18n="{lkey}">{ltext}</span>'
    return f'''<article class="card">{shot}<div class="card-body">
<h3 data-i18n="{pkey[:-2]}.t">{title}</h3><div class="tags">{tag_html}</div><p data-i18n="{pkey}">{ptext}</p>{a}</div></article>'''

CAL_MOCK = """<div class="shot phones green">
<div class="phone-frame side"><img src="assets/calorie-2.webp" width="360" height="783" alt="CalorieAI — дневник питания" loading="lazy"></div>
<div class="phone-frame"><img src="assets/calorie-1.webp" width="360" height="783" alt="CalorieAI — главный экран с калориями и БЖУ" loading="lazy"></div>
<div class="phone-frame side"><img src="assets/calorie-3.webp" width="360" height="783" alt="CalorieAI — отчёт по весу" loading="lazy"></div>
</div>"""

PROJECTS = f'''
<div class="wrap">
<div class="page-head"><div class="eyebrow" data-i18n="proj.eyebrow">Портфолио</div>
<h1 data-i18n="proj.h1">Избранные <em>проекты</em></h1>
<p data-i18n="proj.lead">Реальные продукты для реального бизнеса — от интернет-магазина до презентации для инвесторов, Telegram-сервиса и мобильного приложения.</p></div>
<section class="projects">
{card('<div class="shot"><img src="assets/morehleba.webp" width="1200" height="750" alt="Сайт пекарни Море хлеба" loading="lazy"></div>',
      "Море хлеба", ["Интернет-магазин", "PHP", "ЮKassa", "CRM"], "proj.mh.p",
      "Интернет-магазин ремесленной пекарни во Владивостоке: каталог с КБЖУ, корзина, вход по звонку, личный кабинет, оплата через ЮKassa и CRM для заказов. 99/100 в Lighthouse на мобильных.",
      "https://morehleba.ru/")}
{card('<div class="shot"><img src="assets/vmr.webp" width="1200" height="750" alt="Презентация ВМР ТРАНС" loading="lazy"></div>',
      "ВМР ТРАНС", ["Презентация", "Видео", "Инвесторы"], "proj.vmr.p",
      "Кинематографичная видео-презентация для инвесторов компании по аквакультуре на Дальнем Востоке: 16 полноэкранных слайдов с видео и ленивой загрузкой — быстро открывается даже с мобильного интернета.",
      "https://maxperepelitsa.store/vmr-trans/")}
{card('<div class="shot phones dark"><div class="phone-frame side"><img src="assets/greymax-1.webp" width="360" height="780" alt="GREYMAX — экран приветствия" loading="lazy"></div><div class="phone-frame"><img src="assets/greymax-2.webp" width="360" height="780" alt="GREYMAX — главный экран Mini App" loading="lazy"></div><div class="phone-frame side"><img src="assets/greymax-3.webp" width="360" height="780" alt="GREYMAX — выбор тарифа" loading="lazy"></div></div>',
      "GREYMAX", ["Telegram-бот", "Mini App", "Python", "Подписки"], "proj.gm.p",
      "Telegram-бот с оплатой подписок и Mini App с фирменным маскотом: автоматическая выдача доступа после оплаты через ЮKassa и СБП, личный кабинет, работа 24/7 на собственном сервере.",
      None, "proj.nda", "Коммерческий проект · демо по запросу")}
{card(CAL_MOCK, "CalorieAI", ["iOS", "SwiftUI", "API"], "proj.cal.p",
      "iOS-трекер питания в духе FatSecret: дневник, подсчёт калорий и БЖУ, гибридный поиск продуктов (локальная база + API через собственный сервер), отчёты по весу и прогрессу.",
      None, "proj.ios", "iOS-приложение · демо по запросу")}
</section></div>'''

def svc(n, icon, title, text, items, price, term):
    lis = "".join(f'<li data-i18n="svc.{n}{c}">{t}</li>' for c, t in zip("abc", items))
    return f'''<div class="svc"><div class="ico">{I[icon]}</div><h3 data-i18n="svc.{n}h">{title}</h3>
<p data-i18n="svc.{n}p">{text}</p><ul>{lis}</ul>
<div class="price"><b><span data-i18n="svc.from">от</span> {price} ₽</b><small data-i18n="svc.{n}t">{term}</small></div></div>'''

SERVICES = f'''
<div class="wrap">
<div class="page-head"><div class="eyebrow" data-i18n="svc.eyebrow">Услуги</div>
<h1 data-i18n="svc.h1">Что я могу <em>сделать для вас</em></h1>
<p data-i18n="svc.lead">Цены — стартовые. Итоговая стоимость зависит от объёма задач: после короткого обсуждения пришлю точную оценку и сроки.</p></div>
<section><div class="services">
{svc(1, "layout", "Лендинг", "Одностраничный сайт для бизнеса, услуги или мероприятия, который превращает посетителей в заявки.", ["Индивидуальный дизайн", "Мобильная версия и SEO", "Настройка хостинга, домена и SSL"], "20 000", "5–10 дней")}
{svc(2, "cart", "Интернет-магазин", "Каталог, корзина, онлайн-оплата, личный кабинет клиента и админка для заказов.", ["Оплата ЮKassa / СБП", "Вход по SMS или звонку", "CRM для заказов"], "70 000", "3–5 недель")}
{svc(3, "play", "Сайт-презентация", "Эффектная презентация для инвесторов или партнёров с видео и анимацией.", ["Полноэкранные слайды", "Видео и анимации", "Быстрая загрузка"], "30 000", "1–2 недели")}
{svc(4, "bot", "Telegram-бот", "Бот для заказов, записи, подписок или поддержки — работает 24/7.", ["Оплата внутри Telegram", "Админ-панель и уведомления", "Деплой на сервер"], "20 000", "1–3 недели")}
{svc(5, "tgapp", "Telegram Mini App", "Полноценное веб-приложение внутри Telegram: магазин, сервис или личный кабинет.", ["Интерфейс как у нативного приложения", "Авторизация через Telegram", "Оплата и бэкенд"], "60 000", "3–6 недель")}
{svc(6, "phone", "iOS-приложение (первая версия)", "Мобильное приложение на SwiftUI, чтобы проверить идею или дать клиентам удобный инструмент.", ["SwiftUI, нативный вид", "API и сервер", "Помощь с публикацией в App Store"], "120 000", "4–8 недель")}
</div>
<p class="note" data-i18n="svc.oferta">Цены указаны для ознакомления и не являются публичной офертой (ст. 437 ГК РФ).</p>
<p class="note" data-i18n="svc.note">Также беру поддержку и доработку существующих проектов, настройку серверов (VPS, Docker, Nginx) и перенос доменов — пишите, обсудим.</p>
</section></div>'''

CONTACT = f'''
<div class="wrap">
<div class="page-head"><div class="eyebrow" data-i18n="ct.eyebrow">Контакты</div>
<h1 data-i18n="ct.h1">Давайте <em>обсудим</em></h1>
<p data-i18n="ct.lead">Быстрее всего со мной связаться в Telegram. Расскажите коротко о проекте — я отвечу с идеями, сроками и ценой.</p></div>
<section>
<div class="contact-card">
  <div><h2 data-i18n="ct.card">Пишите в Telegram — это самый быстрый способ начать проект</h2>
  <p data-i18n="ct.cardp">Без форм и ожидания: сообщение приходит мне напрямую.</p></div>
  <div><a class="btn" href="{TG}" target="_blank" rel="noopener" style="width:100%">{TG_SVG}<span data-i18n="ct.btn">Написать в Telegram</span></a>
  <div class="handle">@xxxtentac1onxx</div></div>
</div>
<div class="info">
  <div><b data-i18n="ct.i1">Город</b><span data-i18n="ct.i1v">Владивосток, Приморский край (UTC+10)</span></div>
  <div><b data-i18n="ct.i2">Ответ</b><span data-i18n="ct.i2v">Обычно в течение 1–2 часов</span></div>
  <div><b data-i18n="ct.i3">Формат</b><span data-i18n="ct.i3v">Удалённо, работаю с клиентами по всей России</span></div>
</div>
</section></div>'''

PRIVACY = f'''
<div class="wrap legal">
<div class="page-head"><div class="eyebrow" data-i18n="pv.eyebrow">Документы</div>
<h1 data-i18n="pv.h1">Политика конфиденциальности</h1>
<p data-i18n="pv.date">Редакция от 25 сентября 2026 года (добавлен раздел об отзывах)</p></div>
<section data-i18n="pv.body">
<h2>1. Кто я</h2>
<p>Сайт maxperepelitsa.store — личное портфолио Максима Перепелицы (далее — «владелец сайта»). Связь: Telegram <a href="{TG}">@xxxtentac1onxx</a>.</p>
<h2>2. Какие данные собирает сайт</h2>
<p>При обычном просмотре сайт <b>не собирает персональные данные</b>: на нём нет регистрации, систем веб-аналитики (Яндекс Метрика, Google Analytics и т. п.), рекламных пикселей и cookie-файлов. Шрифты и все файлы загружаются с того же сервера, без обращений к сторонним сервисам. Единственная форма на сайте — форма отзыва (см. раздел 4).</p>
<p>В памяти браузера (localStorage) сохраняется только выбранный язык интерфейса («ru» или «en»). Эта настройка не передаётся владельцу сайта и не позволяет вас идентифицировать; удалить её можно, очистив данные сайта в браузере.</p>
<h2>3. Технические журналы хостинга</h2>
<p>Как и любой веб-сервер, хостинг-провайдер (ООО «Таймвэб», серверы в России) автоматически ведёт технические журналы запросов (IP-адрес, дата и время, запрошенная страница, данные браузера). Они нужны для работы и защиты сайта, не используются владельцем для идентификации посетителей и хранятся в соответствии с правилами провайдера.</p>
<h2>4. Отзывы</h2>
<p>Если вы оставляете отзыв, обрабатываются: имя, компания или должность (по желанию), выбранный проект, оценка и текст отзыва. Цель — публикация отзыва на странице «Отзывы» после проверки. Обработка ведётся на основании вашего <a href="consent.html">согласия</a>, данные хранятся на сервере хостинг-провайдера в России до отзыва согласия. Для защиты от спама на сутки сохраняется необратимый хэш IP-адреса, по которому вас нельзя определить. Чтобы удалить или изменить отзыв, напишите мне в Telegram.</p>
<h2>5. Переход в Telegram и на другие сайты</h2>
<p>Кнопки «Нанять меня», «Написать» и подобные ведут в мессенджер Telegram, ссылки в разделе «Проекты» — на сторонние сайты. Если вы пишете мне в Telegram, вы сами решаете, какие сведения сообщить; они используются только для ответа на ваше обращение и обсуждения заказа и не передаются третьим лицам. Обработка данных внутри Telegram и на сторонних сайтах регулируется их собственными политиками.</p>
<h2>6. Ваши права</h2>
<p>Вы можете в любой момент отозвать согласие, попросить удалить отзыв, нашу переписку и сведения, которые вы мне сообщили, написав в Telegram. Вопросы по этой политике — туда же.</p>
<h2>7. Изменения</h2>
<p>При изменении состава собираемых данных политика будет обновлена заранее. Обработка ведётся в соответствии с Федеральным законом № 152-ФЗ «О персональных данных».</p>
</section></div>'''

REVIEWS = f'''
<div class="wrap">
<div class="page-head"><div class="eyebrow" data-i18n="rv.eyebrow">Отзывы</div>
<h1 data-i18n="rv.h1">Что говорят <em>клиенты</em></h1>
<p data-i18n="rv.lead">Отзывы оставляют сами заказчики, я только проверяю их на спам перед публикацией.</p></div>
<section><div id="reviews-list" class="reviews" aria-live="polite"><p class="rv-empty">…</p></div></section>
<section><div class="rv-form-wrap">
<h2 data-i18n="rv.formh">Оставить отзыв</h2>
<p class="rv-note" data-i18n="rv.formp">Мы работали вместе? Расскажите, как всё прошло. Отзыв появится после проверки.</p>
<form id="review-form" class="rv-form" novalidate>
  <label><span data-i18n="rv.name">Ваше имя *</span><input name="name" maxlength="60" required autocomplete="name"></label>
  <label><span data-i18n="rv.company">Компания или должность</span><input name="company" maxlength="80" autocomplete="organization"></label>
  <label><span data-i18n="rv.project">Проект</span><select name="project">
    <option value="morehleba" data-i18n="rv.p1">Море хлеба</option><option value="vmr" data-i18n="rv.p2">ВМР ТРАНС</option>
    <option value="greymax">GREYMAX</option><option value="calorieai">CalorieAI</option>
    <option value="other" data-i18n="rv.p5" selected>Другой проект</option></select></label>
  <fieldset class="rv-rating"><legend data-i18n="rv.rating">Оценка</legend>
    <div class="rv-stars-in">{"".join(f'<input type="radio" id="r{n}" name="rating" value="{n}"{" checked" if n == 5 else ""}><label for="r{n}" title="{n}">★</label>' for n in range(5, 0, -1))}</div>
  </fieldset>
  <label class="full"><span data-i18n="rv.text">Отзыв *</span><textarea name="text" rows="5" maxlength="1000" required></textarea></label>
  <div class="hp" aria-hidden="true"><label>Website<input name="website" tabindex="-1" autocomplete="off"></label></div>
  <label class="rv-consent full"><input type="checkbox" name="consent" required>
    <span data-i18n="rv.consent">Я даю <a href="consent.html" target="_blank">согласие на обработку и публикацию</a> моего имени, компании и отзыва на этом сайте и принимаю <a href="privacy.html" target="_blank">политику конфиденциальности</a>.</span></label>
  <div class="full rv-actions"><button type="submit" class="btn btn-dark"><span data-i18n="rv.send">Отправить отзыв</span></button>
  <p id="rv-status" class="rv-status" role="status"></p></div>
</form></div></section>
</div>'''

CONSENT = f'''
<div class="wrap legal">
<div class="page-head"><div class="eyebrow" data-i18n="pv.eyebrow">Документы</div>
<h1 data-i18n="cs.h1">Согласие на обработку персональных данных</h1>
<p data-i18n="cs.date">Для формы отзыва · редакция от 25 сентября 2026 года</p></div>
<section data-i18n="cs.body">
<p>Отправляя отзыв на сайте maxperepelitsa.store, я свободно, своей волей и в своём интересе даю согласие Перепелице Максиму Викторовичу (далее — «оператор», связь: Telegram <a href="{TG}">@xxxtentac1onxx</a>) на обработку моих персональных данных на следующих условиях.</p>
<h2>1. Какие данные</h2>
<p>Имя, компания или должность (если указаны), выбранный проект, оценка и текст отзыва.</p>
<h2>2. Цель</h2>
<p>Публикация отзыва о работе оператора на странице maxperepelitsa.store/reviews.html.</p>
<h2>3. Действия с данными</h2>
<p>Сбор, запись, хранение, уточнение, использование, распространение (публикация на сайте), удаление. Обработка ведётся без передачи третьим лицам, данные хранятся на сервере в России.</p>
<h2>4. Данные, разрешённые для распространения</h2>
<p>Неограниченному кругу лиц на указанной странице сайта могут быть показаны: имя, компания или должность, проект, оценка, текст отзыва и месяц его публикации. Иная передача и обработка этих данных третьими лицами мной не разрешается.</p>
<h2>5. Срок и отзыв согласия</h2>
<p>Согласие действует до его отзыва. Отозвать согласие и потребовать удалить отзыв можно в любой момент, написав оператору в Telegram; отзыв будет удалён в течение 3 рабочих дней.</p>
</section></div>'''

PAGES = [
    ("home", "index.html", "Max Perepelitsa — веб-разработчик и создатель Telegram-ботов",
     "Портфолио Max Perepelitsa: сайты, интернет-магазины, Telegram-боты, Mini Apps и iOS-приложения под ключ. Владивосток, работаю удалённо.", HOME, False),
    ("about", "about.html", "Обо мне — Max Perepelitsa",
     "Разработчик из Владивостока: сайты, Telegram-боты и приложения полного цикла — от идеи до запуска.", ABOUT, True),
    ("projects", "projects.html", "Проекты — Max Perepelitsa",
     "Портфолио: интернет-магазин пекарни, видео-презентация для инвесторов, Telegram-сервис подписок и iOS-трекер питания.", PROJECTS, True),
    ("reviews", "reviews.html", "Отзывы клиентов — Max Perepelitsa",
     "Отзывы клиентов о работе Max Perepelitsa: сайты, Telegram-боты и приложения.", REVIEWS, True, ("reviews.js",)),
    ("services", "services.html", "Услуги и цены — Max Perepelitsa",
     "Разработка лендингов, интернет-магазинов, Telegram-ботов, Mini Apps и iOS-приложений. Цены от 20 000 ₽.", SERVICES, True),
    ("contact", "contact.html", "Контакты — Max Perepelitsa",
     "Напишите в Telegram @xxxtentac1onxx, чтобы обсудить проект.", CONTACT, False),
    ("privacy", "privacy.html", "Политика конфиденциальности — Max Perepelitsa",
     "Политика конфиденциальности сайта maxperepelitsa.store.", PRIVACY, False),
    ("consent", "consent.html", "Согласие на обработку персональных данных — Max Perepelitsa",
     "Согласие на обработку и публикацию персональных данных для формы отзыва.", CONSENT, False),
]

HTACCESS = """RewriteEngine On
RewriteCond %{HTTPS} off
RewriteCond %{HTTP:X-Forwarded-Proto} !https
RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

<IfModule mod_expires.c>
ExpiresActive On
ExpiresByType image/webp "access plus 30 days"
ExpiresByType image/png "access plus 30 days"
ExpiresByType text/css "access plus 30 days"
ExpiresByType application/javascript "access plus 30 days"
</IfModule>
<IfModule mod_deflate.c>
AddOutputFilterByType DEFLATE text/html text/css application/javascript image/svg+xml
</IfModule>
"""

if __name__ == "__main__":
    import shutil
    shutil.rmtree(ROOT, ignore_errors=True)
    shutil.copytree(Path(__file__).parent / "assets", ROOT / "assets")
    (ROOT / ".htaccess").write_text(HTACCESS)
    for key, file, title, desc, body, cta, *extra in PAGES:
        (ROOT / file).write_text(page(key, file, title, desc, body, cta, *extra), encoding="utf-8")
    # серверная часть отзывов (PHP) + секретный конфиг, которого нет в git
    shutil.copytree(Path(__file__).parent / "server", ROOT, dirs_exist_ok=True)
    secret = Path(__file__).parent / "server-secret" / "config.php"
    if secret.exists():
        shutil.copy(secret, ROOT / "api" / "config.php")
        (ROOT / "api" / "config.php").chmod(0o644)
    else:
        print("ВНИМАНИЕ: нет server-secret/config.php — запустите make_config.sh")
    urls = "".join(f"<url><loc>{SITE}/{'' if f == 'index.html' else f}</loc></url>" for _, f, *_ in PAGES if f != "consent.html")
    urls += f"<url><loc>{SITE}/vmr-trans/</loc></url>"
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    print("built:", sorted(p.name for p in ROOT.iterdir()))
