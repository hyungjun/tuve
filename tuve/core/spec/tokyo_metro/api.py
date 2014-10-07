from tuve.core.spec.common.api import ABCSpec
from tuve.mixin.introspective import PlainIntrospective
from tuve.core.spec.tokyo_metro import query

class TokyoMetroAPI(PlainIntrospective, ABCSpec):
    Query = query.TokyoMetroQuery
    def initialized(self, key):
        self.key = key
        self.add_param('acl:consumerKey', self.key)
        self.endpoint(host='api.tokyometroapp.jp', nmspc_iter=['api', 'v2'])
    def __str__(self):
        return '{s._endpoint}/{s._query.resource}?{s.extended_params}'.format(s=self)

    #
    # High level interfaces endpoint
    #
    @property
    def datapoints(self):
        return query.TokyoMetroDataPointsQuery(resource='datapoints', spec=self)
    @property
    def places(self):
        return query.TokyoMetroPlacesQuery(resource='places', spec=self)
