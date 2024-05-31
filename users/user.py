from flask import Blueprint, render_template
from users.forms import Register_form, Login_form

user_bp = Blueprint('users', __name__, url_prefix='/user')

@user_bp.route('/')
def home_user():
    reg_url = '<br><a href="/user/register">Зарегистрироваться</a><br>'
    login_url = '<a href="/user/login">Логин</a><br>'
    return f'Добро пожаловать на наш сайт и выберите страницу {reg_url+login_url}'

@user_bp.route('/register')
def register():
    form = Register_form()
    return render_template('register.html', form=form)
@user_bp.route('/login')
def login():
    form = Login_form()
    return render_template('login.html', form=form)