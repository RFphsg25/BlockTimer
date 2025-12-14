# Projekt Applikation

Dieses Git-Repository wurde im Rahmen des Moduls "Projekt Applikation" im Herbstsemester 2025 der Pädagogischen Hochschule St.Gallen erstellt.

## Entwickler:innen

Der Autor dieses Repositories ist Reto Frischknecht, Student der Pädagogischen Hochschule St.Gallen des Jahrgangs 2022.

## Inhalt

Dieses Repository beinhaltet den **BlockTimer**, der Schülerinnen und Schülern in Arbeits- und Prüfungssituationen durch eine visuelle Hilfestellung die Organisation erleichtern soll.

Das Programm ermöglicht es, Unterrichtsphasen als farbige Zeitblöcke zu visualisieren. So können die Lernenden auf einen Blick erkennen, wie viel Zeit noch für welche Phase verbleibt.

### Funktionen

- Eingabe von 1 bis 6 Zeitblöcken mit Namen und Zeit (Stunden, Minuten, Sekunden)
- zufällige farbige Darstellung der Zeitblöcke proportional zur Gesamtzeit
- Countdown-Balken läuft über die Zeitblöcke
- Anzeige, wenn die Zeit abgelaufen ist

### Verwendung

Das Programm wird mit `python main.py` gestartet.

Nach dem Start werden die Zeitblöcke eingegeben:
1. Anzahl Zeitblöcke (1-6)
2. Für jeden Block: Stunden, Minuten, Sekunden und Name eingeben
3. Der Timer startet automatisch

**Beispiel:**
- Block 1: "Einführung" - 0h 10min 0s
- Block 2: "Gruppenarbeit" - 0h 25min 0s
- Gesamtzeit: 35 Minuten

### Dateien

- `main.py` - Hauptprogramm mit Eingabe und Steuerung
- `countdown.py` - Countdown-Funktion
- `block.py` - Darstellung der Zeitblöcke

## Mögliche Erweiterungen

- Pause-Funktion
- Ton bei Blockwechsel
- Zeitpläne speichern

## Lizenz

Dieses Repository ist öffentlich zugänglich und kann in eigener Form weiterentwickelt werden.

## Datum

* 10.11.2025 - Erstellung v1 Readme
* 13.12.2025 - Anpassung der Lizenz-Readme - v2
* 14.12.2025 - Readme v3 fertiggestellt - Projekt V3 mit Input-System abgeschlossen