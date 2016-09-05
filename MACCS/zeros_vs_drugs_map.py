import numpy as np
import pandas as pd

zero_fingerprints_drugs = np.load('../data/between_data/zero_fingerprints_drugs.npy')
drugs_map = pd.read_csv('../data/final_data/drugs_map.csv', index_col=0)
# drugs_map = drugs_map.ix[:, :'BRD-A00546892']
print "length before: ", drugs_map.shape
# zero_fingerprints_drugs = np.append(zero_fingerprints_drugs, [3], 0)


match = 0

for item, column in enumerate(drugs_map):
  print item
  if drugs_map[column]['fingerprints'] in zero_fingerprints_drugs:
    del drugs_map[column]
    match = match + 1

drugs_map.to_csv('../data/final_data/drugs_map_no_zeros.csv')

print "Length after deletion:", drugs_map.shape
print "Match", match
