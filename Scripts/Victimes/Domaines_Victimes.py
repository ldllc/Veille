import pandas as pd

fichier_source = '../../CSV/Stats/Victimes/Victimes_Globales.csv'
df = pd.read_csv(fichier_source, sep='|')
colonnes_a_extraire = df.iloc[:, [0, 2]]
nouveau_df = pd.DataFrame({
    'Dates': colonnes_a_extraire.iloc[:, 0],
    'Domaines': colonnes_a_extraire.iloc[:, 1]
})
fichier_destination = '../../CSV/Stats/Victimes/Victimes_Domaines.csv'
nouveau_df.to_csv(fichier_destination, index=False, sep='|')