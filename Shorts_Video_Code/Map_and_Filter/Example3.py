"""Convert strings longer than 3 characters to Uppercase"""

arr = ["py", "python", "PyCodeArena", "Hi"]

res = map(str.upper, filter(lambda n: len(n) > 3, arr))

print(list(res))