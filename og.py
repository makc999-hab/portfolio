#!/usr/bin/env python3
"""Собирает превью для соцсетей assets/og.jpg (1200×630) в стиле сайта. Запуск: python3 og.py"""
import re, subprocess, time
from pathlib import Path

HERE = Path(__file__).parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

fonts = "".join(re.findall(r"@font-face \{.*?\}", (HERE / "assets/style.css").read_text(), re.S)).replace("url(fonts/", "url(../assets/fonts/")
HTML = f"""<!doctype html><html><head><meta charset="utf-8"><style>{fonts}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1200px;height:630px;background:#100904;color:#ffedd7;font-family:Inter,sans-serif;font-weight:500;text-transform:uppercase;
  display:grid;grid-template-columns:1fr 400px;gap:56px;align-items:center;padding:0 72px;position:relative;overflow:hidden}}
body::before{{content:"";position:absolute;left:72px;right:72px;top:64px;border-top:1px dashed #40372e}}
body::after{{content:"";position:absolute;left:72px;right:72px;bottom:64px;border-top:1px dashed #40372e}}
.top{{position:absolute;left:72px;right:72px;top:30px;display:flex;justify-content:space-between;font-size:16px}}
.top span:last-child{{color:#6c5f51}}
.bot{{position:absolute;left:72px;right:72px;bottom:30px;display:flex;justify-content:space-between;font-size:16px;color:#b8a896}}
.badge{{display:flex;align-items:center;gap:12px;color:#dc5000;font-size:18px;margin-bottom:26px}}
.badge i{{width:9px;height:9px;border-radius:50%;background:#dc5000}}
h1{{font-size:88px;line-height:.88;font-weight:500}}
.role{{font-size:26px;color:#b8a896;margin-top:28px;line-height:1.2}}
img{{width:400px;height:400px;border-radius:12px;object-fit:cover;filter:sepia(.18) saturate(.9)}}
</style></head><body>
<div class="top"><span>Max Perepelitsa</span><span>Portfolio 2026</span></div>
<div><div class="badge"><i></i>Открыт для заказов</div>
<h1>Max<br>Perepelitsa</h1>
<div class="role">Сайты · Telegram-боты · Приложения</div></div>
<img src="../assets/avatar.webp" alt="">
<div class="bot"><span>maxperepelitsa.store</span><span>Vladivostok</span></div>
</body></html>"""

if __name__ == "__main__":
    out = HERE / "resume"; out.mkdir(exist_ok=True)
    src = out / "og.html"; src.write_text(HTML, encoding="utf-8")
    png = out / "og.png"
    png.unlink(missing_ok=True)
    p = subprocess.Popen([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--user-data-dir=/private/tmp/claude-501/chr-og",
                          "--window-size=1200,630", "--force-device-scale-factor=1", "--virtual-time-budget=3000",
                          f"--screenshot={png}", src.as_uri()],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(60):  # headless Chrome иногда не выходит сам — ждём файл и закрываем
        time.sleep(0.5)
        if png.exists() and png.stat().st_size > 0: time.sleep(0.5); break
    p.kill()
    subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "88", str(png), "--out", str(HERE / "assets/og.jpg")],
                   stdout=subprocess.DEVNULL, check=True)
    png.unlink()
    print("og.jpg", (HERE / "assets/og.jpg").stat().st_size)
