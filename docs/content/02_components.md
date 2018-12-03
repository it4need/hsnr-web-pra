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