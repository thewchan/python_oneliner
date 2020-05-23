"""NumPy shape examples."""
import numpy as np


a = np.array([1, 2, 3, 4])
print(a)
print(f'Dimension of a is {a.shape}.')

b = np.array([[2, 1, 2],
              [3, 2, 3],
              [4, 3, 4]])
print(b)
print(f'Dimension of b is {b.shape}.')

c = np.array([[[1, 2, 3], [2, 3, 4], [3, 4, 5]],
              [[1, 2, 4], [2, 3, 5], [4, 3, 4]]])
print(c)
print(f'Dimension of c is {c.shape}.')
