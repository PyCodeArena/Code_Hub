""" Start indexing from 1 instead of 0 using enumerate() """

arr = ["Python", "JS", "C++"]

for i, v in enumerate(arr, start=1):
    print(i, "=>", v)  