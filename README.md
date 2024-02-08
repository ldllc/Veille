# Comment fonctionne le système de veille

## I - Fonctionnement

Il y a deux codes par catégories : le Scrapper et le CSV.

### 1) Le Scrapper

Le Scrapper est le programme chargé de récupérer les tableaux des sites concernés, à savoir :

- [RansomFeed](https://ransomfeed.it/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [Ransom-DB](https://www.ransom-db.com/)
- [Ransomware Live](https://www.ransomware.live/#/)

Ces tableaux sont parsés et stockés dans des CSV avec leurs noms respectifs. Ils sont ensuite enregistrés dans le dossier CSV, puis dans le dossier "Donnees_" approprié.

### 2) Le CSV

Le CSV se charge de comparer les tableaux puis de récupérer les informations communes mais également les plus importantes pour les placer dans un tableau CSV commun. Ce tableau sera stocké dans le dossier CSV, puis dans le dossier "Base_" approprié.

## II - Les Stats

Les stats proposent 4 données différentes : 

- Le top 10 des groupes les plus actifs de la journée, du mois et de l'année. Est également présent le groupe avec le plus d'attaques de l'année passée.
- Le compte des attaques de la journée, de la journée d'avant, du mois, du mois dernier ainsi que l'année en cours et également l'année d'avant.
- Les groupes attaquants s'attaquants aux commerces.
- Les victimes du commerce ayant été attaquées.
