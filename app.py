from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.station import stations_ns


def create_app(config_object):
    """create app with all settings"""
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    """init db and register namespaces"""
    db.init_app(app)
    api = Api(app)
    api.add_namespace(stations_ns)


def create_data():
    with app.app_context():
        db.create_all()


app = create_app(Config())
create_data()


if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
