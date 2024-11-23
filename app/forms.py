from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length

# Форма регистрации
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])  # Имя
    email = StringField('Email', validators=[DataRequired(), Email()])  # Почта
    password = PasswordField('Password', validators=[DataRequired()])  # Пароль
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])  # Подтверждение пароля
    submit = SubmitField('Sign Up')

# Форма для логина
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])  # Почта
    password = PasswordField('Password', validators=[DataRequired()])  # Пароль
    remember = BooleanField('Remember Me')  # Запомнить пользователя
    submit = SubmitField('Login')
