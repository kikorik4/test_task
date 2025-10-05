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
        category1 = Category(name="Test Category 1")
        category2 = Category(name="Test Category 2")

        product1 = Product(name="Test Product 1", price=100.0, description="Test Description 1", category_id=category1.id)
        product2 = Product(name="Test Product 2", price=200.0, description="Test Description 2", category_id=category2.id)

        _db.session.add_all([category1, category2, product1, product2])
        _db.session.commit()

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