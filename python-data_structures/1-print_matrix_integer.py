def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row:
            print(str.format("{0:2d}", num), end=" ")
        print()