# coding: utf-8

class RouterConfig:
    routes = [
        {
            'route': '/',
            'method': 'HomeController@index',
        },
        {
            'name': 'employees.index',
            'route': '/employees',
            'method': 'EmployeeController@index',
        },
        {
            'name': 'employees.create',
            'route': '/employees/create',
            'method': 'EmployeeController@create',
        },
        {
            'name': 'employees.store',
            'route': '/employees/store',
            'method': 'EmployeeController@store',
            'condition': {'method': ['POST']}
        },
        {
            'name': 'employees.show',
            'route': '/employees/:id',
            'method': 'EmployeeController@show'
        },
        {
            'name': 'employees.update',
            'route': '/employees/:id',
            'method': 'EmployeeController@update',
            'condition': {'method': ['POST']}
        },
        {
            'name': 'employees.delete',
            'route': '/employees/:id/delete',
            'method': 'EmployeeController@delete',
            'condition': {'method': ['POST']}
        },
    ]

    @staticmethod
    def getAllRoutes():
        allRoutes = {}
        for routes in RouterConfig.routes:
            if 'name' in routes:
                allRoutes[routes['name']] = routes['route']

        return allRoutes
