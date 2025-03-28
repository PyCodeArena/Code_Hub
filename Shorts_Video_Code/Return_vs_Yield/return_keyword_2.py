def get_squares(num):
    squared_num = num ** 2
    return num, squared_num

res = get_squares(5)
print(f"Output 1: {res}")
print(f"Data Types 2: {type(res)}")


def greet():
    return "PyCodeArena", 26

res = greet()
print(f"\nOutput 2: {res}")
print(f"Data Types 2: {type(res)}")