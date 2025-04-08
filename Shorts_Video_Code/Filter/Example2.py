""" Filter non-empty strings """

arr = ["Python", "", "PCA", "", "Ayu"]

res = list(filter(lambda x: x != "", arr))

print(res)