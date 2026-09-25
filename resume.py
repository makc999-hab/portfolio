#!/usr/bin/env python3
"""Собирает резюме RU/EN в PDF (assets/resume-ru.pdf, resume-en.pdf). Запуск: python3 resume.py"""
import subprocess, time
from pathlib import Path

HERE = Path(__file__).parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

DATA = {
 "ru": dict(
  name="Максим Перепелица", latin="Max Perepelitsa",
  role="Веб-разработчик · Telegram-боты · iOS",
  city="Владивосток, Приморский край · 24 года",
  h_about="О себе",
  about="Делаю сайты, Telegram-ботов, Mini Apps и iOS-приложения полного цикла: дизайн, вёрстка, бэкенд, "
        "платежи, сервер, домен и SSL. Довожу проекты до запуска и поддерживаю после. Слежу за скоростью "
        "(99/100 в Google Lighthouse на мобильных) и за удобством на телефоне.",
  h_exp="Опыт", job="Фриланс-разработчик", period="2026 — наст. время",
  projects=[
   ("Море хлеба", "интернет-магазин пекарни", "Каталог с КБЖУ, корзина, вход по звонку, личный кабинет, оплата ЮKassa, CRM для заказов. Ускорил сайт с 60 до 99 баллов Lighthouse."),
   ("ВМР ТРАНС", "презентация для инвесторов", "16 полноэкранных видеослайдов, ленивая загрузка видео, адаптация под мобильные, публикация на хостинге."),
   ("GREYMAX", "Telegram-бот и Mini App", "Продажа подписок, автоматическая выдача доступа, оплата ЮKassa и СБП, админ-функции; Python (aiogram), SQLite, Docker, VPS 24/7."),
   ("CalorieAI", "iOS-приложение", "Трекер питания на SwiftUI: дневник, подсчёт калорий и БЖУ, гибридный поиск продуктов через собственный API-прокси, отчёты."),
  ],
  h_skills="Навыки",
  skills=[("Фронтенд", "HTML, CSS, JavaScript, адаптивная вёрстка, анимации, SEO, оптимизация скорости"),
          ("Бэкенд", "Python (aiogram, FastAPI), PHP, SQLite, REST API"),
          ("Мобильная разработка", "SwiftUI (iOS), Telegram Mini Apps"),
          ("Инфраструктура", "Linux VPS, Docker, Nginx, SSL, FTP-деплой, Git"),
          ("Интеграции", "Telegram Bot API, ЮKassa, СБП, SMS-сервисы, внешние API")],
  h_edu="Образование",
  edu=[("Владивостокский государственный университет (ВВГУ)", "Кафедра информационных технологий и систем, бакалавриат", "2024 — наст. время"),
       ("Колледж ВВГУ в г. Артёме", "09.02.03 «Программирование в компьютерных системах»", "2020 — 2024")],
  h_contacts="Контакты",
 ),
 "en": dict(
  name="Max Perepelitsa", latin="Максим Перепелица",
  role="Web Developer · Telegram Bots · iOS",
  city="Vladivostok, Russia · 24 years old",
  h_about="About",
  about="I build websites, Telegram bots, Mini Apps and iOS apps end to end, from design, layout and backend "
        "to payments, server, domain and SSL. I take projects all the way to launch and support them afterwards. "
        "I focus on speed (99/100 on Google Lighthouse for mobile) and on how things work on a phone.",
  h_exp="Experience", job="Freelance developer", period="2026 — present",
  projects=[
   ("More Hleba", "bakery online store", "Catalog with nutrition facts, cart, phone-call login, customer account, YooKassa payments and an order CRM. I raised its Lighthouse score from 60 to 99."),
   ("VMR TRANS", "investor presentation", "16 fullscreen video slides with lazy-loaded video, mobile layout and hosting setup."),
   ("GREYMAX", "Telegram bot & Mini App", "Subscription sales with automatic access delivery, YooKassa and SBP payments and admin tools. Built with Python (aiogram), SQLite and Docker on a VPS running 24/7."),
   ("CalorieAI", "iOS app", "A SwiftUI nutrition tracker with a food diary, calorie and macro counting, hybrid food search through my own API proxy, and reports."),
  ],
  h_skills="Skills",
  skills=[("Frontend", "HTML, CSS, JavaScript, responsive layout, animation, SEO, performance"),
          ("Backend", "Python (aiogram, FastAPI), PHP, SQLite, REST APIs"),
          ("Mobile", "SwiftUI (iOS), Telegram Mini Apps"),
          ("Infrastructure", "Linux VPS, Docker, Nginx, SSL, FTP deployment, Git"),
          ("Integrations", "Telegram Bot API, YooKassa, SBP, SMS services, third-party APIs")],
  h_edu="Education",
  edu=[("Vladivostok State University (VVSU)", "Department of Information Technologies and Systems, Bachelor's program", "2024 — present"),
       ("VVSU College, Artyom", "Programming in Computer Systems (09.02.03)", "2020 — 2024")],
  h_contacts="Contacts",
 ),
}

