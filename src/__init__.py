from os import environ
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from flask_wtf.csrf import CSRFProtect
from os import environ
import smtplib
from decouple import config


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]=False
# app.secret_key = environ["SECRET_KEY"]
# app.secret_key = config('SECRET_KEY', default='')
app.secret_key = "secret"
csrf = CSRFProtect(app)


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contact_us", methods=["GET", "POST"])
def contact_us():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(message)
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            print("Got here")
            connection.starttls()
            # connection.ehlo()
            print("start tls")
            connection.login("oncoor@yahoo.com", "9Pythons")
            print("connected")
            connection.sendmail(from_addr="oncoor@yahoo.com",
                                to_addrs="seanthewonderful@gmail.com",
                                msg=f'''
                                Subject: Contact Us submission from oncoor.com\n\n
                                You received a message from the 'Contact Us' form on oncoor.com from {name}:
                                \n{message}
                                To reply, send a message to {name}'s email address: {email}
                                ''')
        flash("Your message has been sent! We will reach back out to you at the email address you provided.", category='dark')
        return redirect(url_for('home'))
    return render_template('home.html')

@app.route("/player")
def player():
    return render_template('player.html')
        

if __name__ == "__main__":
    app.jinja_env.auto_reload = app.debug
    DebugToolbarExtension(app)
    # connect_to_db(app)
    app.run(debug=True)