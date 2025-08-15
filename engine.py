class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def start(self):
        print(f"{self.engine_type} engine started.")

class car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine   # Composition: Car "has-a" Engine

    def start_car(self):
        print(f"starting {self.brand} car......")
        self.engine.start()           # Access Engine's method 

# Create an Engine object
my_engine = Engine("V8")

# Create a Car object with the Engine
my_car = car("Toyota", my_engine)

# Start the car (which uses the Engine's method)
my_car.start_car()
