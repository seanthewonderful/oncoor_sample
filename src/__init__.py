from os import environ
from flask import Flask, render_template, redirect, url_for
# from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]=False

@app.route("/")
def home():
    return render_template('index.html')



if __name__ == "__main__":
    app.jinja_env.auto_reload = app.debug
    # DebugToolbarExtension(app)
    # connect_to_db(app)
    app.run(debug=True)