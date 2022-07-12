import pandas
import csv

df = pandas.read_csv('src/players.csv')

# print(df['name'].to_list())
# print(df.name)
# print(df[df['name'] == 'Bella Wright'])

# player_data = []
# names = df.name
# print(names)
# for ea in names:
    

# print(df._data)

with open('src/players.csv', 'r') as players:
    player_data = list(csv.DictReader(players))
    
# b = player_data['name' == 'Bella Wright']['shop_item1']
# print(player_data.name)
player = player_data['name' == 'Calvin Knapp']
name = "Calvin Knapp"
for player in player_data:
    if player['name'] == name:
        print(player)
# print(player)