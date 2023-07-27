def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row:
            print(str.format("{:d}", num), end="")
        print()