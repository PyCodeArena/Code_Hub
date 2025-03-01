""" 👉 To get all Keywords """

# Method 1: Using help
help("keywords")

# ---------------------------------------
# Method 2: Using Keyword Module

import keyword
key_list = keyword.kwlist
print(key_list)

# ---------------------------------------
# Count Total Number of Keywords

print(f"Total no of Keywords: {len(key_list)}")