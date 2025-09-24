# l = [1, 2, 3, 4, 5]
# mean = sum(l) / len(l)
# # print ("mean of the list is : ", mean)
# Program to calculate mean of a list with user input

# Taking input as space-separated numbers
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Calculate mean
mean = sum(numbers) / len(numbers)

print("The mean of the list is:", mean)
