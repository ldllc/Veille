import requests
import csv
import os

url = "https://raw.githubusercontent.com/Casualtek/Cyberwatch/main/cyberattacks.json"
chemin_csv = "../../CSV/Stats/Victimes/Victimes_Globales.csv"

def recuperer_infos_json(url):
    try:
        reponse = requests.get(url)
        reponse.raise_for_status()
        data_json = reponse.json()
        return data_json

    except requests.exceptions.RequestException as erreur:
        print(f"Une erreur s'est produite lors de la récupération des données JSON : {erreur}")
        return None

def enregistrer_csv(data, chemin_csv):
    try:
        os.makedirs(os.path.dirname(chemin_csv), exist_ok=True)

        with open(chemin_csv, mode='w', newline='', encoding='utf-8') as fichier_csv:
            writer = csv.writer(fichier_csv, delimiter='|')

            writer.writerow(['Date', 'Victime', 'Domaine', 'Pays', 'Résumé', 'Titre', 'URL'])

            for ligne in data:
                writer.writerow([
                    ligne['date'],
                    ligne['victim'],
                    ligne['domain'],
                    ligne['country'],
                    ligne['summary'].replace('\n', ' '),
                    ligne['title'],
                    ligne['url']
                ])

    except IOError as erreur:
        print(f"Une erreur s'est produite lors de l'enregistrement du fichier CSV : {erreur}")

def main():
    data_json = recuperer_infos_json(url)

    if data_json:
        enregistrer_csv(data_json, chemin_csv)

if __name__ == "__main__":
    main()