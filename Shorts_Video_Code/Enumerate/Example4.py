""" print the index, roll number, and name using enumerate() with tuple unpacking """

arr = [(1001, "Py"), (1002, "Python")]

for i, (roll, name) in enumerate(arr):
    print(i, roll, name) 