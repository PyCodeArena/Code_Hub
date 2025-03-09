""" 
Reference Counting in Python
Understanding how Python manages memory
"""
a = [10]  # RC: 1 
b = a     # RC: 2 
c = a     # RC: 3

# Changing references
c = [21]  # RC of [10]: 2 → 
          # 'c' now refers to a new list [21]
b = [11]  # RC of [10]: 1 → 
          # 'b' now refers to a new list [11]
a = [31]  # RC of [10]: 0 → 
          # 'a' now refers to a new list [31], 
          # [10] is deallocated