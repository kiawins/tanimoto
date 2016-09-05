import pandas as pd
import numpy as np


fp = np.load('MACCS_fingerprints.npy')
fp_test = fp[0:2]
active_fp = fp_test
fp_size = len(active_fp)

print len(fp)

def tanimoto(vector1, vector2):
  vector_sum = vector1 + vector2
  onlyOne = len(vector_sum[vector_sum == 1])
  both = len(vector_sum[vector_sum == 2])
  return float(both)/(onlyOne + both)

result = np.ndarray(shape=(fp_size, fp_size))
result.fill(0)

for index1, drug1 in enumerate(active_fp):
  for index2, drug2 in enumerate(active_fp[(index1+1):]):
    real_index2 = index2 + index1 + 1
    result[index1, real_index2] = tanimoto(drug1, drug2)
    print index1, ": ", real_index2

np.save('tanimoto_results.npy', result)
np.savetxt('tanimoto_results.txt', result)
np.savetxt('tanimoto_results.csv', result, delimiter=",")

print result