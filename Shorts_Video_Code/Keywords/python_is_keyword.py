""" 
👉 To check whether a string is a Keyword or not 
"""

import keyword

str_arr = ["if", 26, "def", "True", "home"]

for each in str_arr:
  flag = keyword.iskeyword(each)
  print(f"'{each}' is a keyword? -> {flag}")