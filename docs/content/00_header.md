# Projektinformations-System (PIS)
## Aufgabe der Anwendung
Das Projektinformationssystem (nachfolgend mit PIS bezeichnet) ist eine Webapplikation, mit der ein Unternehmen 
relevante Informationen zu kundenspezifischen Projekten verwalten kann. Dazu gehören insbesondere:

## Übersicht der fachlichen Funktionen
- Verwaltung der Projektdaten
    - Anlegen, Ändern und Löschen von Projektdaten
- Verwaltung der Kundendaten
    - Anlegen, Ändern und Löschen von Kundendaten
- Verwaltung der Mitarbeiterdaten
    - Anlegen, Ändern und Löschen von Mitarbeiterdaten
- Projektübersicht als Auswertung
    - Projektübersicht mit allen Projekten
        - nach Projektbezeichnung sortiert
        - Auflistung der Projektmitarbeiter, sortiert nach Name, Vorname
        - wöchentlicher Aufwand.
        
## Allgemeines zum Applikationsaufbau
Die Applikation wurde mit CherryPy in Python entwickelt. Es wird das Model-View-Controller (MVC) Entwurfsmuster 
zur Strukturierung der Applikation verwendet. Als Template-Engine wird mako verwendet. Die erzeugten Daten der Models 
werden in JSON-Dateien gespeichert. 