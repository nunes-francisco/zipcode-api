# Teste de servidor REST
# 27/07/2018

import os

import tornado.ioloop
import tornado.web
import __init__


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # self.render('index.html')
        self.write('<h3> App version {}<h3>'.format(__init__.version))


# Onde o tornado irá procurar arquivos státicos
settings = {'template_path': os.path.join(os.path.dirname(__file__), "template"),
            'static_path': os.path.join(os.path.dirname(__file__), "static"), 'debug': True}

# URI
application = tornado.web.Application([(r"/", MainHandler)], **settings)

# Start server
if __name__ == "__main__":
    print("srever running...")
    print("Press ctrl + c to close")
    application.listen(8889)
    tornado.ioloop.IOLoop.instance().start()
