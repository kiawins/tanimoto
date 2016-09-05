import numpy as np
import pandas as pd

lincs = pd.read_csv('../data/initial_data/lincs_embedding.csv', header=None)
lincs_drugs = lincs[0].as_matrix()
print "len(lincs_drugs)", len(lincs_drugs)
# print lincs_drugs

lincs_with_smiles = pd.read_csv('../data/ECFP/lincs_smiles_merge_clean.csv', index_col=0)
smiles_drugs = lincs_with_smiles['pert_id'].as_matrix()
print "len(smiles_drugs)", len(smiles_drugs)
# print smiles_drugs

mask = np.in1d(lincs_drugs, smiles_drugs)
# print mask
print "len(mask)", len(mask)
print "sum(mask)", sum(mask)

print "-------"
indices = np.arange(lincs_drugs.shape[0])[mask]
print "len(indices)", len(indices)
# print indices

print "---------"
distances = np.load('../data/final_data/normalized_distance.npy')
print distances.shape

distances_for_smiles = distances[indices, :][:, indices]
print distances_for_smiles.shape

np.save('../data/ecfp/lincs_distances_for_smiles.npy', distances_for_smiles)