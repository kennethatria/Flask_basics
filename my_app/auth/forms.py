# app/auth/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, SelectField
from wtforms.validators import DataRequired, Email, EqualTo
from my_app.auth.models import User


class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    email = StringField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('confirm_password')])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email is already in use.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is already in use.')


class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class EditForm(FlaskForm):
    """
    Form to edit user
    """
    company = StringField('Company')
    email = StringField('Email', validators=[DataRequired(), Email()])
    old_password = PasswordField('Old Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired(),EqualTo('confirm_password')])
    confirm_new_password = PasswordField('Confirm New Password', validators = [DataRequired(), EqualTo('new_password')])
    role = SelectField('Role', choices=[('Client','Client'),('Admin','Admin')],validators=[DataRequired()])
    submit = SubmitField('Edit')