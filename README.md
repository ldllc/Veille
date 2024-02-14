# Comment fonctionne le système de veille

## I - Qu'est ce que la veille

La veille en cybersécurité consiste en une surveillance continue des menaces et des vulnérabilités informatiques pour anticiper les risques potentiels. Les professionnels utilisent cette approche pour rester informés des dernières tendances, attaques émergentes et développements technologiques pertinents, renforçant ainsi la défense des systèmes d'information. C'est une composante essentielle pour maintenir une posture de sécurité proactive et protéger efficacement les données et les réseaux.

## II - Fonctionnement

### 1) Récupération des données 

Le code commence par récupérer les tableaux des sites concernés, à savoir :

- [RansomFeed](https://ransomfeed.it/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [Ransom-DB](https://www.ransom-db.com/)
- [Ransomware Live](https://www.ransomware.live/#/)

Les tableaux sont récupérés et stockés dans des fichiers CSV<sup>1</sup> avec leurs noms respectifs.

### 2) Traitement des données

Les données sont ensuite traitées et mise en commun dans un seul fichier CSV en reprenant les informations communes et majeures.

### 3) Mise en page

pour finir les fichiers CSV sont mis en page dans un fichier Excel avec une feuille par thème qui sont :

- Groupes
- Attaques
- Victimes Retail
- Attaquants Retail
- Presse
- Statistiques

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
- eventregistry
- tkinter
- customtkinter

*`Install.ps1` s'exécute dans le terminal PowerShell. (Clic droit sur le fichier puis cliquer sur exécuter avec PowerShell ce qui installera les dépendances automatiquement.)* 

## IV - Code

### 1) Groupes

#### a) Scraper<sup>2</sup>

Le script `Scraper_Groupes.py` récupère les tableaux affichant les groupes sur :

- [RansomFeed](https://raw.githubusercontent.com/nuke86/ransomFeed/main/groups.json)
- [MITRE ATT&CK](https://attack.mitre.org/groups/)
- [Ransom-DB](https://www.ransom-db.com/ransomware-groups)
- [Ransomware Live](https://raw.githubusercontent.com/JMousqueton/ransomware.live/main/groups.json)

Ils seront enregistrés dans un fichier CSV dans le dossier [Donnees_Groupes](CSV/Groupes/Donnees_Groupes) avec leur nom respectifs.

#### b) Traitement 

Le script `CSV_Groupes.py` s'occupe de traiter les données des fichiers fraîchement enregistrés pour récupérer les informations communes et également les plus importantes pour les enregistrer dans le dossier [Base_Groupes](CSV/Groupes/Base_Groupes/Groupes.csv) avec comme nom de fichier `Groupes.csv`. 

### 2) Attaques

#### a) Scraper

Le script `Scraper_Attaques.py` récupère les tableaux affichant les groupes sur :

- [RansomFeed](https://raw.githubusercontent.com/nuke86/ransomFeed/main/posts.json)
- [Ransomware Live](https://data.ransomware.live/posts.json)

Ils seront enregistrés dans un fichier CSV dans le dossier [Donnees_Attaques](CSV/Attaques/Donnees_Attaques) avec leur nom respectifs.

#### b) Traitement 

Le script `CSV_Attaques.py` s'occupe de traiter les données des fichiers fraîchement enregistrés pour récupérer les informations communes et également les plus importantes pour les enregistrer dans le dossier [Base_Attaques](CSV/Attaques/Base_Attaques/Attaques.csv) avec comme nom de fichier `Attaques.csv`. 

### 3) Victimes

Le script `Scraper_Victimes.py` récupère les tableaux affichant les groupes sur :

- [Ransomware Live](https://raw.githubusercontent.com/Casualtek/Cyberwatch/main/cyberattacks.json)

Ils seront enregistrés dans un fichier CSV dans le dossier [Victimes](CSV/Victimes) avec leur nom respectifs.

### 4) Stats

#### a) Attaquants

Le script `Attaquants_Retail.py` cherche dans les fichiers `Groupes.csv` et `Attaques.csv` les groupes ayant attaqué des points de vente pour les enregistrer dans le fichier `Attaquants_Retail.csv` dans le dossier [Attaquants_Retail](CSV/Stats/Attaquants_Retail).

#### b) Victimes

Le script `Victimes_Retail.py` cherche dans le fichiers`Victimes.csv` les victimes qui sont des points de vente et enregistre le résultat dans le fichier`Victimes_Retail.csv` dans le dossier [Victimes_Retail](CSV/Stats/Victimes_Retail).

#### c) Attaques par groupes

Le script `Comptes_Journaliers.py` se charge de compter le nombre d'attaques par jour effectuées par chaque groupes et enregistre le résultat dans le fichier `Compte_Journaliers.csv` dans le dossier [Comptes_Journaliers](CSV/Stats/Comptes_Journaliers).

#### d) Comptes des attaques

Le script `Comptes_Attaques.py` se charge de compter le nombre d'attaques pour : la journée, celle d'avant, la même journée de l'année passée, le mois, le mois d'avant, le même mois de l'année passée, l'année actuelle et l'année dernière. Ces données seront enregistrées dans le fichier `Comptes_Attaques.csv` se trouvant dans le dossier [Comptes_Attaques](CSV/Stats/Comptes_Attaques_).

### 5) Excel

Le script `Excel.py` se charge de récupérer les fichiers de stats, mais également les fichiers `Groupes.csv`, `Attaques.csv` et `Victimes.csv` pour les mettre dans le fichier Excel `Veille.xlsx` sous forme de tableau. Il y aura une feuille par fichiers.

## V - Site

### 1) Hébergement

Le site est hébergé localement sur la machine ce qui permet l'accès aux personnes autorisées seulement. Pour s'y rendre il faut taper le lien [localhost:8000/Veille.html](localhost:8000/Veille.html). Il n'est pas accessible autrement. Si le code n'a pas été lancé pour mettre à jour la veille, il ne sera pas accessible. 

Si nous voulons le lancer quand même sans actualiser la veille, il faudra taper dans un terminal Powershell `python -m http.server` ou exécuter le Script `Lancement_Serveur.ps1` qui ouvrira le bon port<sup>3</sup>.

*(Pour rappel un Powershell s'exécute avec un clic droit sur le fichier puis cliquer sur exécuter avec PowerShell ce qui exécutera le code)*

### 2) Fonctionnement

Le site contient les informations du fichier Excel mais sous format web. le rendu y est plus épuré et plus intuitif pour trier les données. Il permet également de télécharger le fichier Excel avec son bouton de téléchargement.

L'idée derrière le site était de présenter le fichier Excel sous une autre forme pour que même une personne n'étant pas familière avec excel puisse consulter le tableau et le manipuler.

## VI - L'application

### 1) Objectif

Le but de l'application est de prendre les données les plus importantes du fichier Excel et de les synthétiser. Les données de l'application sont les mêmes que pour le Excel et le site à la seule différence que seuls les groupes actifs sont affichés.

## VI - Définitions

- CSV<sup>1</sup> : Le format CSV (Comma-Separated Values) est un type de fichier texte où les données d'un tableau sont représentées sous forme de lignes, avec les valeurs des colonnes séparées par des virgules.

    *Exemple de fichier CSV:*

    Nom,prénom,âge<br>Doe,John,36<br><br>

- Scraper<sup>2</sup> : Un scraper est un programme informatique conçu pour extraire automatiquement des données d'un site web en naviguant à travers ses pages et en récupérant les informations spécifiées.<br><br>

- Port<sup>3</sup> : Un port est un point virtuel où les connexions réseau commencent et se terminent. Les ports sont basés sur des logiciels et gérés par le système d'exploitation d'un ordinateur. Chaque port est associé à un processus ou à un service spécifique.<br><br>

*source Scraper: [Cloudflare](https://www.cloudflare.com/fr-fr/learning/bots/what-is-data-scraping/)*<br>
*source Port: [Cloudflare](https://www.cloudflare.com/fr-fr/learning/network-layer/what-is-a-computer-port/)*