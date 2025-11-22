


def is_prime(num):
  if num > 1:
    for n in range(2, num):
      if num % n == 0:
        return "Not Prime"
    return "Prime"
  else:
    return "Not Prime"

arr = [2, 7, 10, -2]
for num in arr:
  print(num, "=>", is_prime(num))
  
  
  
