# This is a decorator
def my_decorrator(func):
    def wrapper():
        print("Before the function runs...")
        func()
        print("After the function runs...")
    return wrapper

# Apply decorator
@my_decorrator
def say_hello():
    print("Hello, World!")

# Call the decorated function
say_hello()
