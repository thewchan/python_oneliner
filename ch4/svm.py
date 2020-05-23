"""Support vector machine one-liner example."""
import numpy as np
from sklearn import svm


# Data structure: [Math score, language score, creativity score, study field]
X = np.array([[9, 5, 6, 'computer science'],
              [10, 1, 2, 'computer science'],
              [4, 9, 3, 'literature'],
              [1, 8, 1, 'literature'],
              [0, 1, 10, 'art'],
              [5, 7, 9, 'art']])

svm_model = svm.SVC().fit(X[:, :-1], X[:, -1])
student_0 = svm_model.predict([[3, 3, 6]])
student_1 = svm_model.predict([[8, 1, 1]])

print("Training data: [Math score, language score, creativity score, study"
      " field")
print(X)
print('Predicting student 0: [3, 3, 6]')
print(student_0)
print('Predicting student 1: [8, 1, 1]')
print(student_1)
