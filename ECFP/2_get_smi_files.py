import pandas as pd
import numpy as np

data = pd.read_csv('../data/ECFP/lincs_smiles_merge_clean.csv', index_col=0)
print data.shape

smiles = np.array(data['SMILES'])
print len(smiles)
chunks = np.array_split(smiles, 21)
print len(chunks)
print len(chunks[0])

for i in range(0, (len(chunks))):
  print i
  np.savetxt('../data/ECFP/chunks/smiles' + str(i) + '.smi', chunks[i], fmt="%s", newline='\n')
