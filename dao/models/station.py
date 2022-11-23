from sqlalchemy.sql import func
from setup_db import db
from marshmallow import Schema, fields


class Station(db.Model):
    """model to station object"""
    __tablename__ = 'station'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    condition = db.Column(db.String, default='running')
    date_created = db.Column(db.DateTime, default=func.now())
    date_broken = db.Column(db.DateTime)
    x = db.Column(db.Integer, default=100)
    y = db.Column(db.Integer, default=100)
    z = db.Column(db.Integer, default=100)


class StationSchema(Schema):
    """simple schema to Station's model serialization """
    id = fields.Integer()
    name = fields.String()
    condition = fields.String()
    date_created = fields.DateTime()
    date_broken = fields.DateTime()
    # x = fields.Integer()
    # y = fields.Integer()
    # z = fields.Integer()


class StationSchemaState(Schema):
    """simple schema to Station's position serialization """
    x = fields.Integer()
    y = fields.Integer()
    z = fields.Integer()


station_schema = StationSchema()
stations_schema = StationSchema(many=True)
station_schema_state = StationSchemaState()
