""" Square All Even Numbers from a List """

arr = [1, 2, 3, 4, 5, 6]

f_res = filter(lambda x: x % 2 == 0, arr)

m_res  = map(lambda n: n ** 2, f_res) 

print(list(m_res))