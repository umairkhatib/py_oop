#Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.
class Countdown:
    def __init__(self, start):
        """Initialize with starting number"""
        self.start = start + 1  # +1 because we decrement first in __next__

    def __iter__(self):
        """Returns the iterator object (self)"""
        return self

    def __next__(self):
        """Returns next value in countdown"""
        self.start -= 1
        if self.start < 0:
            raise StopIteration  # Signals end of iteration
        return self.start

# Test the countdown
if __name__ == "__main__":
    print("Manual iteration:")
    countdown = Countdown(3)
    it = iter(countdown)
    print(next(it))  # 3
    print(next(it))  # 2
    print(next(it))  # 1
    print(next(it))  # StopIteration raised

    print("\nFor loop iteration:")
    for number in Countdown(5):
        print(f"T-minus {number}")