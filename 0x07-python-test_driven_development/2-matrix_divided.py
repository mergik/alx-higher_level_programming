#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Args:
        matrix (list): A list of lists representing the matrix.
                       Each element in the matrix should be an integer
                       or float.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list: A new matrix with all elements divided by `div`, rounded to
        2 decimal places.

    Raises:
        TypeError: If `matrix` is not a list of lists of integers/floats,
                   or if `div` is not a number.
        TypeError: If each row of the matrix does not have the same size.
        ZeroDivisionError: If `div` is equal to 0.
    """
    if not isinstance(matrix, list) or\
            not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
