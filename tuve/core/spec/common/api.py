from abc import ABCMeta, abstractmethod
from tuve.core.spec.common.endpoint import EndPoint
from tuve.core.spec.common.query import Query
from tuve.core.spec.common.parameter import ParamList

class ABCSpec(ABCMeta('APIMetaBase', (), {})):

    _endpoint = None
    _query = None
    _params = None
    Query = Query

    def __init__(self, *args, **kwargs):
        self._params = ParamList()
        self._query = Query()
        self.initialized(*args, **kwargs)

    @abstractmethod
    def __str__(self):
        """
        Classes such as a HTTP requester that are trying to use this API spec class can invoke `__str__` on its instance to get a formatted URL.
        """
    @abstractmethod
    def initialized(self):
        """
        """
    @property
    def extended_params(self):
        """
        When Spec is holding extra params for some reason, this property can be used for extending parameters of `query` object. For example,

            URL = '{s.endpoint}/{s.query}'.format(s=self)

        this could be extended by rewriting like below.

            URL = '{s.endpoint}/{s.query.resource}?{s.extended_params}'.format(s=self)
        """
        if self._query and self._params:
            return self._query.params + self._params
        raise AttributeError('Attribute both `query` and `params` should not be missing in order to extend.')

    def endpoint(self, *args, **kwargs):
        self._endpoint = EndPoint(*args, **kwargs)
        return self

    def query(self, resource):
        return self.Query(resource=resource, spec=self)

    def add_param(self, key, val):
        self._params.add_param(key, val)
        return self
