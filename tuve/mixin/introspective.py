import collections
from tuve.compat.collection import items
from tuve.compat.string import unicode, format
from tuve.compat.cls import singledispatch

def ellipsis(string, max_len=32):
    str_len = len(string)
    return string if str_len <= max_len else string[:max_len] + '...[%s:%s]' % (max_len, str_len)

class Introspective(object):
    def _pad_items(self, mapping=None, padding=0, max_len=48):
        kvs = {k: getattr(self, k) for k in self.__slots__
               } if hasattr(self, '__slots__') else mapping or vars(self)
        if not kvs:
            return []
        keys = [ellipsis(unicode(v)) for v in kvs.keys()]
        vals = [ellipsis(unicode(v)) for v in kvs.values()]
        key_width = max(map(len, keys)) + padding
        val_width = max(map(len, vals)) + padding
        base = '{:{to}{width}}'
        return sorted((
            format(base, k, to='>', width=key_width),
            format(base, v, to='<', width=val_width)
            ) for k, v in zip(keys, vals)
        )

class PlainIntrospective(Introspective):
    def introspect(self):
        try:
            _repr = repr(self)
        except Exception as e:
            _repr = repr(e)
        try:
            _str = unicode(self)
        except Exception as e:
            _str = repr(e)
        print('\n========= Plain Introspection =========')
        print('repr : %s' % _repr)
        print('str  : %s' % _str)
        if hasattr(self, '__slots__'):
            print('slots: %s' % self.__slots__)
        print('attrs:')
        print( '\n'.join('|'.join(line) for line in self._pad_items()))
        print('')

@singledispatch
def i(obj):
    i = PlainIntrospective()
    i.__dict__ = vars(obj)
    i.introspect()

@i.register(collections.MutableMapping)
def introspect_dict(obj):
    i = PlainIntrospective()
    i.__dict__ = obj
    i.introspect()
