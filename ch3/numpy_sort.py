"""NumPy sorting example.

We will use this one-liner to find the names of the top three students with the
highest SAT scores. We'll ask for the student names and not the sorted SAT
scores.
"""
import numpy as np


sat_scores = np.array([1100, 1256, 1543, 1043, 989, 1412, 1343])
students = np.array(['John', 'Bob', 'Alice', 'Joe', 'Jane', 'Frank', 'Carl'])

# One-liner
top_3 = students[np.argsort(sat_scores)][:-4:-1]
print(students)
print(sat_scores)
print(top_3)
