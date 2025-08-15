# Base class: Person
class Person:
    """
    Person class represents a basic person with a name.
    """

    def __init__(self, name):
        """
        Constructor to initialize the person's name.
        """
        self.name = name


# Derived class: Teacher (inherits from Person)
class Teacher(Person):
    """
    Teacher class inherits from Person and adds a subject field.
    """

    def __init__(self, name, subject):
        """
        Constructor for Teacher:
        - Calls the base class constructor using super()
        - Adds subject as an additional field
        """
        super().__init__(name)  # Call the base class constructor
        self.subject = subject

    def display_info(self):
        """
        Display the teacher's information.
        """
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")


# Example usage
teacher1 = Teacher("umair Khatib", "python")
teacher1.display_info()
