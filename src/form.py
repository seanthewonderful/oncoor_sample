from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, EmailField
from wtforms.validators import DataRequired, Email

class ContactUs(FlaskForm):
    email = EmailField('Email', render_kw={'placeholder':'Email Address'}, validators=[Email()])
    name = StringField('Your Name')