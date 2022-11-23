from setup_db import db
from marshmallow import Schema, fields


class Indication(db.Model):
    __tablename__ = 'indication'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String, nullable=False)
    axis = db.Column(db.String, nullable=False)
    distance = db.Column(db.Integer, nullable=False)


class IndicationSchema(Schema):
    id = fields.Integer()
    user = fields.String()
    axis = fields.String()
    distance = fields.Integer()


indication_schema = IndicationSchema()
indications_schema = IndicationSchema(many=True)
