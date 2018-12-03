# coding: utf-8

from app.core.controller import BaseController
from app.models.Customer import Customer
from app.models.Project import Project


class CustomerController(BaseController):
    def __init__(self):
        BaseController.__init__(self)

    def index(self):
        customers = Customer().all()
        return self.view.load('customers.index', {'customers': customers})

    def create(self):
        return self.view.load('customers.create')

    def store(self, **kwargs):
        customer = Customer().create(kwargs)
        if customer:
            self.redirect('customers.index', notificationData={'success': 'Der Kunde wurde erfolgreich eingetragen.'})
        else:
            self.redirect('customers.store',
                          notificationData={'danger': 'Leider konnte der Kunde nicht erfolgreich angelegt werden.'})

    def show(self, id):
        customer = Customer().findOrFail(id)

        return self.view.load('customers.edit', {'_old': customer[0]})

    def update(self, id, **kwargs):
        customer = Customer().update(id, kwargs)
        if customer:
            self.redirect('customers.index',
                          notificationData={'success': 'Der Kunde mit der ID ' + id + ' wurde erfolgreich geändert.'})
        else:
            self.redirect('customers.index', notificationData={'danger': 'Der Kunde konnte nicht geändert werden.'})

    def delete(self, id):
        allProjects = Project().all({'customer_id': int(id)})

        if len(allProjects) > 0:
            self.redirect('customers.index', notificationData={
                'danger': 'Bevor der Kunde mit der ID ' + id + ' gelöscht werden darf, müssen alle Projekte entfernt werden.'})

        customer = Customer().delete(id)
        if customer:
            self.redirect('customers.index',
                          notificationData={'success': 'Der Kunde mit der ID ' + id + ' wurde erfolgreich gelöscht.'})
        else:
            self.redirect('customers.index', notificationData={'danger': 'Der Kunde konnte nicht gelöscht werden.'})
