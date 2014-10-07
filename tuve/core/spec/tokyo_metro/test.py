# -*- encoding: utf-8 -*-

import os

from tuve.mixin.introspective import i
from tuve.core.spec.tokyo_metro.namespace import TokyoMetro as TM
from tuve.core.spec.tokyo_metro.api import TokyoMetroAPI
from tuve.core.spec.tokyo_metro.query import TokyoMetroQuery
from tuve.compat.string import unicode

KEY = os.environ['TUVE_API_KEY']

def test_idea():
    tm = TokyoMetroAPI(KEY)
    q = TokyoMetroQuery('datapoints')
    q.add_param('rdf:type', 'odpt:Train')
    querystring = 'datapoints?rdf:type=odpt:Train'
    tm._query = q
    assert 'https://api.tokyometroapp.jp/api/v2/' + querystring + '&acl:consumerKey=%s' % KEY == unicode(tm)

def test_api_endpoint():
    from tuve.core.spec.common.endpoint import EndPoint
    ep = EndPoint(host='api.tokyometroapp.jp', nmspc_iter=['api', 'v2'])
    assert unicode(ep) == 'https://api.tokyometroapp.jp/api/v2'

def test_chaining():
    tm = TokyoMetroAPI(KEY)
    tm.query('datapoints').add_param('rdf:type', 'odpt:Train').add_param('dc:title', '東京')
    tm.query('datapoints').on('odpt.Station:TokyoMetro.Marunouchi.Tokyo')

def test_extended_query():
    assert TokyoMetroQuery == TokyoMetroAPI('').Query
    assert isinstance(TokyoMetroAPI('').query(''), TokyoMetroQuery)

def test_places():
    url = 'https://api.tokyometroapp.jp/api/v2/places?rdf:type=ug:Poi&lon=139.766926&lat=35.681265&radius=1000&acl:consumerKey=%s' % KEY
    query = TokyoMetroAPI(KEY).query('places').add_param('rdf:type', 'ug:Poi').add_param('lon', '139.766926').add_param('lat', '35.681265').add_param('radius', '1000')
    query_by_where = TokyoMetroAPI(KEY).places.add_param('rdf:type', 'ug:Poi').where('139.766926', '35.681265', '1000')
    query_by_where_with_num = TokyoMetroAPI(KEY).places.add_param('rdf:type', 'ug:Poi').where(139.766926, 35.681265, 1000)
    assert url == unicode(query) == unicode(query_by_where) == unicode(query_by_where_with_num)

def test_namespace():
    from tuve.compat.string import unicode
    assert 'TokyoMetro.Ginza.Shibuya' == unicode(TM.Ginza.Shibuya)

def test_functionality():
    from tornado.httpclient import HTTPClient
    qs = 'https://api.tokyometroapp.jp/api/v2/places?rdf:type=ug:Poi&lon=139.705678&lat=35.678156&radius=500&acl:consumerKey=%s' % KEY
    query = TokyoMetroAPI(KEY).places.POI(139.705678, 35.678156, 500)
    assert qs == unicode(query)
    # res = HTTPClient().fetch(unicode(query))
    # for ld in ujson.loads(res.body): i(ld)
