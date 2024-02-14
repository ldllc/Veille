import os
import csv
from collections import defaultdict
from datetime import datetime, timedelta

csv_file_path = "../../CSV/Attaques/Base_Attaques/Attaques.csv"

# Utiliser un dictionnaire pour stocker les statistiques de chaque jour
daily_stats = defaultdict(lambda: defaultdict(int))

with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|')
    for row in reader:
        discovered_date = row['discovered'].split()[0]  
        group = row['Group']

        daily_stats[discovered_date]['Total'] += 1
        daily_stats[discovered_date][group] += 1

# Répertoire de sortie
output_directory = "../../CSV/Stats/Comptes_Journaliers/"
output_file = os.path.join(output_directory, "Comptes_Journaliers.csv")

# Vérifier et créer le répertoire si nécessaire
os.makedirs(output_directory, exist_ok=True)

# Générer des statistiques pour chaque jour
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter='|')
    writer.writerow(['Date', 'Group', 'Nombre d\'attaques'])

    for date, stats in daily_stats.items():
        for group, occurrences in stats.items():
            if group == 'Total':
                continue
            writer.writerow([date, group, occurrences])
