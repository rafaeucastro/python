import csv

with open("products.csv") as file: 
    reader = csv.reader(file)
    for row in reader:
        print(row)