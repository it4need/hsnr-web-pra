# coding: utf-8

from app.controllers.BaseController import BaseController


class HomeController(BaseController):
    def __init__(self):
        BaseController.__init__(self)

    def index(self):
        return self.view.load('index', {'name': 'Hanno'})