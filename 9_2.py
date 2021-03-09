import requests
import csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()

fields = ['Currency', 'Code', 'Bid', 'Ask']
rows = data[0]

filename = "currency.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=';')
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
