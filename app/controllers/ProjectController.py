# coding: utf-8

from app.core.controller import BaseController
from app.models.Project import Project
from app.models.ProjectEmployee import ProjectEmployee
from app.models.ProjectTime import ProjectTime
from app.models.Customer import Customer


class ProjectController(BaseController):
    def __init__(self):
        BaseController.__init__(self)

    def index(self):
        projects = Project().all()
        return self.view.load('projects.index', {'projects': projects})

    def create(self):
        allCustomers = Customer().all()

        if len(allCustomers) < 1:
            self.redirect('projects.index', {'danger': 'Projekte können erst erstellt werden, wenn bereits Kunden vorhnaden sind.'})

        return self.view.load('projects.create', {'allCustomers': allCustomers})

    def store(self, **kwargs):
        customer = Project().create(self.__convertArgumentsToCorrectDatatype(kwargs))

        if customer:
            self.redirect('projects.index', {'success': 'Der Projet wurde erfolgreich eingetragen.'})
        else:
            self.redirect('projects.store', {'danger': 'Leider konnte das Projekt nicht erfolgreich angelegt werden.'})

    def show(self, id):
        project = Project().findOrFail(id)
        allCustomers = Customer().all()

        return self.view.load('projects.edit', {'_old': project[0], 'allCustomers': allCustomers})

    def update(self, id, **kwargs):
        project = Project().update(id, self.__convertArgumentsToCorrectDatatype(kwargs))

        if project:
            self.redirect('projects.index',
                          {'success': 'Das Projekt mit der ID ' + id + ' wurde erfolgreich geändert.'})
        else:
            self.redirect('projects.index', {'danger': 'Das Projekt konnte nicht geändert werden.'})

    def delete(self, id):
        allProjectEmployees = ProjectEmployee().all({'project_id': int(id)})
        allProjectTime = ProjectTime().all({'project_id': int(id)})

        for time in allProjectTime:
            ProjectTime().delete(time['id'])

        for employee in allProjectEmployees:
            ProjectEmployee().delete(employee['id'])

        project = Project().delete(id)
        if project:
            self.redirect('projects.index', {
                'success': 'Das Projekt mit der ID ' + id + ' wurde mit allen zugehörigen Einträgen erfolgreich gelöscht.'})
        else:
            self.redirect('projects.index', {'danger': 'Das Projekt konnte nicht gelöscht werden.'})

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