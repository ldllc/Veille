import csv
from datetime import datetime, timedelta

csv_file_path = "../../CSV/Attaques/Base_Attaques/Attaques.csv"

current_date = datetime.now()
yesterday_date = (current_date - timedelta(days=1)).strftime('%Y-%m-%d')

current_month = current_date.strftime('%Y-%m')
last_month = (current_date - timedelta(days=current_date.day)).strftime('%Y-%m')
current_year = current_date.strftime('%Y')
last_year = (current_date - timedelta(days=365)).strftime('%Y')

same_day_last_year = (current_date - timedelta(days=365)).strftime('%Y-%m-%d')
same_month_last_year = (current_date - timedelta(days=365)).strftime('%Y-%m')

stats = {
    'today': 0,
    'yesterday': 0,
    'current_month': 0,
    'last_month': 0,
    'current_year': 0,
    'last_year': 0,
    'same_day_last_year': 0,
    'same_month_last_year': 0
}

with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|')
    for row in reader:
        discovered_date = datetime.strptime(row['discovered'].split()[0], '%Y-%m-%d').strftime('%Y-%m-%d')

        if discovered_date == current_date.strftime('%Y-%m-%d'):
            stats['today'] += 1
        if discovered_date == yesterday_date:
            stats['yesterday'] += 1
        if discovered_date.startswith(current_month):
            stats['current_month'] += 1
        if discovered_date.startswith(last_month):
            stats['last_month'] += 1
        if discovered_date.startswith(current_year):
            stats['current_year'] += 1
        if discovered_date.startswith(last_year):
            stats['last_year'] += 1
        if discovered_date == same_day_last_year:
            stats['same_day_last_year'] += 1
        if discovered_date.startswith(same_month_last_year):
            stats['same_month_last_year'] += 1

def save_stats_to_csv(stats, file_name):
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerow(['Période', 'Nombre d\'attaques'])
        writer.writerow(['Aujourd\'hui', stats['today']])
        writer.writerow(['Jour année dernière', stats['same_day_last_year']])
        writer.writerow(['Hier', stats['yesterday']])
        writer.writerow(['Ce mois-ci', stats['current_month']])
        writer.writerow(['Mois année dernière', stats['same_month_last_year']])
        writer.writerow(['Mois dernier', stats['last_month']])
        writer.writerow(['Cette année', stats['current_year']])
        writer.writerow(['Année dernière', stats['last_year']])

stats_folder = "../../CSV/Stats/Comptes_Attaques"
day_stats_file = f"{stats_folder}/Comptes_Attaques.csv"

save_stats_to_csv(stats, day_stats_file)
