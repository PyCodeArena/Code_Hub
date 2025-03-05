"""
Adding Two Lists in Python
"""

# Method 2: Using * Unpacking Operator

list1 = [1, 2]
list2 = [3, 4]

Output = [1, 2, 3, 4]

result = [*list1, *list2]

print(result)