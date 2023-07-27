def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        last = row[-1]
        if last == "":
            row.pop
        for num in row:
            print(str.format("{:d}", num), end=" ")
        print()