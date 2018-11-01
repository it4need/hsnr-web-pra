# coding: utf-8

from app.core.model import BaseModel


class Customer(BaseModel):
    def __init__(self):
        file_name = 'customer'
        data_attributes = ["customerId", "description", "contact", "city"]
        BaseModel.__init__(self, file_name, data_attributes)