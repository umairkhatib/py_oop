#Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    
    def display_info(self):
        print(f"Employee {self.emp_id}: {self.name}")

class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employees = []  # Aggregation: Stores Employee references
    
    def add_employee(self, employee):
        """Adds an existing Employee to the department"""
        self.employees.append(employee)
    
    def list_employees(self):
        print(f"\nEmployees in {self.dept_name}:")
        for emp in self.employees:
            emp.display_info()  # Uses Employee's method

# Implementation
if __name__ == "__main__":
    # Create independent Employee objects
    emp1 = Employee("Alice", 1001)
    emp2 = Employee("Bob", 1002)
    
    # Create Department
    hr_department = Department("Human Resources")
    
    # Add existing employees to department (aggregation)
    hr_department.add_employee(emp1)
    hr_department.add_employee(emp2)
    
    # Show department roster
    hr_department.list_employees()
    
    # Employees still exist independently
    print("\nIndependent employee access:")
    emp1.display_info()