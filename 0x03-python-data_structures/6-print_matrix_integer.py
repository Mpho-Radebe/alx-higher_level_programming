#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(0, len(row) - 1):
            print("{}".format(row[i]), end=" ")
        if len(row) > 0:
            print("{}".format(row[-1]))
        else:
            print()
