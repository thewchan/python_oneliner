"""NumPy Boolean indexing example.

Using Boolean indexing on NumPy arrays, pull Instagram users with more than
100 million followers.
"""
import numpy as np


inst = np.array([[232, '@instagram'],
                 [133, '@selenagomez'],
                 [59, '@victoriassecret'],
                 [120, '@cristiano'],
                 [111, '@beyonce'],
                 [76, '@nike']])

# One-liner
superstars = inst[inst[:, 0].astype(float) > 100, 1]
print(inst)
print('Instagram users with more than 100 million followers:')
print(superstars)
