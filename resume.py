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
*{box-sizing:border-box;margin:0;padding:0;-webkit-print-color-adjust:exact;print-color-adjust:exact}
html,body{background:#100904}
body{font-family:Inter,sans-serif;font-weight:500;font-feature-settings:"ss01" on;color:#ffedd7;font-size:9.6pt;line-height:1.4;width:210mm;height:297mm;display:grid;grid-template-columns:62mm 1fr;text-transform:uppercase}
aside{border-right:1px dashed #40372e;padding:14mm 7mm 12mm 10mm;display:flex;flex-direction:column;gap:7mm}
aside img{width:42mm;height:42mm;border-radius:3mm;object-fit:cover;filter:sepia(.18) saturate(.9)}
aside h3,h2{font-size:7.5pt;font-weight:500;color:#dc5000;margin-bottom:3mm}
.c{font-size:8.4pt;display:grid;gap:2.4mm}
.c b{display:block;font-weight:500;color:#b8a896;font-size:7pt}
.c a{color:#ffedd7;text-decoration:none;text-transform:none}
.sk{display:grid;gap:3mm;font-size:8pt}
.sk b{font-weight:500;display:block}
.sk span{color:#b8a896;text-transform:none;font-weight:400;font-size:8.4pt}
main{padding:15mm 12mm 13mm 10mm;display:flex;flex-direction:column;gap:9mm}
h1{font-size:34pt;line-height:.9;font-weight:500}
.latin{color:#6c5f51;font-size:8.5pt;margin-top:2.5mm}
.role{font-size:11pt;margin-top:4mm}
.city{color:#b8a896;font-size:8pt;margin-top:1.5mm}
.badge{display:inline-flex;align-items:center;gap:2mm;font-size:7.5pt;color:#dc5000;margin-bottom:5mm}
.badge i{width:1.8mm;height:1.8mm;border-radius:50%;background:#dc5000}
section{border-top:1px dashed #40372e;padding-top:5mm}
p{text-transform:none;font-weight:400;font-size:10.4pt;line-height:1.5}
.job{display:flex;justify-content:space-between;font-size:9pt;margin-bottom:3mm}
.job span{color:#b8a896}
.p{margin-bottom:4.2mm}
.p b{font-weight:500;font-size:9.6pt}
.p em{font-style:normal;color:#b8a896;font-size:8pt}
.p div{color:#e9d6bf;font-size:9.2pt;text-transform:none;font-weight:400;margin-top:.8mm}
.e{display:flex;justify-content:space-between;gap:4mm;margin-bottom:4mm;font-size:8.6pt}
.e b{font-weight:500}
.e div span{display:block;color:#b8a896;font-size:9pt;text-transform:none;font-weight:400;margin-top:.6mm}
.e small{color:#b8a896;white-space:nowrap;font-size:8pt}
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
  <div style="border:0"><span class="badge"><i></i>{ok}</span>
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
