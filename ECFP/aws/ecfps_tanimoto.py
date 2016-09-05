import numpy as np
import datetime

print "Start time:", datetime.datetime.now()
ecfp = np.load('data/ecfps_bool_matrix.npy')
ecfp_size = len(ecfp)

def tanimoto_bool(vector1, vector2):
  one_or_another = np.sum(np.logical_or(vector1, vector2))
  both = np.sum(np.logical_and(vector1, vector2))
  if one_or_another == 0:
    return 0
  return float(both)/one_or_another

result = np.ndarray(shape=(ecfp_size, ecfp_size))
result.fill(0)

for index1, drug1 in enumerate(ecfp):
  print index1
  for index2, drug2 in enumerate(ecfp[(index1 + 1):]):
    real_index2 = index2 + index1 + 1
    result[index1, real_index2] = tanimoto_bool(drug1, drug2)

np.save('data/ecfp_tanimoto.npy', result)
print "Finish time:", datetime.datetime.now()
