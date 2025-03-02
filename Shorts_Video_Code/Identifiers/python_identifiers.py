"""
👉 To check if a string is a valid Python identifier:
"""

str_arr = [
  "my_var", "Var123", "_hidden", "var_99", "var name", "__protected", "123variable", "my-variable"
  ]

for each in str_arr:
  flag = each.isidentifier()
  print(f"'{each}' is valid? -> {flag}")