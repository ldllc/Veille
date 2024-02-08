import os

groupes_path = "Scripts/Groupes"
os.chdir(groupes_path)
os.system("python Scrapper_Groupes.py")
print("Les fichiers de groupes ont été créés avec succès.")
os.system("python CSV_Groupes.py")
print("La base de données Groupes a été créée avec succès.")

attaques_path = "../Attaques"
os.chdir(attaques_path)
os.system("python Scrapper_Attaques.py")
print("Les fichiers d'attaques ont été créés avec succès.")
os.system("python CSV_Attaques.py")
print("La base de données Attaques a été créée avec succès.")

victimes_path = "../Victimes"
os.chdir(victimes_path)
os.system("python Scrapper_Victimes.py")
print(f"Le fichier des victimes a été créé avec succès.")

stats_path = "../Stats"
os.chdir(stats_path)
os.system("python Top10_Groupes.py")
os.system("python Comptes_Attaques.py")
os.system("python Attaquants_Retail.py")
os.system("python Victimes_Retail.py")
print("Les stats ont été mises à jour.")

os.chdir("../")
os.system("python Excel.py")
print("Le fichier excel a été créé avec succès.")

print("Mise à jour effectuée avec succès.")
print("Ouverture du Excel...")

os.chdir("../Excel")
excel_file_path = "Veille.xlsx"
os.startfile(excel_file_path)