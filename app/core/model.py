# coding: utf-8
import codecs
import json
import os
import os.path

from app.config.app import AppConfig


class BaseModel:
    def __init__(self, fileName, data_attributes):
        self.data = None
        self.file_name = fileName
        self.data_attributes = data_attributes
        self.__createDatabaseFolderIfNotExist()
        self.__read()

    def create(self, values=[]):
        values.insert(0, self.__getMaxId() + 1)
        self.data['data'].append(list(values))
        self.__save()

    def find(self, findId):
        for data in self.data['data']:
            if data[0] == findId:
                columns = list(self.data_attributes)
                columns.insert(0, 'id')
                return dict(zip(columns, data))

    def all(self):
        all_data = list()
        for data in self.data['data']:
            columns = list(self.data_attributes)
            columns.insert(0, 'id')
            all_data.append(dict(zip(columns, data)))

        return all_data

    def update(self, data_id, values):
        for key, data in enumerate(self.data['data']):
            if data_id == data[0]:
                values.insert(0, data_id)
                self.data['data'][key] = values
                self.__save(self.__getMaxId())
                return True

        return False

    def delete(self, data_id):
        for key, data in enumerate(self.data['data']):
            if data_id == data[0]:
                del self.data['data'][key]
                self.__save(self.__getMaxId())
                return True

        return False

    def __read(self):
        try:
            openedFile = codecs.open(
                os.path.join(AppConfig.database_folder, self.file_name + AppConfig.database_extension), 'r',
                'utf-8')
        except:
            self.data = self.__newJSONStructure()
            self.__save(0)
        else:
            with openedFile:
                self.data = json.load(openedFile)

    def __save(self, maxId=None):
        openedFile = codecs.open(os.path.join(AppConfig.database_folder, self.file_name + AppConfig.database_extension),
                                 'w', 'utf-8')
        with openedFile:
            self.__setMaxId(maxId)
            json.dump(self.data, openedFile, indent=3)

    def __getMaxId(self):
        return self.data['meta']['maxId']

    def __setMaxId(self, maxId=None):
        if maxId is None:
            self.data['meta']['maxId'] = self.__getMaxId() + 1
        else:
            self.data['meta']['maxId'] = maxId

    def __newJSONStructure(self):
        self.data_attributes.insert(0, 'id')

        return {
            "meta": {
                "maxId": 0,
                "columns": [
                    self.data_attributes
                ]
            },
            "data": []
        }

    def __createDatabaseFolderIfNotExist(self):
        if not os.path.exists(AppConfig.database_folder):
            os.makedirs(AppConfig.database_folder)
