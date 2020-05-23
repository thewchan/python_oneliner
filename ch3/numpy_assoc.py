"""NumPy association analysis example.

Here we attempt to find the fraction of customers bought two ebooks together?
Based on this data, the recommender system can offer customers a book "bundle"
to buy a single book.
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
copurchases = np.sum(np.all(basket[:, 2:], axis=1)) / basket.shape[0]
print(copurchases)
