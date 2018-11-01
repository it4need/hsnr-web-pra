# coding: utf-8
import cherrypy
from app.controllers.HomeController import HomeController


class RoutesConfig:
    routes = [
        {
            'route': '/',
            'method': 'HomeController@index',
        }
    ]

    def __init__(self):
        # Mount static content handler
        self.dispatcher = cherrypy.dispatch.RoutesDispatcher()

    def getAllRoutes(self):
        for route in self.routes:
            if 'condition' in route:
                routeConditions = route['condition']
            else:
                routeConditions = {'method': ['GET']}

            if 'name' in route:
                routeName = route['name']
            else:
                routeName = None

            routeController, routeMethod = route['method'].split('@')
            routeController = globals()[routeController]()

            self.dispatcher.connect(
                name=routeName,
                route=route['route'],
                action=routeMethod,
                controller=routeController,
                conditions=routeConditions
            )

        return self.dispatcher
