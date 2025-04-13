""" Multiply All Elements in a List """

from functools import reduce

arr = [1, 2, 3, 4]

mult = lambda num1, num2: num1 * num2 

res = reduce(mult, arr)

print(res)


