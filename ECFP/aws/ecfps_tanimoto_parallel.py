import numpy as np
import datetime
import sklearn
from sklearn.metrics import pairwise

print "Start time:", datetime.datetime.now()
ecfp = np.load('../data/ECFP/ecfps_bool_matrix.npy')
ecfp = ecfp[:100, :]
ecfp_size = len(ecfp)

def tanimoto_bool(vector1, vector2):
  one_or_another = np.sum(np.logical_or(vector1, vector2))
  both = np.sum(np.logical_and(vector1, vector2))
  if one_or_another == 0:
    return 0
  return float(both)/one_or_another

result = pairwise.pairwise_distances(ecfp, Y=None, metric=tanimoto_bool, n_jobs=4)

ones = np.identity(len(result))
result = result - ones

print result
print len(result)
np.save('ecfp_tanimoto.npy', result)

print "Finish time:", datetime.datetime.now()
