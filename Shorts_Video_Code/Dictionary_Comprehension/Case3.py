""" With If-Else Condition """

arr = [2, 6, 3, 5]

# Create a dict where the keys are numbers, & the values are squared if the number is even & cubed if the number is odd.

res = {num:num**2 if num%2 == 0 else num**3 for num in arr}
print(res)  


