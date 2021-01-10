# local outlier factor

from sklearn import datasets
import matplotlib.pyplot as plt

X_train_inlier, _ = datasets.make_blobs(
    centers=1, random_state=3, cluster_std=1, n_samples=200
)
X_train_outlier, _ = datasets.make_blobs(
    centers=1, random_state=7, cluster_std=2, n_samples=3
)

plt.scatter(X_train_inlier[:, 0], X_train_inlier[:, 1], c="red")
plt.scatter(X_train_outlier[:, 0], X_train_outlier[:, 1], c="blue")
plt.show()

import numpy as np
from sklearn.neighbors import LocalOutlierFactor

X = np.r_[X_train_inlier, X_train_outlier]

clf = LocalOutlierFactor(n_neighbors=10)
y_pred = clf.fit_predict(X)
plt.figure()
plt.scatter(X[y_pred == 1, 0], X[y_pred == 1, 1], c="green")
plt.scatter(X[y_pred == -1, 0], X[y_pred == -1, 1], c="black")
plt.show()
