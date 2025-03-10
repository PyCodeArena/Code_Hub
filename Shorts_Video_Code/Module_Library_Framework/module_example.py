import my_module

num = 25

# Fetch variable
print(my_module.name)

# Call function without module variable
out = my_module.greet()
print(out)


# Call function to get square root
res = my_module.get_sqrt(num)
print(f"sqrt of {num} is {res}")
