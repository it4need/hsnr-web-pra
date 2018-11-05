# coding: utf-8

from app.core.controller import BaseController
from app.models.ProjectTime import ProjectTime


class ProjectTimeController(BaseController):
    def __init__(self):
        BaseController.__init__(self)

    def store(self, id, **kwargs):
        projectTime = ProjectTime().create(self.__convertArgumentsToCorrectDatatype(id, kwargs))

        if projectTime:
            self.redirect('projects.show', params={'id': id},
                          notificationData={'success': 'Der Zeiteintrag wurde erfolgreich gespeichert.'})
        else:
            self.redirect('projects.show', params={'id': id},
                          notificationData={'danger': 'Der Zeiteintrag konnte nicht gespeichert werden.'})

    def __convertArgumentsToCorrectDatatype(self, id, args):
        return {
            'project_id': int(id),
            'employee_id': int(args['employee_id']),
            'hours_per_week': int(args['hours_per_week']),
            'week': int(args['week']),
            'year': int(args['year'])
        }
