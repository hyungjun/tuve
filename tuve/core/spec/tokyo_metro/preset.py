# -*- encoding: utf-8 -*-

from tuve.compat.string import unicode

def station_timetable(query, railway_station):
    """
    # 駅時刻表
    query = tm.datapoints.STATION_TIMETABLE(TM.Ginza.Shibuya)
    """
    return query.reset_params(
    ).add_param('rdf:type', 'odpt:StationTimetable'
    ).add_param('odpt:station', 'odpt.Station:' + unicode(railway_station)
    )

def train_information(query, railway=None):
    """
    # 列車運行情報
    query = tm.datapoints.TRAIN_INFORMATION() # query all railway information
    query = tm.datapoints.TRAIN_INFORMATION(TM.Ginza)
    """
    query = query.reset_params().add_param('rdf:type', 'odpt:TrainInformation')
    if railway:
        query.add_param('odpt:railway', 'odpt.Railway:' + unicode(railway))
    return query

def poi(query, lon, lat, radius):
    """
    # 地物情報
    # Querying entrance/elevator information nearby Kitasando station.
    query = tm.places.POI(lon=139.705678, lat=35.678156, radius=500)
    """
    return query.reset_params().add_param('rdf:type', 'ug:Poi'
    ).where(lon, lat, radius)
