import numpy as np
# from sklearn.metrics import roc_curve, auc
import dask.array as da

tanimoto = np.load('../data/final_data/flat_tanimoto.npy')
# print tanimoto[:10]

tanimoto1 = da.from_array(tanimoto, chunks = )

print "tanimoto1: ", tanimoto1[:10]