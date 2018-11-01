# coding: utf-8
import codecs
import json
import os
import os.path

from app.config.app import AppConfig

class Customer(object):
    def __init__(self, workingDir_spl):
        self.workingDir_s = workingDir_spl
        self.readData_p()

    def readData_p(self):
        try:
            fp_o = codecs.open(os.path.join(AppConfig.database_folder, 'customers' + AppConfig.database_extension), 'r', 'utf-8')
        except:
            # Datei neu anlegen
            self.data_o = {}
            self.saveData_p()
        else:
            with fp_o:
                self.data_o = json.load(fp_o)

        return

    def saveData_p(self):
        with codecs.open(os.path.join(AppConfig.database_folder, 'customers' + AppConfig.database_extension), 'w', 'utf-8') as fp_o:
            json.dump(self.data_o, fp_o, indent=3)