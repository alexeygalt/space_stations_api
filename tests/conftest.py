import pytest

from app import create_app
from config import Config
# from project.config import TestingConfig
# from project.server import create_app
from setup_db import db as database


@pytest.fixture
def app():
    app = create_app(Config())
    with app.app_context():
        yield app


@pytest.fixture
def db(app):
    database.init_app(app)
    database.drop_all()
    database.create_all()
    database.session.commit()

    yield database

    database.session.close()


@pytest.fixture
def client(app, db):
    with app.test_client() as client:
        yield client

