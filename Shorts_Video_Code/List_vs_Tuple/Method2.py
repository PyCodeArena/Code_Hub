import sys

lis = [10, 20, 30]
tup = (10, 20, 30)

print(sys.getsizeof(lis))  # 80 bytes
print(sys.getsizeof(tup))  # 64 bytes