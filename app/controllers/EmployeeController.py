# coding: utf-8

from app.core.controller import BaseController
from app.models.Employee import Employee


class EmployeeController(BaseController):
    def __init__(self):
        BaseController.__init__(self)

    def index(self):
        employee = Employee().all()
        return self.view.load('employees.index', {'employees': employee})

    def create(self):
        return self.view.load('employees.create')

    def store(self, **kwargs):
        employee = Employee().create(kwargs)
        if employee:
            self.redirect('employee.index', {'successful': 'success'})
        else:
            return "not stored"
