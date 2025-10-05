# Flask Application - Catalog Management API

Этот проект представляет собой API для управления каталогом товаров, включающим товары и категории. Он предназначен для демонстрации базовых концепций Flask и Docker.

## Описание

Приложение предоставляет API для создания, чтения, обновления и удаления (CRUD) товаров и категорий. Оно использует Flask-SQLAlchemy для взаимодействия с базой данных и Docker для упрощения развертывания.

## Необходимые условия

• Python 3.9 или выше
• Docker

## Установка и запуск

1. Клонируйте репозиторий:

```
bash
  python3 -m venv venv
  source venv/bin/activate # Linux/macOS
  # venv\Scripts\activate  # Windows

```

3. Установите зависимости:

  
```
bash
  pip install -r requirements.txt

```

4. Сборка Docker-образа:

```

bash
  docker build -t flask-app .

```

▌Конфигурация

•  База данных: По умолчанию, приложение использует SQLite базу данных (instance/products.db). Вы можете изменить URL базы данных в файле app/__init__.py или через переменную окружения DATABASE_URL.
•  Порт: Приложение по умолчанию слушает порт 5000. Это можно изменить в команде запуска flask run или в Dockerfile.

▌API Endpoints

▌Товары (Products)

•  GET /products: Получить список всех товаров.
•  GET /products/{id}: Получить информацию о товаре с указанным ID.
•  POST /products: Создать новый товар. Требует JSON-данные в теле запроса:
  
```

json
  {
   "name": "Product Name",
   "description": "Product Description",
   "price": 99.99,
   "category_id": 1
  }

```

•  DELETE /products/{id}: Удалить товар с указанным ID.
•  GET /categories: Получить список всех категорий.
•  POST /categories: Создать новую категорию. Требует JSON-данные в теле запроса:

```

json
  {
   "name": "Category Name",
  }

```

▌Зависимости

•  Flask
•  Flask-SQLAlchemy
•  SQLAlchemy
•  [pytest, factory_boy, Faker (если используете для тестов)]
