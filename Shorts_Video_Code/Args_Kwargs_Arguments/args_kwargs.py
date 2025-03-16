
""" Using *args & **kwargs 
(Both Positional & Keyword Arguments)"""

def greet_person(name, *args, **kwargs):
    print(f"Hello, {name}!")
    print("Additional Info:", args)
    print("More Details:", kwargs)

greet_person("Ayu", 26, "Developer", language="Python", country="India")

