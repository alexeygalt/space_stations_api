from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.station import stations_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(stations_ns)


def create_data():
    with app.app_context():
        db.create_all()


app = create_app(Config())
create_data()


# @app.errorhandler(404)
# def page_404_error(error):
#     return jsonify({"Error 404": 'Sorry, information Not Found'}), 404


if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
