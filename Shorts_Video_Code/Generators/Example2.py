l = [1, 2, 3, 4, 5]

# Generator Function
def square_list(l):
    for num in l:
        yield num ** 2

gen_obj = square_list(l)

# Getting values from generator
print(list(gen_obj))  