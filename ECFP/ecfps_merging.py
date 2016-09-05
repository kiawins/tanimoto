import pandas as pd
import numpy as np

files = []

for i in range(1, 17):
  file = pd.read_csv('../data/ECFP/fingerprints_results/ecfp_' + str(i) + '.csv', index_col=0, header=None)
  print "file shape: ", file.shape
  files.append(file)

result = pd.concat(files)
print type(result)
print result.head()
print result.shape

print "------------"
print result.index


print "------------"

drugs_map = pd.read_csv('../data/ECFP/lincs_smiles_drugs_map.csv', index_col=0)
drugs_map = drugs_map.iloc[:, :15973]

# print drugs_map.head()
print drugs_map.shape

just_drugs_names = drugs_map.columns.values
print just_drugs_names
print type(just_drugs_names)
print len(just_drugs_names)

print "------------"

result.set_index(just_drugs_names, inplace=True)

print result.head()

result.to_csv('../data/ECFP/final/ecfps.csv')