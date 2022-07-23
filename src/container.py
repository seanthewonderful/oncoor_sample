from flask import Flask, render_template, redirect, url_for, request, flash
from flask_wtf.csrf import CSRFProtect
from jinja2 import StrictUndefined
# from flask_debugtoolbar import DebugToolbarExtension
import smtplib
from .extensions import db


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]=False
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///oncoorDB.db'
# app.config["SQLALCHEMY_DATABASE_URI"] = ''
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secretsecrets"
# db = SQLAlchemy(app)
csrf = CSRFProtect(app)

from .models import Player, ShopItem, player_data, shop_items
from .forms import AddPlayer, AddShopItem

sender_email = "bigbirthdaybuddyboy@gmail.com"
receiver_email = "seanthewonderful@gmail.com"
gmail_app_pw = ""


@app.route("/")
def home():
    return render_template('home.html', players=player_data,
                                        items=shop_items)

@app.route("/contact_us", methods=["GET", "POST"])
def contact_us():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(sender_email, "fdadisgioynmjxig")
            mssg = f'''Subject: Contact Us submission from oncoor.com\n\nYou received a message from the 'Contact Us' form on oncoor.com from {name}:\n{message}\nTo reply, send a message to {name}'s email address: {email}'''
            connection.sendmail(from_addr=sender_email,
                                to_addrs=receiver_email,
                                msg=mssg)
        flash("Your message has been sent! We will reach back out to you at the email address you provided.", category='info')
        # return redirect(url_for('home')+"#staples")
        return redirect(request.referrer)
    return render_template('home.html')

@app.endpoint("player")
@app.route("/player/<name>")
def player(name):
    def find_player(name):
        for player in player_data:
            if player['name'] == name:
                return player
    player = find_player(name)
    return render_template('player.html', player=player)

@app.endpoint("shop")
@app.route("/shop")
def shop():
    return render_template('shop.html', items=shop_items)


if __name__ == "__main__":
    app.run()





from .extensions import db


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    school = db.Column(db.String(80))
    sport = db.Column(db.String(40))
    position = db.Column(db.String(50), nullable=True)
    img1_url = db.Column(db.String(500))
    img2_url = db.Column(db.String(500))
    shop_items = db.relationship('ShopItem', backref='player')
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name}, {self.position} at {self.school}"
    
class ShopItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    price = db.Column(db.Integer)
    img1_url = db.Column(db.String(1000))
    img2_url = db.Column(db.String(1000))
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=True)
    
    def __repr__(self):
        return f"Shop item {self.name}, player_id={self.player_id}"
    

player_data = Player.query.all()
shop_items = ShopItem.query.all()

# def seed_db():
#     for each in player_data:
#         new_player = Player(
#             first_name = each['name'].split()[0],
#             last_name = each['name'].split()[1],
#             school = each['school'],
#             sport = each['sport'],
#             img1_url = each['img1'],
#             img2_url = each['img2']
#         )
#         db.session.add(new_player)
#         db.session.commit()
        
# def seed_shop():
#     for each in player_data:
#         new_item = ShopItem(
#             name = each['shop_item1'],
#             price = each['shop_item1_price'],
#             img1_url = each['shop_item1_img1'],
#             img2_url = each['shop_item1_img2'],
#             player_id = Player.query.filter_by(last_name=each['name'].split()[1]).first().id
#         )
#         db.session.add(new_item)
#         db.session.commit()




from src import app
from flask import Flask, render_template, redirect, url_for, request, flash
import smtplib
from models import Player, ShopItem, db, player_data, shop_items
from forms import AddPlayer, AddShopItem


sender_email = "bigbirthdaybuddyboy@gmail.com"
receiver_email = "seanthewonderful@gmail.com"
gmail_app_pw = ""




def add_player():
    form = AddPlayer()
    if form.validate_on_submit():
        new_player = Player(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            school = form.schoo.data,
            sport = form.sport.data,
            position = form.position.data,
            img1_url = form.img1_url.data,
            img2_url = form.img2_url.data            
        )
        db.session.add(new_player)
        db.session.commit()
        flash("Player added", category="success")
    
def add_shop_item():
    form = AddShopItem()
    if form.validate_on_submit():
        new_item = ShopItem(
            name = form.name.data,
            price = form.price.data,
            img1_url = form.img1_url.data,
            img2_url = form.img2_url.data,
            player_id = (Player.query.filter_by(last_name=form.player_lastname.data).first()).id
        )
        db.session.add(new_item)
        db.session.commit()
        flash("Item added", category="success")


@app.route("/")
def home():
    return render_template('home.html', players=player_data,
                                        items=shop_items)

@app.route("/contact_us", methods=["GET", "POST"])
def contact_us():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(sender_email, "fdadisgioynmjxig")
            mssg = f'''Subject: Contact Us submission from oncoor.com\n\nYou received a message from the 'Contact Us' form on oncoor.com from {name}:\n{message}\nTo reply, send a message to {name}'s email address: {email}'''
            connection.sendmail(from_addr=sender_email,
                                to_addrs=receiver_email,
                                msg=mssg)
        flash("Your message has been sent! We will reach back out to you at the email address you provided.", category='info')
        # return redirect(url_for('home')+"#staples")
        return redirect(request.referrer)
    return render_template('home.html')

@app.endpoint("player")
@app.route("/player/<name>")
def player(name):
    def find_player(name):
        for player in player_data:
            if player['name'] == name:
                return player
    player = find_player(name)
    return render_template('player.html', player=player)

@app.endpoint("shop")
@app.route("/shop")
def shop():
    return render_template('shop.html', items=shop_items)