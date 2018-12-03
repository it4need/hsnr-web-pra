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