"""Our goal is to replace every other string with the string immediately in
front of it.
"""


visitors = ['Firefox', 'corrupted', 'Chrome', 'corrupted', 'Safari',
            'corrupted', 'Safari', 'corrupted', 'Chrome', 'corrupted',
            'Firefox', 'corrupted']

# One-liner
visitors[1::2] = visitors[::2]

print(visitors)
