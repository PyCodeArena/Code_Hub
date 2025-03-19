
"""Ways to Prevent Generator Exhaustion"""

# Method 1️⃣ : Store Values in a List
gen = (x for x in range(5))  

# Store values first
values = list(gen)  

print(f"First Time: {values}")  
print(f"Second Time: {values}")  
# No exhaustion!


# Method 2️⃣ : Create a New Generator Each Time
def gen_func():
    return (x for x in range(5))

gen1 = gen_func()  
print(f"First Time: {tuple(gen1)}")  

gen2 = gen_func()  
print(f"Second Time: {tuple(gen2)}")  
# Works again!
