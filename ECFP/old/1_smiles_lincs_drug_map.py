import numpy as np
import pandas as pd

lincs = pd.read_csv('../data/initial_data/lincs_embedding.csv', header=None)
lincs_drugs = lincs[0]
print lincs_drugs[:10]
print len(lincs_drugs)
print type(lincs_drugs)
print "-----------"

smiles = pd.read_csv('../data/initial_data/meta_SMILES.csv')
print len(smiles)
print type(smiles)
print smiles.loc[41725:]
print "------------"

smiles['SMILES'].replace('', np.nan, inplace=True)
smiles.dropna(subset=['SMILES'], inplace=True)
print len(smiles)
print smiles.loc[41725:]
smiles.to_csv('../data/ECFP/meta_SMILES_clean_data.csv')

print "------------"
clean_smiles = pd.read_csv('../data/ECFP/meta_SMILES_clean_data.csv')
print len(clean_smiles)
print type(clean_smiles)
# print len(smiles_drugs)
print clean_smiles.loc[41725:]
smiles_drugs = clean_smiles['pert_id']
print "-----------"

overlap = np.intersect1d(lincs_drugs, smiles_drugs)
fake_smiles = 0

print overlap
print "Overlap length:", len(overlap)

map = dict()

print "-----------LOOP"

for drug in overlap:
  smiles_index = np.where(smiles['pert_id']==drug)[0]
  lincs_index = np.where(lincs[0]==drug)[0]

  if smiles.iloc[smiles_index]['SMILES'].values[0] != '-666':
    map[drug] = np.array([lincs_index, smiles_index]).flatten()
  else:
    fake_smiles = fake_smiles + 1

print "Fake smiles: ", fake_smiles

print "Final map length:", len(map)
print "-----------"

result = pd.DataFrame(map, index=['lincs', 'smiles'])
print "Index values: ", result.index
print "Columns: ", result.columns
print result.shape
print result.head()
print result.tail()
print smiles.tail()

# # result.to_csv('../data/ECFP/lincs_smiles_drugs_map.csv')