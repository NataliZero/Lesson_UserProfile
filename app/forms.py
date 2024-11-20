from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User
from flask_login import current_user, login_required

# Форма редактирования профиля
class EditProfileForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    email = StringField('Электронная почта', validators=[DataRequired(), Email()])
    password = PasswordField('Новый пароль', validators=[EqualTo('confirm', message='Пароли должны совпадать')])
    confirm = PasswordField('Подтверждение нового пароля')
    submit = SubmitField('Обновить профиль')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user is not None:
                raise ValidationError('Пользователь с таким именем уже существует.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user is not None:
                raise ValidationError('Пользователь с таким адресом электронной почты уже существует.')

    def validate_password(self, password):
        if len(password) > 50:
            raise ValidationError("Слишком длинная строка для пароля.")

    def validate_confirm(self, confirm):
        if len(confirm) > 50:
            raise ValidationError("Слишком длинная строка для подтверждения пароля.")

    def prefill_form(self):
        self.username.data = current_user.username
        self.email.data = current_user.email
        self.password.data = current_user.password
        self.confirm.data = current_user.password


# Форма входа
class LoginForm(FlaskForm):
    email = StringField('Электронная почта', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')
