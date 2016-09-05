import numpy as np
import matplotlib.pyplot as plt

pvalues = np.load('../../data/final_data/lincs_pvalues.npy')

test = pvalues[:1, :]

p_shape = pvalues.shape

print "------------"

small = pvalues[pvalues <= 0.01]

# print "shape:", small.shape

print "len(small)", len(small)
print "p_shape[0]", p_shape[0]
print "p_shape[1]", p_shape[1]

print float(len(small))/(p_shape[0]*p_shape[1])

test = test.flatten()

plt.hist(test, bins=100)
plt.title("P-values of lincs correlation")
plt.savefig('foo.png')

# plt.plot(tanimoto[:1000], lincs[:1000], 'r.')


# hist(test)