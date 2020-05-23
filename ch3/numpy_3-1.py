"""Exercise 3-1.

Pull the name of the person with the highest salary from the matrix
by using selective Boolean indexing.
"""
import numpy as np


salaries = np.array([[99, 101, 103],
                     [110, 108, 105],
                     [90, 88, 85]])
taxation = np.array([[0.2, 0.25, 0.22],
                     [0.4, 0.5, 0.5],
                     [0.1, 0.2, 0.1]])
names = np.array(['alice', 'bob', 'tim'])

# One-liner:
print(names[np.nonzero((salaries * (1 - taxation)) == np.max
                       (salaries * (1 - taxation)))[0]])
