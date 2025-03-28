def generator():
    yield "PyCodeArena"
    yield "Python"
    yield "Shorts"

res = generator()
print(next(res))
print(next(res))


