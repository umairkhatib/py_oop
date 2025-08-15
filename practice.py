class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
            print(f"Student Name:{self.name}")
            print(f"Marks:{self.marks}")
            print("-"*20)

if __name__ == "__main__":

            student1=Student("Umair",82)
            student2=Student("Marry",85)
            student3=Student("Kamran",87)

            print("\nDisplaying student Details:")
            student1.display()
            student2.display()
            student3.display()