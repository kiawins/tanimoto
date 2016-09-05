import numpy as np
import pandas as pd

#calculation of max distance for p-value < 0.01%

top_lincs = np.load('../data/stats/top_closest_lincs.npy')
total_similar_lincs_pairs = len(top_lincs)
print "Top lincs size:", total_similar_lincs_pairs

max_distance = max(top_lincs)

print "max_distance", max_distance

print "-----------"

tanimoto = np.load('../data/final_data/flat_tanimoto.npy')
lincs = np.load('../data/final_data/flat_lincs.npy')

data = pd.DataFrame({'tanimoto': tanimoto, 'lincs': lincs})
print "Data shape: ", data.shape

###############

t_mask = (data['tanimoto'] > 0.85)
data_tanimoto_more_085 = data.loc[t_mask]

print "data_tanimoto_more_085: ", len(data_tanimoto_more_085)
print "------------"

l_mask = (data_tanimoto_more_085['lincs'] < max_distance)
final_data = data_tanimoto_more_085.loc[l_mask]

print "final data: ", len(final_data)
print "result: ", float(len(final_data))/len(data_tanimoto_more_085)

print final_data

final_data.to_csv('../data/stats/tanimoto_more_085_with_top_lincs.csv')

########
# Top lincs size: 4137157
# max_distance 0.179359280117
# -----------
# Data shape:  (413715600, 2)
# data_tanimoto_more_085:  4627240
# ------------
# final data:  212166
# result:  0.045851522722