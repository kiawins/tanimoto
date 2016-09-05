import numpy as np
import pandas as pd

#calculation of max distance for p-value < 0.01%

lincs_distance = np.load('../data/final_data/flat_lincs.npy')
size = len(lincs_distance)
print "Size:", size

std = np.std(lincs_distance)
mean = np.mean(lincs_distance)

print std
print mean

z = -2.5758 #from z-score table

max_distance = z * std + mean #max distance for pvalue < 0.01%

print "max_distance", max_distance
total_similar_lincs_pairs = len(lincs_distance[ lincs_distance < max_distance])
print "Less then max_distance size: ",  total_similar_lincs_pairs

print "-----------"

tanimoto = np.load('../data/final_data/flat_tanimoto.npy')
lincs = np.load('../data/final_data/flat_lincs.npy')

data = pd.DataFrame({'tanimoto': tanimoto, 'lincs': lincs})

###############

mask = (data['lincs'] < max_distance)
data_with_similar_lincs = data.loc[mask]

print "data_with_similar_lincs: ", len(data_with_similar_lincs)
print "------------"

t_mask = (data_with_similar_lincs['tanimoto'] > 0.85)
final_data = data_with_similar_lincs.loc[t_mask]

print "final data: ", len(final_data)
print "result: ", float(len(final_data))/total_similar_lincs_pairs

print final_data

final_data.to_csv('../data/stats/20832_lincs_tanimoto_more_085')


###########
#data_with_similar_lincs:  20832

# final data:  152
# result:  0.00729646697389