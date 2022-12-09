
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import UserMixin
# import sys
# sys.path.insert(0, '../src')
# from src import app
from os import environ

# app.config["SQLALCHEMY_DATABASE_URI"] = environ["POSTGRES_URI"]
# SQLALCHEMY_DATABASE_URI = config("POSTGRES_URI")
db = SQLAlchemy()

class Admin(UserMixin, db.Model):
    __tablename__ = 'admin'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60))
    title = db.Column(db.String(60))
    clearance = db.Column(db.String(40))
    password_hash = db.Column(db.String(200))
    
    def __repr__(self):
        return f"Admin: {self.username}, {self.title}\nClearance Lvl: {self.clearance}"

class Player(db.Model):
    __tablename__ = 'player'
    
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
    __tablename__ = 'shop_item'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    price = db.Column(db.Integer)
    img1_url = db.Column(db.String(1000), nullable=True)
    img2_url = db.Column(db.String(1000), nullable=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=True)
    
    def __repr__(self):
        return f"Shop item {self.name}, player_id={self.player_id}"


def get_player(id):
    return Player.query.get(id)

def get_admin(admin_id):
    return Admin.query.get(admin_id)

def connect_to_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = environ["POSTGRES_URI"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = environ["SECRET_KEY"]
    db.app = app
    db.init_app(app)
      
if __name__ == "__main__":
    from src import app
    connect_to_db(app)
    print("Connected to DB.")
