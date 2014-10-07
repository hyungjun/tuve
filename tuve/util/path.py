import importlib
from pathlib import Path

class To(object):
    def __init__(self, path):
        self.path = path

    @classmethod
    def _provide_hop(cls, attr, *paths):
        setattr(cls, attr, property(lambda self: self.path.joinpath(*paths)))

pathmap = [line.split() for line in '''\
    logs     logs
    docs     docs
    command  tuve command
    core     tuve core
    frontend frontend
    dist     frontend dist
    assets   frontend dist assets
'''.splitlines()]

for hops in pathmap:
    To._provide_hop(*hops)

def imports(self, *names):
    body = self.as_posix().rpartition('/tuve/')[2]
    if not body:
        raise ImportError('Attempting to import outside tuve !')
    import_path = '.'.join(['tuve'] + body.split('/') + list(names))
    try:
        return importlib.import_module(import_path)
    except Exception as e:
        raise ImportError(e)

def find_module(self, by_name=False):
    return [
        node.name if by_name else node for node in self.iterdir()
        if node.is_dir() and node.joinpath('__init__.py').exists()]

Path.imports = imports
Path.find_module = find_module
Path.str = property(lambda self: str(self))
Path.to = property(lambda self: To(self))
# Path with APP_PATH resolved
app_path = Path(__file__).parent.parent.parent.resolve()
