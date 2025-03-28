def generator():
    yield "Hello, PyCodeArena!"

gen = generator()
res = next(gen)

print(f"Output: {res}")
print(f"Data Types: {type(res)}")