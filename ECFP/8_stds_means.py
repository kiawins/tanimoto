import numpy as np
import pandas as pd

lincs = np.load('data/lincs_distances_for_smiles.npy')
lincs = lincs.flatten()
print "------"

ecfps = np.load('data/ecfps_tanimoto.npy')
ecfps = ecfps.flatten()
print "------"

data = pd.DataFrame({'ecfps': ecfps, 'lincs': lincs})
print "Data shape: ", data.shape

stds = np.array([])
means = np.array([])

# for i in range(20):
for i in range(2):
  print i`
  bin_data = data[(data['lincs'] > i*0.05) & (data['lincs'] < (i+1)*0.05)]
  tanimoto = bin_data['ecfps'].as_matrix()
  print "amount of elements in the bean:", tanimoto.shape
  stds = np.append(stds, [np.std(tanimoto)])
  print stds
  means = np.append(means, [np.mean(tanimoto)])
  print means


print "stds:", stds
print "means:", means

# stds: [ 0.37631434  0.191768    0.12195956  0.0885928   0.06621736  0.05262721
#   0.04613396  0.04233338  0.03727536  0.03162098  0.02741907  0.02441929
#   0.02200673  0.02033171  0.01913399  0.01836025  0.01864422  0.0182641
#   0.01714756  0.01727871]
# means: [ 0.73390558  0.19152101  0.13318249  0.11124237  0.09846482  0.09051234
#   0.08492735  0.07843414  0.07062777  0.06522305  0.06246021  0.06105905
#   0.06028242  0.05988018  0.05977614  0.06021376  0.06130162  0.0612812
#   0.06056717  0.06040541]