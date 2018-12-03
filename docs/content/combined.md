
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

## Grundsätzliches

### Order-Struktur
/app
: enthält die gesamte Applikationslogik

/app/config
: enthält die gesamten Konfigurations-Dateien

/app/controllers 
: enthält die spezifischen Applikations-Controller

/app/core
: enthält die Basis-Klassen zur globalen Verwendung

/app/models 
: enthält die spezifischen Models für die Interaktion mit den JSON-Dateien

/content/assets
: enthält alle statischen und kompilierten Elemente, wie z.B. JavaScript-Dateien und CSS-Dateien

/data
: enthält die erzeugten JSON-Dateien des Models

/docs
: enthält die Dokumentation der Anwendung

/ressources/saas
: enthält alle vorkompilierten CSS-Dateien in Saas

/views
: enthält die mako-Templates zur Anzeige im View

/views/_partials
: enthält allgemeine mako-Templates, welche unabhängig vom jeweiligen Template sind

### Starten des Cherrypy-Servers
Damit der Cherrypy-Applikationsserver gestartet werden kann, wird folgende Kommandozeile ausgeführt:
```bash
$ python3 server.py
```
Die Applikation ist anschließend unter http://localhost:8080 erreichbar.

### Routing
Die Applikation nutzt einen eigenen Routing-Dispatcher, welcher explizites Routing ermöglicht. Dadurch kann das Projekt
in einigen Schritten einfach in einen REST-Ansatz konvertiert werden. Weiterhin ist die Bennung der Funktionen unabhängig
von der URL-Struktur und es können verschiedene Parameter übergeben werden. Die gesamte Konfiguration des Routings ist 
in der app/config/routes.py zu finden.

## Komponenten
### Beschreibung der Basiskomponenten
In Allgemeinen besteht die gesamte Applikation aus vier Klassen: Controller.py, Model.py, Router.py, View.py. Diese 
Klassen sind für grundsätzliche applikationsunabhängige Aufgaben zuständig. Sie generalisieren also die Grund-Prozesse 
der Applikation. Im Einzelnen gehen wir auf diese kurz ein und beschreiben die Benutzung dieser.

#### Controller.py
Die Basis-Klasse des Controllers beinhaltet allgemeine Funktionen, welche für alle abgeleiteten Controller sinnvoll sind.
Der Controller arbeitet im MVC-Pattern hauptsächlich mit den Models zur Dateninteraktion und dem Views zur Präsentation
zusammen. Der Controller nimmt vom Router die entsprechende Funktion entgegen und verarbeitet diese dann.

#### Model.py
#### Router.py
#### View.py

### Programmierschnittstellen
#### Controller.py

##### Programmierschnittstellen
* `redirect(string url, dictonary params = {}, dictonary notificationData = {}) : null`
    * Beschreibung
    : erzeugt einen HTTP-Redirect an `url` mit `params` als HTTP-Argumente und `notificationData` als Flash-Message. 
    * Rückgabewerte
    : `null`
    
* `route(string route, dictonary params = {}) : string`
    * Beschreibung
    : generiert eine fertige Route aus `route` mithilfe der angegebenen Parameter in `params`
    * Rückgabewerte
    : `string` Konstrutierte Route, welche `params` enthält
    
#### Model.py



#### Router.py
* `getAllRoutes(list routerConfig) : RoutesDispatcher`
    * Beschreibung
    : generiert eine `RoutesDispatcher` anhand der übergebenen Liste in `routerConfig` und importiert dynamisch die 
      jeweiligen Controller für die Verwendung (Autoloading)
    * Rückgabewerte
    : `object`: RoutesDispatcher
    
#### View.py
* `__init__(string view_search_folder) : null`
    * Beschreibung
    : Konsturktor, welcher den Lookup-Folder für mako in `view_search_folder` setzt
    * Rückgabewerte
    : `null`
    
* `load(string template, dictonary data_opl={}) : string`
    * Beschreibung
    : Lädt das Template `template` und übergibt `data_opl` an das View als Parameter weiter
    * Rückgabewerte
    : `string`: fertig vom View gerenderter String zur Ausgabe
