from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from app import db
from app.models import User
from app.forms import EditProfileForm

# Функция для регистрации маршрутов
def init_routes(app):
    # Главная страница
    @app.route('/')
    def home():
        return render_template('index.html')  # Отображаем шаблон index.html

    # Маршрут редактирования профиля
    @app.route('/edit_profile', methods=['GET', 'POST'])
    @login_required
    def edit_profile():
        form = EditProfileForm()
        if form.validate_on_submit():
            current_user.username = form.username.data
            current_user.email = form.email.data
            if form.password.data:
                current_user.set_password(form.password.data)
            db.session.commit()
            flash('Профиль успешно обновлён!')
            return redirect(url_for('edit_profile'))
        elif request.method == 'GET':
            form.prefill_form()  # Заполнение формы текущими данными
        return render_template('edit_profile.html', form=form)
