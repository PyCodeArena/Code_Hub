""" 
Create a decorator that ensures a division function always divides the larger number by the smaller one, guaranteeing the result is ≥ 1.

Example:
If we pass
🔹(10, 2) → return 5
🔹(2, 10) → return 5 (❌ not 0.2)
"""

def div_decorator(func):
    def wrapper(*args, **kwargs):
        nume, deno = max(args), min(args)
        return func(nume, deno)
    return wrapper

@div_decorator
def div_func(num1, num2):
    return num1 / num2

print(div_func(10, 2))
print(div_func(2, 10))