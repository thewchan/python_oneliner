"""Logistic regression one-liner example."""
import numpy as np
from sklearn.linear_model import LogisticRegression


X = np.array([[0, 'No'],
              [10, 'No'],
              [60, 'Yes'],
              [90, 'Yes']])
n = len(X)

# One-liner
model = LogisticRegression().fit(X[:, 0].reshape(n, 1), X[:, 1])

print(f'Smoking data: \n {X}')
print('Predicting cancer positives with smoker that smoked:')
print('2, 12, 13, 40, 90 cigarettes')
print(model.predict([[2], [12], [13], [40], [90]]))
