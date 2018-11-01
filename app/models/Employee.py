# coding: utf-8

from app.core.model import BaseModel


class Employee(BaseModel):
    def __init__(self):
        file_name = 'employee'
        data_attributes = ['last_name', 'first_name', 'position']
        BaseModel.__init__(self, file_name, data_attributes)
        print(self.data)
