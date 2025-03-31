""" Simple Decorator Example"""

def decorator_function(func):  
    def wrapper():  
        print("Before Execution")  
        func()  
        print("After Execution")  
    return wrapper  

@decorator_function  
def greet():  
    print("Hello, PyCodeArena!")  

greet()  

