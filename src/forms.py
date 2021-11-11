from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(), 
        Length(min=2, max=20)
    ])
    email = StringField('Email', validators=[
        DataRequired()
    ])
    submit = SubmitField('Sign Up')