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