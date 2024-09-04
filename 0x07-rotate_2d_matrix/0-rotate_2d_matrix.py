#!/usr/bin/python3
""" 0-rotate_2d_matrix """


def rotate_2d_matrix(matrix):
    """ This function rotates a matrix clockwise """
    or_matrix = [[n for n in row] for row in matrix]
    column = len(matrix)
    row = len(matrix)

    for i in range(column):
        for j in range(row):
            matrix[i][j] = or_matrix[column - j - 1][i]
