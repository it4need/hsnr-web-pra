# coding: utf-8

from app.core.controller import BaseController
from app.models.ProjectTime import ProjectTime
from app.models.Project import Project
from app.models.Employee import Employee


class ReportController(BaseController):
    def __init__(self):
        BaseController.__init__(self)

    def index(self):
        allProjects = sorted(Project().all(), key=lambda project: project['label'])
        allEmployees = Employee().all()


        for key, project in enumerate(list(allProjects)):
                allProjectTimes = ProjectTime().all({'project_id': int(project['id'])})
                timeList = self.__generateHoursPerEmployeePerWeekYear(allProjectTimes)
                allProjects[key]['timeList'] = timeList
                timeListSummary = self.__generateSummaryForProject([allProjects[key]])
                allProjects[key]['timeList_summary'] = timeListSummary

        return self.view.load('reports.index',
                              {'projects': allProjects, 'allEmployees': allEmployees})

    def __generateHoursPerEmployeePerWeekYear(self, allProjectTimes):
        result = {}
        years = []

        for projectTime in allProjectTimes:
            name = projectTime['employee'][0]['last_name'] + ', ' + projectTime['employee'][0]['first_name']
            result[name] = {}
            years.append(projectTime['year'])

        years = list(set(years))
        for year in years:
            for projectTime in allProjectTimes:
                name = projectTime['employee'][0]['last_name'] + ', ' + projectTime['employee'][0]['first_name']

                result[name][year] = {}
                for week in range(1, 54):
                    result[name][year][week] = 0

        for projectTime in allProjectTimes:
            name = projectTime['employee'][0]['last_name'] + ', ' + projectTime['employee'][0]['first_name']

            result[name][projectTime['year']][projectTime['week']] += projectTime['hours_per_week']

        return result

    def __generateSummaryForProject(self, allProjectTimes):
        years = {}
        result = {}
        result[0] = []

        for project in allProjectTimes:
            for timeList in project['timeList'].items():
                for year, values in timeList[1].items():
                    years[year] = {}

                    for week, week_work_hours in values.items():
                        years[year][week] = 0

        for year in set(list(years)):
            for project in allProjectTimes:
                for timeList in project['timeList'].items():
                    for timeList_year, values in timeList[1].items():
                        if(year == timeList_year):
                            for week, week_work_hours in values.items():
                                if week_work_hours != 0:
                                    years[year][week] += week_work_hours


        for year, values in years.items():
            result[year] = {}

            for week, week_work_hours in values.items():
                result[year][week] = week_work_hours

                if (week_work_hours != 0):
                    result[0].append(str(week))

        result[0] = list(set(result[0]))
        return result