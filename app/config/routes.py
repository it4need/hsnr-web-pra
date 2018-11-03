# coding: utf-8

class RouterConfig:
    routes = [
        {
            'route': '/',
            'method': 'HomeController@index',
        },
        {
            'route': '/employees',
            'method': 'EmployeeController@index',
        },
        {
            'name': 'employee.create',
            'route': '/employees/create',
            'method': 'EmployeeController@create',
        },
        {
            'name': 'employee.store',
            'route': '/employees/store',
            'method': 'EmployeeController@store',
            'condition': {'method': ['POST']}
        }
    ]

    @staticmethod
    def getAllRoutes():
        allRoutes = {}
        for routes in RouterConfig.routes:
            if 'name' in routes:
                allRoutes[routes['name']] = routes['route']

        return allRoutes
