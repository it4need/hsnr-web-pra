# coding: utf-8

import os.path
from app.config.app import AppConfig
from app.config.routes import RouterConfig
from mako.lookup import TemplateLookup


class View(object):
    def __init__(self, view_search_folder):
        self.lookup_o = TemplateLookup(directories=view_search_folder)

    def load(self, template, data_opl={}):
        data_opl['routes'] = RouterConfig.getAllRoutes()
        return self.__render(template, data_opl)

    def __render(self, template_spl, data_opl):
        header = self.__render_header(data_opl)
        footer = self.__render_footer(data_opl)
        content = self.__render_template(template_spl, data_opl)
        return header + content + footer

    def __render_header(self, data_opl):
        return self.__render_template('partials/header', data_opl)

    def __render_footer(self, data_opl):
        return self.__render_template('partials/footer', data_opl)

    def __render_template(self, template_spl, data_opl):
        template = self.lookup_o.get_template(template_spl + AppConfig.view_extension)
        rendered = template.render(data=data_opl)
        return rendered
