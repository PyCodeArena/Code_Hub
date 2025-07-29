""" Reverse a List """

arr = [1, 2, 3, 4]

res = []

for each in arr:
    res = [each] + res
    
print(res)
