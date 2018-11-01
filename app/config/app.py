# coding: utf-8
import os


class AppConfig(object):
    if os.name == 'nt':
        root_dir = os.path.dirname(os.path.abspath(__file__)) + '\\..\\..\\'
    else:
        root_dir = os.path.dirname(os.path.abspath(__file__)) + '/../../'

    view_folder = root_dir + 'views'
    view_extension = '.html'
    database_folder = root_dir + 'data'
    database_extension = '.json'
