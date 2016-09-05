import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

tanimoto = np.load('/data/flat_tanimoto.npy')
lincs = np.load('/data/flat_lincs.npy')

mask = (tanimoto > 0.85)

fpr, tpr, thresholds = roc_curve(mask, lincs)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, label='ROC curve (area = %auc)' % roc_auc)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Tanimoto coefficient > 0.85')
plt.legend(loc="lower right")

plt.savefig('roc_curve.png')

