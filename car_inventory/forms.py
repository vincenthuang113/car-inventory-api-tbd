from xml.dom import ValidationErr
from click import confirm
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo

class UserLoginForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired()])
    last_name = StringField('Last Name', validators=[InputRequired()])
    email = StringField('Email', validators = [InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired(), EqualTo('confirm', message = 'Make sure your passwords match.')])
    confirm = PasswordField('Re-enter')
    submit_button = SubmitField()

    def validate_first_name(form, field):
        if len(field.data) > 50:
            raise ValidationErr('Name must be under 50 characters')
    def validate_last_name(form, field):
        if len(field.data) > 50:
            raise ValidationErr('Name must be under 50 characters')