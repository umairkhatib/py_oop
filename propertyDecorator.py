class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Private attribute

    # Getter (property)
    @property
    def price(self):
        print("Getting price...")
        return self._price

    # Setter
    @price.setter
    def price(self, new_price):
        print("Updating price...")
        if new_price >= 0:
            self._price = new_price
        else:
            raise ValueError("Price cannot be negative!")

    # Deleter
    @price.deleter
    def price(self):
        print("Resetting price...")
        self._price = None

# Demonstration
if __name__ == "__main__":
    laptop = Product("Laptop", 999.99)
    
    # Get price (uses @property)
    print(f"Current price: ${laptop.price}")  
    
    # Set price (uses @price.setter)
    laptop.price = 899.99  
    print(f"Discounted price: ${laptop.price}")  
    
    # Try invalid price
    try:
        laptop.price = -100  # Triggers ValueError
    except ValueError as e:
        print(f"Error: {e}")
    
    # Delete price (uses @price.deleter)
    del laptop.price
    print(f"After deletion: {laptop.price}")  # None