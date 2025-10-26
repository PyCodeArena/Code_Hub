""" NumPy arrays use less memory compared to lists.
Lists store references to objects; NumPy uses homogeneous types (fixed-size)."""

import sys
import numpy as np

lst = [1, 2, 3, 4]
arr = np.array([1, 2, 3, 4])

print(sys.getsizeof(lst))  # 88 Larger
print(arr.nbytes)          # 32 Smaller


