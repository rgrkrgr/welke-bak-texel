"""Zet referentie/data/afvalkalender-2026.json in index.html, zodat de pagina ook zonder webserver werkt.

Draai opnieuw na elke wijziging in de JSON:  python bouw.py
"""
import json
import re
from pathlib import Path

map_ = Path(__file__).parent
data = json.loads((map_ / "referentie/data/afvalkalender-2026.json").read_text(encoding="utf-8"))
html_pad = map_ / "index.html"
html = html_pad.read_text(encoding="utf-8")

inhoud = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
blok = f'<script type="application/json" id="kalender">{inhoud}</script>'
nieuw, n = re.subn(r'<script type="application/json" id="kalender">.*?</script>', lambda _: blok, html, flags=re.S)
if n != 1:
    raise SystemExit("Kalenderblok niet gevonden in index.html")
html_pad.write_text(nieuw, encoding="utf-8")
print("index.html bijgewerkt")
