# coding: utf-8

from app.core.model import BaseModel


class Employee(BaseModel):
    def __init__(self):
        self.file_name = 'employee'
        self.data_attributes = ['last_name', 'first_name', 'position']
        BaseModel.__init__(self)
        print(self.data)
