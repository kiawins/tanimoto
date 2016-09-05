import pandas as pd
import numpy as np

fp = np.load('MACCS_fingerprints_boolean.npy')
fp_test = fp[0:1000]
active_fp = fp_test
chunk_size = 100
fp_size = len(active_fp)

def tanimoto_bool(vector1, vector2):
  one_or_another = np.sum(np.logical_or(vector1, vector2))
  both = np.sum(np.logical_and(vector1, vector2))
  if one_or_another == 0:
    return 0
  return float(both)/one_or_another

iteration_array = np.arange(fp_size/chunk_size)
result = np.ndarray(shape=(chunk_size, fp_size))

for chunk_index in iteration_array:
  result.fill(0)

  for index1, drug1 in enumerate(active_fp[chunk_index*chunk_size : (chunk_index + 1)*chunk_size]):
    real_index1 = chunk_index*chunk_size + index1
    for index2, drug2 in enumerate(active_fp[(real_index1 + 1):]):
      real_index2 = index2 + real_index1 + 1
      result[index1, real_index2] = tanimoto_bool(drug1, drug2)

  np.save('tanimoto_results' + '_' + str(chunk_index) + '.npy', result)
  np.savetxt('tanimoto_results' + '_' + str(chunk_index) + '.csv', result, delimiter=",")
