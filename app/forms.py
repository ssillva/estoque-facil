from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateField
from wtforms.widgets import CheckboxInput
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Nome de Usuario', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Enviar')