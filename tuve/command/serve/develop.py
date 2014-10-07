from tornado.web import Application
from tuve.core.handler import APIHandler
from tuve.core.handler.frontend import FrontendProxy
from tuve.util.option import Namespace

DEFAULTS = Namespace(
    HOST='localhost',
    PORT=8000,
    DEBUG=True,
    API_KEY='',
    LOG_LEVEL=5,
)
def handlers(opt):
    return [
        (r"/api/?(.*)", APIHandler, dict(opt=opt)),
    ]
def settings(opt):
    return dict(
        debug=opt.DEBUG,
        default_handler_class=FrontendProxy,
        static_path=opt.path.to.assets.str,
        static_url_prefix='/assets/'
    )
def application(opt):
    return Application(handlers(opt), **settings(opt))

def prepare(opt):
    opt.grace_update(DEFAULTS)
    opt.l.reset_level(opt.LOG_LEVEL)
    opt.l.info('TUVE is serving in <%s> context at:', opt.context)
    opt.l.info(opt.path)
    opt.env_fallback('API_KEY', 'TUVE_API_KEY')
    opt.log_introspection()

def main(opt):
    prepare(opt)
    import ujson
    from tornado import log
    from tornado import escape
    from tornado.httpserver import HTTPServer
    from tornado.ioloop import IOLoop
    escape.json = ujson # for better json io
    log.enable_pretty_logging()
    server = HTTPServer(application(opt))
    server.listen(opt.PORT)
    IOLoop.instance().start()
