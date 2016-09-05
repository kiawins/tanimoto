import pandas as pd
import numpy as np

files = []

for i in range(0, 21):
  file = pd.read_csv('../data/ECFP/chunks/ecfp/ecfp_' + str(i) + '.csv', index_col=0, header=None)
  print "file shape: ", file.shape
  files.append(file)

result = pd.concat(files)
print type(result)
print result.head()
print result.shape

print "------------"
print result.index


print "------------"

drugs_map = pd.read_csv('../data/ECFP/lincs_smiles_merge_clean.csv', index_col=0)
print drugs_map.shape

just_drugs_names = drugs_map['pert_id']
print "just_drugs_names", just_drugs_names[:10]
print type(just_drugs_names)
print len(just_drugs_names)

print "------------"

result.set_index(just_drugs_names, inplace=True)

print result.head()
print result.shape

result.to_csv('../data/ECFP/ecfps.csv')