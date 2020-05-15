"""When given a list of strings, this one-liner crates a new list of tuples,
each consisting of a Boolean value and the original string. The Boolean value
indicates whether the string 'anonymous' appears in the original string. We
call the resulting list 'mark' because the Boolean values mark the string
elements in the list that contain the string 'anonymous'.
"""


txt = ['lambda functions are anonymous functions.',
       'anonymous functions dont have a name.',
       'functions are objects in Python.']

# One-liner
mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt)

print(list(mark))

# list comprehension version

mark = [('anonymous' in s, s) for s in txt]
print(mark)
