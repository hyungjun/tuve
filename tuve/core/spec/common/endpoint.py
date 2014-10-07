from tuve.mixin.introspective import PlainIntrospective

class MaybePort(str):
    def __str__(self):
        return ':' + self if self else ''

class EndPoint(PlainIntrospective):
    __slots__ = 'schema host port maybe_port nmspc'.split()
    def __init__(self, schema='https', host='localhost', port='', nmspc_iter=()):
        self.schema = schema
        self.host = host
        self.port = port
        self.maybe_port = MaybePort(port)
        self.nmspc = '/'.join(nmspc_iter)
    def __str__(self):
        return '{s.schema}://{s.host}{s.maybe_port}/{s.nmspc}'.format(s=self)


