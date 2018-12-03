# coding: utf-8

from app.core.controller import BaseController
from app.models.Employee import Employee
from app.models.ProjectEmployee import ProjectEmployee
from app.models.ProjectTime import ProjectTime


class EmployeeController(BaseController):
    def __init__(self):
        BaseController.__init__(self)

    def index(self):
        employees = Employee().all()
        return self.view.load('employees.index', {'employees': employees})

    def create(self):
        return self.view.load('employees.create')

    def store(self, **kwargs):
        employee = Employee().create(kwargs)
        if employee:
            self.redirect('employees.index',
                          notificationData={'success': 'Der Mitarbeiter wurde erfolgreich eingetragen.'})
        else:
            self.redirect('employees.store', notificationData={
                'danger': 'Leider konnte der Mittarbeiter nicht erfolgreich angelegt werden.'})

    def show(self, id):
        employee = Employee().findOrFail(id)
        return self.view.load('employees.edit', {'_old': employee[0]})

    def update(self, id, **kwargs):
        employee = Employee().update(id, kwargs)
        if employee:
            self.redirect('employees.index', notificationData={
                'success': 'Der Mitarbeiter mit der ID ' + id + ' wurde erfolgreich geändert.'})
        else:
            self.redirect('employees.index',
                          notificationData={'danger': 'Der Mitarbeiter konnte nicht geändert werden.'})

    def delete(self, id):
        associatedProjects = ProjectEmployee().all({'employee_id': int(id)})
        associatedProjectsTimeTable = ProjectTime().all({'employee_id': int(id)})

        if associatedProjectsTimeTable:
            self.redirect('employees.index',
                          notificationData={'danger': 'Der Mitarbeiter konnte nicht gelöscht werden, da es noch zugehörige Zeiteinträge in Projekten gibt.'})

        employee = Employee().delete(id)

        for project in associatedProjects:
            ProjectEmployee().delete(project['id'])

        if employee:
            self.redirect('employees.index', notificationData={
                'success': 'Der Mitarbeiter mit der ID ' + id + ' wurde erfolgreich gelöscht. All seine Projektassoziationen wurden aufgehoben.'})
        else:
            self.redirect('employees.index',
                          notificationData={'danger': 'Der Mitarbeiter konnte nicht gelöscht werden.'})
