import numpy as np

def get_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Enter the element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)
    return np.array(matrix)

def print_matrix(matrix):
    for row in matrix:
        print(row)

def perform_operation(matrix1, matrix2, operation):
    if operation == '+':
        result = matrix1 + matrix2
    elif operation == '-':
        result = matrix1 - matrix2
    elif operation == '*':
        result = np.dot(matrix1, matrix2)
    elif operation == '/':
        result = np.divide(matrix1, matrix2)
    else:
        print("Invalid operation!")
        return

    print("Result:")
    print_matrix(result)

while True:
    # Get input matrices
    print("Enter the first matrix:")
    matrix1 = get_matrix()

    print("Enter the second matrix:")
    matrix2 = get_matrix()

    # Display inserted matrices
    print("Inserted matrices:")
    print("Matrix 1:")
    print_matrix(matrix1)
    print("Matrix 2:")
    print_matrix(matrix2)

    # Ask user to approve or correct matrices
    approval = input("Do you approve the inserted matrices? (Y/N): ")

    if approval.upper() == "Y":
        # Get operation
        operation = input("Enter the operation (+, -, *, /): ")

        # Perform operation
        perform_operation(matrix1, matrix2, operation)
    else:
        # Ask user to correct matrices
        correction = input("Which matrix would you like to correct? (1/2): ")

        if correction == "1":
            matrix1 = get_matrix()
        elif correction == "2":
            matrix2 = get_matrix()
        else:
            print("Invalid input!")

    repit = input("Would you like to calculate again? (Y/N): ").upper()
    while repit not in ['Y', 'N']:
        print("Invalid input. Please enter 'Y' to continue or 'N' to exit.")
        repit = input().upper()

    if repit == 'N':
        print("Goodbye!\n")
        break
