import csv
from collections import defaultdict
from datetime import datetime, timedelta

csv_file_path = "../../CSV/Attaques/Base_Attaques/Attaques.csv"

day_stats = defaultdict(int)
month_stats = defaultdict(int)
year_stats = defaultdict(int)

current_date = datetime.now()
current_month = current_date.strftime('%Y-%m')
current_year = current_date.strftime('%Y')
previous_year = (current_date - timedelta(days=365)).strftime('%Y')

with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|')
    for row in reader:
        discovered_date = row['discovered'].split()[0]  
        group = row['Group']

        if discovered_date == current_date.strftime('%Y-%m-%d'):
            day_stats[group] += 1
        if discovered_date.startswith(current_month):
            month_stats[group] += 1
        if discovered_date.startswith(current_year):
            year_stats[group] += 1

def save_stats_to_csv(stats, file_name):
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        writer.writerow(['Group', 'Nombre d\'attaques'])
        for group, occurrences in sorted(stats.items(), key=lambda x: x[1], reverse=True)[:10]:
            writer.writerow([group, occurrences])

day_stats_file = "../../CSV/Stats/Activite/Day_Stats.csv"
month_stats_file = "../../CSV/Stats/Activite/Month_Stats.csv"
year_stats_file = "../../CSV/Stats/Activite/Year_Stats.csv"
previous_year_stats_file = "../../CSV/Stats/Activite/Previous_Year_Stats.csv"

save_stats_to_csv(day_stats, day_stats_file)
save_stats_to_csv(month_stats, month_stats_file)
save_stats_to_csv(year_stats, year_stats_file)

previous_year_stats = defaultdict(int)
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|')
    for row in reader:
        discovered_date = row['discovered'].split()[0]
        group = row['Group']
        if discovered_date.startswith(previous_year):
            previous_year_stats[group] += 1

save_stats_to_csv(previous_year_stats, previous_year_stats_file)