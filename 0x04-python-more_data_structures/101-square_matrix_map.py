#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map((lambda row: list(map((lambda item: item * item), row))), matrix))
