# Python program to find sum of array

def array_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total

# Example array
arr = [1, 2, 3, 4, 5]

print("Array:", arr)
print("Sum of array elements:", array_sum(arr))
