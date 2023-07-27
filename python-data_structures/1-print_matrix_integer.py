def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row:
            print("".join("{:d}".format(num)))
    print()