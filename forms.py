from flask_wtf import FlaskForm
from wtforms.validators import Email
from wtforms.validators import DataRequired,length,EqualTo
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms import StringField
from wtforms import BooleanField

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),length(min=2,max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

    