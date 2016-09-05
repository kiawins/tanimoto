import numpy as np
import scipy
from scipy.stats import spearmanr
import sklearn
from sklearn.metrics import pairwise
import datetime

print "Starting time: ", datetime.datetime.now()

lincs_array = np.load('../../data/lincs_correlation/lincs_array_selected_drugs.npy')
lincs_array = lincs_array[:1000,:]

def inner_loop_calc(drug1, drug2):
  return spearmanr(drug1, drug2)[0]

dist = sklearn.metrics.pairwise.pairwise_distances(lincs_array, Y=None, metric=inner_loop_calc, n_jobs=8)
print dist[:5, :]

print "Finish time before save: ", datetime.datetime.now()

# np.save('../../data/lincs_correlation/lincs_correlations.npy', dist)

print "Finish time after save: ", datetime.datetime.now()
