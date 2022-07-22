
from dataclasses import dataclass
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_debugtoolbar import DebugToolbarExtension
import flask_sqlalchemy
from jinja2 import StrictUndefined
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
import smtplib
# from decouple import config
import csv
import random
import pandas


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]=False
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///oncoorDB.db'
# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///oncoorDB.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secretsecrets"

# db = SQLAlchemy(app)
# db.init_app(app)

from src.models import Player, ShopItem, db
from src.forms import AddShopItem, AddPlayer

csrf = CSRFProtect(app)
# app.add_url_rule("/player", endpoint="player")

sender_email = "bigbirthdaybuddyboy@gmail.com"
receiver_email = "seanthewonderful@gmail.com"
gmail_app_pw = ""

# with open('src/players.csv', 'r') as players:
#     player_data = list(csv.DictReader(players))

# df = pandas.read_csv('src/players.csv')
# i1 = df.shop_item1.to_list()
# i1_price = df.shop_item1_price.to_list()
# i1_img = df.shop_item1_img1.to_list()
# i1_img2 = df.shop_item1_img2.to_list()
# i1_list = list(zip(i1, i1_price, i1_img, i1_img2))
# items = random.sample(i1_list, len(i1_list))

player_data = Player.query.all()
shop_items = ShopItem.query.all()


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

if __name__ == "__main__":
    app.jinja_env.auto_reload = app.debug
    DebugToolbarExtension(app)
    app.run(debug=True)