"""Create four classes:
A with a method show(),
B and C that inherit from A and override show(),
D that inherits from both B and C.
Create an object of D and call show() to observe MRO."""
class A:
    def show(self):
        print("A's show()")

class B(A):
    def show(self):
        print("B's show()")

class C(A):
    def show(self):
        print("C's show()")

class D(B, C):  # Multiple inheritance
    pass

# Create object and observe MRO
if __name__ == "__main__":
    d = D()
    d.show()  # Which show() gets called?
    
    # Print Method Resolution Order
    print("\nMethod Resolution Order (MRO):")
    print(D.__mro__)