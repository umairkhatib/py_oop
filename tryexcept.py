#Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.
# 1. Define custom exception
class InvalidAgeError(Exception):
    """Raised when age is below 18"""
    def __init__(self, age):
        self.age = age
        super().__init__(f"Age {age} is invalid. Must be 18+")

# 2. Age validation function
def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    print(f"✅ Age {age} is valid - access granted!")

# 3. Main program with user input
if __name__ == "__main__":
    print("=== Age Verification System ===")
    
    while True:
        try:
            # Get user input
            user_input = input("\nEnter your age (or 'q' to quit): ")
            
            # Exit condition
            if user_input.lower() == 'q':
                print("Goodbye!")
                break
                
            # Convert and validate
            age = int(user_input)
            check_age(age)
            
        except ValueError:
            print("⚠️ Error: Please enter a valid number")
        except InvalidAgeError as e:
            print(f"⚠️ {e}")
            print(f"🔞 Sorry, {e.age} is below the required age\n")