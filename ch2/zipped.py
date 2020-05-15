"""Our data consists of the column names and the employee data organized as
list of tuples (rows). Assign the column names to the rows and, thus, create a
list of dictionaries. Each dictionary assigns the column names to the
respective data values.
"""


column_names = ['name', 'salary', 'job']
db_rows = [('Alice', 180_000, 'data scientist'),
           ('Bob', 99_000, 'mid-level manager'),
           ('Frank', 87_000, 'CEO')]

# One-liner
db = [dict(zip(column_names, row)) for row in db_rows]
print(db)
