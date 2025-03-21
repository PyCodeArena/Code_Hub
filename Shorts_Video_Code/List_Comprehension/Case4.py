
""" With Multiple For Loops """

arr = [(2, 6), (3, 7, 5)]

# Flatten a list of nested tuples.
res = [num for each in arr for num in each]
print(res)  

