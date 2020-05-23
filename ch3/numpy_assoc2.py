"""NumPy association analysis example.

Here we would like to find the two items that were purchased most often
together.
"""
import numpy as np


# Row is customer shopping basket
# row = [course 1, course 2, ebook 1, ebook 2]
# value 1 indicates that an item was bought.
basket = np.array([[0, 1, 1, 0],
                   [0, 0, 0, 1],
                   [1, 1, 0, 0],
                   [0, 1, 1, 1],
                   [1, 1, 1, 0],
                   [0, 1, 1, 0],
                   [1, 1, 0, 1],
                   [1, 1, 1, 1]])

# One-liner
copurchases = [(i, j, np.sum(basket[:, i] + basket[:, j] == 2))
               for i in range(4) for j in range(i + 1, 4)]
print(copurchases)
