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
        {
            'name': 'customers.index',
            'route': '/customers',
            'method': 'CustomerController@index',
        },
        {
            'name': 'customers.create',
            'route': '/customers/create',
            'method': 'CustomerController@create',
        },
        {
            'name': 'customers.store',
            'route': '/customers/store',
            'method': 'CustomerController@store',
            'condition': {'method': ['POST']}
        },
        {
            'name': 'customers.show',
            'route': '/customers/:id',
            'method': 'CustomerController@show'
        },
        {
            'name': 'customers.update',
            'route': '/customers/:id',
            'method': 'CustomerController@update',
            'condition': {'method': ['POST']}
        },
        {
            'name': 'customers.delete',
            'route': '/customers/:id/delete',
            'method': 'CustomerController@delete',
            'condition': {'method': ['POST']}
        },
        {
            'name': 'projects.index',
            'route': '/projects',
            'method': 'ProjectController@index',
        },
        {
            'name': 'projects.create',
            'route': '/projects/create',
            'method': 'ProjectController@create',
        },
        {
            'name': 'projects.store',
            'route': '/projects/store',
            'method': 'ProjectController@store',
            'condition': {'method': ['POST']}
        },
        {
            'name': 'projects.show',
            'route': '/projects/:id',
            'method': 'ProjectController@show'
        },
        {
            'name': 'projects.update',
            'route': '/projects/:id',
            'method': 'ProjectController@update',
            'condition': {'method': ['POST']}
        },
        {
            'name': 'projects.delete',
            'route': '/projects/:id/delete',
            'method': 'ProjectController@delete',
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
