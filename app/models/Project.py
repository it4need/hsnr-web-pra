# coding: utf-8

from app.core.model import BaseModel
from app.models.Customer import Customer
from app.models.ProjectEmployee import ProjectEmployee
from app.models.ProjectTime import ProjectTime

class Project(BaseModel):
    def __init__(self):
        file_name = 'project'
        data_attributes = ["project_id", "label", "description", "start_date", "end_date", "budget",
                           "customer_id"]
        BaseModel.__init__(self, file_name, data_attributes)

    def _transformData(self, projects):
        formattedProjects = list(projects)

        for project in formattedProjects:
            project['customer'] = Customer().findOrFail(project['customer_id'])[0]
            project['list_employees'] = ProjectEmployee().all({'project_id': project['id']})
            project['time_costs'] = self.__calculateProjectTime(project['id'])
            project['time_period'] = project['start_date']

            if project['end_date'] is not None:
                project['time_period'] += ' – ' + project['end_date']

        return formattedProjects

    def __calculateProjectTime(self, project_id):
        sum = 0
        allProjectTimes = ProjectTime().all({'project_id': project_id})

        for time in allProjectTimes:
            sum = sum + time['hours_per_week']

        return sum