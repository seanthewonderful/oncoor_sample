import pandas
import csv

file = 'src/players.csv'


l = []

with open(file, 'r') as d:
    data = csv.DictReader(d)
    for row in data:
        l.extend([row['name'], row['school'], row['sport']])
        
    
print(l)     
        
        