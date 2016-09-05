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

###############

print "Data shape: ", data.shape

mask = (data['lincs'] < max_distance)
data_with_similar_lincs = data.loc[mask]

print "data_with_similar_lincs: ", len(data_with_similar_lincs)
print "------------"

t_mask = (data_with_similar_lincs['tanimoto'] > 0.85)
final_data = data_with_similar_lincs.loc[t_mask]

print "final data: ", len(final_data)
print "result: ", float(len(final_data))/total_similar_lincs_pairs

print final_data

final_data.to_csv('../data/stats/top_lincs_tanimoto_more_085')


###########