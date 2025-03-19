l = [2, 6, 9, 5]

""" List Comprehension"""
# square all elements
l1 = [num**2 for num in l]
print(l1)

""" Set Comprehension"""
# square all elements
s1 = {num**2 for num in l}
print(s1)

""" Dictionary Comprehension"""
# key: original num, value: Squared num
d1 = {num: num**2 for num in l}
print(d1)

