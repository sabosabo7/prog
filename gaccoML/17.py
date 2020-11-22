from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVC
from imblearn.over_sampling import SMOTE

X1, _ = datasets.make_blobs(n_samples=300, cluster_std=4, random_state=5, centers=1)
X2, _ = datasets.make_blobs(n_samples=50, cluster_std=1, random_state=3, centers=1)

X = np.r_[X1, X2]
y = np.r_[np.zeros(300), np.ones(50)]

plt.scatter(X[y == 0, 0], X[y == 0, 1], c="red")
plt.scatter(X[y == 1, 0], X[y == 1, 1], c="blue")

svm_normal = SVC(kernel="linear").fit(X, y)
svm_weight = SVC(kernel="linear", class_weight={1: 6}).fit(X, y)

normal_coefs = svm_normal.coef_
normal_intercepts = svm_normal.intercept_
weight_coefs = svm_weight.coef_
weight_intercepts = svm_weight.intercept_

line_x = np.linspace(-5, 3)
normal_line_y = (
    -(line_x * normal_coefs[0][0] + normal_intercepts[0]) / normal_coefs[0][1]
)
weight_line_y = (
    -(line_x * weight_coefs[0][0] + weight_intercepts[0]) / weight_coefs[0][1]
)

plt.plot(line_x, normal_line_y, c="black")
plt.plot(line_x, weight_line_y, c="green")


smote = SMOTE(random_state=1)
X_resampled, y_resampled = smote.fit_sample(X, y)
svm_weight_2 = SVC(kernel="linear").fit(X_resampled, y_resampled)
weight_2_coefs = svm_weight_2.coef_
weight_2_intercepts = svm_weight_2.intercept_
weight_2_line_y = (
    -(line_x * weight_2_coefs[0][0] + weight_2_intercepts[0]) / weight_2_coefs[0][1]
)

plt.plot(line_x, weight_2_line_y, c="green")
plt.show()
