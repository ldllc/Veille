import pandas as pd

presse_specialisee = pd.read_csv('../../CSV/Presse/Presse/Presse_Specialisee.csv', delimiter='|')
presse = pd.read_csv('../../CSV/Presse/Presse/Presse.csv', delimiter='|')

presse_specialisee = presse_specialisee[['Date de publication', 'Titre', 'URL', 'Source']]
presse = presse[['date', 'title', 'url', 'source']]

presse_specialisee.columns = ['Date', 'Titre', 'URL', 'Source']
presse.columns = ['Date', 'Titre', 'URL', 'Source']

presse_globale = pd.concat([presse_specialisee, presse], ignore_index=True)
presse_globale.to_csv('../../CSV/Presse/Presse_Globale/Presse_Globale.csv', index=False, sep='|')