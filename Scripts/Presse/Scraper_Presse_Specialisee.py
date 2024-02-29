import feedparser
import csv
import os
from datetime import datetime

def parse_date(date_string):
    try:
        return datetime.strptime(date_string, '%a, %d %b %Y %H:%M:%S %Z').strftime('%Y-%m-%d')
    except ValueError:
        try:
            return datetime.strptime(date_string, '%a, %d %b %Y %H:%M:%S').strftime('%Y-%m-%d')
        except ValueError:
            try:
                return datetime.strptime(date_string, '%a, %d %b %Y %H:%M:%S %z').strftime('%Y-%m-%d')
            except ValueError:
                try:
                    return datetime.fromisoformat(date_string).strftime('%Y-%m-%d')
                except ValueError:
                    return None

def lire_flux_rss(urls):
    nom_fichier_csv = "../../CSV/Presse/Presse/Presse_Specialisee.csv"
    
    try:
        with open(nom_fichier_csv, 'r', newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            existing_fieldnames = reader.fieldnames
            url_key = 'URL' if 'URL' in existing_fieldnames else existing_fieldnames[0]
            
            existing_urls = set(row[url_key] for row in reader)
    except FileNotFoundError:
        existing_urls = set()

    fieldnames = ['Source', 'Date de publication', 'Titre', 'URL']
    data_list = []

    for url in urls:
        feed = feedparser.parse(url)

        if feed.bozo == 0:
            for entry in feed.entries:
                if entry.link not in existing_urls:
                    formatted_date = parse_date(entry.published)

                    data_list.append({
                        "Source": url,
                        "Date de publication": formatted_date,
                        "Titre": entry.title,
                        "URL": entry.link
                    })
        else:
            print(f"Erreur lors de l'analyse du flux RSS {url}")

    with open(nom_fichier_csv, 'a', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='|')

        if os.path.getsize(nom_fichier_csv) == 0:
            writer.writeheader()
        writer.writerows(data_list)

urls_flux_rss = [
    "https://cybersecuritynews.com/feed/",
    "https://blog.virustotal.com/feeds/posts/default",
    "https://www.securityweek.com/feed/",
    "https://isc.sans.edu/rssfeed.xml",
    "https://www.xmco.fr/feed/",
    "https://threatpost.com/feed/",
    "https://www.databreaches.net/feed/",
    "https://www.bleepingcomputer.com/feed/",
    "https://www.darkreading.com/rss.xml",
    "https://www.zataz.com/feed/",
    "https://feeds.feedburner.com/TheHackersNews",
    "https://www.cybersecuritydive.com/feeds/news/",
    "https://blog.xpnsec.com/rss.xml",
    "https://www.lefigaro.fr/rss/figaro_flash-actu.xml",
    "https://feeds.feedburner.com/TheHackersNews",
    "https://securelist.com/feed/",
    "https://feeds.fortinet.com/fortinet/blog/psirt&x=1",
    "https://www.forcepoint.com/rss.xml",
    "https://blog.xpnsec.com/rss.xml",
    #"https://therecord.media/feed",
    "https://fetchrss.com/rss/65b0eb775582bd1c19083c4365b0fdb664898a0daa63bef4.xml",
    "https://unit42.paloaltonetworks.com/feed/",
    "https://feeds.fortinet.com/fortinet/blog/threat-research&x=1",
    "https://www.sentinelone.com/feed/",
    "https://www.lemagit.fr/rss/ContentSyndication.xml"
]

lire_flux_rss(urls_flux_rss)