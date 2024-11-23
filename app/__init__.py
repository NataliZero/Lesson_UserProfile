from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Инициализация Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Убедитесь, что у вас есть секретный ключ
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Инициализация расширений
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Указываем имя роута для логина

# Импортируем модель пользователя
from app.models import User

# Настройка Flask-Login для загрузки пользователя
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Импортируем маршруты
from app import routes
