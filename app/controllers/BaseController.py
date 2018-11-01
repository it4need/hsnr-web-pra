# coding: utf-8

from app.core.view import View
from app.config.app import AppConfig


class BaseController(object):
    def __init__(self):
        self.view = View(AppConfig.view_folder)
