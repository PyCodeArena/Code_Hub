""" Add elements of two lists """

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

outut = [5, 7, 9]

add = lambda num1, num2: num1 + num2 

res = list(map(add, arr1, arr2))

print(res)