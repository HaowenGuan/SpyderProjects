#%%
import json
from collections import namedtuple

sheldon = []
leonard = []
with open('corpus.json', 'r') as f:
    corpus = json.load(f)
    for scene in corpus:
        dialogue = corpus[scene]
        dialogue = dialogue.replace('\t', '')
        dialogue = dialogue.split('\n')
        for line in dialogue:
            if line.startswith('Sheldon') and ':' in line:
                sheldon.append(line[line.index(':') + 2:])
            elif line.startswith('Leonard') and ':' in line:
                leonard.append(line[line.index(':') + 2:])
# %%
f = open('sheldon_full_text.txt', 'w')
f.write('\n'.join(sheldon))
f.close()
f = open('leonard_full_text.txt', 'w')
f.write('\n'.join(leonard))
f.close()
# %%
import pandas as pd

beauty_and_beast = pd.read_csv('https://raw.githubusercontent.com/idc9/stor390/master/data/beauty_clean_df.csv')

belle = []
beast = []
for i in range(1, len(beauty_and_beast)):
    row = beauty_and_beast.iloc[i]
    if row['person'] == 'BELLE':
        belle.append(row['line'])
    elif row['person'] == 'BEAST':
        beast.append(row['line'])
# %%
f = open('belle_test_text.txt', 'w')
f.write('\n'.join(belle))
f.close()
f = open('beast_test_text.txt', 'w')
f.write('\n'.join(beast))
f.close()
# %%
