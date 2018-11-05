# coding: utf-8

from app.core.controller import BaseController
from app.models.Project import Project
from app.models.ProjectEmployee import ProjectEmployee


class ProjectEmployeeController(BaseController):
    def __init__(self):
        BaseController.__init__(self)

    def store(self, id, **kwargs):
        projectEmployee = ProjectEmployee().create(self.__convertArgumentsToCorrectDatatype(id, kwargs))

        if projectEmployee:
            self.redirect('projects.show', params={'id': id},
                          notificationData={'success': 'Der Mitarbeiter wurde erfolgreich assoziiert.'})
        else:
            self.redirect('projects.show', params={'id': id},
                          notificationData={'danger': 'Der Mitarbeiter konnte leider nicht assoziiert werden.'})

    def delete(self, id):
        projectEmployeeId = ProjectEmployee().find(int(id))[0]['project_id']
        projectEmployee = ProjectEmployee().delete(int(id))

        if projectEmployee:
            self.redirect('projects.show', params={'id': int(projectEmployeeId)}, notificationData={
                'success': 'Der Mitarbeiter wurde dem Projekt entzogen.'})
        else:
            self.redirect('projects.show', params={'id': int(projectEmployeeId)},
                          notificationData={'danger': 'Der Mitarbeiter konnte nicht vom Projekt entzogen werden.'})

    def __convertArgumentsToCorrectDatatype(self, id, args):
        return {
            'project_id': int(id),
            'employee_id': int(args['employee_id']),
        }
