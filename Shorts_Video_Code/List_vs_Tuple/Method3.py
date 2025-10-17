import time

# Creation Time
start = time.time()
large_list = list(range(10_00_000))
end = time.time()
print(f"List Timing: {end - start} sec")

start_ = time.time()
large_tupl = tuple(range(10_00_000))
end_ = time.time()
print(f"Tuple Timing: {end_-start_} sec")



hash((1, 2, 3))   # ✅ Works
hash([1, 2, 3])   # ❌ Error


{(1, 2): 'Valid'}   # ✅ Works
{[1, 2]: 'Invalid'} # ❌ Error


l = [10, 20, 30]

l.append(40)    # [10, 20, 30, 40]
l.pop()         # [10, 20, 30]
l.insert(0, 5)  # [5, 10, 20, 30]


t = (10, 10, 50)
t.count(10)     # 2 (frequency)


