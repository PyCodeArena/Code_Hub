""" List vs Generator """

import sys

# List (Consumes More Memory)

res = [n**2 for n in range(100000)]  
# Stores all values in memory

size = sys.getsizeof(res)
# Memory consumption is high
print(f"Total size of the list: {size} bytes.")  
