import requests
import csv
# import json

# with open('m9\NBP.NBP.json') as json_file:
#     data = json.load(json_file)

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
rates = data[0].get('rates')
# print(rates) to jest lista, ktorej elementami sa slowniki

# for r in rates:
#     print(r) #wylistowala slowniki
# for r in rates:
#     for key, value in r.items():
        # print(r.get(key)) #OK dla ostatniej waluty, chociaz nie wiem czemu key a nie value
        #alternatywa dla print(value)
fields = ['Currency', 'Code', 'Bid', 'Ask']
rows = [v.values() for v in rates]

filename = "currency.csv"
with open(filename, 'w' , encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=';')
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)
