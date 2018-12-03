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