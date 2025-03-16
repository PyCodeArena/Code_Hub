
""" Using **kwargs Only 
    (Keyword Arguments)"""

def user_info(**kwargs):
    print(f"Data Type: {type(kwargs)}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    return "User Info Processed"

print(user_info(name="Ayu", age=26))
print(user_info(country="India"))

