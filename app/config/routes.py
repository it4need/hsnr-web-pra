# coding: utf-8

class RouterConfig:
    routes = [
        {
            'route': '/',
            'method': 'HomeController@index',
        },
        {
            'name': 'employee.index',
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
        },
        {
            'name': 'employee.show',
            'route': '/employees/:id',
            'method': 'EmployeeController@show'
        },
        {
            'name': 'employee.update',
            'route': '/employees/:id',
            'method': 'EmployeeController@update',
            'condition': {'method': ['POST']}
        },
        {
            'name': 'employee.delete',
            'route': '/employees/delete/:id',
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
