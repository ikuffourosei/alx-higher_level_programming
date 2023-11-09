#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    mat_len = len(matrix)
    mat_len_2 = len(matrix[0])
    # intialize an empty list
    new_mat = []
    for i in range(mat_len):
        # initialize an empty list to contain rows
        row = []
        for j in range(mat_len_2):
            row.append(matrix[i][j] ** 2)
        new_mat.append(row)
    return new_mat
