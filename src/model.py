import pandas
import csv
import random
from __init__ import db, app

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

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40), index=True, unique=False)
    last_name = db.Column(db.String(40), index=True, unique=False)
    school = db.Column(db.String(80), index=True, unique=False)
    sport = db.Column(db.String(40), index=True, unique=False)
    position = db.Column(db.String(50))
    img1_url = db.Column(db.String(500))
    img2_url = db.Column(db.String(500))
    shop_items = db.relationship('Shop Item', backref='player', lazy='dynamic')
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name}, {self.position} at {self.school}"
    
class ShopItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140), index=True, unique=True)
    price = db.Column(db.Numeric(precision=6, scale=2))
    img1_url = db.Column(db.String(1000))
    img2_url = db.Column(db.String(1000))
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    