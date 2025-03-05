
"""
Adding Two Tuples in Python
"""

# Method 4: Using itertools Module

list1 = [1, 2]
list2 = [3, 4]

Output = [1, 2, 3, 4]

from itertools import chain

result = list(chain(list1, list2))

print(result)

