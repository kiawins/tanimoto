import pandas as pd
import numpy as np

lincs_85_90 = pd.read_csv('../data/stats/between0.85_0.9.csv', index_col=0)
top_lincs = np.load('../data/stats/top_closest_lincs.npy')
lincs = np.load('../data/final_data/flat_lincs.npy')
print "Just lincs: ", lincs[:10]

lincs_85_90_array = np.array(lincs_85_90['lincs'], dtype=pd.Series)

print lincs_85_90_array[:10]
print top_lincs[(len(top_lincs) - 100):len(top_lincs)]

overlap = np.intersect1d(lincs_85_90_array, top_lincs)

print "overlap length:", len(overlap)
print "YO: ", len(overlap)/len(lincs_85_90)

np.save('../data/stats/85_90_overlap.npy', overlap)


