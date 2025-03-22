""" With Multiple For Loops """

arr = [("Py","Code"),("Arena","Python")]

# Flatten the list of tuples & Create a dict where the keys are words, and the values are their corresponding lengths.

res = {word: len(word) for each in arr for word in each}
print(res)
