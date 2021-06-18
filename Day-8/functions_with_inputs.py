def greet(name):
    # name is a parameter
    # "Angela" is an argument
    print(f"Hello {name}")

# greet("Angela")

# more than one parameter
def greet_new(name, location):
    print(f"Hello {name}")
    print(f"{location} is a great place")

greet_new("Tharun", "Hyderabad")
# positional argument (default way, 1st argument assigned to 1st parameter and so-on....)
greet_new("Hyderabad", "Tharun")

# to be more specific, we can use keyword argument
greet_new(name= "Tharun", location="France")
