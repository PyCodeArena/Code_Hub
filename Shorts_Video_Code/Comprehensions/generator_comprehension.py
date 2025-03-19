""" Generator Comprehension """

# Creates a generator, not a tuple
gen = (x for x in range(5))  
print(f"Type: {type(gen)}")  

#  To convert it into a tuple

# Method 1: Convert Generator to tuple
print(f"Method 1: {tuple(gen)}")

# Method 2: Directly Create a Tuple from Generator Expression
tup2 = tuple(x for x in range(5))
print(f"Method 2: {tup2}")

