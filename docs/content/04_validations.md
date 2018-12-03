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