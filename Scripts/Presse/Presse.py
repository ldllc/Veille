from eventregistry import *
import csv

er = EventRegistry(apiKey='fde1f196-e72f-4ea5-9987-5bfa85629d34')

q = QueryArticlesIter(
    conceptUri=er.getConceptUri("cyberattack"),
    categoryUri=er.getCategoryUri("cybersecurity"))

# Create a CSV file and write the header
csv_file_path = '../../CSV/Presse/Presse.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['title', 'url', 'date', 'source']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter='|')
    csv_writer.writeheader()

    # Obtain 500 articles that were shared the most on social media, sorted by date in descending order
    for art in q.execQuery(er, sortBy="date", sortOrder="desc", maxItems=500):
        # Check if 'socialScore' key exists in the article
        social_score = art.get('socialScore', 'N/A')

        # Write article information to the CSV file
        csv_writer.writerow({
            'title': art['title'],
            'url': art['url'],
            'date': art['date'],
            'source': art['source']['title'],
        })
