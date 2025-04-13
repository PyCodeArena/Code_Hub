""" Find the Maximum Element in a List """

from functools import reduce

arr = [11, 1, 26, 9]

max_ = lambda n1, n2: n1 if n1 > n2 else n2 

res = reduce(max_, arr)

print(res)

