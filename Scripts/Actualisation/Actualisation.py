import os

groupes_path = "../Groupes"
os.chdir(groupes_path)
os.system("python Scraper_Groupes.py")
print("Les fichiers de groupes ont été créés avec succès.")
os.system("python CSV_Groupes.py")
print("La base de données Groupes a été créée avec succès.")

attaques_path = "../Attaques"
os.chdir(attaques_path)
os.system("python Scraper_Attaques.py")
print("Les fichiers d'attaques ont été créés avec succès.")
os.system("python CSV_Attaques.py")
print("La base de données Attaques a été créée avec succès.")

victimes_path = "../Victimes"
os.chdir(victimes_path)
os.system("python Scraper_Victimes.py")
os.system("python Retail_Victimes.py")
os.system("python Domaines_Victimes.py")
print(f"Les victimes ont été mises à jour.")

stats_path = "../Stats"
os.chdir(stats_path)
os.system("python Comptes_Journaliers.py")
os.system("python Comptes_Attaques.py")
os.system("python Attaquants_Retail.py")
print("Les stats ont été mises à jour.")

stats_path = "../Presse"
os.chdir(stats_path)
os.system("python Scraper_Presse.py")
os.system("python Scraper_Presse_Specialisee.py")
os.system("python CSV_Presse_Globale.py")
print("Les articles de presse ont été mis à jour.")

os.chdir("../Excel")
os.system("python Excel.py")
print("Le fichier excel a été créé avec succès.")

print("Mise à jour effectuée avec succès.")