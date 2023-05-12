# Solarpotential Große Dächer Berlin

## Ergebnisse
**`top_10000.xlsx`** enthält Daten zu den 10000 größten Dächern nach geeigneter Bruttofläche.

## Datengrundlage
### Solar-Daten: 
[Solarpotenzialanalyse Berlin, IP SYSCON im Auftrag der SenWEB](https://energieatlas.berlin.de/project/cardoMap/docs/Abschlussdokumentation_Solarpotenziale_Berlin_IP_SYSCON.pdf)
### Adress-Daten (zur Bestimmung des Bezirks):
[Geoportal Berlin](https://fbinter.stadt-berlin.de/fb/index.jsp), Datensatz "Adressen Berlin"
## Anleitung zum ausführen
### Daten Download:
#### Solar:
- Link: https://fbinter.stadt-berlin.de/fb/atom/solar/pv_2021.zip
- ZIP-Datei herunterladen & entpacken, Datei "gebaeude_pv_2021.gpkg" in Ordner data/solar ablegen
#### Adressen
- Link: https://fbinter.stadt-berlin.de/fb/atom/Hauskoordinaten/HKO_EPSG5650.zip
- ZIP-Datei herunterladen & entpacken, Datei "adressen-be_mitPLZ.txt" in Ordner data/addresses ablegen
### Ausführen:
- mitte_buildings.py ausführen
- Die N größten Dächer (einstellbarer Parameter) werden als Excel-Datei ausgegeben ("top_N.xlsx")