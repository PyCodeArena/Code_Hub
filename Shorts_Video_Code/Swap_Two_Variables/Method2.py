""" Swap Two Variables """

a = 10
b = 20

# Method 2: Using Arithmetic Operations
print(f"Before Swapping: {a=}, {b=}")

a = a + b
b = a - b
a = a - b 

print(f"After  Swapping: {a=}, {b=}")