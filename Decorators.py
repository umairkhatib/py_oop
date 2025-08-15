#Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello()
def log_function_call(func):
    """Decorator that logs when a function is called."""
    def wrapper(*args, **kwargs):
        print("Function is being called")  # Log message
        return func(*args, **kwargs)  # Execute the original function
    return wrapper

# Apply the decorator
@log_function_call
def say_hello(name):
    print(f"Hello, {name}!")

# Test the decorated function
say_hello("Alice")