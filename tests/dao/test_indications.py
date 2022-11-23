import pytest

from dao.indication import IndicationDAO

from dao.models.indication import Indication


class TestIndicationDAO:

    @pytest.fixture
    def indications_dao(self, db):
        return IndicationDAO(db.session)

    @pytest.fixture
    def indication_1(self, db):
        i = Indication(user="test", axis='y', distance=100)
        db.session.add(i)
        db.session.commit()
        return i

    def test_create(self, indications_dao, indication_1):
        data = {
            "user": "alex",
            "axis": "y"
            }
        new_indication = indications_dao.create(data)
        assert AttributeError

    def test_create_2(self, indications_dao, indication_1):
        data = {
            "user": "alex",
            "axis": "y",
            "distance": 100
            }
        new_indication = indications_dao.create(data)
        assert new_indication.id == 2