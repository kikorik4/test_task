import pytest
import json
from app.models import Product, Category
from .factories import ProductFactory, CategoryFactory

def test_list_products(client, db_session):
    """Проверяем получение списка продуктов"""
    response = client.get("/products")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0

    if data:
        assert "id" in data[0]
        assert "name" in data[0]
        assert "price" in data[0]
        assert "category_id" in data[0]

def test_get_product_by_id(client, db_session):
    """Проверяем получение продукта по id"""
    product = db_session.query(Product).first()
    if product:
        response = client.get(f"/products/{product.id}")
        assert response.status_code == 200
        data = response.get_json()
        assert data["id"] == product.id
        assert data["name"] == product.name
    else:
        pytest.skip("No products found in the database")

def test_create_product(client, db_session):
    """Проверяем создание нового продукта"""
    category = CategoryFactory.create()

    new_product_data = {
        "name": "New Test Product",
        "price": 50.0,
        "category_id": category.id
    }
    response = client.post("/products", json=new_product_data)
    assert response.status_code == 201
    data = response.get_json()
    assert data["name"] == "New Test Product"
    assert data["category_id"] == category.id

def test_delete_product(client, db_session):
    """Проверяем удаление продукта по id"""
    product = ProductFactory.create()
    response = client.delete(f"/products/{product.id}")
    assert response.status_code == 204
    deleted_product = Product.query.get(product.id)
    assert deleted_product is None

def test_get_category(client, db_session):
    """Проверяем получение категорий"""
    response = client.get("/category")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_product_creation_with_factory(db_session):
    """Проверяем создание продукта с использованием фабрики"""
    product = ProductFactory.create()
    assert product.name is not None
    assert product.price > 0
    assert product.category is not None

def test_category_creation_with_factory(db_session):
    """Проверяем создание категории с использованием фабрики"""
    category = CategoryFactory.create()
    assert category.id is not None