from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from config import Config

# Инициализация приложения
app = Flask(__name__)
app.config.from_object(Config)

# Инициализация расширений
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Указываем, какой маршрут использовать для логина, если пользователь не авторизован

# Импорт маршрутов после инициализации приложения
from app import routes
