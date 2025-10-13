""" Using Basic If-else Conditions """

def is_leap(year):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    return "Leap Year"
  
  else:
    return "Not a Leap Year"
  
print(is_leap(2000))
print(is_leap(1900))
print(is_leap(2024))