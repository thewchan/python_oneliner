"""Lambda function example.

Create a filter function that takes a list of books x and a minimum rating y
and returns a list of potential bestsellers that have higher than minimum
rating, y' > y.
"""
import numpy as np


books = np.array([['Coffee Break Numpy', 4.6],
                  ['Lord of the Rings', 5.0],
                  ['Harry Potter', 4.3],
                  ['Winnie-the-Pooh', 3.9],
                  ['The Clown of God', 2.2],
                  ['Coffee Break Python', 4.7]])

predict_bestseller = (lambda x, y: x[x[:, 1].astype(float) > y])(books, 3.9)

print(books)
print('Predicted bestsellers:')
print(predict_bestseller)
