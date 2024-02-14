import requests
import csv
import json

url = "https://raw.githubusercontent.com/Casualtek/Cyberwatch/main/cyberattacks.json"

response = requests.get(url)
data = response.json()

csv_path = "../../CSV/Stats/Victimes_Retail/Victimes_Retail.csv"

# Liste des mots clés associés aux magasins, points de vente, commerce, etc.
keywords = ['magasin', 'point de vente', 'boutique', 'marchand', 'hypermarché', 'supermarché', 'retail', 'commerçant']

# Filtrer les données en fonction des mots clés
filtered_data = [entry for entry in data if any(keyword in entry['title'].lower() or keyword in entry['summary'].lower() for keyword in keywords)]

sorted_data = sorted(filtered_data, key=lambda x: x['date'], reverse=True)

with open(csv_path, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file, delimiter='|')

    writer.writerow(['ID', 'Victim', 'Domain', 'Date', 'Country', 'Title', 'Summary', 'URL'])

    for idx, entry in enumerate(sorted_data, start=1):
        writer.writerow([
            idx,
            entry['victim'],
            entry['domain'],
            entry['date'],
            entry['country'],
            entry['title'],
            entry['summary'],
            entry['url']
        ])
