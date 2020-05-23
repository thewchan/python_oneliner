"""Numpy broadcasting example.

Using air pollution as an example, we are trying to find cities with above-
average pollution peaks from a set of data.
"""
import numpy as np


X = np.array([[42, 40, 41, 43, 44, 43],     # Hong Kong
              [30, 31, 29, 29, 29, 30],     # New York
              [8, 13, 31, 11, 11, 9],       # Berlin
              [11, 11, 12, 13, 11, 12]])    # Montreal

cities = np.array(['Hong Kong', 'New York', 'Berlin', 'Montreal'])

# One-liner
polluted = set(cities[np.nonzero(X > np.average(X))[0]])

print('Air pollution data:')
print(X)
print('Cities in consideration:')
print(cities)
print('Cities with above average air pollution:')
print(polluted)
