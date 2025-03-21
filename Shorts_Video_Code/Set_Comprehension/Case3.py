""" With If-Else Condition """

s = [2, 6, 3, 5]

# Square even numbers and cube odd numbers in a set
res = {num**2 if num%2 == 0 else num**3 for num in s}
print(res)  

