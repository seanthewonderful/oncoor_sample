from flask import Flask
from flask_wtf.csrf import CSRFProtect
from jinja2 import StrictUndefined
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]=False
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///oncoorDB.db'
# app.config["SQLALCHEMY_DATABASE_URI"] = ''
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secretsecrets"
csrf = CSRFProtect(app)

from src import views, models