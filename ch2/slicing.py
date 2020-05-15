"""Our goal is to find a particular text query within a multi-line string. We
want to find the query in the text and return its immediate environment, up to
18 positions around the found query. Extracting the environment as well as the
query is useful for seeing the textual context of the found string---just as
Google presents text snippets around a searched keyword. Here we are looking
for the string 'SQL' in an Amazon letter to shareholders---with the immediate
environment of up to 18 positions around the string 'SQL'.
"""


letters_amazon = """We spend several years building out own database engine,
Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible service with
the same or better durability and availability as the commercial engines, but
at one-tenth of the cost. We were not surprised when this worked.
"""

# One-liner
find = lambda x, q: x[x.find(q) - 18:x.find(q) + 18] if q in x else -1

print(find(letters_amazon, 'SQL'))
