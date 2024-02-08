import requests
import csv
import json

url = "https://raw.githubusercontent.com/Casualtek/Cyberwatch/main/cyberattacks.json"

response = requests.get(url)
data = response.json()

csv_path = "../../CSV/Victimes/Ransomwarelive.csv"

sorted_data = sorted(data, key=lambda x: x['date'], reverse=True)

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