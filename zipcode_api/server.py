
from datetime import date

import tornado.ioloop
import tornado.web
import zipcode_api

version = zipcode_api.version
print(version)

# Construindo API RESTful
# http://www.drdobbs.com/open-source/building-restful-apis-with-tornado/240160382
# +--------------------------------------+ +--------------------------------------+ +---------------------------------+
# | Verbo HTTP e URL de requisição       | | Tupla (regexp, request_class) que    | | RequestHandler subclass e metodo|
# |                                      | | corresponde ao caminho da solicitação| | chamado                         |
# |                                      | |                                      | |                                 |
# +--------------------------------------+ +--------------------------------------+ +---------------------------------+
# +--------------------------------------+ +--------------------------------------+ +---------------------------------+
# | GET                                  | | (r"/api/([0-9]+)", BrainHandler)     | | BrainHandler.get                |
# | http://localhost:8888/api/500| |                                      | |                                 |
# +--------------------------------------+ +--------------------------------------+ +---------------------------------+
# +--------------------------------------+ +--------------------------------------+ +---------------------------------+
# | GET                                  | | (r"/version", VersionHandler)        | | VersionHandler.get              |
# | http://localhost:8888/version        | |                                      | |                                 |
# +--------------------------------------+ +--------------------------------------+ ]---------------------------------+
# Está api tem como proposito testar serevidor REST


class VersionHandler(tornado.web.RequestHandler):

    def get(self):
        #filters = self.request.arguments
        response = {'version': f'{version}',
                    'last_build': date.today().isoformat()}
        #key = self.get_argument('key', None, True)
        #print(filters.get('uf')[0].decode())
        self.write(response)


class ZipHandler(tornado.web.RequestHandler):
    def get(self, id):
        response = {'id': int(id),
                    'name': 'Brain',
                    'version': f'{version}',
                    'release_date': date.today().isoformat()}
        self.write(response)


application = tornado.web.Application([
    (r"/api/([0-9]+)", ZipHandler),
    (r"/version", VersionHandler)
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
