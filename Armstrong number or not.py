# Check if a number is an Armstrong number

# Get input from user
num = int(input("Enter a number: "))

# Convert number to string to count digits
num_str = str(num)
num_digits = len(num_str)

# Calculate the sum of digits raised to the power of number of digits
sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)

# Check if the number is an Armstrong number
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
