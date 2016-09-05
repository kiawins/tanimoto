import numpy as np
import pandas as pd
import simplejson

lincs = pd.read_csv('../data/initial_data/lincs_embedding.csv')

drugs_names = lincs.ix[:, '56582'] #the name of the column with drugs
drugs_names.set_value(max(drugs_names.index) + 1,  '56582')
# drugs_names.append(pd.Series(['56582']))
# print drugs_names

# dict_file = open('../data/between_data/drugs_dict.json')
drugs_dict_tanimoto = simplejson.loads('../data/between_data/drugs_dict.json')

print drugs_dict_tanimoto

# drugs = dict()

# for index, drug in enumerate(drugs_names):
#   print index
#   print drug
#   drugs[drug] = [index]

# print drugs

# with open('drugs_dict.json', 'w') as f:
#   json.dump(drugs, f)