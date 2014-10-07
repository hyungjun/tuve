from tuve.compat.string import unicode

class ParamList(list):
    def __str__(self):
        return '&'.join(unicode(param) for param in self)
    def __add__(self, other):
        return ParamList(super(ParamList, self).__add__(other))
    def add_param(self, key, val):
        self.append(Parameter(key, val))

class Parameter(object):
    __slots__ = 'key val'.split()
    def __init__(self, key, val):
        self.key = key
        self.val = val
    def __str__(self):
        return '{s.key}={s.val}'.format(s=self)
    @property
    def as_plist(self):
        return ParamList([self])

