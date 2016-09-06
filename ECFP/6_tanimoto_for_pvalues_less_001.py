import numpy as np
import pandas as pd

#calculation of max distance for p-value < 0.01%

lincs = np.load('../data/ECFP/lincs_distances_for_smiles.npy')
lincs = lincs.flatten()
print "len(lincs)", len(lincs)

std = np.std(lincs)
print "std:", std
mean = np.mean(lincs)
print "mean:", mean

z = -2.5758 #from z-score table

max_distance = z * std + mean #max distance for pvalue < 0.01%

print "max_distance", max_distance
total_similar_lincs_pairs = len(lincs[ lincs < max_distance])
print "Less then max_distance size: ",  total_similar_lincs_pairs

print "-----------"

ecfps = np.load('../data/ECFP/ecfps_tanimoto.npy')
ecfps = ecfps.flatten()

data = pd.DataFrame({'ecfps': ecfps, 'lincs': lincs})

###############

mask = (data['lincs'] < max_distance)
data_with_similar_lincs = data.loc[mask]

print "data_with_similar_lincs: ", len(data_with_similar_lincs)
print "------------"

t_mask = (data_with_similar_lincs['ecfps'] > 0.85)
final_data = data_with_similar_lincs.loc[t_mask]

print "final data: ", len(final_data)
print "result: ", float(len(final_data))/total_similar_lincs_pairs

print final_data

###########
# data_with_similar_lincs:  20832
# ------------
# final data:  26
# result:  0.00124807987711
#
#              ecfps     lincs
# 1079417    1.00000  0.059574
# 4495634    0.85389  0.064033
# 5594960    1.00000  0.072207
# 10048181   0.85389  0.064033
# 28415033   1.00000  0.059574
# 29696675   1.00000  0.072207
# 36125729   1.00000  0.075488
# 38424036   1.00000  0.075488
# 39564031   1.00000  0.076086
# 44262676   1.00000  0.066431
# 55550485   1.00000  0.076086
# 57686416   1.00000  0.066431
# 58195902   1.00000  0.049927
# 64317941   1.00000  0.049927
# 137412757  1.00000  0.075463
# 141295295  1.00000  0.069782
# 225422542  1.00000  0.071278
# 258984344  1.00000  0.065005
# 277749646  1.00000  0.069782
# 298236162  1.00000  0.071278
# 314550492  1.00000  0.065005
# 315061867  1.00000  0.076981
# 317461869  1.00000  0.076981
# 326606135  1.00000  0.075463
# 385869772  1.00000  0.045061
# 406249450  1.00000  0.045061