# Function to left rotate array by d positions
def left_rotate(arr, d):
    n = len(arr)
    d = d % n  # handle if d > n
    return arr[d:] + arr[:d]

# Example
arr = [1, 2, 3, 4, 5, 6, 7]
d = 2  # rotate by 2 positions
print("Original array:", arr)
print("Array after left rotation:", left_rotate(arr, d))
