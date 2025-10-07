n = int(input("Enter a number: "))
sum_sq = 0

for i in range(1, n + 1):
    sum_sq += i * i   # or i**2

print("Sum of squares of first", n, "natural numbers is:", sum_sq)
