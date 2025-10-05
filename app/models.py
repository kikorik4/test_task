from sqlalchemy.orm import relationship

from .routes import db


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    def __repr__(self):
        return f"Category {self.id}, {self.name}"

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = relationship('Category', backref='products')

    def __repr__(self):
        return f"Product {self.id}, {self.name}, {self.price}, {self.category_id}"

    def to_json(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

