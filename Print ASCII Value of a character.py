 # Program to print ASCII value of a character

# taking input from user
char = input("Enter a character: ")

# check if only one character is entered
if len(char) == 1:
    print(f"The ASCII value of '{char}' is:", ord(char))
else:
    print("Please enter only a single character.")
