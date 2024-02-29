import requests
import csv
from datetime import datetime

url = "https://data.ransomware.live/posts.json"
output_csv_path = "../../CSV/Attaques/Donnees_Attaques/Ransomwarelive.csv"
current_year = 2022
response = requests.get(url)
data = response.json()

filtered_data = [item for item in data if int(item['published'][:4]) >= current_year]

with open(output_csv_path, 'a', newline='', encoding='utf-8') as csv_file:  # Utilisation de 'a' au lieu de 'w'
    fieldnames = ["post_title", "group_name", "discovered", "description", "website", "published", "post_url", "country"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='|')
    
    # Écrire uniquement l'en-tête si le fichier est vide
    if csv_file.tell() == 0:
        writer.writeheader()
    
    for item in filtered_data:
        writer.writerow(item)

json_url = "https://raw.githubusercontent.com/nuke86/ransomFeed/main/posts.json"
csv_path = "../../CSV/Attaques/Donnees_Attaques/Ransomfeedit.csv"

def convert_to_csv(data):
    headers = ["post_title", "group_name", "discovered"]

    with open(csv_path, 'a', newline='', encoding='utf-8') as csvfile:  # Utilisation de 'a' au lieu de 'w'
        csv_writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter='|')
        
        # Écrire uniquement l'en-tête si le fichier est vide
        if csvfile.tell() == 0:
            csv_writer.writeheader()
        
        for entry in data:
            csv_writer.writerow(entry)

def main():
    try:
        response = requests.get(json_url)
        response.raise_for_status()
        json_data = response.json()

        csv_data = []
        for entry in json_data:
            formatted_entry = {
                "post_title": entry.get("post_title", ""),
                "group_name": entry.get("group_name", ""),
                "discovered": datetime.fromisoformat(entry.get("discovered", "")).strftime('%Y-%m-%d %H:%M:%S')
            }
            csv_data.append(formatted_entry)

        convert_to_csv(csv_data)

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    main()
