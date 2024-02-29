import os
import pandas as pd

script_directory = os.path.dirname(os.path.realpath(__file__))

mitre_df = pd.read_csv(os.path.join(script_directory, '../../CSV/Groupes/Donnees_Groupes/MitreAttack.csv'), delimiter='|')
ransomfeed_df = pd.read_csv(os.path.join(script_directory, '../../CSV/Groupes/Donnees_Groupes/Ransomfeed.csv'), delimiter='|')
ransomdb_df = pd.read_csv(os.path.join(script_directory, '../../CSV/Groupes/Donnees_Groupes/Ransomdb.csv'), delimiter='|')
ransomwarelive_df = pd.read_csv(os.path.join(script_directory, '../../CSV/Groupes/Donnees_Groupes/Ransomwarelive.csv'), delimiter='|')

mitre_df['Name'] = mitre_df['Name'].str.lower()
ransomfeed_df['name'] = ransomfeed_df['name'].str.lower()
ransomdb_df['Group Name'] = ransomdb_df['Group Name'].str.lower()
ransomwarelive_df['name'] = ransomwarelive_df['name'].str.lower()

mitre_names = set(mitre_df['Name'].tolist())
ransomfeed_names = set(ransomfeed_df['name'].tolist())
ransomdb_names = set(ransomdb_df['Group Name'].tolist())
ransomwarelive_names = set(ransomwarelive_df['name'].tolist())

all_group_names = sorted(mitre_names.union(ransomfeed_names, ransomdb_names, ransomwarelive_names))

bdd_df = pd.DataFrame(columns=['ID', 'Name', 'Status', 'Last Attack', 'Description', 'Sources'])

bdd_df['Name'] = all_group_names
bdd_df['ID'] = range(1, len(all_group_names) + 1)

Status_list = []
last_attack_list = []
description_list = []
sources_list = []

for group_name in bdd_df['Name']:
    if group_name in ransomwarelive_names:
        row = ransomwarelive_df[ransomwarelive_df['name'] == group_name].iloc[0]
        Status_list.append('Active' if row['available'] else 'Inactive')
    elif group_name in ransomdb_names:
        row = ransomdb_df[ransomdb_df['Group Name'] == group_name].iloc[0]
        if row['Last Seen'] == 'online':
            Status_list.append('Active')
        elif row['Last Seen'] == 'offline':
            Status_list.append('Inactive')
        else:
            Status_list.append('Indetermined')
    else:
        Status_list.append('Indetermined')

    if group_name in ransomfeed_names:
        row = ransomfeed_df[ransomfeed_df['name'] == group_name].iloc[0]
        last_attack_list.append(row.get('lastscrape', 'unknowned'))
    elif group_name in ransomwarelive_names:
        row = ransomwarelive_df[ransomwarelive_df['name'] == group_name].iloc[0]
        last_attack_list.append(row.get('lastscrape', 'unknowned'))
    elif group_name in ransomdb_names:
        row = ransomdb_df[ransomdb_df['Group Name'] == group_name].iloc[0]
        last_attack_list.append(row.get('Last Incident \\ Victim', 'unknowned'))
    else:
        last_attack_list.append('unknowned')

    mitre_description = mitre_df[mitre_df['Name'] == group_name]['Description'].tolist()
    ransomdb_description = ransomdb_df[ransomdb_df['Group Name'] == group_name]['Vraie_Description'].tolist()

    if mitre_description:
        description_list.append(mitre_description[0])
    elif ransomdb_description:
        description_list.append(ransomdb_description[0])
    else:
        description_list.append('not provided')

    if group_name in ['arvin_club', 'arvinclub', 'avoslocker']:
        row = bdd_df[bdd_df['Name'] == group_name].iloc[0]
        sources_list.append(row['Sources'])
    elif group_name in ransomwarelive_names:
        row = ransomwarelive_df[ransomwarelive_df['name'] == group_name].iloc[0]
        fqdn = row.get('fqdn', 'not provided')
        slug = row.get('slug', 'not provided')
        profile = row.get('profile', 'not provided')
        sources_list.append(f"{fqdn};{slug};{profile}")
    elif group_name in ransomdb_names:
        row = ransomdb_df[ransomdb_df['Group Name'] == group_name].iloc[0]
        fqdn = row.get('fqdn', 'not provided')
        slug = row.get('slug', 'not provided')
        profile = row.get('profile', 'not provided')
        sources_list.append(f"{fqdn};{slug};{profile}")
    else:
        sources_list.append('not provided')

bdd_df['Status'] = Status_list
bdd_df['Last Attack'] = last_attack_list
bdd_df['Description'] = description_list
bdd_df['Sources'] = sources_list
bdd_df['First Letter'] = bdd_df['Name'].str[0].str.lower()
bdd_df = bdd_df.sort_values(by=['First Letter', 'Name'], key=lambda x: x.str.lower())
bdd_df = bdd_df.drop(columns=['First Letter'])

combined_names = {'arvin_club': 'arvinclub', 'avoslocker': 'avos_locker'}
bdd_df['Name'] = bdd_df['Name'].replace(combined_names)
bdd_df['Name'] = bdd_df['Name'].replace({'avos_locker': 'avoslocker'})
bdd_df['Name'] = bdd_df['Name'].replace({'avos locker': 'avoslocker'})
bdd_df['Name'] = bdd_df['Name'].replace({'mount-locker': 'mount locker'})
bdd_df['Name'] = bdd_df['Name'].replace({'n3tworm': 'n3tw0rm'})
bdd_df['Name'] = bdd_df['Name'].replace({'payload.bin': 'payloadbin'})
bdd_df['Name'] = bdd_df['Name'].replace({'pysa (mespinoza)': 'pysa'})
bdd_df['Name'] = bdd_df['Name'].replace({'ragnar locker': 'ragnarlocker'})
bdd_df['Name'] = bdd_df['Name'].replace({'red alert': 'redalert'})
bdd_df['Name'] = bdd_df['Name'].replace({'revil sodinokibi': 'revil'})
bdd_df['Name'] = bdd_df['Name'].replace({'vice society': 'vicesociety'})
bdd_df['Name'] = bdd_df['Name'].replace({'xing locker': 'xinglocker'})

bdd_df.drop_duplicates(subset='Name', inplace=True)

csv_path = os.path.join(script_directory, '../../CSV/Groupes/Base_Groupes/Groupes.csv')
bdd_df.to_csv(csv_path, index=False, sep='|')