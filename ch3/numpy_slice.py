"""NumPy slicing examples."""
import numpy as np


a = np.array([[0, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 10, 11],
              [12, 13, 14, 15]])
print(a)
print('Slicing out third column: >>>a[:, 2]')
print(a[:, 2])
print('Slicing out second row: >>>a[1, :]')
print(a[1, :])
print('Slicing out second row, every other element: >>>a[1, ::2]')
print(a[1, ::2])
print('Slicing out all columns excecpt last: >>>[:, :-1]')
print(a[:, :-1])
