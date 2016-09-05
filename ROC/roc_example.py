import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from scipy import interp

# Import some data to play with
iris = datasets.load_iris()
X = iris.data
y = iris.target

# print "X: ", X
# print y
# print len(y)

# print "---------"

# Binarize the output
y = label_binarize(y, classes=[0, 1, 2])
n_classes = y.shape[1]

# print y
# print len(y)
# print "n_classes", n_classes

# Add noisy features to make the problem harder
random_state = np.random.RandomState(0)
n_samples, n_features = X.shape
X = np.c_[X, random_state.randn(n_samples, 200 * n_features)]

# print "random_state: ", random_state
# print "n_samples: ", n_samples
# print "n_features: ", n_features

# print "--------"
# print X
# print X.shape

# shuffle and split training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5, random_state=0)

# print "X_train: ", X_train
# print "X_test: ", X_test
# print "y_train: ", y_train
# print "y_test: ", y_test

print "-----------"

# Learn to predict each class against the other
classifier = OneVsRestClassifier(svm.SVC(kernel='linear', probability=True, random_state=random_state))
y_score = classifier.fit(X_train, y_train).decision_function(X_test)

# print "classifier: ", classifier
# print "y_score: ", y_score

# Compute ROC curve and ROC area for each class
fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(n_classes):
    print "i: ", i
    print "y_test[:, i]: ", y_test[:, i]
    print "y_score[:, i]", y_score[:, i]
    fpr[i], tpr[i], _ = roc_curve(y_test[:, i], y_score[:, i])
    print "fpr[i]: ", fpr[i]
    print "tpr[i]", tpr[i]
    print "YO _", _
    roc_auc[i] = auc(fpr[i], tpr[i])
    # print "roc_auc[i]: ", roc_auc[i]

# print "roc_auc: ", roc_auc

# Compute micro-average ROC curve and ROC area
fpr["micro"], tpr["micro"], _ = roc_curve(y_test.ravel(), y_score.ravel())
roc_auc["micro"] = auc(fpr["micro"], tpr["micro"])

# print "roc_auc[micro]: ", roc_auc["micro"]


##############################################################################
# Plot of a ROC curve for a specific class
plt.figure()
plt.plot(fpr[2], tpr[2], label='ROC curve (area = %0.2f)' % roc_auc[2])
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
# plt.show()

plt.savefig('fig1.png')