CSS = """
@page{size:A4;margin:0}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Inter,sans-serif;color:#111;font-size:10.2pt;line-height:1.45;width:210mm;height:297mm;display:grid;grid-template-columns:64mm 1fr}
aside{background:#0b0b0b;color:#eee;padding:14mm 8mm 12mm 10mm;display:flex;flex-direction:column;gap:7mm}
aside img{width:40mm;height:40mm;border-radius:5mm;object-fit:cover}
aside h3{font-size:8pt;letter-spacing:.12em;text-transform:uppercase;color:#9a9a9a;margin-bottom:2.5mm}
.c{font-size:9pt;display:grid;gap:1.8mm}
.c b{display:block;font-weight:600;color:#fff}
.c a{color:#bbb;text-decoration:none}
.sk{display:grid;gap:2.6mm;font-size:8.8pt}
.sk b{color:#fff;font-weight:600;display:block}
.sk span{color:#bbb}
main{padding:14mm 12mm 12mm 11mm;display:flex;flex-direction:column;gap:6mm}
h1{font-size:27pt;line-height:1.05;letter-spacing:-.02em;font-weight:800}
.latin{color:#777;font-size:10pt;margin-top:1mm}
.role{font-family:'Playfair Display',serif;font-weight:700;font-size:14pt;margin-top:3mm}
.city{color:#555;font-size:9.5pt;margin-top:1.5mm}
.badge{display:inline-flex;align-items:center;gap:2mm;background:#ececec;border-radius:10mm;padding:1mm 3.5mm;font-size:8.5pt;font-weight:500;margin-bottom:3mm}
.badge i{width:2mm;height:2mm;border-radius:50%;background:#16a34a}
h2{font-size:10pt;letter-spacing:.12em;text-transform:uppercase;border-bottom:1.5px solid #111;padding-bottom:1.5mm;margin-bottom:3mm}
.job{display:flex;justify-content:space-between;font-weight:700;margin-bottom:2.5mm}
.job span{font-weight:500;color:#666}
.p{margin-bottom:2.8mm;padding-left:3.5mm;border-left:2px solid #e3e3e3}
.p b{font-weight:700}
.p em{font-style:normal;color:#666}
.p div{color:#333;font-size:9.4pt}
.e{display:flex;justify-content:space-between;gap:4mm;margin-bottom:2.5mm}
.e div span{display:block;color:#555;font-size:9.2pt}
.e small{color:#666;white-space:nowrap;font-size:9pt}
"""

def html(d, lang):
    ok = "Открыт для заказов" if lang == "ru" else "Available for freelance work"
    projects = "".join(f'<div class="p"><b>{n}</b> <em>— {t}</em><div>{x}</div></div>' for n, t, x in d["projects"])
    skills = "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in d["skills"])
    edu = "".join(f'<div class="e"><div><b>{a}</b><span>{b}</span></div><small>{c}</small></div>' for a, b, c in d["edu"])
    site = "Сайт-портфолио" if lang == "ru" else "Portfolio"
    import re
    fonts = "".join(re.findall(r"@font-face \{.*?\}", (HERE / "assets/style.css").read_text(), re.S)).replace("url(fonts/", "url(../assets/fonts/")
    return f"""<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>{d['name']} — CV</title>
<style>{fonts}{CSS}</style></head><body>
<aside>
  <img src="../assets/avatar.webp" alt="">
  <div><h3>{d['h_contacts']}</h3><div class="c">
    <div><b>Telegram</b><a href="https://t.me/xxxtentac1onxx">@xxxtentac1onxx</a></div>
    <div><b>{site}</b><a href="https://maxperepelitsa.store">maxperepelitsa.store</a></div>
    <div><b>GitHub</b><a href="https://github.com/makc999-hab">github.com/makc999-hab</a></div>
  </div></div>
  <div><h3>{d['h_skills']}</h3><div class="sk">{skills}</div></div>
</aside>
<main>
  <div><span class="badge"><i></i>{ok}</span>
    <h1>{d['name']}</h1><div class="latin">{d['latin']}</div>
    <div class="role">{d['role']}</div><div class="city">{d['city']}</div></div>
  <section><h2>{d['h_about']}</h2><p>{d['about']}</p></section>
  <section><h2>{d['h_exp']}</h2><div class="job">{d['job']}<span>{d['period']}</span></div>{projects}</section>
  <section><h2>{d['h_edu']}</h2>{edu}</section>
</main></body></html>"""

if __name__ == "__main__":
    out = HERE / "resume"; out.mkdir(exist_ok=True)
    for lang, d in DATA.items():
        src = out / f"resume-{lang}.html"
        src.write_text(html(d, lang), encoding="utf-8")
        pdf = HERE / "assets" / f"resume-{lang}.pdf"
        p = subprocess.Popen([CHROME, "--headless=new", "--disable-gpu", "--user-data-dir=/private/tmp/claude-501/chr-cv",
                              "--no-pdf-header-footer", f"--print-to-pdf={pdf}", src.as_uri()],
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        for _ in range(40):
            time.sleep(0.5)
            if pdf.exists() and pdf.stat().st_size > 0 and p.poll() is not None: break
        p.kill()
        print(pdf.name, pdf.stat().st_size if pdf.exists() else "FAILED")
