""" Swap Two Variables """

a = 10
b = 20

# Method 1: Using Third Variable
print(f"Before Swapping: {a=}, {b=}")

temp = a
a = b
b = temp       

print(f"After  Swapping: {a=}, {b=}")