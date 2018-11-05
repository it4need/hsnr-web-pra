# coding: utf-8

from app.core.controller import BaseController
from app.models.Project import Project
from app.models.ProjectEmployee import ProjectEmployee
from app.models.ProjectTime import ProjectTime
from app.models.Customer import Customer
from app.models.Employee import Employee


class ProjectController(BaseController):
    def __init__(self):
        BaseController.__init__(self)

    def index(self):
        projects = Project().all()
        return self.view.load('projects.index', {'projects': projects})

    def create(self):
        allCustomers = Customer().all()

        if len(allCustomers) < 1:
            self.redirect('projects.index', notificationData=
            {'danger': 'Projekte können erst erstellt werden, wenn bereits Kunden vorhanden sind.'})

        return self.view.load('projects.create', {'allCustomers': allCustomers})

    def store(self, **kwargs):
        project = Project().create(self.__convertArgumentsToCorrectDatatype(kwargs))

        if project:
            self.redirect('projects.index', notificationData={'success': 'Der Projet wurde erfolgreich eingetragen.'})
        else:
            self.redirect('projects.store',
                          notificationData={'danger': 'Leider konnte das Projekt nicht erfolgreich angelegt werden.'})

    def show(self, id):
        project = Project().findOrFail(id)
        allCustomers = Customer().all()
        allEmployees = Employee().all()
        allProjectTimes = ProjectTime().all({'project_id': int(id)})
        timeList = self.__generateHoursPerEmployeePerWeekYear(allProjectTimes)

        return self.view.load('projects.edit',
                              {'_old': project[0], 'allCustomers': allCustomers, 'allEmployees': allEmployees, 'timeList': timeList})

    def update(self, id, **kwargs):
        project = Project().update(id, self.__convertArgumentsToCorrectDatatype(kwargs))

        if project:
            self.redirect('projects.index', notificationData=
            {'success': 'Das Projekt mit der ID ' + id + ' wurde erfolgreich geändert.'})
        else:
            self.redirect('projects.index', notificationData={'danger': 'Das Projekt konnte nicht geändert werden.'})

    def delete(self, id):
        allProjectEmployees = ProjectEmployee().all({'project_id': int(id)})
        allProjectTime = ProjectTime().all({'project_id': int(id)})

        for time in allProjectTime:
            ProjectTime().delete(time['id'])

        for employee in allProjectEmployees:
            ProjectEmployee().delete(employee['id'])

        project = Project().delete(id)
        if project:
            self.redirect('projects.index', notificationData={
                'success': 'Das Projekt mit der ID ' + id + ' wurde mit allen zugehörigen Einträgen erfolgreich gelöscht.'})
        else:
            self.redirect('projects.index', notificationData={'danger': 'Das Projekt konnte nicht gelöscht werden.'})

    def __convertArgumentsToCorrectDatatype(self, args):
        return {
            'project_id': args['project_id'],
            'label': args['label'],
            'description': args['description'],
            'start_date': args['start_date'],
            'end_date': args['end_date'],
            'budget': float(args['budget']),
            'customer_id': int(args['customer_id']),
        }
    def __generateHoursPerEmployeePerWeekYear(self, allProjectTimes):
        result = {}
        years = []

        for projectTime in allProjectTimes:
            result[projectTime['employee_id']] = {}
            years.append(projectTime['year'])

        years = list(set(years))
        for year in years:
            for projectTime in allProjectTimes:
                result[projectTime['employee_id']][year] = {}
                for week in range(1, 54):
                    result[projectTime['employee_id']][year][week] = 0

        for projectTime in allProjectTimes:
            result[projectTime['employee_id']][projectTime['year']][projectTime['week']] += projectTime['hours_per_week']

        return result