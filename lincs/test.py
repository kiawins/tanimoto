import numpy as np
from scipy.spatial.distance import euclidean

a = {'a': [1], 'b': [3]}
print a['b']

if 'a' in a:
  a['a'] = np.append(a['a'], [2], 0)

print a
print type(a['a'])
print type(a['b'])