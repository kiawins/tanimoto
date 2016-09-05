import pandas as pd
import numpy as np

tanimoto = np.load('../data/final_data/flat_tanimoto.npy')
lincs = np.load('../data/final_data/flat_lincs.npy')

data = pd.DataFrame({'tanimoto': tanimoto, 'lincs': lincs})
# data = pd.DataFrame({'tanimoto': [1,2,3,4,5,6], 'lincs': [1,2,3,4,5,6]})

print "shape: ", data.shape

# mask = (data['tanimoto'] >= 2) & (data['tanimoto'] < 6)
# print data.loc[mask]

def get_interval(min, max):
  mask = (data['tanimoto'] >= min) & (data['tanimoto'] < max)
  result = data.loc[mask]
  print 'size', str(min), '-', str(max), ': ', result.shape
  result.to_csv('../data/stats/between' + str(min) + '_' + str(max) + '.csv')
  return data.loc[mask]

get_interval(0.95,1)
get_interval(0.90,0.95)
get_interval(0.85,0.90)
get_interval(0.85,1)
