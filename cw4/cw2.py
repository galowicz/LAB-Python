#!/usr/bin/env python3
from pathlib import Path
import sys
import argparse
import numpy as np

def sort_arr (unsorted : list ):
	sorted_list = unsorted
	n = len(unsorted)
	for i in range(n):
		for j in range(0, n-i-1):
			if sorted_list[j] > sorted_list[j+1]:
				sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
	
	return sorted_list

if __name__ == '__main__':
	
	# parser = argparse.ArgumentParser(description="calculate roots of quadratic equation")
	# parser.add_argument('a',metavar="a", type=float,help="parameter of quadratic equation",)
	# parser.add_argument('b',metavar="b", type=float,help="parameter of quadratic equation",)

	# arr = np.random.random_sample(size=(20))
	arr = np.random.randint(10,size=(20))
	print(arr)
	sorted_arr = sort_arr(arr)
	print(sorted_arr)
	print(np.sort(arr))