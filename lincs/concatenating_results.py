import pandas as pd
import numpy as np

lincs = np.load('lincs_array.npy')
size = len(lincs)
total_lincs = 0

result = np.ndarray(shape=(1, size))
result.fill(0)

print result
print result.shape

for i in range(1, 12):
  data = np.load('euclidean_distance_results_' + str(i) + '.npy')
  total_lincs = total_lincs + len(data)
  print "Lincs amount: ", total_lincs
  print "Data", data.shape
  print "Data", data
  result = np.concatenate((result, data), axis=0)
  print "Result", result.shape


final_result = result[1:]

print "Final result", final_result.shape
print "Final result", final_result
np.save('euclidean_distance_results.npy', final_result)
np.savetxt('euclidean_distance_results.csv', final_result, delimiter=",")
