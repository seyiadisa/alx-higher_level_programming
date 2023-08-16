#!/usr/bin/python3
def print_matrix_integer(matrix=[]):
    if len(matrix) == 0:
        print()
        return None

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            end_string = "" if j == len(matrix[i]) - 1 else " "
            print("{0}".format(matrix[i][j]), end=end_string)
        print()
