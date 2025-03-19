""" Generator Exhaustion """
# If we are using the same Generator Twice

gen = (x for x in range(3))  
print(f"First Time: {tuple(gen)}")  
# ✅ Output: (0, 1, 2, 3, 4)

print(f"Second Time: {tuple(gen)}")  
# ⚠️ Output: () (Generator is empty now)
