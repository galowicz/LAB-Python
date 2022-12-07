#!/usr/bin/env python3
from pathlib import Path
import sys
import argparse
import numpy as np

def sub_matrix(matrix, row, column):
    sub_matrix = matrix[:]
    sub_matrix = np.delete(sub_matrix, 0, axis=0) 
    sub_matrix = np.delete(sub_matrix, column, axis = 1) 
    return sub_matrix

def matrix_det(matrix):
	rows = len(matrix)
	cols = len(matrix[0])

	if rows != cols:
		raise ValueError("matrix not square")
		return

	if rows == 1:
		return matrix[0][0]
	elif rows == 2:	
		return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
	else:
		det = 0
		for col in range(cols):
			sign = (-1) ** (0 + col)
			det += sign * matrix[0][col] * matrix_det(sub_matrix(matrix, 0, col))
		return det

randomMatrix = np.random.randint(3, size=(8, 8))
determinant = matrix_det(randomMatrix)
print (randomMatrix)
print ('\n determinant = ',determinant)