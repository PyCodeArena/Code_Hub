""" NumPy supports advanced mathematical operations (e.g., mean, std, dot product, matrix operations).
Python lists are limited to basic operations."""

# NumPy array operations
import numpy as np
arr = np.array([3, 2, 1])
print(np.mean(arr))  
print(np.std(arr))   
print(np.dot(arr, arr))

# List operations
lst = [3, 2, 1]
lst.append(4)
lst.sort()
print(lst)