""" Reverse a String """

str1 = "Python"

def reverse_str(s):
    if len(s) == 0:
        return ""
    return reverse_str(s[1:]) + s[0]


print(reverse_str(str1))