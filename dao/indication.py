from dao.models.indication import Indication


class IndicationDAO:
    def __init__(self, session):
        self.session = session

    def create(self, data):
        try:
            new_indication = Indication(**data)
            self.session.add(new_indication)
            self.session.commit()
            return new_indication
        except Exception as e:
            print(e)
            self.session.rollback()

