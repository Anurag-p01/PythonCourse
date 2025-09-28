def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0   # First Fibonacci number
    elif n == 2:
        return 1   # Second Fibonacci number
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

# Example usage:
n = 10
print(f"The {n}th Fibonacci number is:", fibonacci(n))
