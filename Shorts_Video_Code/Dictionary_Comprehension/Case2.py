""" With Only If Condition """

arr = [2, 6, 3, 5]

# Create a dict where the keys are numbers, & the values are their squares for even numbers.

res = {num:num**2 for num in arr if num%2 == 0}
print(res)  
