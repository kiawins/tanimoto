import numpy as np
import scipy
from scipy.stats import spearmanr
import sklearn
from sklearn.metrics import pairwise

lincs_array = np.load('../data/lincs_correlation/lincs_array_selected_drugs.npy')
ecfp = np.load('../data/ecfp/ecfps_bool_matrix.npy')
lincs_array = lincs_array[:100,:]

def inner_loop_calc(drug1, drug2):
  return spearmanr(drug1, drug2)[1]

dist = sklearn.metrics.pairwise.pairwise_distances(ecfp, Y=None, metric=inner_loop_calc, n_jobs=8)
# print dist[:5, :]

