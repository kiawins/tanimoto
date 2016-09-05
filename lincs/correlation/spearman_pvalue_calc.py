import numpy as np
import pandas as pd
import scipy
from scipy.stats import spearmanr
from joblib import Parallel, delayed
from joblib.pool import has_shareable_memory
from joblib import load, dump

lincs_array = np.load('../../data/lincs_correlation/lincs_array_selected_drugs.npy')
lincs_array = lincs_array[:5,:]

print len(lincs_array)

def crete_matrix_of_zeros(size):
  matrix = np.ndarray(shape=(size, size), dtype='float64')
  matrix.fill(0)
  return matrix

correlation = crete_matrix_of_zeros(len(lincs_array))
pvalue = crete_matrix_of_zeros(len(lincs_array))

def inner_loop_calc(index1, drug1, index2, drug2):
  # a, b = spearmanr(drug1, drug2)
  # print type(a), "a: ", a
  # print type(a), "b: ", b
  real_index2 = index1 + index2 + 1
  # correlation[index1, real_index2], pvalue[index1, real_index2] = spearmanr(drug1, drug2)
  correlation[index1, real_index2] = 2*3
  pvalue[index1, real_index2] = 1*4

x = [1,2,3]

def by_2(x):
  return x*2


Parallel(n_jobs=7)(delayed(by_2)(i)
  for i in x:


# for index1, drug1 in enumerate(lincs_array):
#   print index1

#   Parallel(n_jobs=7)(delayed(inner_loop_calc)(index1, drug1, index2, drug2)
#     for index2, drug2 in enumerate(lincs_array[(index1 + 1):,:]))

  # for index2, drug2 in enumerate(lincs_array[(index1 + 1):,:]):
  #   inner_loop_calc(index1, drug1, index2, drug2)

print "correlation: ", correlation
print "pvalue: ", pvalue

print type(correlation)
print type(correlation[0,0])


# np.save('../../data/lincs_correlation/correlation_matrix.npy', correlation)
# np.save('../../data/lincs_correlation/pvalue_matrix.npy', pvalue)
