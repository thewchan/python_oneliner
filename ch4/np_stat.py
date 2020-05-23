"""Calculating basic statistics of NumPy arrays in one line."""
import numpy as np


x = np.array([[8, 9, 11, 12],
              [1, 2, 2, 1],
              [2, 8, 9, 9],
              [9, 6, 6, 3],
              [3, 3, 3, 3]])

# One-liner
avg, var, std = np.average(x, axis=1), np.var(x, axis=1), np.std(x, axis=1)

print('Data:')
print(x)
print("Averages: " + str(avg))
print("Variance: " + str(var))
print("Standard Deviations: " + str(std))
