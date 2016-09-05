import pandas as pd

sm = pd.read_csv('../data/initial_data/meta_SMILES.csv')
sm.head()
pd.options.display.max_colwidth = 400
print sm[sm['pert_id']=='BRD-K18076490']['SMILES']
