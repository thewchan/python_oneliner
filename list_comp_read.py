filename = 'list_comp_read.py'

f = open(filename)
lines = []
for line in f:
    lines.append(line.strip())

print(lines)

"""['filename = 'list_comp_read.py"
'',
'f = open(filename)',
'lines = []',
'for line in f:',
'lines.append(line.strip())',
'',
'print(lines)']
"""

# One-line version: print([line.strip() for line in open('list_comp_read.py')])
