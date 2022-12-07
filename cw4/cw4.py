#!/usr/bin/env python3
from pathlib import Path
import sys
import argparse
import numpy as np

def matrix_sum(m1,m2):
	return m1 + m2
if __name__ == '__main__':
	v1 = np.random.randint(10,size=(128,128))
	v2 = np.random.randint(10,size=(128,128))
	print(v1)
	print(v2)
	print (matrix_sum(v1, v2))