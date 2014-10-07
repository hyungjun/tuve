from tuve.command.serve.develop import DEFAULTS, application, prepare

DEFAULTS.DEBUG = False
DEFAULTS.LOG_LEVEL = 30

def main(opt):
    prepare(opt)
    import ujson
    from tornado import escape
    from tornado.ioloop import IOLoop
    from tornado.httpserver import HTTPServer
    from tornado.ioloop import IOLoop
    escape.json = ujson # for better json io
    server = HTTPServer(application(opt))
    server.bind(opt.PORT)
    server.start(0) # fork !
    IOLoop.instance().start()
