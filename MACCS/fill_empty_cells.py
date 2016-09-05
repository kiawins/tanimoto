import numpy as np
import pandas as pd

fp = np.load('../data/final_data/tanimoto_matrix.npy')
print "-----1"
fp_t = fp.transpose()
print "------2"

new_fp = fp + fp_t

print "------3"

np.save('../data/final_data/tanimoto_matrix_no_empty.npy', new_fp)