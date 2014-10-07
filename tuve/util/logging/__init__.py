import logging

DEFAULT_LOGGER_NAME = 'tuve-def'

class ColorizedStreamFormatter(logging.Formatter):

    level_color_code = dict(
        NOTSET   = 37,
        DEBUG    = 36,
        INFO     = 32,
        WARNING  = 33,
        ERROR    = 35,
        CRITICAL = 31,
    )
    def format(self, record):
        foreground = self.level_color_code.get(record.levelname, 37) # fallback to white
        record.coloredname         = '\033[0;%sm%s\033[0m'   % (37, record.name)
        record.coloreddelimiter    = '\033[0;%sm%s\033[0m'   % (35, '@')
        record.coloredlevelinitial = '\033[1;%sm|%s|\033[0m' % (foreground, record.levelname[0])
        record.coloredbgopen       = '\033[0;30;%sm' % (foreground + 10)
        record.coloredbgclose      = '\033[0m'
        record.location            = ('%s.%s:' % (record.filename[:-3], record.funcName)) if record.levelno > 5 else ''
        return super(ColorizedStreamFormatter, self).format(record)

    def __init__(self, fmt=None, datefmt=None):
        summary  = '%H:%M:%S'
        detail   = '%Y-%m-%d ' + summary
        time_fmt = summary
        super(ColorizedStreamFormatter, self).__init__(fmt, time_fmt)

colored_stream_formatter = ColorizedStreamFormatter(
    '%(coloredname)s%(coloreddelimiter)s'
    '%(asctime)s%(coloredlevelinitial)s'
    '%(location)s'
    '%(coloredbgopen)s %(message)s %(coloredbgclose)s'
)

# domain specific log machinery
logging.VERBOSE = 5
Logger = logging.Logger
logging.addLevelName(logging.VERBOSE, 'VERBOSE')
Logger.verbose = lambda inst, msg, *args, **kwargs: inst.log(logging.VERBOSE, msg, *args, **kwargs)

for name in (
    'verbose' , # DEV CODING-TIME
    'debug'   , # DEV RUN-TIME
    'info'    , # SERVICE TRACKING
    'warning' , # DEPRECATION, CATCHABLE
    'error'   , # BOOTSTRAP FAIL, UNCATCHABLE
    'critical'  # SECURITY
    ): setattr(Logger, name[0], getattr(Logger, name))

def colored(name=None, level=50):
    name = name or DEFAULT_LOGGER_NAME
    if name in logging.Logger.manager.loggerDict:
        return logging.getLogger(name)
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    logger.setLevel(level)
    handler.setLevel(level)
    handler.setFormatter(colored_stream_formatter)
    logger.addHandler(handler)
    logger.debug('initializing <%s> logger at level %s !' % (name, level))
    return logger

def reset_level(logger, level):
    logger.setLevel(level)
    for h in logger.handlers:
        h.setLevel(level)

Logger.reset_level = reset_level
