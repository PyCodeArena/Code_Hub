""" Generator Expressions """

l = [1, 2, 3, 4, 5]
gen_exp = (num ** 2 for num in l)

print(next(gen_exp))  # Output: 1
print(next(gen_exp))  # Output: 4
