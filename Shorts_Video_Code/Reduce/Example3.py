""" Concatenate List of Strings """

from functools import reduce

arr = ["Py", "Code", "Arena"]

res = reduce(lambda a, b: a + b, arr) 

print(res)

