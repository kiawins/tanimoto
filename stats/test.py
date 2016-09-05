import pandas as pd
import numpy as np

tanimoto = np.load('../data/final_data/flat_tanimoto.npy')
lincs = np.load('../data/final_data/flat_lincs.npy')
print "Just lincs: ", lincs[:100]
print "Lincs 23: ", lincs[23]
print "Type lincs: ", type(lincs[3])
print "-----------"

data = pd.DataFrame({'tanimoto': tanimoto, 'lincs': lincs}, dtype='float64')

print "DATA: ", data.head()
print "data['lincs']: ", data['lincs'][23]
print "type(data['lincs']): ", type(data['lincs'][23])
print "-----------"

def get_interval(min, max):
  mask = (data['tanimoto'] >= min) & (data['tanimoto'] < max)
  result = data.loc[mask]
  print "result['lincs'][54]: ", result['lincs'][:55]
  print "type(result['lincs'][54]: ", type(result['lincs'][54])
  print result.head()

  # result.to_csv('../data/stats/between' + str(min) + '_' + str(max) + '.csv')
  return result

get_interval(0.85,0.90)

lincs_85_90 = pd.read_csv('../data/stats/between0.85_0.9.csv', index_col=0)
print "lincs_85_90: ", lincs_85_90.head()


########################

import numpy as np
import pandas as pd

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
print "Less then max_distance size: ",  len(lincs_distance[ lincs_distance < max_distance])

print "-----------"


# standartized = (lincs_distance - mean)/std

# print "len(standartized)", len(standartized)

# np.save('../data/stats/flat_lincs_standartized.npy', standartized)


standartized_distance = np.load('../data/stats/flat_lincs_standartized.npy')

# plt.hist(standartized_distance, bins=100)
# plt.title("Lincs euclidean distance standartized")
# plt.savefig('euclidean_distance_standartized_hist.png')

print "-----------"

std = np.std(standartized_distance)
mean = np.mean(standartized_distance)
median = np.median(standartized_distance)

print "std: ", std
print "mean: ", mean
print "median: ", median

z = - 2.5758

distance_point_1 = z * std + mean
distance_point_2 = - z * std + mean

print "distance_point_1", distance_point_1
print "distance_point_2", distance_point_2

print "-----------"
print "Less then distance_point_1 size: ",  len(standartized_distance[ standartized_distance <= distance_point_1])
print "Less then distance_point_1: ",  len(standartized_distance[ standartized_distance <= distance_point_1])/float(size)
print "Less then distance_point_2: ",  len(standartized_distance[ standartized_distance <= distance_point_2])/float(size)

print "-----------"
print "Less then distance_point_2: ",  len(standartized_distance[ standartized_distance <= -2.33])/float(size)

# RESULT:
# Size: 413715600
# -----------
# 1.0
# 4.12246949233e-15
# distance_point_1 -2.5758
# distance_point_2 2.5758
# -----------
# Less then distance_point_1 size:  20832
# Less then distance_point_1:  5.03534311977e-05
# Less then distance_point_2:  0.991507165792
# -----------
# Less then distance_point_2:  9.74824251249e-05