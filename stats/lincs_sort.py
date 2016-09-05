import numpy as np

lincs = np.load('../data/final_data/flat_lincs.npy')
threshold = 0.01

print "-------1"

lincs_sorted =  np.sort(lincs)

print "-------2"
print "lincs_sorted: ", lincs_sorted[0:40]

top_length = int(len(lincs) * threshold) + 1

print "-------3"
print "top_length: ", top_length

top_closest_lincs = lincs_sorted[0:top_length]

print "-------4"
print "top_closest_lincs start: ", top_closest_lincs[0:40]
print "top_closest_lincs end: ", top_closest_lincs[(len(top_closest_lincs) - 40):len(top_closest_lincs)]

np.save('../data/stats/sorted_lincs.npy', lincs_sorted)
np.save('../data/stats/top_closest_lincs.npy', top_closest_lincs)