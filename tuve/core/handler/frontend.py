from functools import partial
from tornado.web import RequestHandler, StaticFileHandler
from tuve.util.path import app_path

class FrontendProxy(StaticFileHandler):
    root = app_path.to.dist.str
    def initialize(self):
        self.get = partial(self.get, 'index.html')

