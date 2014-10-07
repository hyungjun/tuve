from tuve.compat.collection import items

class ClassNamePrintMeta(type):
    def __str__(cls):
        return cls.__name__

class NamespaceMock(object):
    __mock_name__ = None
    def __init__(self, name=None):
        self.__mock_name__ = name
    def __getattr__(self, attr):
        mock = NamespaceMock(attr)
        setattr(self, attr, mock)
        return mock

def freeze_mock(mock, metaclass=type, qualname=None):
    name = mock.__mock_name__ or mock.__class__.__name__
    if qualname:
        name = '%s.%s' % (qualname, name)
    nmspc = {
        key: freeze_mock(val, metaclass=metaclass, qualname=name)
        for key, val in items(vars(mock))
        if isinstance(val, NamespaceMock)
    }
    return metaclass(name, (object,), nmspc)
