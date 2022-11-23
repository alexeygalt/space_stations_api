from dao.station import StationDAO
from dao.indication import IndicationDAO
from setup_db import db

station_dao = StationDAO(db.session)
indication_dao = IndicationDAO(db.session)
