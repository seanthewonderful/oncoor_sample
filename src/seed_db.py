import csv
import os
import models
from src import app


os.system("dropdb oncoor_db")
os.system("createdb oncoor_db")

models.connect_to_db(app)
models.db.create_all()

def seed_players():
    with open('src/players.csv', 'r') as d:
        player_data = csv.DictReader(d)
        for each in player_data:
            new_player = models.Player(
                first_name = each['name'].split()[0],
                last_name = each['name'].split()[1],
                school = each['school'],
                sport = each['sport'],
                img1_url = each['img1'],
                img2_url = each['img2']
            )
            models.db.session.add(new_player)
            models.db.session.commit()
        
def seed_shop():
    with open('src/players.csv', 'r') as d:
        player_data = csv.DictReader(d)
        for each in player_data:
            new_item = models.ShopItem(
                name = each['shop_item1'],
                price = each['shop_item1_price'],
                img1_url = each['shop_item1_img1'],
                img2_url = each['shop_item1_img2'],
                player_id = models.Player.query.filter_by(last_name=each['name'].split()[1]).first().id
            )
            models.db.session.add(new_item)
            models.db.session.commit()