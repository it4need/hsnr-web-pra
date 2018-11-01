# coding: utf-8
import cherrypy
from app.controllers.HomeController import HomeController


class RouterConfig:
    routes = [
        {
            'route': '/',
            'method': 'HomeController@index',
        }
    ]

