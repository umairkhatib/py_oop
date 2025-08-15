# Logger class demonstrates the use of Constructor (__init__) and Destructor (__del__) in Python.
# The Constructor runs when an object is created.
# The Destructor runs when an object is destroyed.

class Logger:
    """
    Logger class is a simple example to show how constructors and destructors work.
    """

    def __init__(self):
        """
        Constructor:
        Automatically runs when an object of the class is created.
        """
        print("📜 Logger object has been created.")

    def __del__(self):
        """
        Destructor:
        Automatically runs when the object is destroyed (removed from memory).
        """
        print("🗑️ Logger object has been destroyed.")


# Example usage:
print("Before creating the object...")
log = Logger()  # Creating an object, constructor will be called
print("The object is now in use...")
del log  # Manually deleting the object, destructor will be called
print("Program is ending...")
