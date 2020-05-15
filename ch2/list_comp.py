employees = {'Alice': 100_000,
             'Bob': 99_817,
             'Carol': 122_908,
             'Frank': 88_123,
             'Eve': 93_121}

top_earners = []
for key, val in employees.items():
    if val >= 100_000:
        top_earners.append((key, val))

print(top_earners)

# One-Liner equivalent
top_earners = [(k, v) for k, v in employees.items() if v >= 100_000]
print(top_earners)
