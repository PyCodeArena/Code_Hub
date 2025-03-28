def generator():
    yield "Hi", "Leaner!"

res = generator()
val1 = next(res)
print(f"Output 1: {val1}")
print(f"Data Types 1: {type(val1)}")

def generator():
    yield ["Hi", "Leaner!"], 26

res = generator()
val1 = next(res)
print(f"\nOutput 2: {val1}")
print(f"Data Types 2: {type(val1)}")