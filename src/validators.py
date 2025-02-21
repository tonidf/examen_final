from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, ValidationError, EmailField
from wtforms.validators import Length, DataRequired, Email, EqualTo


class RegisterForm(FlaskForm):

    email = EmailField('Correo electronico', validators=[DataRequired(), Length(min=10, max=30), Email()])
    username = StringField('Nombre de usuario', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6, max=12), EqualTo('confirm', 'La contraseña debe ser la misma')])
    confirm = PasswordField('Repite la contraseña', validators=[DataRequired(), Length(min=6, max=12)])

    submit = SubmitField('Registrarse')

class LoginForm(FlaskForm):

    username = StringField('Nombre de usuario', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6, max=12)])
    submit = SubmitField('Iniciar sesion')

class ContactForm(FlaskForm):
    fullname = StringField('Nombre', validators=[DataRequired(), Length(min=4, max=20)])
    phone = StringField('Nombre', validators=[DataRequired(), Length(min=4, max=20)])
    email = email = EmailField('Correo electronico', validators=[DataRequired(), Length(min=10, max=30), Email()])