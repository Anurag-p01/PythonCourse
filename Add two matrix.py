# Function to take matrix input from user
def input_matrix(rows, cols):
    print("Enter matrix elements row by row:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter elements of row {i+1}, separated by space: ").split()))
        matrix.append(row)
    return matrix

# Function to add two matrices
def add_matrices(A, B):
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result

# Main program
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nMatrix A:")
A = input_matrix(rows, cols)

print("\nMatrix B:")
B = input_matrix(rows, cols)

# Add matrices
result = add_matrices(A, B)

# Display result
print("\nResultant Matrix after Addition:")
for row in result:
    print(row)
