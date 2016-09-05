import numpy as np
import pandas as pd

lincs = pd.read_csv('../../data/initial_data/lincs_embedding.csv', header=None)
drugs_map = pd.read_csv('../../data/final_data/drugs_map.csv', index_col=0)
print "drugs_map shape", drugs_map.shape

print drugs_map.head()

drug_lincs = np.array(drugs_map.loc['lincs'], dtype=pd.Series)

lincs_embedding_selected_drugs = lincs.loc[drug_lincs]
print "lincs_embedding_selected_drugs", lincs_embedding_selected_drugs.shape

lincs_embedding_selected_drugs.to_csv('../../data/lincs_correlation/lincs_embedding_selected_drugs.csv')
print "drug_lincs", lincs_embedding_selected_drugs[:10]
