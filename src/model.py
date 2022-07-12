import pandas
import csv
import random

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


with open('src/players.csv', 'r') as players:
    player_data = list(csv.DictReader(players))
    
# b = player_data['name' == 'Bella Wright']['shop_item1']
# print(player_data.name)

# name = "Calvin Knapp"
# for player in player_data:
#     if player['name'] == name:
#         print(player)
# print(player)