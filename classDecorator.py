#Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.
# Class decorator that adds a greet() method
def add_greeting(cls):
    """Decorator to add a greet() method to any class"""
    def greet(self):
        return "Hello from Decorator!"
    
    # Add the new method to the class
    cls.greet = greet
    return cls  # Return the modified class

# Apply the decorator
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Test the decorated class
p = Person("Alice")
print(p.greet())  # Output: Hello from Decorator!
print(p.name)     # Output: Alice