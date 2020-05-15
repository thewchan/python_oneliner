"""Given a list of integers that reflect the measured cardiac cycle, we want to
clean the data by removing the first and last two values from the list. Then,
we create a new list with expected future heart rates by copying the cardiac
cycle to future time instances.
"""
import matplotlib.pyplot as plt


cardiac_cycle = [62, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62]

# One-liner
expected_cycles = cardiac_cycle[1:-2] * 10
plt.plot(expected_cycles)
plt.show()
