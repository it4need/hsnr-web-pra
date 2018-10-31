# coding: utf-8

import cherrypy
from .view import View
from .customer_model import Customer_model

class Application(object):
    def __init__(self, workingDir_spl):
        # spezielle Initialisierung können hier eingetragen werden
        self.view = View(workingDir_spl)
        self.customer_model = Customer_model(workingDir_spl)

    @cherrypy.expose
    def index(self):
        return self.view.load('index', {'name': 'Hanno'})