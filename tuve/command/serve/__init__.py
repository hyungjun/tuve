OPTIONS = [
    ['--HOST'     , str , 'Host name for serving'],
    ['--PORT'     , int , 'Port number for serving'],
    ['--DEBUG'    , bool, 'Related to mp forking and auto-reload in Tornado'],
    ['--API_KEY'  , str , 'API KEY if necessary'],
    ['--LOG_LEVEL', int , '5=VERBOSE...50=CRITICAL, [5, 10, 20, 30, 40, 50]'],
]
def register(sub_parser):
    serve_parser = sub_parser.add_parser(
        'serve',
        help='Serve TUVE backend',
        epilog='When DEBUG flag is off, Tornado tries to fork processes by a number of processors. '
        'And if API_KEY is missing, TUVE will looks up OS environment variables if `TUVE_API_KEY` is defined.'
    )
    serve_parser.add_argument(
        'context',
        metavar = 'CONTEXT',
        choices = 'production develop'.split(),
        nargs   = '?',
        default = 'develop',
        help    = (
            "TUVE's running context. "
            "You have `production` and `develop(default)` context."
        )
    )
    for name, type, help in OPTIONS:
        serve_parser.add_argument(name, type=type, help=help, metavar='')
