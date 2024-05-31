from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired

class Register_form(FlaskForm):
    name = StringField('Имя', validators=[DataRequired('Заполните имя')])
    email = EmailField('Почта', validators=[DataRequired('Заполните поле')])
    password = PasswordField('Пароль', validators=[DataRequired('Заполните пароль')])
    password2 = PasswordField('Поттвердите Пароль', validators=[DataRequired('Заполните пароль')])
    button = SubmitField('Зарегистрироваться')

class Login_form(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired('Заполните поле')])
    password = PasswordField('Пароль', validators=[DataRequired('Заполните пароль')])
    button = SubmitField('Войти')

