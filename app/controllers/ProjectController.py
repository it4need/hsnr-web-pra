# coding: utf-8

from app.core.controller import BaseController
from app.models.Project import Project
from app.models.ProjectTime import ProjectTime

class ProjectController(BaseController):
    def __init__(self):
        BaseController.__init__(self)

    def index(self):
        projects = Project().all()
        project_time = ProjectTime().all()
        return self.view.load('projects.index', {'projects': projects})

    def create(self):
        return self.view.load('customers.create')

    def store(self, **kwargs):
        customer = Customer().create(kwargs)
        if customer:
            self.redirect('customers.index', {'success': 'Der Kunde wurde erfolgreich eingetragen.'})
        else:
            self.redirect('customers.store', {'danger': 'Leider konnte der Kunde nicht erfolgreich angelegt werden.'})

    def show(self, id):
        customer = Customer().findOrFail(id)
        print(customer)
        return self.view.load('customers.edit', {'_old': customer[0]})

    def update(self, id, **kwargs):
        customer = Customer().update(id, kwargs)
        if customer:
            self.redirect('customers.index', {'success': 'Der Kunde mit der ID ' + id + ' wurde erfolgreich geändert.'})
        else:
            self.redirect('customers.index', {'danger': 'Der Kunde konnte nicht geändert werden.'})

    def delete(self, id):
        customer = Customer().delete(id)
        if customer:
            self.redirect('customers.index', {'success': 'Der Kunde mit der ID ' + id + ' wurde erfolgreich gelöscht.'})
        else:
            self.redirect('customers.index', {'danger': 'Der Kunde konnte nicht gelöscht werden.'})