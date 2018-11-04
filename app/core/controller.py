# coding: utf-8

import cherrypy

from app.core.view import View
from app.config.app import AppConfig
from app.config.routes import RouterConfig


class BaseController(object):
    def __init__(self):
        self.view = View(AppConfig.view_folder)

    def redirect(self, toUrl, sessionData = {}):
        if toUrl in RouterConfig.getAllRoutes():
            for key, data in sessionData.items():
                cherrypy.session['notifications_' + str(key)] = data
            raise cherrypy.HTTPRedirect(RouterConfig.getAllRoutes()[toUrl])
        else:
            raise cherrypy.HTTPRedirect(toUrl)
