# Employee class to demonstrate public, protected, and private variables in Python.
# Public: Accessible from anywhere.
# Protected: Intended for internal use, but still accessible outside (by convention).
# Private: Name-mangled, not directly accessible outside the class.

class Employee:
    """
    Employee class with three different access levels for variables:
    - Public: Accessible anywhere
    - Protected: Accessible, but intended for internal/subclass use
    - Private: Not directly accessible from outside the class (name-mangled)
    """

    def __init__(self, name, salary, ssn):
        # Public variable
        self.name = name
        
        # Protected variable (single underscore)
        self._salary = salary
        
        # Private variable (double underscore)
        self.__ssn = ssn

    def display_info(self):
        """
        Display all variables from inside the class.
        """
        print("Inside class:")
        print("Name (public):", self.name)
        print("Salary (protected):", self._salary)
        print("SSN (private):", self.__ssn)


# Example usage
emp = Employee("John Doe", 50000, "123-45-6789")

# Accessing public variable — Works fine
print("Public variable (name):", emp.name)

# Accessing protected variable — Works (but discouraged outside class/subclass)
print("Protected variable (_salary):", emp._salary)

# Accessing private variable directly — Will cause AttributeError
try:
    print("Private variable (__ssn):", emp.__ssn)
except AttributeError as e:
    print("Error accessing private variable directly:", e)

# Accessing private variable using name mangling — Works, but not recommended
print("Private variable via name mangling:", emp._Employee__ssn)

# Accessing all variables from inside the class (works fine)
emp.display_info()
