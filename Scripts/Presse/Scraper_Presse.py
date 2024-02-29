from eventregistry import *
import csv

er = EventRegistry(apiKey='fde1f196-e72f-4ea5-9987-5bfa85629d34')

q = QueryArticlesIter(
    conceptUri=er.getConceptUri("cyberattack"),
    categoryUri=er.getCategoryUri("cybersecurity"))

csv_file_path = '../../CSV/Presse/Presse/Presse.csv'

seen_titles = set()

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['title', 'url', 'date', 'source']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='|')
    csv_writer.writeheader()

    for art in q.execQuery(er, sortBy="date", sortOrder="desc", maxItems=500):
        title = art['title']
        if title not in seen_titles:
            seen_titles.add(title)
            csv_writer.writerow({
                'title': title,
                'url': art['url'],
                'date': art['date'],
                'source': art['source']['title'],
            })