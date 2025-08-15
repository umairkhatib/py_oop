#Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.
class Multiplier:
    def __init__(self, factor):
        """Initialize with a multiplication factor"""
        self.factor = factor
    
    def __call__(self, x):
        """Make the object callable - multiplies input by factor"""
        return x * self.factor

# Testing
if __name__ == "__main__":
    # Create multiplier objects
    double = Multiplier(2)
    triple = Multiplier(3)
    
    # 1. Verify they're callable
    print("Is double callable?", callable(double))  # True
    
    # 2. Call objects like functions
    print("Double of 5:", double(5))    # 10
    print("Triple of 5:", triple(5))    # 15
    
    # 3. Use in higher-order functions
    numbers = [1, 2, 3]
    doubled = list(map(double, numbers))
    print("Doubled list:", doubled)     # [2, 4, 6]