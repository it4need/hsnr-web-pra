
# Aufgabe der Anwendung
Das Projektinformationssystem (nachfolgend mit PIS bezeichnet) ist eine Webapplikation, mit der ein Unternehmen 
relevante Informationen zu kundenspezifischen Projekten verwalten kann. Dazu gehören insbesondere:

# Übersicht der fachlichen Funktionen
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
        
# Allgemeines zum Applikationsaufbau
Die Applikation wurde mit CherryPy in Python entwickelt. Es wird das Model-View-Controller (MVC) Entwurfsmuster 
zur Strukturierung der Applikation verwendet. Als Template-Engine wird mako verwendet. Die erzeugten Daten der Models 
werden in JSON-Dateien gespeichert. 

# Grundsätzliches

## Order-Struktur
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

## Starten des Cherrypy-Servers
Damit der Cherrypy-Applikationsserver gestartet werden kann, wird folgende Kommandozeile ausgeführt:
```bash
$ python3 server.py
```
Die Applikation ist anschließend unter http://localhost:8080 erreichbar.

## Routing
Die Applikation nutzt einen eigenen Routing-Dispatcher, welcher explizites Routing ermöglicht. Dadurch kann das Projekt
in einigen Schritten einfach in einen REST-Ansatz konvertiert werden. Weiterhin ist die Bennung der Funktionen unabhängig
von der URL-Struktur und es können verschiedene Parameter übergeben werden. Die gesamte Konfiguration des Routings ist 
in der app/config/routes.py zu finden.

# Komponenten
## Beschreibung der Basiskomponenten
In Allgemeinen besteht die gesamte Applikation aus vier Klassen: Controller.py, Model.py, Router.py, View.py. Diese 
Klassen sind für grundsätzliche applikationsunabhängige Aufgaben zuständig. Sie generalisieren also die Grund-Prozesse 
der Applikation. Im Einzelnen gehen wir auf diese kurz ein und beschreiben die Benutzung dieser.

### Controller.py
Die Basis-Klasse des Controllers beinhaltet allgemeine Funktionen, welche für alle abgeleiteten Controller sinnvoll sind.
Der Controller arbeitet im MVC-Pattern hauptsächlich mit den Models zur Dateninteraktion und dem Views zur Präsentation
zusammen. Der Controller nimmt vom Router die entsprechende Funktion entgegen und verarbeitet diese dann.

### Model.py
Die Basis-Klasse des Models liefert generalisierte Möglichkeiten zur Datenmanipulation und -interaktion, welche durch
das abgeleitete Model durchgeführt werden können. Das Model wird hauptsächlich mit den Controllern interagieren. 

### Router.py
Der Router ist für das Routing der Applikation zuständig. Er kümmert sich um die Zuordnung der jeweiligen URI-Endpunkte
mit den dafür verantwortlichen Controllern. Er kommuniziert ausschließlich mit den Controllern.

### View.py
Das View ist dafür zuständig, dass das jeweilige Template zur Präsentation aufbereitet wird und anschließend durch
den TemplateParser gerendet wird. Das View steht lediglich in Verbindung mit den Controllern.

## Programmierschnittstellen

### Controller.py
* `redirect(string url, dictionary params = {}, dictionary notificationData = {}) : null`
    * Beschreibung
    : erzeugt einen HTTP-Redirect an `url` mit `params` als HTTP-Argumente und `notificationData` als Flash-Message. 
    * Rückgabewerte
    : `null`
    
* `route(string route, dictionary params = {}) : string`
    * Beschreibung
    : generiert eine fertige Route aus `route` mithilfe der angegebenen Parameter in `params`
    * Rückgabewerte
    : `string` Konstrutierte Route, welche `params` enthält
    
### Model.py
* `__init__(string fileName, list data_attributes) : null`
    * Beschreibung
    : erstellt `fileName` als Datei im dazugehörigen Speicherpfad und definiert `data_attributes` als Felder des Models
    * Rückgabewerte
    : `null`
    * Werfende Exceptions
    : `Exception`: falls `data_attributes` den Key `id` beinhaltet
    
* `create(dictionary values) : integer|boolean`
    * Beschreibung
    : erstellt einen Eintrag in der zum Model zugehörigen JSON-Datei mit den Argumenten `values`
    * Rückgabewerte
    : `int`, falls Eintrag mit der ID des übergebenen Eintrags erfolgreich persistiert werden konnte, ansonsten `false`
  
* `find(int id) : list|boolean`
    * Beschreibung
    : liefert den zur `id` zugehörigen Dateneintrag 
    * Rückgabewerte
    : `list` mit untergeordneten `dictionary`, falls Eintrag erfolgreich gefunden werden konnte, ansonsten `false` 
    
