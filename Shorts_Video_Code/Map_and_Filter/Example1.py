""" Find squares of numbers & return only those that are greater than 20 """

arr = [1, 2, 3, 4, 5, 6]

m_res = map(lambda n: n ** 2, arr)

f_res = filter(lambda x: x > 20, m_res)

print(list(f_res)) 