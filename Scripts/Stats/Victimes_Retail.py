import pandas as pd

# Liste des mots à rechercher dans la colonne Summary
keywords = ['Point de vente', 'Boutique', 'Magasin', 'Commerce', 'Échoppe', 'Marchand',
            'Épicerie', 'Supérette', 'Supermarché', 'Hypermarché', 'Grand magasin', 'Centre commercial']

# Chemin des fichiers CSV
input_file_path = '..\\..\\CSV\\Victimes\\Ransomwarelive.csv'
output_file_path = '../../CSV/Stats/Victimes_Retail/Victimes_Retail.csv'

# Charger le fichier CSV dans un DataFrame
df = pd.read_csv(input_file_path, delimiter='|', encoding='utf-8')

# Convertir la colonne 'Summary' en minuscules pour rendre la recherche insensible à la casse
df['Summary'] = df['Summary'].str.lower()

# Filtrer les lignes qui contiennent au moins un mot-clé dans la colonne Summary
filtered_df = df[df['Summary'].str.contains(r'\b(?:' + '|'.join(keywords) + r')\b', case=False, na=False, regex=True)]

# Enregistrer le DataFrame filtré dans un nouveau fichier CSV
filtered_df.to_csv(output_file_path, sep='|', encoding='utf-8', index=False)