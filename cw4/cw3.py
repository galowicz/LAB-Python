#!/usr/bin/env python3
from pathlib import Path
import sys
import argparse
import numpy as np
def scalar(v1:list,v2:list):
	# if len(v1) != len (v2):
	# 	raise ValueError("vectors need to have same length")
	return v1 * v2

if __name__ == '__main__':
	v1 = np.random.randint(10,size=(5))
	v2 = np.random.randint(10,size=(5))
	print(v1)
	print(v2)
	print(scalar(v1, v2))