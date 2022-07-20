import pandas
import csv
import random
from flask_sqlalchemy import SQLAlchemy


df = pandas.read_csv('src/players.csv')

# print(df['name'].to_list())
# print(df.name)
names = df.shop_item1
# print(names[1])
# print(df[df['name'] == 'Bella Wright'])

i1 = df.shop_item1.to_list()
i1_price = df.shop_item1_price.to_list()
i1_img = df.shop_item1_img1.to_list()
i1_img2 = df.shop_item1_img2.to_list()
# i2 = df.shop_item2.to_list()
# i2_price = df.shop_item2_price.to_list()
# i2_img = df.shop_item2_img1.to_list()

i1_list = list(zip(i1, i1_price, i1_img, i1_img2))
# print(random.sample(i1_list, len(i1_list)))
# print(i1_list[0][0])

items = random.sample(i1_list, len(i1_list))


with open('src/players.csv', 'r') as players:
    player_data = list(csv.DictReader(players))
    
# b = player_data['name' == 'Bella Wright']['shop_item1']
# print(player_data.name)

# name = "Calvin Knapp"
# for player in player_data:
#     if player['name'] == name:
#         print(player)
# print(player)


db = SQLAlchemy()

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    school = db.Column(db.String(80))
    sport = db.Column(db.String(40))
    position = db.Column(db.String(50), nullable=True)
    img1_url = db.Column(db.String(500))
    img2_url = db.Column(db.String(500))
    shop_items = db.relationship('Shop Item', backref='player', lazy='dynamic')
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name}, {self.position} at {self.school}"
    
class ShopItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    price = db.Column(db.Numeric(precision=6, scale=2))
    img1_url = db.Column(db.String(1000))
    img2_url = db.Column(db.String(1000))
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=True)
    
    def __repr__(self):
        return f"Shop item {self.name}, player_id={self.player_id}"
    
    
sean = Player(first_name='Sean',
              last_name='Fagan',
              school='BYU',
              sport='Baseball',
              position='Catcher',
              img1_url='#',
              img2_url='#',
              )
bat = ShopItem(name='Seans Bat',
               price=29.00,
               img1_url='#',
               img2_url='#',
               player='sean'
               )