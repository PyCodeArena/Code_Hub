
"""
Adding Two Dictionaries in Python
"""

# Method 2: Using Unpacking Operator

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

Output = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

result = {**dict1, **dict2}

print(result)

