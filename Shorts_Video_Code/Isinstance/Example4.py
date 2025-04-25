""" isinstance() with Inheritance """

class Animal:
    pass

class Dog(Animal):
    pass

class Lion:
    pass 

d = Dog()

# Check if 'd' is an instance of Dog
print(isinstance(d, Dog))

# Check if 'd' is also considered an instance of Animal
print(isinstance(d, Animal)) 

# Check if 'd' is an instance of Lion
print(isinstance(d, Lion))
