# coding: utf-8

from app.core.model import BaseModel


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