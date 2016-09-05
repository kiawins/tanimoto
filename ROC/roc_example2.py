import numpy as np
from sklearn.metrics import roc_curve, auc

# y = np.array([1, 1, 2, 2])
y = np.array([False, False, True, True])
# y = np.array([1, 2, 4, True])
scores = np.array([0.1, 0.4, 0.35, 0.8])
fpr, tpr, thresholds = roc_curve(y, scores)
roc_auc = auc(fpr, tpr)


print "fpr: ", fpr
print "tpr: ", tpr
print "thresholds: ", thresholds
print "roc_auc: ", roc_auc


# fpr
# array([ 0. ,  0.5,  0.5,  1. ])
# tpr
# array([ 0.5,  0.5,  1. ,  1. ])
# thresholds
# array([ 0.8 ,  0.4 ,  0.35,  0.1 ])