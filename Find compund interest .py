# Compound Interest Calculator

# Input values
P = float(input("Enter the principal amount: "))
r = float(input("Enter the annual interest rate (in %): ")) / 100
n = int(input("Enter number of times interest applied per year: "))
t = float(input("Enter time in years: "))

# Calculate compound interest
A = P * (1 + r / n) ** (n * t)
CI = A - P

# Output results
print(f"\nFinal Amount (A) = {A:.2f}")
print(f"Compound Interest = {CI:.2f}")
