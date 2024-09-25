#!/usr/bin/python3

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError, Email, EqualTo, InputRequired

def non_empty(field_name):
    def _non_empty(form, field):
        data = field.data or ''
        if field.data is None or not field.data.strip():
            raise ValidationError(f'{field_name} cannot be empty.')
        if len(data) < 2 or len(data) > 20:
            raise ValidationError('{field_name} must be between 2 and 20 characters long.')
    return _non_empty

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                            validators=[non_empty('Username')])
    email = StringField('Email Address',
                         validators=[non_empty('Email address'), Email()])
    password = PasswordField('Password', validators=[non_empty('Password')])
    confirm_password = PasswordField('Confirm Password',
                                      validators=[non_empty('Confirm password'), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
        email = StringField('Email Address',
                            validators=[non_empty('Email address'), Email()])
        password = PasswordField('Password', validators=[non_empty('Password')])
        remember = BooleanField('Remember me')
        submit = SubmitField('Login')
