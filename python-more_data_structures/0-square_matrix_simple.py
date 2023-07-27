def square_matrix_simple(matrix=[]):
    #create an empty list
    square_matrix = []
    # iterate through each row
    for r in matrix:
        #create empty list
        square_row= []
        #iterate through each element in the current row
        for b in r:
            square_value = b ** 2
            square_row .append(square_value)
        #append square row to square matrix
        square_matrix.append(square_row)
    return square_matrix