"""KNN one-liner example."""
import numpy as np
from sklearn.neighbors import KNeighborsRegressor


X = np.array([[35, 30000], [45, 45000], [40, 50000],
              [35, 35000], [25, 32500], [40, 40000]])

# One-liner
knn = KNeighborsRegressor(n_neighbors=3).fit(X[:, 0].reshape(-1, 1), X[:, 1])
res = knn.predict([[30]])

print("Training data: [House size, House Price")
print(X)
print('KNN prediction at House size = 30')
print(res)
