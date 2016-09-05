import pandas as pd
import numpy as np

fp = np.load('MACCS_fingerprints.npy')

fp_boolean = np.array([fp[0]])
print "START: ", fp_boolean

for index, drug in enumerate(fp):
  print index
  fp_bool = drug == 1
  fp_boolean = np.append(fp_boolean, [fp_bool], 0)


result = fp_boolean[1:]
print "-------------"
print result
print "LENGTH:", len(result)

np.save('MACCS_fingerprints_boolean.npy', result)