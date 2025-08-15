class Car:
    def __init__(self, brand):
        # Public variable
        self.brand = brand
    
    # Public method
    def start(self):
        print(f"The {self.brand} car has started!")

# Instantiate the class
my_car = Car("Changan")

# Access public variable from outside
print("Car brand:", my_car.brand)  # Output: Car brand: Changan

# Call public method from outside
my_car.start()  # Output: The Toyota car has started!