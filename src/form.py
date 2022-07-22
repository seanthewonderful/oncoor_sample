from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, EmailField, IntegerField
from wtforms.validators import DataRequired, Email

class ContactUs(FlaskForm):
    email = EmailField('Email', render_kw={'placeholder':'Email Address'}, validators=[Email()])
    name = StringField('Your Name')
    
    
class AddPlayer(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    school = StringField("School", validators=[DataRequired()])
    Sport = StringField("Sport", validators=[DataRequired()])
    Position = StringField("Position", validators=[DataRequired()])
    img1_url = StringField("Image URL", validators=[DataRequired()])
    img2_url = StringField("Image URL", validators=[DataRequired()])
    submit = SubmitField("Submit")
    

class AddShopItem(FlaskForm):
    name = StringField("Item Name", validators=[DataRequired()])
    price = IntegerField("Price", validators=[DataRequired()])
    img1_url = StringField("Image URL", validators=[DataRequired()])
    img2_url = StringField("Image URL")
    player_lastname = StringField("Player's last name, if connected to item")
    submit = SubmitField("Submit")
    