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

### Beispiel der Transformierung im Employee-Model
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