import pandas as pd
import numpy as np

fingerprints = np.load('../data/between_data/MACCS_fingerprints_boolean.npy')
fp_test = fingerprints[0:1000]
active_fp = fingerprints
fp_size = len(active_fp)

zero_drugs = np.array([], dtype=int)

for index, fp in enumerate(active_fp):
  if np.sum(fp) == 0:
    zero_drugs = np.append(zero_drugs, [index], 0)
    print "index:", index
    # print "fp:", fp

# np.savetxt('ZERO_fingerprints.csv', zero_drugs, delimiter=",")

print "Total zero drugs: ", len(zero_drugs)
print "Total zero drugs: ", zero_drugs

np.save('../data/between_data/zero_fingerprints_drugs.npy', zero_drugs)