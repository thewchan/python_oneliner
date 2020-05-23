"""NumPy statistics example.

Find all outlier days for which the statistics deviate more than the standard
deviation from their mean statistics.
"""
import numpy as np


# (row = day), (col = users, bounce, duration)
a = np.array([[815, 70, 115],
              [767, 80, 50],
              [912, 74, 77],
              [554, 88, 70],
              [1008, 65, 128]])

mean, stdev = np.mean(a, axis=0), np.std(a, axis=0)

# One-liner
outliers = ((np.abs(a[:, 0] - mean[0]) > stdev[0]) *
            (np.abs(a[:, 1] - mean[1]) > stdev[1]) *
            (np.abs(a[:, 2] - mean[2]) > stdev[2]))
print(a[outliers])
