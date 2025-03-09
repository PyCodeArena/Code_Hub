""" 
Reference Counting in Python
Understanding how Python manages memory
"""

# Initial Reference Count of value 10
a = 10  # RC: 1
b = a   # RC: 2
c = a   # RC: 3

print(f"Reference count of 10 ➝ 3")

# Changing references
c = 21  # RC of 10: 2 (c is now pointing to 21)
b = 11  # RC of 10: 1 (b is now pointing to 11)
a = 31  # RC of 10: 0 (a is now pointing to 31, 
        # 10 is deallocated)

# Once reference count becomes zero, 
# the value 10 will be deallocated.
# Python’s garbage collector will remove it 
# automatically.