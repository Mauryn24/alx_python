#!/usr/bin/env python3
def print_matrix_integer(matrix=[[]]):
    # Check if the matrix is empty
    if not matrix:
        print()
        return

    # Loop through each row in the matrix
    for row in matrix:
        # Loop through each element in the row
        for i, element in enumerate(row):
            # Print the element with proper formatting
            print("{:d}".format(element), end="")
            
            # Print a space unless it's the last element in the row
            if i < len(row) - 1:
                print(" ", end="")
        
        # Move to the next line after printing all elements in the row
        print()