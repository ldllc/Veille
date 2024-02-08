import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import json
from urllib.request import urlopen

url1 = "https://attack.mitre.org/groups/"
response1 = requests.get(url1)

if response1.status_code == 200:
    soup1 = BeautifulSoup(response1.text, 'html.parser')
    table1 = soup1.find('table', {'class': 'table'})

    if table1:
        with open('../../CSV/Groupes/Donnees_Groupes/MitreAttack.csv', 'w', newline='', encoding='utf-8') as csvfile1:
            csvwriter1 = csv.writer(csvfile1, delimiter='|')
            header1 = [th.text.strip() for th in table1.find_all('th')]
            csvwriter1.writerow(header1)
            rows1 = table1.find_all('tr')[1:]
            for row1 in rows1:
                data1 = [td.text.strip() for td in row1.find_all('td')]
                csvwriter1.writerow(data1)
    else:
        print("Tableau non trouvé sur la page.")
else:
    print(f"Échec de la requête. Statut de la requête : {response1.status_code}")

url2 = "https://raw.githubusercontent.com/nuke86/ransomFeed/main/groups.json"
response2 = requests.get(url2)
data2 = response2.json()

output_csv_path2 = "../../CSV/Groupes/Donnees_Groupes/Ransomfeed.csv"
with open(output_csv_path2, 'w', newline='', encoding='utf-8') as csvfile2:
    csv_writer2 = csv.writer(csvfile2, delimiter='|')
    header2 = ['name', 'slug', 'lastscrape', 'profile']
    csv_writer2.writerow(header2)
    for group2 in data2:
        for location2 in group2['locations']:
            row2 = [group2['name'], location2['slug'], location2['lastscrape'], ', '.join(group2['profile'])]
            csv_writer2.writerow(row2)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
url = 'https://www.ransom-db.com/ransomware-groups'
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('div', class_='table-responsive')
    rows = table.find_all('tr')
    with open('../../CSV/Groupes/Donnees_Groupes/Ransomdb.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile, delimiter='|')
        header = [th.text.strip() for th in rows[0].find_all('th')]
        csv_writer.writerow(header)
        for row in rows[1:]:
            csv_writer.writerow([td.text.strip() for td in row.find_all('td')])

url4 = "https://raw.githubusercontent.com/JMousqueton/ransomware.live/main/groups.json"
response4 = urlopen(url4)
data4 = json.load(response4)
headers4 = ["name", "fqdn", "slug", "lastscrape", "available", "profile"]

with open("../../CSV/Groupes/Donnees_Groupes/Ransomwarelive.csv", "w", newline="", encoding="utf-8") as csvfile4:
    csvwriter4 = csv.writer(csvfile4, delimiter="|")
    csvwriter4.writerow(headers4)
    
    for entry4 in data4:
        if "locations" in entry4:
            for location4 in entry4["locations"]:
                name4 = entry4["name"]
                fqdn4 = location4["fqdn"]
                slug4 = location4["slug"]
                lastscrape4 = location4["lastscrape"] if "lastscrape" in location4 else ""
                available4 = location4["available"] if "available" in location4 else ""
                profile4 = ", ".join(entry4["profile"]) if "profile" in entry4 else ""
                csvwriter4.writerow([name4, fqdn4, slug4, lastscrape4, available4, profile4])