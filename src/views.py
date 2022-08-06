import smtplib
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from os import environ
import random
from src import app
from src.forms import AddPlayer, AddShopItem, DeletePlayer, DeleteShopItem, RegisterForm, LoginForm
from src.models import db, Player, ShopItem, Admin, get_player
from flask_wtf.csrf import CSRFProtect


sender_email = "bigbirthdaybuddyboy@gmail.com"
receiver_email = "seanthewonderful@gmail.com"
gmail_app_pw = environ["GMAIL_PW"]
login_manager = LoginManager()
login_manager.init_app(app)
csrf = CSRFProtect(app)


@app.route("/")
def home():
    return render_template('home.html', players=Player.query.all(),
                                        items=random.sample(ShopItem.query.all(), k=4))


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
    def get_player(id):
        return Player.query.get(id)
    return render_template('shop.html', 
                           items=ShopItem.query.all(),
                           get_player=get_player)


@app.endpoint("shop_item")
@app.route("/shop_item/<name>", methods=["GET", "POST"])
def shop_item(name):
    item = ShopItem.query.filter_by(name=name).first()
    return render_template('shop_item.html', 
                           item=item,
                           get_player=get_player)


""" Administrator Routes """

@app.endpoint("admin")
@app.route("/admin", methods=["GET", "POST"])
@login_required
def admin():
    if current_user.is_authenticated:
        choices = [("", "---")]
        for player in Player.query.all():
            choices.append((player.id, player.first_name +" "+ player.last_name))
        item_choices = [("", "---")]
        for item in ShopItem.query.all():
            item_choices.append((item.id, item.name))
        add_player_form = AddPlayer()
        add_shop_form = AddShopItem()
        add_shop_form.player_connection.choices = choices
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
                            shop_items=ShopItem.query.all(),
                            get_player=get_player)
    return redirect(url_for('admin_login'))
    

@app.endpoint('admin_register')
@app.route("/admin_register", methods=["GET", "POST"])
@login_required
def admin_register():
    form = RegisterForm()
    if form.validate_on_submit():
        if Admin.query.filter_by(username=form.username.data).first():
            flash("Name already in use. Please try Firstname Lastname1", category="warning")
            return redirect(url_for('admin_register'))
        else:
            new_admin = Admin(
                username = form.username.data,
                title = form.title.data,
                clearance = form.clearance.data,
                password_hash = generate_password_hash((form.password_hash.data), method='pbkdf2:sha256', salt_length=8)
            )
            db.session.add(new_admin)
            db.session.commit()
            flash("Success", category="success")
            db.session.close()
            return redirect(url_for('admin_register'))
    return render_template('admin_register.html',
                           register_form=form,
                           admins = Admin.query.all())


@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    form = LoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(username=(form.username.data)).first()
        if admin:
            password = form.password.data
            if check_password_hash(admin.password_hash, password):
                login_user(admin)
                return redirect(url_for('admin'))
            else:
                flash("Incorrect password", category="danger")
                return redirect(url_for('admin_login'))
        else:
            flash("Username does not exist", category="danger")
            return redirect(url_for('admin_login'))
    return render_template('admin_login.html', login_form=form)


@app.route("/admin_logout")
def admin_logout():
    logout_user()
    flash("Logged out", category="primary")
    return redirect(url_for('admin_login'))


""" Player Edits """

@app.route("/add_player", methods=["GET", "POST"])
@login_required
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


@app.endpoint("edit_player")
@app.route("/edit_player", methods=["GET", "POST"])
@login_required
def edit_player():
    if request.method == "POST":
        try:
            print(request.form['player_'])
        except:
            player = Player.query.get(request.form['player_id'])
            player.first_name = request.form['first_name']
            player.last_name = request.form['last_name']
            player.school = request.form['school']
            player.sport = request.form['sport']
            player.position = request.form['position']
            player.img1_url = request.form['img1_url']
            player.img2_url = request.form['img2_url']
            db.session.commit()
            db.session.close()
            flash("Changed made", category="success")
            return redirect(url_for('edit_player'))
        else:
            player = Player.query.get(request.form['player_'])
            db.session.delete(player)
            db.session.commit()
            db.session.close()
            flash("Player deleted", category="danger")
            return redirect(url_for('edit_player'))
    return render_template('edit_player.html', 
                           players=Player.query.all(),
                           add_player_form=AddPlayer())


@app.route("/delete_player", methods=["GET", "POST"])
@login_required
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


""" Shop Item Edits """

@app.route("/add_shop_item", methods=["GET", "POST"])
@login_required
def add_shop_item():
    choices = [("", "---")]
    for player in Player.query.all():
        choices.append((player.id, player.first_name +" "+ player.last_name))
    add_shop_form = AddShopItem()
    add_shop_form.player_connection.choices = choices
    if add_shop_form.validate_on_submit():
        if add_shop_form.player_connection.data == '':
            player_id = None
        else:
            player_id = add_shop_form.player_connection.data
        new_item = ShopItem(
            name = add_shop_form.name.data,
            price = add_shop_form.price.data,
            img1_url = add_shop_form.img1_url.data,
            img2_url = add_shop_form.img2_url.data,
            player_id = player_id
        )
        db.session.add(new_item)
        db.session.commit()
        flash(f"Item added: {new_item.name}", category="success")
        db.session.close()
        return redirect(url_for('admin'))
    return redirect(url_for('admin'))


@app.endpoint("edit_shop_items")
@app.route("/edit_shop_items", methods=["GET", "POST"])
@login_required
def edit_shop_items():
    def get_player(id):
        return Player.query.get(id)
    if request.method == "POST":
        try:
            print(request.form['item_'])
        except:
            item = ShopItem.query.get(request.form['item_id'])
            item.name = request.form['name']
            item.price = request.form['price']
            item.img1_url = request.form['img1_url']
            item.img2_url = request.form['img2_url']
            if request.form['player_connection'] == '':
                player_id = None
            else:
                player_id = request.form['player_connection']
            item.player_id = player_id
            db.session.commit()
            db.session.close()
            flash("Changes made", category="success")
            return redirect(url_for('edit_shop_items'))
        else:
            item = ShopItem.query.get(request.form['item_id'])
            db.session.delete(item)
            db.session.close()
            flash("Item deleted")
            return redirect(url_for('edit_shop_items'))
    return render_template('edit_shop_items.html', 
                           items=ShopItem.query.all(),
                           players=Player.query.all(),
                           get_player=get_player,
                           add_shop_form=AddShopItem())


@app.route("/delete_shop_item", methods=["GET", "POST"])
@login_required
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


""" Flask Login Manager """

@login_manager.user_loader
def load_user(admin_id):
    return Admin.query.get(int(admin_id))

@login_manager.unauthorized_handler
def unauthorized():
    return "Sorry, you must be logged in to see this page."
