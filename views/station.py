from flask_restx import Resource, Namespace
from flask import request
from implemented import station_dao, indication_dao
from dao.models.station import stations_schema, station_schema, station_schema_state


stations_ns = Namespace('stations')


@stations_ns.route('/')
class StationsView(Resource):
    def get(self):
        return stations_schema.dump(station_dao.get_all()), 200

    def post(self):
        upload_data = request.get_json()
        if station_dao.create(upload_data):
            return station_schema.dump(station_dao.create(upload_data)), 201
        return f"Can't create station with name '{upload_data.get('name')}'", 404


@stations_ns.route("/<int:sid>")
class StationsView(Resource):
    def get(self, sid):
        if station_dao.get_one(sid):
            return station_schema.dump(station_dao.get_one(sid)), 200
        return f'Station {sid} not found', 404

    def put(self, sid: int):
        upload_data = request.get_json()
        if not upload_data.get('id'):
            upload_data['id'] = sid
        if station_dao.update(upload_data):
            return station_schema.dump(station_dao.update(upload_data)), 201
        return f'Station {upload_data.get("id")} not found', 404

    def delete(self, sid):
        if station_dao.get_one(sid):
            return station_schema.dump(station_dao.delete(sid)), 204
        return f'Station {sid} not found', 404


@stations_ns.route("/<int:sid>/state/")
class StationsView(Resource):
    def get(self, sid):
        if station_dao.get_one(sid):
            return station_schema_state.dump(station_dao.get_one(sid)), 200
        return f'Station {sid} not found', 404

    def post(self, sid):
        indication_data = request.get_json()
        if station_dao.get_one(sid):
            if indication_dao.create(indication_data):
                station_dao.update_partial(indication_data, sid)
                return station_schema_state.dump(station_dao.get_one(sid)), 201
            return f'ValidationError, check all column'
        return f'Station {sid} not found', 404
