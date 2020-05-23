"""NumPy broadcasting example.

We have data for a variety of professions, and we want to increase the
salaries of just the data scientists by 10 percent every other year.
"""
import numpy as np


data_scientist = [130, 132, 137]
product_manager = [127, 140, 145]
designer = [118, 118, 127]
software_engineer = [129, 131, 137]

employees = np.array([data_scientist,
                      product_manager,
                      designer,
                      software_engineer])
print(employees)

# One-liner
employees[0, ::2] = employees[0, ::2] * 1.1
print('After salary raise...')
print(employees)
