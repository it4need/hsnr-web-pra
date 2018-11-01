# coding: utf-8
import os


class AppConfig(object):
    try:
        root_dir = os.path.dirname(os.path.abspath(__file__)) + '/../../'
    except:
        root_dir = os.path.dirname(os.path.abspath(sys.executable)) + '/../../'

    view_folder = root_dir + '/views'
    view_extension = '.html'
    database_folder = root_dir + '/data'
    database_extension = '.json'
