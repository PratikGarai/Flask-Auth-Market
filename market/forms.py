from market.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError


class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user : 
            raise ValidationError('Username already exists!')
        
    def validate_email(self, email_to_check):
        user = User.query.filter_by(email=email_to_check.data).first()
        if user : 
            raise ValidationError('Email already in use!')

    username = StringField(label='Username', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email Address', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Enter Password', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')



class LoginForm(FlaskForm):

    username = StringField(label='Username', validators=[Length(min=2, max=30), DataRequired()])
    password = PasswordField(label='Enter Password', validators=[Length(min=6), DataRequired()])
    submit = SubmitField(label='Login')