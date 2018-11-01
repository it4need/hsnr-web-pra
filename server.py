# coding: utf-8
import cherrypy
from app.config.app import AppConfig
from app.config.routes import RouterConfig
from app.core.router import RouteDispatcher

def main():
    cherrypy.engine.autoreload.unsubscribe()

    static_config = {
        '/': {
            'tools.staticdir.root': AppConfig.root_dir,
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './content',
            'request.dispatch': RouteDispatcher().getAllRoutes(RouterConfig.routes),
        }
    }

    cherrypy.tree.mount(root=None, config=static_config)
    cherrypy.config.update({'request.show_tracebacks': False})

    cherrypy.engine.start()
    cherrypy.engine.block()


if __name__ == '__main__':
    main()
# EOF
