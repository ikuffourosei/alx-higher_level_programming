#!/usr/bin/python3

"""module to divide the matrix elements
"""
def matrix_divided(matrix, div):
    """
    A function that divides the elements of a matrix

    Args:
        matrix: the matrix 
        div: (int or float)
    Return:
        A new matrix
    Raise:
        TypeError: matrix must be a list of lists (int or float)
        TypeError: Each row of the matrix must have the same size
        TypeError: ''div'' must be a number
        ZeroDivisionError: div should not be 0
    """
    if not isinstance(matrix, list):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ValueError('division by zero')
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    new_matrix = [] #initialize the empty matrix
    for row in range(len(matrix)):
        row_matrix = [] #initialize the row matrix
        for col in range(row_len):
            result = round((matrix[row][col] / div), 2)
            row_matrix.append(result)
        new_matrix.append(row_matrix)
    return new_matrix
