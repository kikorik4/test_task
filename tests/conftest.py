import pytest
from datetime import datetime

from app.models import Category, Product
from app.routes import create_app, db as _db


@pytest.fixture
def app():
    _app = create_app()
    _app.config["TESTING"] = True
    _app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with _app.app_context():
        _db.create_all()

        yield _app

        _db.session.remove()
        _db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def db_session(app):
    with app.app_context():
        yield _db.session