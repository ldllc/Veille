import pandas as pd

file_ransomfeed = "../../CSV/Attaques/Donnees_Attaques/Ransomfeedit.csv"
file_ransomwarelive = "../../CSV/Attaques/Donnees_Attaques/Ransomwarelive.csv"

df_ransomfeed = pd.read_csv(file_ransomfeed, sep='|')
df_ransomwarelive = pd.read_csv(file_ransomwarelive, sep='|')

merged_df = pd.merge(df_ransomfeed, df_ransomwarelive, on=['post_title', 'group_name', 'discovered'], how='outer')
merged_df.insert(0, 'ID', range(1, 1 + len(merged_df)))
merged_df = merged_df.rename(columns={'post_title': 'Name', 'group_name': 'Group'})
merged_df = merged_df.fillna("Not provided")

final_df = merged_df[['ID', 'Name', 'Group', 'discovered', 'published', 'country', 'description', 'website', 'post_url']]
final_df = final_df.drop_duplicates(subset=['Name', 'Group', 'discovered'])
final_df = final_df.sort_values(by='discovered', ascending=False)
final_df = final_df.reset_index(drop=True)

output_file = "../../CSV/Attaques/Base_Attaques/Attaques.csv"
final_df.to_csv(output_file, index=False, sep='|')
