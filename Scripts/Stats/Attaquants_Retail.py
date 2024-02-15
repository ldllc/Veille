import pandas as pd

chemin_original = "../../CSV/Groupes/Base_Groupes/Groupes.csv"
chemin_destination = "../../CSV/Stats/Attaquants_Retail/Attaquants_retail.csv"

donnees_originales = pd.read_csv(chemin_original, sep='|')
nom_colonne_appropriee = 'Description'

groupes_retail = donnees_originales.dropna(subset=[nom_colonne_appropriee])
groupes_retail = groupes_retail[groupes_retail[nom_colonne_appropriee].str.contains('retail|retailer', case=False)]

if not groupes_retail.empty:
    groupes_retail.to_csv(chemin_destination, index=False, sep='|', mode='w', header=True)