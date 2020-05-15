"""Our goal is to create a new training data sample from our data---a list of
lists, each consisting of six floats---by including only every other float
value from the original data set.
"""


price = [[9.9, 9.8, 9.8, 9.4, 9.5, 9.7],
         [9.5, 9.4, 9.4, 9.3, 9.2, 9.1],
         [8.4, 7.9, 7.9, 8.1, 8.0, 8.0],
         [7.1, 5.9, 4.8, 4.8, 4.7, 3.9]]

# One-liner
sample = [line[::2] for line in price]

print(sample)
