import pandas
import csv
import random
from flask_sqlalchemy import SQLAlchemy
from src.main import app


db = SQLAlchemy(app)

df = pandas.read_csv('src/players.csv')
players_df = pandas.read_csv('src/players.csv', usecols=["name", "school", "sport", "img1", "img2"])


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


def seed_db():
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
    img1_url = db.Column(db.String(1000))
    img2_url = db.Column(db.String(1000))
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=True)
    
    def __repr__(self):
        return f"Shop item {self.name}, player_id={self.player_id}"
    
    

# if __name__ == "__main__":
#     app.jinja_env.auto_reload = app.debug
#     app.run(debug=True)