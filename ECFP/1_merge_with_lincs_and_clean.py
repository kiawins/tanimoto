import pandas as pd

lincs = pd.read_csv('../data/initial_data/lincs_embedding.csv', header=None)
header = ['pert_id']
header.extend(range(1,33))
lincs.columns = header
print "LINKS:", lincs.shape

smiles = pd.read_csv('../data/initial_data/meta_SMILES.csv')
print "SMILES:", smiles.shape

result = pd.merge(lincs, smiles, on='pert_id')
print "result:", result.shape

result = result[result.SMILES != '-666']
print "After deleting 666", result.shape

result['SMILES'].replace('', np.nan, inplace=True)
result.dropna(subset=['SMILES'], inplace=True)
print "After deleting empty", result.shape

result.to_csv('../data/ecfp/lincs_smiles_merge_clean.csv')
