from flask import Flask
from os import environ
from jinja2 import StrictUndefined

app = Flask(__name__)

app.secret_key = environ["SECRET_KEY"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = environ["SQLALCHEMY_DATABASE_URI"]
app.jinja_env.undefined = StrictUndefined
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

    
from src import models
from src import views, forms
models.connect_to_db(app)


if __name__ == "__main__":
    app.run()