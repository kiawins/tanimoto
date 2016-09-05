import pandas as pd
import numpy as np
from scipy.spatial.distance import euclidean

data_save_interval = 4000
saved_lincs = data_save_interval * (-1)

data = np.load('lincs_array.npy')
# data_test = data[:1000]
actual_data = data
size = len(actual_data)

result = np.ndarray(shape=(data_save_interval, size))
result.fill(0)

for index1, drug1 in enumerate(actual_data):
  print index1

  if index1 % data_save_interval == 0:
    np.save('euclidean_distance_results_' + str(index1/data_save_interval) + '.npy', result)
    result.fill(0)

    saved_lincs = saved_lincs + data_save_interval

  index1_for_file = index1 - saved_lincs
  for index2, drug2 in enumerate(actual_data[(index1 + 1):]):
    real_index2 = index2 + index1 + 1
    result[index1_for_file, real_index2] = euclidean(drug1, drug2)

np.save('euclidean_distance_results_last.npy', result)
