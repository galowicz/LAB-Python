#!/usr/bin/env python3
from pathlib import Path
import sys
import argparse
import numpy as np

def matrix_mul(m1,m2):
	result = np.zeros((len(m1),len(m1)))

	if len(m1[0]) != len(m2):
		raise ValueError("matrices not even")
		return
	for row in range(len(m1[0])):
		for col in range(len(m1)):
			for i in range(len(m2)):
				result[row][col] += m1[row][col] * m2[i][col]
	return result

if __name__ == '__main__':
	v1 = np.random.randint(10,size=(128,128))
	v2 = np.random.randint(10,size=(128,128))
	print(v1)
	print(v2)
	print (matrix_mul(v1, v2))