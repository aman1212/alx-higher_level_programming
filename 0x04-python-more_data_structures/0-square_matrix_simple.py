#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list(map(list, matrix))
    i = len (new_matrix)
    for x in range(0,i):
     y= len(new_matrix[x])
     for z in range(0,y):
      new_matrix [x] [z] = new_matrix [x] [z] ** 2
    return new_matrix
