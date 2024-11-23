from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from app import app, db, bcrypt
from app.models import User
from app.forms import LoginForm, RegistrationForm

@app.route('/')
def home():
    return render_template('home.html')  # Главная страница

# Страница логина
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('account'))  # Если уже авторизованы, перенаправляем на аккаунт

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()  # Ищем пользователя по email
        if user and bcrypt.check_password_hash(user.password, form.password.data):  # Проверка пароля
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')  # Параметр next для редиректа
            return redirect(next_page) if next_page else redirect(url_for('home'))  # Перенаправление на домашнюю страницу или другую

        else:
            flash('Login unsuccessful. Please check email and password', 'danger')  # Сообщение о неудачной попытке логина

    return render_template('login.html', title='Login', form=form)

# Страница регистрации
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('account'))  # Если уже авторизованы, перенаправляем на аккаунт

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')  # Хешируем пароль
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)  # Создаём нового пользователя
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now log in', 'success')
        return redirect(url_for('login'))  # Перенаправляем на страницу логина

    return render_template('register.html', title='Register', form=form)

# Страница аккаунта
@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    return render_template('account.html', title='Account')  # Страница аккаунта

# Страница выхода
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))  # Перенаправляем на главную страницу