* `findOrFail(int id) : list`
    * Beschreibung
    : siehe `find()`
    * Rückgabewerte
    : `list` mit untergeordneten `dictionary`: falls Eintrag erfolgreich gefunden werden konnte
    * Werfende Exceptions
    : `Exception`, falls der Eintrag nicht erfolgreich gefunden werden konnte
      
* `all(dictionary where = None) : list`
    * Beschreibung
    : liefert alle Einträge zurück, welche mit `where` als Bedingung vereinbar sind
    * Rückgabewerte
    : `list`: alle Einträge, welche mit `where` als Bedingung vereinbar sind
    
* `update(integer id, dictionary values) : boolean`
    * Beschreibung
    : Aktualisiert den Eintrag mit der `id` mit den Werten in `values`
    * Rückgabewerte
    : `true`: falls der Eintrag aktualisiert werden konnten, ansonsten `false`
    * Werfende Exceptions
    : `Exception`: falls `values` den Key `id` beinhaltet
    
* `delete(integer id) : boolean`
    * Beschreibung
    : Löscht den Eintrag mit der `id` permanent
    * Rückgabewerte
    : `true`: falls der Eintrag gelöscht werden konnte, ansonsten `false`

### Router.py
* `getAllRoutes(list routerConfig) : RoutesDispatcher`
    * Beschreibung
    : generiert eine `RoutesDispatcher` anhand der übergebenen Liste in `routerConfig` und importiert dynamisch die 
      jeweiligen Controller für die Verwendung (Autoloading)
    * Rückgabewerte
    : `object`: RoutesDispatcher
    
### View.py
* `__init__(string view_search_folder) : null`
    * Beschreibung
    : Konsturktor, welcher den Lookup-Folder für mako in `view_search_folder` setzt
    * Rückgabewerte
    : `null`
    
* `load(string template, dictionary data_opl={}) : string`
    * Beschreibung
    : Lädt das Template `template` und übergibt `data_opl` an das View als Parameter weiter
    * Rückgabewerte
    : `string`: fertig vom View gerenderter String zur Ausgabe

# Datenablage
Die Models generieren bei initialen Aufruf die JSON-Dateien, welche zur Datenablage verwendet werden. Diese liegen 
standardmäßig im Ordner `/data`. Jedes Model benutzt ein dazugehöriges individuelles Datenerzeugnis. Pivotelemente
werden ebenso in einzelnen Models verwaltet wie die eigentlichen Daten selbst.

## Beispiel einer JSON-Datei
```json
{
   "meta": {
      "maxId": 2,
      "columns": [
         [
            "id",
            "customer_id",
            "label",
            "contact",
            "city"
         ]
      ]
   },
   "data": [
      [
         1,
         "CUSTOMER-00001",
         "Max Mustermann AG",
         "Max Mustermann",
         "Musterstadt"
      ],
      [
         2,
         "CUSTOMER-00002",
         "Erika Mustermann AG",
         "Erika Mustermann",
         "Musterstadt"
      ]
   ]
}
```

## Transformierung der Daten
Da es über normale 1-n-Beziehungen ebenso Pivottabellen geben muss und grundsätzlich eine Transformierung der Daten
manchmal sinnvoll erscheint, kann in der eigentlich Model-Klasse eine spezielle Funktion mit dem Namen `_transformData`
implementiert werden. Diese Funktion wird dann vor der Datenausgabe aufgerufen und manipuliert das entsprechende Ergebnis.
Als Übergabeparameter enthält diese die aktuelle Liste und muss dann die manipulierte Liste zurückgeben.

### Beispiel im Employee
```python
class Employee(BaseModel):
    def __init__(self):
        file_name = 'employee'
        data_attributes = ['last_name', 'first_name', 'position']
        BaseModel.__init__(self, file_name, data_attributes)

    def _transformData(self, employees):
        formattedEmployees = list(employees)

        for employee in formattedEmployees:
            employee['name'] = employee['last_name']

            if employee['first_name'] is not None:
                employee['name'] += ', ' + employee['first_name']

        return formattedEmployees
```

# Validierungen
Die HTML5-Validierungen wurden mithilfe des ["Nu Html Checker"](https://validator.w3.org/nu/#textarea) vom W3C 
durchgeführt. Die Ergebnisse befinden sich in folgender Tabelle:

| Route | Fehler | Warnungen |
|-------|--------|----------|
| / | 0 | 0 |
| /employees | 0 | 0 |
| /employees/create  | 0 | 0 | 
| /employees/{id}  | 0 | 0 | 
| /projects | 0 | 0 |
| /projects/create  | 0 | 2 | 
| /projects/{id}  | 0 | 2 | 
| /customers | 0 | 0 |
| /customers/create  | 0 | 0 | 
| /customers/{id}  | 0 | 0 | 


Die Warnungen können ignoriert werden, da diese lediglich für ältere Browser relevant sind (HTML5 polyfilling).
