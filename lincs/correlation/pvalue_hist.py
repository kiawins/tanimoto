import numpy as np
import matplotlib.pyplot as plt

lincs_pvalues = np.load('../data/final_data/lincs_pvalue.npy')
size = len(lincs_pvalues)
print "Size:", size

std = np.std(lincs_pvalues)
mean = np.mean(lincs_pvalues)

# print std
# print mean

# z = - 2.5758

# distance_point_1 = z * std + mean
# distance_point_2 = - z * std + mean

# print "distance_point_1", distance_point_1
# print "distance_point_2", distance_point_2

# print "-----------"
# print "Less then distance_point_1 size: ",  len(lincs_pvalues[ lincs_pvalues <= distance_point_1])
# print "Less then distance_point_1: ",  len(lincs_pvalues[ lincs_pvalues <= distance_point_1])/float(size)
# print "Less then distance_point_2: ",  len(lincs_pvalues[ lincs_pvalues <= distance_point_2])/float(size)

# standartized = (lincs_pvalues - mean)/std

# print "len(standartized)", len(standartized)

# np.save('../data/stats/flat_lincs_standartized.npy', standartized)

# print "-----------"