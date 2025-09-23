name = input("Enter your name: ")   
age = int(input("Enter your age: "))
if age >= 18:
    print(f"{name}, you are a valid voter")
else:
    print(f"{name}, you are not a valid voter")