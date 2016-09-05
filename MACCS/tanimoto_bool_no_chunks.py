import pandas as pd
import numpy as np

fp = np.load('MACCS_fingerprints_boolean.npy')
# fp_test = fp[0:1000]
# active_fp = fp_test
active_fp = fp
fp_size = len(active_fp)

def tanimoto_bool(vector1, vector2):
  one_or_another = np.sum(np.logical_or(vector1, vector2))
  both = np.sum(np.logical_and(vector1, vector2))
  if one_or_another == 0:
    return 0
  return float(both)/one_or_another

result = np.ndarray(shape=(fp_size, fp_size))
result.fill(0)

for index1, drug1 in enumerate(active_fp):
  print index1
  if index1 % 3000 == 0:
    np.save('tanimoto_results.npy', result)
  for index2, drug2 in enumerate(active_fp[(index1 + 1):]):
    real_index2 = index2 + index1 + 1
    result[index1, real_index2] = tanimoto_bool(drug1, drug2)

np.save('tanimoto_results_final.npy', result)
np.savetxt('tanimoto_results_final.csv', result, delimiter=",")