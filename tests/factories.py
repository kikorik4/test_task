import factory
from faker.proxy import Faker

from app.models import Product, Category
from app.routes import db

faker = Faker()

class CategoryFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Category
        sqlalchemy_session = db.session

    name = factory.Faker('word')

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Override the default `_create` with a custom function."""
        category = model_class(*args, **kwargs)
        db.session.add(category)
        db.session.commit()  # Сохраняем в базе данных!
        return category

class ProductFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Product
        sqlalchemy_session = db.session

    name = factory.Faker('word')
    price = factory.Faker('pyfloat', positive=True, max_value=1000)
    description = factory.Faker('text')
    category = factory.SubFactory(CategoryFactory)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        product = model_class(*args, **kwargs)
        db.session.add(product)
        db.session.commit()
        return product
