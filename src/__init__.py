
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from flask_wtf.csrf import CSRFProtect
import smtplib
from decouple import config
from model import player_data, items


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]=False
# app.secret_key = environ["SECRET_KEY"]
# app.secret_key = config('SECRET_KEY', default='')
app.secret_key = "secret"
csrf = CSRFProtect(app)
# app.add_url_rule("/player", endpoint="player")

sender_email = "bigbirthdaybuddyboy@gmail.com"
receiver_email = "briandfagan@gmail.com"
gmail_app_pw = ""

@app.route("/")
def home():
    return render_template('home.html', players=player_data,
                                        items=items)

@app.route("/contact_us", methods=["GET", "POST"])
def contact_us():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(message)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            print("Got here")
            connection.starttls()
            print("start tls")
            connection.login(sender_email, "fdadisgioynmjxig")
            print("connected")
            mssg = f'''Subject: Contact Us submission from oncoor.com\n\nYou received a message from the 'Contact Us' form on oncoor.com from {name}:\n{message}\nTo reply, send a message to {name}'s email address: {email}'''
            connection.sendmail(from_addr=sender_email,
                                to_addrs=receiver_email,
                                msg=mssg)
        flash("Your message has been sent! We will reach back out to you at the email address you provided.", category='info')
        return redirect(url_for('home')+"#staples")
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
    return render_template('shop.html', items=items)

if __name__ == "__main__":
    app.jinja_env.auto_reload = app.debug
    DebugToolbarExtension(app)
    app.run(debug=True)