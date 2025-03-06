
"""
Adding Two Dictionaries in Python
"""

# Method 4: Using dict() Constructor

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

Output = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

res = dict(dict1.items() | dict2.items())

print(res)

