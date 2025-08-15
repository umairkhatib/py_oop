class Bank:
    # Class variable shared by all instances
    bank_name = "Bank Alfalah"
    
    def __init__(self, customer_name):
        self.customer_name = customer_name
    
    @classmethod
    def change_bank_name(cls, new_name):
        """Class method to modify the bank name for all instances"""
        cls.bank_name = new_name
    
    def display(self):
        """Display customer and bank information"""
        print(f"Customer: {self.customer_name}")
        print(f"Bank: {self.bank_name}")
        print("-" * 30)

# Demonstration
if __name__ == "__main__":
    # Create instances with original bank name
    customer1 = Bank("Umair")
    customer2 = Bank("Ali")
    
    print("Original bank name:")
    customer1.display()
    customer2.display()
    
    # Change the bank name using class method
    Bank.change_bank_name("Meezan Bank")
    
    print("\nAfter changing bank name:")
    customer1.display()  # Shows new name
    customer2.display()  # Shows new name
    
    # New instance created after the change
    customer3 = Bank("Kamran")
    print("\nNew customer after name change:")
    customer3.display()  # Also shows new name