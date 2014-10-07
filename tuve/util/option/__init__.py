import os
from argparse import ArgumentParser, Namespace
from argparse import RawTextHelpFormatter
from tuve.util.path import app_path
from tuve.util.logging import colored, DEFAULT_LOGGER_NAME
from tuve.mixin.introspective import Introspective
from tuve.compat.cls import func
from tuve.compat.collection import items

def grace_update(self, mapping):
    for key, val in items(vars(mapping)):
        if getattr(self, key) == None:
            setattr(self, key, val)

def generic_main(self):
    imports = self.path.to.command.imports
    command = imports(self.command)
    if hasattr(command, 'main'):
        return command.main(self)
    return imports(self.command, self.context).main(self)

def log_introspection(self, logger=None):
    logger = logger or self.l
    for key, val in self._pad_items():
        logger.verbose('%s|%s', key, val)

def env_fallback(self, key, env_key):
    if not getattr(self, key):
        val = os.environ.get(env_key)
        if val:
            setattr(self, key, val)
        else:
            self.l.warning('Option `%s` was not provided.' % key)

Namespace.grace_update = grace_update
Namespace.generic_main = generic_main
Namespace.log_introspection = log_introspection
Namespace.env_fallback = env_fallback
Namespace._pad_items = func(Introspective._pad_items)
Namespace.path = app_path
Namespace.l = colored(DEFAULT_LOGGER_NAME)

class ArgumentParserError(Exception):
    pass
class AppArgumentParser(ArgumentParser):
    def error(self, message):
        raise ArgumentParserError(message)
arg_parser = AppArgumentParser(
    prog='python tuve',
    formatter_class=RawTextHelpFormatter
)
cmd_names = app_path.to.command.find_module(by_name=True)
sub_parser = arg_parser.add_subparsers(
    dest='command',
    metavar='COMMAND',
    help=("TUVE's entry point.\n"
        "You might want to specity 'serve' in most cases\n"
        "Possible values: \033[35m%s\033[0m\n\n" % '|'.join(cmd_names)
    )
)
def register_commands(command='command'):
    for command in app_path.joinpath('tuve', command).find_module():
        command.imports().register(sub_parser)
