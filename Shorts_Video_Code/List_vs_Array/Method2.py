""" NumPy is much faster than Python lists.
    It uses C-based implementations for internal operations (vectorized)."""

import time
import numpy as np

# NumPy (Vectorized)
start = time.time()
a = np.arange(10_00_000)
b = a * 2
end = time.time()
print(f"Array: {end - start :.3f} sec")

# Python List (Loop-based)
start_ = time.time()
l = list(range(10_00_000))
m = [x * 2 for x in l]
end_ = time.time()
print(f"List: {end_ - start_ :.3f} sec")