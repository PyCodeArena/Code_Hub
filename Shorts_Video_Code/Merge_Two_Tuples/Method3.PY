
"""
Adding Two Tuples in Python
"""

# Method 3: Using itertools Module

tup1 = (1, 2)
tup2 = (3, 4)

Output = (1, 2, 3, 4)

from itertools import chain

result = tuple(chain(tup1, tup2))

print(result)