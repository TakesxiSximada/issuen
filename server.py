# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
from sandstorm.handlers import YAStaticFileHandler as StaticFileHandler


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r'/(.*)', StaticFileHandler, {'path': 'static'}),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
