# Comment fonctionne le système de veille

## I - Qu'est ce que la veille

Faire la veille, c'est rechercher et collecter des informations pertinentes pour l'entreprise, pour ensuite s'en servir dans la prise de décision. 

C'est se tenir au courant de ce qui se dit sur l'entreprise, sur les concurrents, sur le secteur d'activité et sur ce qui peut l'impacter.

## II - Fonctionnement

### Première partie : récupération des données 

Le code commence par récupérer les tableaux des sites concernés, à savoir :

- [RansomFeed](https://ransomfeed.it/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [Ransom-DB](https://www.ransom-db.com/)
- [Ransomware Live](https://www.ransomware.live/#/)

Les tableaux sont récupérés et stockés dans des fichiers CSV<sup>*1</sup> avec leurs noms respectifs.

### Deuxième partie : traitement des données

Les données sont ensuite traitées et mise en commun dans un seul fichier CSV en reprenant les informations communes et majeures.

### Troisième partie : mise en page

pour finir les fichiers CSV sont mis en page dans un fichier Excel avec une feuille par thème qui sont :

- Groupes
- Attaques
- Victimes 
- Stats

## III - Installation

/!\\ Nécessite au moins d'avoir installé Python au préalable. /!\\

le code fonctionne sur pyhton et nécessite les dépendances présentes dans le fichier `Install.ps1`. Pour rappel, les dépendances nécessaires sont :

- requests
- pandas
- openpyxl
- lxml
- pyarrow
- selenium
- bs4

*`Install.ps1` s'exécute dans le terminal PowerShell. (Clic droit sur le fichier puis cliquer sur exécuter avec PowerShell ce qui installera les dépendances automatiquement.)* 

## IV - Le code

### 1) Groupes

#### a) Srapper

Le script `Scrapper_Groupes.py` récupère les tableaux affichant les groupes sur :

- [RansomFeed](https://raw.githubusercontent.com/nuke86/ransomFeed/main/groups.json)
- [MITRE ATT&CK](https://attack.mitre.org/groups/)
- [Ransom-DB](https://www.ransom-db.com/ransomware-groups)
- [Ransomware Live](https://raw.githubusercontent.com/JMousqueton/ransomware.live/main/groups.json)

Ils seront enregistrés dans un fichier CSV dans le dossier [Donnees_Groupes](CSV/Groupes/Donnees_Groupes) avec leur nom respectifs.


#### b) Traitement 

Le script `CSV_Groupes.py` s'occupe de traiter les données des fichiers fraîchement enregistrés pour récupérer les informations communes et également les plus importantes pour les enregistrer dans le dossier [Base_Groupes](CSV/Groupes/Base_Groupes/Groupes.csv) avec comme nom de fichier `Groupes.csv`. 















Les Définitions

- CVS, (Concurrent Version System) est un outil permettant de gérer l'évolution dans le temps d'un ensemble de fichiers

