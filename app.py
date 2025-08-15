class Counter:
    # Class variable to keep track of Student objects
    count = 0

    @classmethod
    def increment(cls):
        """Increments the counter when a new Student is created."""
        cls.count += 1

    @classmethod
    def display_count(cls):
        """Displays the total number of Student objects created."""
        print(f"Total Students created: {cls.count}")

# Define a class named 'Student' to represent a student's information
class Student:
    # Constructor method (__init__) - called when creating a new Student object
    def __init__(self, name, marks):
        """
        Initialize a Student object with name and marks.
        
        Parameters:
        - name (str): The name of the student
        - marks (float/int): The marks obtained by the student
        
        The 'self' keyword refers to the instance of the class.
        It allows us to access and modify the object's attributes.
        """
        # Assign the 'name' parameter to the instance variable 'self.name'
        self.name = name
        
        # Assign the 'marks' parameter to the instance variable 'self.marks'
        self.marks = marks

        # Increment counter when a Student is created
        Counter.increment()


    
    # Method to display student details
    def display(self):
        """
        Prints the student's name and marks in a formatted way.
        
        This method doesn't return anything; it just prints to the console.
        """
        # Print student name with a label
        print(f"Student Name: {self.name}")
        
        # Print student marks with a label
        print(f"Marks: {self.marks}")
        
        # Print a separator line for better readability (20 hyphens)
        print("-" * 20)


# Main program execution (only runs if this script is executed directly)
if __name__ == "__main__":
    # Example 1: Create a student object with name "Umair" and marks 85
    student1 = Student("Umair", 85)
    
    # Example 2: Create a student object with name "Marry" and marks 92
    student2 = Student("Marry", 92)
    
    # Example 3: Create a student object with name "Kamran" and marks 78
    student3 = Student("Kamran", 78)

    # Example 4: Create a student object with name "Abid" and marks 77
    student4 = Student("abid", 77)
    
    # Display details of all students by calling the display() method
    print("\nDisplaying Student Details:")
    student1.display()  # Calls display() for student1
    student2.display()  # Calls display() for student2
    student3.display()  # Calls display() for student3
    student4.display()  # Calls display() for student4


    # Display total students created
    Counter.display_count()