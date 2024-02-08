import csv
from datetime import datetime, timedelta

csv_file_path = "../../CSV/Attaques/Base_Attaques/Attaques.csv"

day_stats = 0
yesterday_stats = 0
current_month_stats = 0
last_month_stats = 0
current_year_stats = 0
last_year_stats = 0

current_date = datetime.now()
yesterday_date = (current_date - timedelta(days=1)).strftime('%Y-%m-%d')

current_month = current_date.strftime('%Y-%m')
last_month = (current_date - timedelta(days=current_date.day)).strftime('%Y-%m')
current_year = current_date.strftime('%Y')
last_year = (current_date - timedelta(days=365)).strftime('%Y')

with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|')
    for row in reader:
        discovered_date = datetime.strptime(row['discovered'].split()[0], '%Y-%m-%d').strftime('%Y-%m-%d')

        if discovered_date == current_date.strftime('%Y-%m-%d'):
            day_stats += 1
        if discovered_date == yesterday_date:
            yesterday_stats += 1
        if discovered_date.startswith(current_month):
            current_month_stats += 1
        if discovered_date.startswith(last_month):
            last_month_stats += 1
        if discovered_date.startswith(current_year):
            current_year_stats += 1
        if discovered_date.startswith(last_year):
            last_year_stats += 1

def save_stats_to_csv(stats, file_name):
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerow(['Période', 'Nombre d\'attaques'])
        writer.writerow(['Aujourd\'hui', stats['today']])
        writer.writerow(['Hier', stats['yesterday']])
        writer.writerow(['Ce mois-ci', stats['current_month']])
        writer.writerow(['Mois dernier', stats['last_month']])
        writer.writerow(['Cette année', stats['current_year']])
        writer.writerow(['Année dernière', stats['last_year']])

stats_folder = "../../CSV/Stats/comptes"
day_stats_file = f"{stats_folder}/Day_Stats.csv"
yesterday_stats_file = f"{stats_folder}/Yesterday_Stats.csv"
current_month_stats_file = f"{stats_folder}/Current_Month_Stats.csv"
last_month_stats_file = f"{stats_folder}/Last_Month_Stats.csv"
current_year_stats_file = f"{stats_folder}/Current_Year_Stats.csv"
last_year_stats_file = f"{stats_folder}/Last_Year_Stats.csv"

stats = {
    'today': day_stats,
    'yesterday': yesterday_stats,
    'current_month': current_month_stats,
    'last_month': last_month_stats,
    'current_year': current_year_stats,
    'last_year': last_year_stats
}

save_stats_to_csv(stats, day_stats_file)