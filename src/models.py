from flask import Flask, render_template, redirect, url_for, request, flash
from jinja2 import StrictUndefined
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
import csv
from os import environ


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]=False
# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///oncoorDB.db'
app.config["SQLALCHEMY_DATABASE_URI"] = environ["POSTGRES_URI"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "secretsecrets"
db = SQLAlchemy(app)
csrf = CSRFProtect(app)




class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    school = db.Column(db.String(80))
    sport = db.Column(db.String(40))
    position = db.Column(db.String(50), nullable=True)
    img1_url = db.Column(db.String(500))
    img2_url = db.Column(db.String(500))
    shop_items = db.relationship('ShopItem', backref='player')
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name}, {self.position} at {self.school}"
    
class ShopItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    price = db.Column(db.Integer)
    img1_url = db.Column(db.String(1000), nullable=True)
    img2_url = db.Column(db.String(1000), nullable=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=True)
    
    def __repr__(self):
        return f"Shop item {self.name}, player_id={self.player_id}"
    

player_data = Player.query.all()
shop_items = ShopItem.query.all()

def seed_players():
    with open('src/players.csv', 'r') as d:
        player_data = csv.DictReader(d)
        for each in player_data:
            new_player = Player(
                first_name = each['name'].split()[0],
                last_name = each['name'].split()[1],
                school = each['school'],
                sport = each['sport'],
                img1_url = each['img1'],
                img2_url = each['img2']
            )
            db.session.add(new_player)
            db.session.commit()
        
def seed_shop():
    with open('src/players.csv', 'r') as d:
        player_data = csv.DictReader(d)
        for each in player_data:
            new_item = ShopItem(
                name = each['shop_item1'],
                price = each['shop_item1_price'],
                img1_url = each['shop_item1_img1'],
                img2_url = each['shop_item1_img2'],
                player_id = Player.query.filter_by(last_name=each['name'].split()[1]).first().id
            )
            db.session.add(new_item)
            db.session.commit()
            
      
def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = environ["POSTGRES_URI"]
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
      
if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    connect_to_db(app)
    print("Connected to DB.")