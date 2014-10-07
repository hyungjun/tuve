# -*- encoding: utf-8 -*-

SPEC = """
  RDF  | TYPE             | TUVE_API          | DATAPOINTS | PLACES | INFO_EN              | INFO_JP
  -----+------------------+-------------------+------------+--------+----------------------+--------
  odpt | Train            | TRAIN             | ✓          |        | Train Location       | 列車ロケーション情報
  odpt | TrainInformation | TRAIN_INFORMATION | ✓          |        | Train Running        | 運行情報
  odpt | StationTimetable | STATION_TIMETABLE | ✓          |        | Station Timetable    | 駅時刻表
  odpt | StationFacility  | STATION_FACILITY  | ✓          |        | Station Facilities   | 施設情報（駅施設情報）
  odpt | PassengerSurvey  | PASSENGER_SURVEY  | ✓          |        | Number of Passengers | 駅情報（乗降人員数）
  odpt | RailwayFare      | RAILWAY_FARE      | ✓          |        | Railway Fare         | 運賃情報
  ug   | Poi              | POI               | ✓          | ✓      | Entrance Features    | 地物（駅出入口）情報
  mlit | Station          | GEO_STATION       |            | ✓      | Geo Data (Station)   | 国土交通省国土数値情報 地物（駅）情報
  mlit | Railway          | GEO_RAILWAY       |            | ✓      | Geo Data (Railway)   | 国土交通省国土数値情報 地物（線路）情報
  odpt | Station          | STATION           | ✓          | ✓      | Station General      | 東京メトロ駅情報
  odpt | Railway          | RAILWAY           | ✓          | ✓      | Railway Directions   | 東京メトロ路線情報
"""
