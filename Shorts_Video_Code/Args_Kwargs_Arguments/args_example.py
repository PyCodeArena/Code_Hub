
""" Using *args Only 
    (Positional Arguments)"""

def add_numbers(*args):
  print(f"Data Type: {type(args)}")
  if not args:
      return "No numbers provided!"
  return f"Sum: {sum(args)}"

print(add_numbers(1, 2, 3, 4))
print(add_numbers())


