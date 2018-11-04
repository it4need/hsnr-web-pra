# coding: utf-8

from app.core.model import BaseModel
from app.models.Employee import Employee

class ProjectEmployee(BaseModel):
    def __init__(self):
        file_name = 'project_employee'
        data_attributes = ["project_id", "employee_id"]
        BaseModel.__init__(self, file_name, data_attributes)

    def _transformData(self, projectsEmployee):
        formattedProjectEmployee = list(projectsEmployee)

        for projectEmployee in formattedProjectEmployee:
            projectEmployee['employee'] = Employee().find(projectEmployee['employee_id'])

        return formattedProjectEmployee
