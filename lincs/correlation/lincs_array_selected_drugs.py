import numpy as np
import pandas as pd

lincs = pd.read_csv('../../data/lincs_correlation/lincs_embedding_selected_drugs.csv')
print lincs.head()

print "++++++++++"
lincs_array = lincs.iloc[:, 2:]
# lincs_array.to_csv('../../data/lincs_correlation/lincs_array_selected_drugs.csv')
print lincs_array.head()

print "%%%%%%%%%%%%%%%%%%%%%%"

lincs_array22 = np.load('../../data/lincs_correlation/lincs_array_selected_drugs.npy')

print lincs_array22.shape
print lincs_array22[0, 0]
print type(lincs_array22[0, 0])

print "----------"
# np.save('../../data/lincs_correlation/lincs_array_selected_drugs.npy', lincs_array)

lincs_array11 = np.memmap('../../data/lincs_correlation/lincs_array_selected_drugs.npy', mode='r', shape=(20340,32), dtype=np.float64)

print lincs_array11.shape
print lincs_array11[0, 0]
print type(lincs_array11)



# correlation = np.ndarray(shape=(len(lincs_array), len(lincs_array)))
# correlation.fill(0)

# pvalue = np.ndarray(shape=(len(lincs_array), len(lincs_array)))
# pvalue.fill(0)