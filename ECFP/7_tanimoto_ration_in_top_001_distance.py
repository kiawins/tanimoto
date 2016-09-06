import numpy as np
import pandas as pd

#calculation max for 1% top closest distances

lincs = np.load('../data/ECFP/lincs_distances_for_smiles.npy')
lincs = lincs.flatten()
lincs_sorted =  np.sort(lincs)
threshold = 0.01
top_length = int(len(lincs) * threshold) + 1

max_distance = lincs_sorted[top_length]

print "max_distance", max_distance
print "-----------"

ecfps = np.load('../data/ECFP/ecfps_tanimoto.npy')
ecfps = ecfps.flatten()

data = pd.DataFrame({'ecfps': ecfps, 'lincs': lincs})
print "Data shape: ", data.shape

###############

t_mask = (data['ecfps'] > 0.85)
data_tanimoto_more_085 = data.loc[t_mask]

print "data_tanimoto_more_085: ", len(data_tanimoto_more_085)
print "------------"

l_mask = (data_tanimoto_more_085['lincs'] < max_distance)
final_data = data_tanimoto_more_085.loc[l_mask]

print "final data: ", len(final_data)
print "result: ", float(len(final_data))/len(data_tanimoto_more_085)

print final_data

########
# max_distance 0.179359280117
# -----------
# Data shape:  (413715600, 2)
# data_tanimoto_more_085:  82762
# ------------
# final data:  16374
# result:  0.197844421353