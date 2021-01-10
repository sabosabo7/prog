from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.model_selection import GridSearchCV

iris = load_iris()
X = iris.data
y = iris.target

clf = tree.DecisionTreeClassifier()
params = {"max_depth": list(range(1, 5)), "criterion": ["gini", "entropy"]}

grid_search = GridSearchCV(
    estimator=clf, param_grid=params, cv=5, return_train_score=True
)
grid_search.fit(X, y)

print(grid_search.best_score_)
print(grid_search.best_params_)
