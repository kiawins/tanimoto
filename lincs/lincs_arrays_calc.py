import pandas as pd
import numpy as np

data = pd.read_csv('lincs_embedding.txt', sep=",", header = None)
data_test = data[:1000]
actual_data = data.transpose()

#shape result array necessary length
result = np.array([actual_data[0][1:]])


for index in actual_data:
  if index % 100 == 0:
    print index
  linc = np.array(actual_data[index][1:])
  result = np.append(result, [linc], 0)


final_result = result[1:]
print "-------------"
print final_result[0]
print "LENGTH:", len(final_result[0])
print "LENGTH:", len(final_result)

np.save('lincs_array.npy', final_result)
