""" Immutable Data Types """

s = "PyCode"
print(f"Id before modification: {id(s)}")

# Trying to modify (creates a new string)
s += " Arena"
print(f"Id after modification: {id(s)}")
print(f"New String: {s}")  
# New string created -> Different memory location
