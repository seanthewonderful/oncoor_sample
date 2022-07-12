from os import environ
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from flask_wtf.csrf import CSRFProtect
from os import environ
import smtplib
from decouple import config
from model import player_data


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]=False
# app.secret_key = environ["SECRET_KEY"]
# app.secret_key = config('SECRET_KEY', default='')
app.secret_key = "secret"
csrf = CSRFProtect(app)

sender_email = "bigbirthdaybuddyboy@gmail.com"
receiver_email = "seanthewonderful@gmail.com"
gmail_app_pw = ""

@app.route("/")
def home():
    return render_template('home.html', players=player_data)

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

@app.route("/player/<name>")
def player(name):
    player = player_data['name' == name]
    return render_template('player.html', player=player)
        

if __name__ == "__main__":
    app.jinja_env.auto_reload = app.debug
    DebugToolbarExtension(app)
    app.run(debug=True)