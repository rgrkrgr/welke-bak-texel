# Project: website met afvalkalender Texel

## Doel
Bezoekers zien in één oogopslag welke kleur container er **deze week** aan de weg moet.

## Functionaliteit
1. **Zonder adres (standaard):** toon de container(s) van de huidige week voor heel Texel
   (grijs / oranje / groen + blauw), plus de volgende week. Feestdagen en inhaaldagen tonen als die week van toepassing zijn.
2. **Met postcode + huisnummer:** toon aanvullende informatie voor dat adres:
   - de precieze ophaaldag(en) op basis van de route (gebied/dorp/straat → weekdag)
   - blauwe container: De Cocksdorp en Oosterend maandag, rest van het eiland dinsdag
   - grofvuil- en grof-tuinafvaldag, inhaaldagen en uitzonderingen
   - eventueel: dichtstbijzijnd inzamelpunt voor papier

## Aandachtspunten
- De gemeente publiceert routes per dorp/wijk (bijv. Den Burg centrum / West / Oost) en losse straten,
  **niet per postcode**. Er is een koppeltabel nodig van adres → route. Zie "Open vragen" in `referentie/bronnen.md`.
- Adres opzoeken kan via de gratis PDOK Locatieserver (postcode + huisnummer → straat, woonplaats, wijk/buurt).
- Snelheid en eenvoud gaan boven alles: de belangrijkste informatie staat bovenaan, zonder klikken.
- Mobiel eerst: de meeste bezoekers kijken op hun telefoon.
- Postcode en huisnummer alleen in de browser van de bezoeker bewaren, niet op een server.

## Mappen
- `referentie/data/` – brondata (PDF's, CSV/JSON)
- `referentie/afbeeldingen/` – afbeeldingen en screenshots
- `referentie/teksten/` – paginateksten
- `.claude/skills/` – geïnstalleerde skills (ui-ux-pro-max e.a.), niet aanpassen

## Databronnen
Zie `referentie/bronnen.md` voor beschrijving, legenda en aandachtspunten.
- **Gebruik voor de site: `referentie/data/afvalkalender-2026.json`** — alle weken met containers, grofvuil- en groftuinafvaldagen, feestdagen, inhaaldagen, routes per weekdag en uitzonderingen. Dit is de bron van waarheid; de PDF en website zijn de oorsprong.
- Afvalkalender 2026 (PDF): `referentie/data/Afvalkalender-Texel-2026.pdf`
- Ophaalroutes: https://www.texel.nl/direct-regelen/afval/afval-ophalen/afvalkalender-en-ophaalroute/

Belangrijk: de kalenderdata zit in kleuren. Gebruik de afbeeldingen in `referentie/afbeeldingen/` om de weken af te lezen.
