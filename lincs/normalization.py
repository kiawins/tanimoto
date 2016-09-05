import numpy as np
import pandas as pd

data = np.load('euclidean_distance_results.npy')
actual_data = data[:43525]
print actual_data.shape


rows_max = actual_data.max(axis=1)
maximum = rows_max.max(axis=0)
print "maximum", maximum

norm_data = actual_data / maximum
print norm_data.shape
print norm_data

# np.save('normalized_distance.npy', norm_data)
