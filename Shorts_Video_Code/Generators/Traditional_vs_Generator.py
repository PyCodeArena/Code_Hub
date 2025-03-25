""" Traditional Collection vs Generator """

# Normal List (Takes More Memory)
nums = [num**2 for num in range(3)]  
# Generates all values at once, 
# consuming more memory  
print(nums)       # Output:[0, 1, 4]

# Generator Function (Consumes Less Memory)
def generate_squares():
    for num in range(3):
        # Yield pauses execution and saves state  
        yield num**2  

gen = generate_squares()  

# Generates values one at a time, 
# saving memory  
print(next(gen))  # Output: 1  
print(next(gen))  # Output: 1  
print(next(gen))  # Output: 4 