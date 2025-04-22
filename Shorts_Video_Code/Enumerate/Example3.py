""" Store index-element pairs as tuples using list comprehension """

arr = ["Py", "Python", "PyCodeArena"]

res = [ (i, v) for i, v in enumerate(arr)]

print(res)

