""" Filter Names With Length > 4 """

names = ["Py", "Python", "PyCodeArena"]

len_fun = lambda word: len(word) > 4 

res = list(filter(len_fun, names))

print(res)