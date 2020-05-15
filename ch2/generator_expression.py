"""Out data is a dictionary of dictionaries storing the hourly wages of company
employees. You want to extract a list of the companies paying below your
state's minimum wage (< $9) for at least 1 employee.
"""


companies = {'Cool Company': {'Alice': 33,
                              'Bob': 28,
                              'Frank': 29},
             'Cheap Company': {'Ann': 4,
                               'Lee': 9,
                               'Chrisi': 7},
             'Soso Company': {'Esther': 38,
                              'Cole': 8,
                              'Paris': 18}}

# One-liner
illegal = [x for x in companies if any(y < 9 for y in companies[x].values())]
print(illegal)
