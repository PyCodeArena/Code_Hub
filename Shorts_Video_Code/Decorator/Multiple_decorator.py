def decorator1(func):
    def wrapper():
        print("✅ Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("✅ Decorator 2")
        func()
    return wrapper

@decorator1
@decorator2
def greet():
  print("👋 Hello Learners!")

greet()
