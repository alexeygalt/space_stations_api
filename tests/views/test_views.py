import pytest

from dao.models.station import Station


class TestStationsViews:

    @pytest.fixture
    def station(self, db):
        s = Station(name="first")
        db.session.add(s)
        db.session.commit()
        return s

    def test_many(self, client, station):
        response = client.get("/stations/")
        assert response.status_code == 200
        assert len(response.json) == 1

    def test_one(self, client, station):
        response = client.get("/stations/1")
        assert response.status_code == 200
        assert len(response.json) == 5

    def test_station_not_found(self, client, station):
        with pytest.raises(Exception) as exc_info:
            response = client.get("/station/2/")
            assert response == exc_info

