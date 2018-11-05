# coding: utf-8

from app.core.model import BaseModel
from app.models.Employee import Employee

class ProjectTime(BaseModel):
    def __init__(self):
        file_name = 'project_time'
        data_attributes = ["project_id", "employee_id", "hours_per_week", 'week', 'year']
        BaseModel.__init__(self, file_name, data_attributes)

    def _transformData(self, projectsTime):
        formattedProjectTime = list(projectsTime)

        for projectTime in formattedProjectTime:
            projectTime['employee'] = Employee().find(projectTime['employee_id'])

        return formattedProjectTime
