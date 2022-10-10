#!/usr/bin/env python3
from pathlib import Path
def list_files(file):
	for child in file.iterdir():
		if child.is_dir():
			list_files(child)
		else:
			print(child)
	
if __name__ == '__main__':
	dev = Path("/dev")
	list_files(dev)