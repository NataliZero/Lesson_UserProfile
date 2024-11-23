from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from app import app, db, bcrypt
from app.models import User
from app.forms import LoginForm

@app.route('/')
def home():
    return render_template('home.html')  # Главная страница

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('account'))  # Перенаправляем, если пользователь уже авторизован

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()  # Проверка пользователя
        if user and bcrypt.check_password_hash(user.password, form.password.data):  # Проверка пароля
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')  # Параметр next для перенаправления после логина
            return redirect(next_page) if next_page else redirect(url_for('home'))  # Перенаправление на домашнюю страницу
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')  # Сообщение о неудачном логине

    return render_template('login.html', title='Login', form=form)  # Отображаем форму логина

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    if request.method == 'POST':
        new_username = request.form.get('username')
        new_email = request.form.get('email')
        new_password = request.form.get('password')

        if new_username:
            current_user.username = new_username
        if new_email:
            current_user.email = new_email
        if new_password:
            hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8')
            current_user.password = hashed_password

        db.session.commit()  # Сохраняем изменения в базе данных
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))  # Перенаправление на страницу аккаунта

    return render_template('account.html', title='Account')  # Отображаем страницу аккаунта

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))  # Перенаправление на главную страницу
