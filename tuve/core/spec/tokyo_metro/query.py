# -*- encoding: utf-8 -*-

import ujson
from tuve.compat.string import unicode
from tuve.core.spec.tokyo_metro import preset
from tuve.core.spec.common.query import Query

#
# generic queries
#
class TokyoMetroQuery(Query):
    """
    tm = TokyoMetro(key)
    tm.datapoints.STATION_TIMETABLE(station=TokyoMetro.Tozai.Otemachi).get()
    """
    def get(self):
        from tornado.httpclient import HTTPClient
        res = HTTPClient().fetch(unicode(self))
        return ujson.loads(res.body)
#
# high level queries
#
class TokyoMetroDataPointsQuery(TokyoMetroQuery):
    """
    データ検索API (/api/v2/datapoints?)
    /api/v2/datapoints では、指定したクエリにマッチした情報を取得する。
    """

    # query presets
    STATION_TIMETABLE = preset.station_timetable
    TRAIN_INFORMATION = preset.train_information

class TokyoMetroPlacesQuery(TokyoMetroQuery):
    """
    地物情報検索API (/api/v2/places?)
    /api/v2/places では、/api/v2/datapoints で提供する検索機能に加え、
    地理情報を用いた領域絞込が可能となる。 APIで検索する対象となるデータは、
    本APIにて提供する地物属性を持つ全ての情報となり、地物属性を持たない情報は結果に含まれない。
    レスポンスは、クエリで指定された中心点から距離が近い地物から順に並べられた配列が取得できる。
    """

    # query presets
    POI = preset.poi

    def where(self, lon, lat, rad):
        return self.add_param('lon', unicode(lon)).add_param('lat', unicode(lat)).add_param('radius', unicode(rad))
