import pandas as pd
import numpy as np

fingerprints = pd.read_csv('/Users/cwins/Desktop/drugs_similarity/MACCS_bitmatrix.csv')
# fingerprints_test = fingerprints[:10]


fp_ts = fingerprints.transpose()
# fp_test_tp = fingerprints_test.transpose()

result = np.array([fp_ts[0][1:]])

for index in fp_ts:
  fp = np.array(fp_ts[index][1:])
  result = np.append(result, [fp], 0)


final_result = result[1:]
print "-------------"
print final_result
print "LENGTH:", len(final_result)

np.save('MACCS_fingerprints.npy', final_result)
