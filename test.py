import pandas as pd
import numpy as np


fp_0 = np.load('tanimoto_results_0.npy')
fp_1 = np.load('tanimoto_results_1.npy')
fp_2 = np.load('tanimoto_results_2.npy')
fp_3 = np.load('tanimoto_results_3.npy')
fp_4 = np.load('tanimoto_results_4.npy')

for string in fp_1:
  print sum(string)

# print "len fp_00: ", len(fp_0[0])
# print "len fp_0: ", len(fp_0)
# print "fp_0: ", fp_0
# print "len fp_1: ", len(fp_1)
# print "fp_1: ", fp_1
# print "len fp_2: ", len(fp_2)
# print "fp_2: ", fp_2
# print "len fp_3: ", len(fp_3)
# print "fp_3: ", fp_3
# print "len fp_4: ", len(fp_4)
# print "fp_4: ", fp_4