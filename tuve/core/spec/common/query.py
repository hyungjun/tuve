from tuve.compat.string import unicode
from tuve.core.spec.common.parameter import ParamList, Parameter
from tuve.core.spec.common.resource import Resource

class Query(object):
    __slots__ = 'resource spec params'.split()
    def __init__(self, resource='', spec='', params=None):
        self.resource = Resource(resource).as_rlist
        self.spec = spec
        self.params = params or ParamList()
    @property
    def _maybe_both(self):
        return '?' if self.resource and self.params else ''
    @property
    def str(self):
        return unicode(self)
    def __str__(self):
        if self.spec:
            return '{s.spec._endpoint}/{s.resource}?{extended_params}'.format(s=self, extended_params=self.params + self.spec._params)
        else:
            return '/{s.resource}{s._maybe_both}{s.params}'.format(s=self)
    def on(self, *resources):
        self.resource.extend(resources)
        return self
    def fork(self, params=False):
        return self.__class__(resource=unicode(self.resource), spec=self.spec,
                              params=self.params if params else None)
    def reset_params(self):
        self.params = ParamList()
        return self
    def add_param(self, key, val):
        self.params.append(Parameter(key, val))
        return self

