from typing import List

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request, abort

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///products.db'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    from .models import Product, Category

    with app.app_context():
        db.create_all()

    @app.route('/products', methods=['GET'])
    def get_products():
        """Получение продуктов"""
        products: List[Product] = db.session.query(Product).all()
        products_list = [p.to_json() for p in products]
        return jsonify(products_list), 200

    @app.route("/products/<int:id>", methods=['GET'])
    def get_product_by_id(id: int):
        """Получение продукта по ид"""
        product: Product = db.session.query(Product).get(id)
        if not product:
            abort(404, description="Product not found")
        return jsonify(product.to_json()), 200

    @app.route("/products", methods=['POST'])
    def create_product():
        """Создание нового продукта"""
        data = request.get_json()
        name = data.get('name')
        price = data.get('price')
        description = data.get('description')
        category_id = data.get('category_id')
        if not name or not price or not category_id:
            abort(400, description="Name, price, and category are required")
        category = db.session.query(Category).filter_by(id=category_id).first()
        if not category:
            abort(400, description="Category not found")
        new_product = Product(name=name,
                              price=price,
                              description=description,
                              category_id=category_id)

        db.session.add(new_product)
        db.session.commit()
        return jsonify(new_product.to_json()), 201

    @app.route('/products/<int:id>', methods=['DELETE'])
    def delete_product(id):
        """Удаление продукта по id"""
        product = Product.query.get_or_404(id)
        db.session.delete(product)
        db.session.commit()
        return jsonify({'message': 'Product deleted'}), 204


    @app.route('/category', methods=["GET"])
    def get_categories():
        """Получение категорий"""
        categories: List[Product] = db.session.query(Category).all()
        categories_list = [p.to_json() for p in categories]
        return jsonify(categories_list), 200

    @app.route("/category", methods=['POST'])
    def create_category():
        """Создание новой категории"""
        name = request.form.get('name', type=str)
        new_category = Category(name=name)
        db.session.add(new_category)
        db.session.commit()
        return jsonify(new_category.to_json()), 201

    return app