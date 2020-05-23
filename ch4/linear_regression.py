"""Simple linear regression one-liner."""
import numpy as np
from sklearn.linear_model import LinearRegression


apple = np.array([155, 156, 157])
n = len(apple)

# One-liner
model = LinearRegression().fit(np.arange(n).reshape(n, 1), apple)

print(f'Apple stock: {apple}')
print(model.predict([[3], [4]]))
