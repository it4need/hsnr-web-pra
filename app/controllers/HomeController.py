# coding: utf-8

from app.core.controller import BaseController
from app.models.Employee import Employee
from app.models.Customer import Customer

class HomeController(BaseController):
    def __init__(self):
        BaseController.__init__(self)

    def index(self):
        return self.view.load('index', {'name': 'Hanno Siebel'})
