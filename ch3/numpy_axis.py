"""NumPy axis example.

Given an array of temperature values, replace every seventh temperature value
with the average of the last seven days (including the seventh day's
temperature value).
"""
import numpy as np

# Data:         M  T  W  Th F  S  Su
tmp = np.array([1, 2, 3, 4, 3, 4, 4,
                5, 3, 3, 4, 3, 4, 6,
                6, 5, 5, 5, 4, 5, 5])

# One-liner
tmp[6::7] = np.averge(tmp.reshape(-1, 7), axis=1)
