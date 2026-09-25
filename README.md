# maxperepelitsa.store

Personal portfolio of **Max Perepelitsa**, a web developer from Vladivostok who builds websites, Telegram bots, Mini Apps and iOS apps.

**Live:** https://maxperepelitsa.store

## Features
- 7 static pages (home, about, projects, reviews, services, contact and legal), with no frameworks or build tools beyond one Python script
- RU / EN switcher: Russian lives in the HTML for SEO, and English comes from a small JS dictionary
- Client reviews: a PHP endpoint with JSON storage and file locking, plus a password-protected moderation panel with CSRF protection and login throttling
- Anti-spam: a honeypot field, a form-timing check, a per-IP daily limit (only a salted IP hash is stored) and a link filter
- Self-hosted fonts and no third-party requests, analytics or cookies (for compliance with Russian Federal Law 152-FZ)
- One-page A4 CV in PDF, generated from HTML with headless Chrome
- Lighthouse-friendly: WebP images, lazy loading and cache headers

## Structure
```
build.py          # generates dist/ (pages, sitemap, robots, .htaccess)
resume.py         # builds assets/resume-{ru,en}.pdf
assets/           # CSS, JS, fonts, images
server/api/       # reviews.php, lib.php
server/admin/     # moderation panel
make_config.sh    # creates server-secret/config.php (admin password hash, salt); not in git
```

## Build
```sh
./make_config.sh      # once
python3 build.py      # -> dist/
python3 resume.py     # optional, rebuild the CV PDFs
```
Upload the contents of `dist/` to any Apache host with PHP 7.4+.
