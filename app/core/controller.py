# coding: utf-8

import cherrypy

from app.core.view import View
from app.config.app import AppConfig
from app.config.routes import RouterConfig


class BaseController(object):
    def __init__(self):
        self.view = View(AppConfig.view_folder)

    def redirect(self, toUrl, params = {}, notificationData = {}):
        if toUrl in RouterConfig.getAllRoutes():
            for key, data in notificationData.items():
                cherrypy.session['notifications_' + str(key)] = data
            raise cherrypy.HTTPRedirect(self.route(RouterConfig.getAllRoutes()[toUrl], params))
        else:
            raise cherrypy.HTTPRedirect(toUrl)

    def route(self, route, params = {}):
        final_route = route

        for key, value in params.items():
            final_route = final_route.replace(':' + str(key), str(value))

        return final_route