""" Filter even numbers from a list """

arr = [1, 2, 3, 4, 26, 10]

even = lambda num: num % 2 == 0 

res = list(filter(even, arr))

print(res)