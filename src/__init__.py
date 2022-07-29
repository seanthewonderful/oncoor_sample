from ast import Delete
from re import L
import smtplib
from flask import Flask, render_template, redirect, url_for, request, flash
from jinja2 import StrictUndefined
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from os import environ
from src.forms import AddPlayer, AddShopItem, DeletePlayer, DeleteShopItem
from src.models import connect_to_db, app, Player, ShopItem, db


sender_email = "bigbirthdaybuddyboy@gmail.com"
receiver_email = "seanthewonderful@gmail.com"
gmail_app_pw = environ["GMAIL_PW"]

@app.route("/")
def home():
    return render_template('home.html', players=Player.query.all(),
                                        items=ShopItem.query.all())

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
@app.route("/player/<first_name>/<last_name>")
def player(first_name, last_name):
    player = Player.query.filter(Player.first_name.like(first_name), Player.last_name.like(last_name)).first()
    return render_template('player.html', player=player)

@app.endpoint("shop")
@app.route("/shop")
def shop():
    return render_template('shop.html', items=ShopItem.query.all())
        
@app.endpoint("admin")
@app.route("/admin", methods=["GET", "POST"])
def admin():
    choices = [("", "---")]
    for player in Player.query.all():
        choices.append((player.id, player.first_name +" "+ player.last_name))
    item_choices = [("", "---")]
    for item in ShopItem.query.all():
        item_choices.append((item.id, item.name))
    add_player_form = AddPlayer()
    add_shop_form = AddShopItem()
    add_shop_form.player_lastname.choices = choices
    delete_player_form = DeletePlayer()
    delete_player_form.players.choices = choices
    delete_shop_item_form = DeleteShopItem()
    delete_shop_item_form.items.choices = item_choices
    return render_template('admin.html', 
                           add_player_form=add_player_form,
                           add_shop_form=add_shop_form,
                           delete_player_form=delete_player_form,
                           delete_shop_item_form=delete_shop_item_form,
                           players=Player.query.all(),
                           shop_items=ShopItem.query.all())


@app.route("/add_player", methods=["GET", "POST"])
def add_player():
    add_player_form = AddPlayer()
    if add_player_form.validate_on_submit():
        new_player = Player(
            first_name = add_player_form.first_name.data,
            last_name = add_player_form.last_name.data,
            school = add_player_form.school.data,
            sport = add_player_form.sport.data,
            position = add_player_form.position.data,
            img1_url = add_player_form.img1_url.data,
            img2_url = add_player_form.img2_url.data            
        )
        db.session.add(new_player)
        db.session.commit()
        flash(f"Player {new_player.first_name} {new_player.last_name} added", category="success")
        db.session.close()
        return redirect(url_for('admin'))
    return redirect(url_for('admin'))

    
@app.route("/add_shop_item", methods=["GET", "POST"])
def add_shop_item():
    add_shop_item_form = AddShopItem()
    if add_shop_item_form.validate_on_submit():
        new_item = ShopItem(
            name = add_shop_item_form.name.data,
            price = add_shop_item_form.price.data,
            img1_url = add_shop_item_form.img1_url.data,
            img2_url = add_shop_item_form.img2_url.data,
            player_id = (Player.query.filter_by(last_name=add_shop_item_form.player_lastname.data).first()).id
        )
        db.session.add(new_item)
        db.session.commit()
        flash(f"Item added: {new_item.name}", category="success")
        db.session.close()
        return redirect(url_for('admin'))
    return redirect(url_for('admin'))

@app.route("/delete_player", methods=["GET", "POST"])
def delete_player():
    choices = [("", "---")]
    for player in Player.query.all():
        choices.append((player.id, player.first_name +" "+ player.last_name))
    delete_player_form = DeletePlayer()
    delete_player_form.players.choices = choices
    if delete_player_form.validate_on_submit():
        player = Player.query.get(delete_player_form.players.data)
        db.session.delete(player)
        db.session.commit()
        flash(f"Player {player.first_name} {player.last_name} deleted", category="danger")
        db.session.close()
        return redirect(url_for('admin'))
    return redirect(url_for('admin'))
        
        

@app.route("/delete_shop_item", methods=["GET", "POST"])
def delete_shop_item():
    item_choices = [("", "---")]
    for item in ShopItem.query.all():
        item_choices.append((item.id, item.name))
    delete_shop_item_form = DeleteShopItem()
    delete_shop_item_form.items.choices = item_choices
    if delete_shop_item_form.validate_on_submit():
        item = ShopItem.query.get(delete_shop_item_form.items.data)
        db.session.delete(item)
        db.session.commit()
        flash(f"Item deleted from shop: {item.name}", category="danger")
        db.session.close()
        return redirect(url_for('admin'))
    return redirect(url_for('admin'))
    
if __name__ == "__main__":
    connect_to_db(app)
    app.run()
    
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
