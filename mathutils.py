# MathUtils class demonstrates the use of a static method in Python.
# The static method 'add' takes two numbers as parameters and returns their sum.
# Note: No class variables or instance variables are used here.

class MathUtils:
    """
    MathUtils is a utility class containing mathematical helper functions.
    Since the functions don't depend on object state (instance variables),
    we use static methods.
    """

    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        
        Parameters:
        a (int/float): First number
        b (int/float): Second number
        
        Returns:
        int/float: Sum of a and b
        """
        return a + b  # Return the sum directly


# Example usage:
# We do not need to create an object of MathUtils because 'add' is a static method.

result = MathUtils.add(5, 7)  # Calling the static method directly using the class name
print("The sum is:", result)  # Output: The sum is: 12
