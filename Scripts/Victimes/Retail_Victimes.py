import csv
import json

csv_path = "../../CSV/Stats/Victimes/Victimes_Globales.csv"
keywords = ['magasin', 'point de vente', 'boutique', 'marchand', 'hypermarché', 'supermarché', 'retail', 'commerçant']

with open(csv_path, mode='r', newline='', encoding='utf-8') as csv_file:
    reader = csv.DictReader(csv_file, delimiter='|')
    data = list(reader)

filtered_data = [entry for entry in data if any(keyword in entry['Titre'].lower() or keyword in entry['Résumé'].lower() for keyword in keywords)]
sorted_data = sorted(filtered_data, key=lambda x: x['Date'], reverse=True)
output_csv_path = "../../CSV/Stats/Victimes/Victimes_Retail.csv"

with open(output_csv_path, mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file, delimiter='|')
    writer.writerow(['Date', 'Victime', 'Domaine', 'Pays', 'Titre', 'Résumé', 'URL'])

    for idx, entry in enumerate(sorted_data, start=1):
        writer.writerow([
            idx,
            entry['Victime'],
            entry['Domaine'],
            entry['Date'],
            entry['Pays'],
            entry['Titre'],
            entry['Résumé'],
            entry['URL']
        ])