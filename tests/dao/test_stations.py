import pytest

from dao.station import StationDAO

from dao.models.station import Station


class TestStationsDAO:

    @pytest.fixture
    def stations_dao(self, db):
        return StationDAO(db.session)

    @pytest.fixture
    def station_1(self, db):
        s = Station(name="first")
        db.session.add(s)
        db.session.commit()
        return s

    @pytest.fixture
    def station_2(self, db):
        s = Station(name="second")
        db.session.add(s)
        db.session.commit()
        return s

    def test_get_one(self, station_1, stations_dao):
        assert stations_dao.get_one(station_1.id) == station_1

    def test_get_all(self, station_1, station_2, stations_dao):
        assert stations_dao.get_all() == [station_1, station_2]

    def test_create(self, stations_dao, station_2):
        data = {

            "name": "Test"
        }
        new_station = stations_dao.create(data)
        assert new_station.id == 2
        assert new_station.name == "Test"
        assert new_station.condition == 'running'
        assert new_station.x == 100
        assert new_station.y == 100
        assert new_station.z == 100

    def test_update(self, stations_dao, station_2):
        data = {

            "name": "updated"
        }
        updated_station = stations_dao.create(data)
        assert updated_station.name == "updated"
        assert updated_station.condition == 'running'

    def test_update_partial_1(self, stations_dao, station_1):
        data = {
            "axis": "z",
            "distance": 200
        }
        updated_station = stations_dao.update_partial(data, 1)
        assert updated_station.z == 300
        assert updated_station.condition == "running"

    def test_update_partial_2(self, stations_dao, station_1):
        data = {
            "axis": "y",
            "distance": 100
        }
        updated_station = stations_dao.update_partial(data, 1)
        assert updated_station.y == 200
        assert updated_station.condition == "running"

    def test_update_partial_3(self, stations_dao, station_1):
        data = {
            "axis": "x",
            "distance": 100
        }
        updated_station = stations_dao.update_partial(data, 1)
        assert updated_station.x == 200
        assert updated_station.condition == "running"

    def test_update_partial_4(self, stations_dao, station_1):
        data = {
            "axis": "x",
            "distance": -200
        }
        updated_station = stations_dao.update_partial(data, 1)
        assert updated_station.condition == "broken"
        assert updated_station.date_broken is not None

    def test_update_partial_5(self, stations_dao, station_1):
        data = {
            "axis": "y",
            "distance": -200
        }
        updated_station = stations_dao.update_partial(data, 1)
        assert updated_station.condition == "broken"
        assert updated_station.date_broken is not None

    def test_update_partial_6(self, stations_dao, station_1):
        data = {
            "axis": "z",
            "distance": -200
        }
        updated_station = stations_dao.update_partial(data, 1)
        assert updated_station.condition == "broken"
        assert updated_station.date_broken is not None

    def test_delete(self, stations_dao, station_1):
        stations_dao.delete(station_1.id)
        assert stations_dao.get_one(station_1.id) is None
