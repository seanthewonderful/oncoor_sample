from flask import Flask
from os import environ
from jinja2 import StrictUndefined

app = Flask(__name__)

from src import DevelopmentConfig
# app.secret_key = environ["SECRET_KEY"]
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["SQLALCHEMY_DATABASE_URI"] = environ["SQLALCHEMY_DATABASE_URI"]
# app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

# env_config = environ.get("APP_SETTINGS")
app.config.from_object(DevelopmentConfig())
app.jinja_env.undefined = StrictUndefined

from src import models
models.connect_to_db(app)
from src import views, forms


if __name__ == "__main__":
    app.run()