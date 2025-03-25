""" List vs Generator """

import sys

# Generator (Memory Efficient)
gen = (n**2 for n in range(100000))  
# Generates values lazily, one at a time

# Minimal memory usage
gen_size = sys.getsizeof(gen)
print(f"Size of Generator: {gen_size} bytes.")  

# Getting the first value from the generator
val1 = next(gen)
val1_size = sys.getsizeof(val1)
print(f"Size of the first value: {val1_size} bytes.")

# Fetching subsequent values
val2 = next(gen)
val2_size = sys.getsizeof(val2)
print(f"Size of the second value: {val2_size} bytes.")

# and so on...

