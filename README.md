# Comment fonctionne le système de veille

## I - Qu'est ce que la veille

La veille en cybersécurité consiste en une surveillance continue des menaces et des vulnérabilités informatiques pour anticiper les risques potentiels. Les professionnels utilisent cette approche pour rester informés des dernières tendances, attaques émergentes et développements technologiques pertinents, renforçant ainsi la défense des systèmes d'information. C'est une composante essentielle pour maintenir une posture de sécurité proactive et protéger efficacement les données et les réseaux.

## II - Fonctionnement

### Première partie : récupération des données 

Le code commence par récupérer les tableaux des sites concernés, à savoir :

- [RansomFeed](https://ransomfeed.it/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [Ransom-DB](https://www.ransom-db.com/)
- [Ransomware Live](https://www.ransomware.live/#/)

Les tableaux sont récupérés et stockés dans des fichiers CSV<sup>1</sup> avec leurs noms respectifs.

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

#### a) Srapper<sup>2</sup>

Le script `Scrapper_Groupes.py` récupère les tableaux affichant les groupes sur :

- [RansomFeed](https://raw.githubusercontent.com/nuke86/ransomFeed/main/groups.json)
- [MITRE ATT&CK](https://attack.mitre.org/groups/)
- [Ransom-DB](https://www.ransom-db.com/ransomware-groups)
- [Ransomware Live](https://raw.githubusercontent.com/JMousqueton/ransomware.live/main/groups.json)

Ils seront enregistrés dans un fichier CSV dans le dossier [Donnees_Groupes](CSV/Groupes/Donnees_Groupes) avec leur nom respectifs.


#### b) Traitement 

Le script `CSV_Groupes.py` s'occupe de traiter les données des fichiers fraîchement enregistrés pour récupérer les informations communes et également les plus importantes pour les enregistrer dans le dossier [Base_Groupes](CSV/Groupes/Base_Groupes/Groupes.csv) avec comme nom de fichier `Groupes.csv`. 

### 2) Attaques


#### a) Srapper

Le script `Scrapper_Attaques.py` récupère les tableaux affichant les groupes sur :

- [RansomFeed](https://raw.githubusercontent.com/nuke86/ransomFeed/main/posts.json)
- [Ransomware Live](https://data.ransomware.live/posts.json)

Ils seront enregistrés dans un fichier CSV dans le dossier [Donnees_Attaques](CSV/Attaques/Donnees_Attaques) avec leur nom respectifs.


#### b) Traitement 

Le script `CSV_Attaques.py` s'occupe de traiter les données des fichiers fraîchement enregistrés pour récupérer les informations communes et également les plus importantes pour les enregistrer dans le dossier [Base_Attaques](CSV/Attaques/Base_Attaques/Attaques.csv) avec comme nom de fichier `Attaques.csv`. 

### 3) Victimes

Le script `Scrapper_Victimes.py` récupère les tableaux affichant les groupes sur :

- [Ransomware Live](https://raw.githubusercontent.com/Casualtek/Cyberwatch/main/cyberattacks.json)

Ils seront enregistrés dans un fichier CSV dans le dossier [Victimes](CSV/Victimes) avec leur nom respectifs.


### 4) Stats

#### a) Attaquants

Le script `Attaquants_Retail.py` cherche dans les fichiers `Groupes.csv` et `Attaques.csv` les groupes ayant attaqué des points de vente pour les enregistrer dans le fichier `Attaquants_Retail.csv` dans le dossier [Attaquants_Retail](CSV/Stats/Attaquants_Retail).

#### b) Victtimes

Le script `Victimes_Retail.py` cherche dans les fichiers `Groupes.csv` et `Victimes.csv` les groupes ayant attaqué des points de vente pour les enregistrer dans le fichier Victimes_Retail.csv` dans le dossier [Victimes_Retail](CSV/Stats/Victimes_Retail).

#### c) Groupes

Le script `Top10_Groupes.py` se charge de déterminer les 10 groupes les plus actifs de la journée, de la journée précédente, du mois, du mois précédent, de l'année et de l'année précédente. Ces données seront enregistrées dans le dossier [Activites](CSV/Stats/Activites).

#### d) Comptes

Le script `Comptes_Attaques.py` se charge de compter le nombre d'attaques dans la journée, de la journée précédente, du mois, du mois précédent, de l'année et de l'année précédente. Ces données seront enregistrées dans le fichier `Day_Stats.csv` se trouvant dans le dossier [Comptes](CSV/Stats/Comptes).

### 5) Excel

Le script `Excel.py` se charge de récupérer les fichiers de stats, mais également les fichiers `Groupes.csv`, `Attaques.csv` et `Victimes.csv` pour les mettre dans le fichier Excel `Veille.xlsx` sous forme de tableau. Il y aura une feuille par fichiers.

## V - Définitions

- CSV, (Concurrent Version System) est un outil permettant de gérer l'évolution dans le temps d'un ensemble de fichiers
- Le terme Scraping (Scrap ou Scraper) fait référence à une technique qui consiste à copier du contenu à partir d'un autre site web en utilisant un logiciel ou un programme informatique spécifique.

