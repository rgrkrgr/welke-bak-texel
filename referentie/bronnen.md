# Databronnen – Afvalkalender Texel

## 1. Afvalkalender 2026 (PDF)

- Bestand: `referentie/data/Afvalkalender-Texel-2026.pdf`
- Afbeeldingen van de pagina's: `referentie/afbeeldingen/afvalkalender-2026-pagina-1.png` en `-pagina-2.png`
- Online versie: https://openpdc.texel.nl/wp-content/uploads/2025/12/Afvalkalender-Texel-2026.pdf
  - Let op: de lokale PDF is gemaakt op 22-04-2026, de online link staat in de uploadmap van 2025/12. Controleer of ze hetzelfde zijn voordat je de data gebruikt.

### Pagina 1 – Huisvuilkalender 2026
Jaaroverzicht per maand met weeknummers. De betekenis zit in de **kleuren**, niet in de tekst.
Gewone tekstextractie (pdftotext) haalt die kleuren dus niet op. Lees de kalender af van de afbeelding en zet hem over naar gestructureerde data.

Legenda:
| Markering | Betekenis |
|---|---|
| Grijs weeknummer | Week van de grijze container (restafval) |
| Oranje/rood weeknummer | Week van de oranje container (plastic, blik, drankkartons) |
| Groen/blauw gedeeld weeknummer | Week van de groene (GFT) én blauwe (papier) container |
| Rood omkaderde dag | Grofvuil (dinsdag in de oranje week) |
| Groen omkaderde dag | Grof tuinafval (dinsdag in de groene week) |
| Paarse dag | Feest- of gedenkdag (geen ophaling) |
| Gele dag | Inhaaldag (als de ophaaldag op een feestdag valt) |

Weken wisselen in een vaste cyclus van drie (oranje → groen/blauw → grijs). Controleer dat wel per week tegen de afbeelding.

### Pagina 2 – Gemeentelijke informatie
Contactnummers, uitleg per container, inzamelpunten voor papier per dorp, oud ijzer, gebruikte kleding, glas
en afvalbrengstation De Hamster (De Vang 27, Oudeschild; openingstijden).
Containers moeten om 07.00 uur aan de weg staan.

## 2. Webpagina: afvalkalender en ophaalroute

- URL: https://www.texel.nl/direct-regelen/afval/afval-ophalen/afvalkalender-en-ophaalroute/
- Bevat:
  - **Ophaalroutes per weekdag per gebied/dorp** voor de groene, grijze en oranje container
  - Aparte tabel voor de **blauwe (papier) container**: De Cocksdorp en Oosterend op maandag, de rest van het eiland op dinsdag
  - Een lijst van de **komende weken** met welke afvalsoort dan wordt opgehaald, inclusief uitzonderingen (bijv. een verschoven ophaaldag voor bepaalde straten)
  - Plaatsingsregels voor de container (o.a. minstens 50 cm tussenruimte)
- Niet beschikbaar: geen API, geen iCal, geen postcodezoeker, geen download behalve de PDF. Data moet uit de HTML worden gehaald.
- Gerelateerde pagina's:
  - Afvalwijzer: https://www.texel.nl/direct-regelen/afval/afval-ophalen/afvalwijzer
  - Grofvuil: https://www.texel.nl/direct-regelen/afval/afval-ophalen/grof-vuil-en-grof-tuinafval/
  - Soorten afval: https://www.texel.nl/direct-regelen/afval/soorten-afval/

## Hoe de bronnen samenhangen
De PDF zegt **welke week** welke container wordt geleegd. De webpagina zegt **op welke weekdag** dat in elk gebied gebeurt.
Samen geven ze de precieze ophaaldatum per gebied. Uitzonderingen en inhaaldagen gaan voor op het vaste patroon.

## Omgezette data
`referentie/data/afvalkalender-2026.json` bevat de kalender (afgelezen van de PDF) plus routes en uitzonderingen (van de website, 24-10-2026).
- Welke feestdag door welke inhaaldag wordt vervangen staat niet expliciet in de PDF; gekoppeld aan de inhaaldag in dezelfde week (`koppeling_afgeleid: true`).
- Kleurcodes (`kleur_hex`) zijn benaderd van de PDF.
- Nieuwe uitzonderingen op de website handmatig toevoegen aan `uitzonderingen`.

## Open vragen
- **Adres → route:** de webpagina deelt routes in per dorp/wijk/straat (Den Burg centrum, Den Burg West, Den Burg Oost,
  Eierland, 't Noorden, Oost, De Westen, losse straten zoals Bosrandweg, Nieuwlanderweg, Zuid Haffel).
  De grenzen van deze gebieden staan niet op de site. Opties: grenzen opvragen bij de gemeente (14 0222),
  of zelf een koppeltabel maken op straatniveau met PDOK-data.
- Eenmalig overnemen of periodiek opnieuw ophalen (scrapen) van de webpagina?
- Voor 2027 komt er een nieuwe kalender; die moet dan opnieuw worden ingelezen.
