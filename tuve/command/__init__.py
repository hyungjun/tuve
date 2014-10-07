import traceback
from tuve.util import option
from tuve.compat.string import unicode
from tuve.compat.collection import items

def autorun(args=None):
    try:
        option.register_commands()
        opt, unknown = option.arg_parser.parse_known_args(args)
        if not opt.command: # python2/3 compatibility
            raise option.ArgumentParserError('too few arguments')
    except (option.ArgumentParserError, ImportError) as e:
        print(e)
        help = option.arg_parser.format_help()
        print('\n%s\n\033[33m%s\033[0m\n' % (help, unicode(e)))
    else:
        try:
            return opt.generic_main()
        except Exception as e:
            tb = traceback.format_exc()
            print('\n%s\n\n\033[31m%s\033[0m' % (
                '===============\nRuntime Error !\n===============', tb))

def run(*args, **kwargs):
    options = ['--%s=%s' % (k, v) for k, v in items(kwargs)]
    return autorun([arg for arg in args if arg] + options)
