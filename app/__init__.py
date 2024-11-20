from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()  # Инициализация базы данных
login = LoginManager()  # Инициализация Flask-Login
login.login_view = 'login'  # Страница входа, если пользователь не авторизован

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Конфигурация приложения

    db.init_app(app)  # Инициализация базы данных с приложением
    login.init_app(app)  # Инициализация Flask-Login с приложением

    with app.app_context():
        from app.routes import init_routes  # Импортируем функцию регистрации маршрутов
        init_routes(app)  # Регистрируем маршруты

    return app
