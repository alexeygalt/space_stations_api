from sqlalchemy.sql import func
from dao.models.station import Station


class StationDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Station).all()

    def get_one(self, sid):
        return self.session.query(Station).get(sid)

    def create(self, data):
        try:
            new_station = Station(
                name=data.get('name')
            )
            self.session.add(new_station)
            self.session.commit()
            return new_station
        except Exception as e:
            print(e)
            self.session.rollback()

    def update(self, data):
        try:
            station = self.session.query(Station).get(data['id'])
            station.name = data.get('name')
            self.session.add(station)
            self.session.commit()
            return station
        except Exception as e:
            print(e)
            self.session.rollback()

    def update_partial(self, data,sid):
        station = self.session.query(Station).get(sid)
        position = data.get('axis')
        distance = data.get('distance')
        if position == 'x':
            station.x += distance
        elif position == 'y':
            station.y += distance
        else:
            station.z += distance
        if any([x < 0 for x in (station.x, station.y, station.z)]):
            station.condition = 'broken'
            station.date_broken = func.now()
        self.session.add(station)
        self.session.commit()


    def delete(self, pk):
        try:
            station = self.session.query(Station).get(pk)
            self.session.delete(station)
            self.session.commit()
        except Exception as e:
            print(e)
            self.session.rollback()
