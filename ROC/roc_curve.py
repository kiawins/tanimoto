import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

fpr = np.load('../data/roc/fpr.npy')
tpr = np.load('../data/roc/tpr.npy')
thresholds = np.load('../data/roc/thresholds.npy')
tanimoto_threshhold = 0.85

# mask = (tanimoto > tanimoto_threshhold)
# fpr, tpr, thresholds = roc_curve(mask, lincs)

roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, label='ROC curve (area = %auc)' % roc_auc)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Tanimoto coefficient > %number' % tanimoto_threshhold)
plt.legend(loc="lower right")

plt.savefig('roc_curve.png')

