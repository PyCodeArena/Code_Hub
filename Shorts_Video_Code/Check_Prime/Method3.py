


arr = [2, 7, 10, -2]
for num in arr:
  is_prime = num > 1 and all(num % n != 0 for n in range(2, int(num **0.5) + 1))
  
  print("Prime" if is_prime else "Not Prime")


