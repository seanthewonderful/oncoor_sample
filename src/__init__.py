from flask import Flask
from os import environ
from jinja2 import StrictUndefined

app = Flask(__name__)

# app.secret_key = environ["SECRET_KEY"]
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = environ["POSTGRES_URI"]
# app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

app.jinja_env.undefined = StrictUndefined

from src import models
models.connect_to_db(app)
from src import views, forms


if __name__ == "__main__":
    app.run()