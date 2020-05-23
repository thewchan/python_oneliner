"""Random forest one-liner example."""
import numpy as np
from sklearn.ensemble import RandomForestClassifier


# Data structure: [Math score, language score, creativity score, study field]
X = np.array([[9, 5, 6, 'computer science'],
              [5, 1, 5, 'computer science'],
              [8, 8, 8, 'computer science'],
              [1, 10, 7, 'literature'],
              [1, 8, 1, 'literature'],
              [1, 1, 6, 'art'],
              [5, 7, 9, 'art']])

forest_model = RandomForestClassifier(n_estimators=10).fit(X[:, :-1], X[:, -1])
students = np.array([[8, 6, 5],
                     [3, 7, 9],
                     [2, 2, 1]])

print("Training data: [Math score, language score, creativity score, study"
      " field")
print(X)
print('Predicting students:')
print(students)
print(forest_model.predict(students))
