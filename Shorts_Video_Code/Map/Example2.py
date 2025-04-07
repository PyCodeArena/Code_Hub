""" Square all elements in a list """

arr = [1, 2, 3, 4]

squared = lambda num: num ** 2

res = list(map(squared, arr)) 

print(res)