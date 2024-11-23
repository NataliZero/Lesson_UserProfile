from datetime import datetime
from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)  # Идентификатор
    username = db.Column(db.String(120), unique=True, nullable=False)  # Имя пользователя
    email = db.Column(db.String(120), unique=True, nullable=False)  # Почта
    password = db.Column(db.String(60), nullable=False)  # Пароль
    date_created = db.Column(db.DateTime, default=datetime.utcnow)  # Дата создания

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
