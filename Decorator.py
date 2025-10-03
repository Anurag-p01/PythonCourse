# This is a decorator
def my_decorator(func):
    def wrapper():
        print("Before the function runs...")
        func()
        print("After the function runs...")
    return wrapper

# Apply decorator
@my_decorator
def say_hello():
    print("Hello, World!")

# Call the decorated function
say_hello()
