# Dog class represents a dog with a name and breed
class Dog:
    """
    Dog class with instance variables 'name' and 'breed'
    and an instance method 'bark'.
    """

    def __init__(self, name, breed):
        """
        Constructor to initialize the dog's name and breed.
        """
        self.name = name
        self.breed = breed

    def bark(self):
        """
        Instance method to make the dog 'bark'.
        Prints a message including the dog's name.
        """
        print(f"{self.name} says: Woof! Woof!")


# Example usage
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

dog1.bark()  # Output: Buddy says: Woof! Woof!
dog2.bark()  # Output: Max says: Woof! Woof!
