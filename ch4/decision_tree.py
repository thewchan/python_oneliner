"""Decision tree one-liner example."""
import numpy as np
from sklearn import tree

# Data structure: [Math score, language score, creativity score, study field]
X = np.array([[9, 5, 6, 'computer science'],
              [1, 8, 1, 'linguistics'],
              [5, 7, 9, 'art']])

# One-liner
decision_tree = tree.DecisionTreeClassifier().fit(X[:, :-1], X[:, -1])
student_0 = decision_tree.predict([[8, 6, 5]])
student_1 = decision_tree.predict([[3, 7, 9]])

print("Training data: [Math score, language score, creativity score, study"
      " field")
print(X)
print('Predicting student 0: [9, 5, 6]')
print(student_0)
print('Predicting student 1: [3, 7, 9]')
print(student_1)
