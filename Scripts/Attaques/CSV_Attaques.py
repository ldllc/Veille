import pandas as pd
from datetime import datetime

file_ransomfeed = "../../CSV/Attaques/Donnees_Attaques/Ransomfeedit.csv"
file_ransomwarelive = "../../CSV/Attaques/Donnees_Attaques/Ransomwarelive.csv"
output_file = "../../CSV/Attaques/Base_Attaques/Attaques.csv"

existing_df = pd.read_csv(output_file, sep='|')

df_ransomfeed = pd.read_csv(file_ransomfeed, sep='|')
df_ransomwarelive = pd.read_csv(file_ransomwarelive, sep='|')

merged_df = pd.merge(df_ransomfeed, df_ransomwarelive, on=['post_title', 'group_name', 'discovered'], how='outer')
merged_df.insert(0, 'ID', range(1, 1 + len(merged_df)))
merged_df = merged_df.rename(columns={'post_title': 'Name', 'group_name': 'Group'})
merged_df = merged_df.fillna("Not provided")

today_attacks = merged_df[merged_df['discovered'] == datetime.today().strftime('%Y-%m-%d')]

today_attacks = today_attacks.groupby(['Name', 'Group'], as_index=False).agg({
    'discovered': 'max',
    'published': 'max',
    'country': ', '.join,
    'description': ', '.join,
    'website': ', '.join,
    'post_url': ', '.join  
})

existing_df = pd.concat([existing_df, today_attacks], ignore_index=True)
existing_df = existing_df.drop_duplicates(subset=['Name', 'Group'])
existing_df = existing_df.sort_values(by='discovered', ascending=False)
existing_df = existing_df.reset_index(drop=True)
existing_df['ID'] = existing_df['ID'].astype(int)
existing_df.to_csv(output_file, index=False, sep='|')
