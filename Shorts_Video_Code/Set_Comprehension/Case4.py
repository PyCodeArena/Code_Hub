""" With Multiple For Loops """

arr = {(2, 6), (3, 7 , 5)}

# Flatten a list of nested tuples.
res = {n for each in arr for n in each}
print(res)  

