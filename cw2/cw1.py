#!/usr/bin/env python3
from pathlib import Path
# import os

def count_files(file):
	# file = Path(path)
	count = 0
	for child in file.iterdir():
		if child.is_dir():
			count += count_files(child) + 1
		else:
			count+=1
	return count
		

if __name__ == '__main__':
	dev = Path('/dev')
	print(count_files(dev))
