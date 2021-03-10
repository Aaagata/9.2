import requests
import csv

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
rates = data[0].get('rates')
# print(rates) to jest lista, ktorej elementami sa slowniki

for r in rates:
    print(r) #wylistowala slowniki

for key, value in r.items():
    print(r.get(key)) #OK dla ostatniej waluty, chociaz nie wiem czemu key a nie value

fields = ['Currency', 'Code', 'Bid', 'Ask']
rows = r


filename = "currency.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=';')
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
