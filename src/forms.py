from ast import Pass
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, IntegerField, SelectField, PasswordField
from wtforms.validators import DataRequired, Email, Optional
from src.models import ShopItem, Player

class ContactUs(FlaskForm):
    email = EmailField('Email', render_kw={'placeholder':'Email Address'}, validators=[Email()])
    name = StringField('Your Name')
    
class AddPlayer(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired()])
    last_name = StringField("Last Name", validators=[DataRequired()])
    school = StringField("School", validators=[DataRequired()])
    sport = StringField("Sport", validators=[DataRequired()])
    position = StringField("Position", validators=[DataRequired()])
    img1_url = StringField("Image URL - Portrait", validators=[DataRequired()])
    img2_url = StringField("Image URL - Banner", validators=[DataRequired()])
    submit = SubmitField("Add Player")
    
choices = [("", "---")]
for player in Player.query.all():
    choices.append((player.id, player.first_name +" "+ player.last_name))
        
item_choices = [("", "---")]
for item in ShopItem.query.all():
    item_choices.append((item.id, item.name))
    
class AddShopItem(FlaskForm):
    name = StringField("Item Name", validators=[DataRequired()])
    price = IntegerField("Price", validators=[DataRequired()])
    img1_url = StringField("Image URL", validators=[DataRequired()])
    img2_url = StringField("Image URL")
    player_connection = SelectField("Player, if connected to item", choices=choices, validators=[Optional()])
    submit = SubmitField("Add Item")

class DeletePlayer(FlaskForm):
    players = SelectField("Beware: Submitting this form will permanently delete the selected player from the database!",
                              choices=[], validators=[DataRequired()])
    submit = SubmitField("Delete Player")
        
class DeleteShopItem(FlaskForm):
    items = SelectField("Beware: Submitting this form will permanently delete the selected item from the database!",
                            choices=[], validators=[DataRequired()])
    submit = SubmitField("Delete Item")
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Firstname Lastname', render_kw={'placeholder':'Use format: Firstname Lastname'}, validators=[DataRequired()])
    password_hash = PasswordField('Password', render_kw={'placeholder':'No rules for password'}, validators=[DataRequired()])
    title = StringField('Title', render_kw={'placeholder':'Your job title'}, validators=[DataRequired()])
    clearance = SelectField('Clearance Level', choices=[('top_secret', 'Top Secret'), ('blue', 'Blue'), ('yellow', 'Yellow'), ('medium_secret', 'Medium Secret'), ('red', 'Red'), ('gold', 'Gold'), ('midnight', 'Midnight')])
    submit = SubmitField('Create Administrator')
    
class LoginForm(FlaskForm):
    username = StringField('Username (Firstname Lastname)', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')