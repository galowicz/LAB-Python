#!/usr/bin/env python3
from pathlib import Path
def read_file(fpath: Path):
	with open(fpath, 'r') as f:
		lines = f.readlines()
	return lines

def save_file(fpath: Path,lines:list):
	with open(fpath.with_suffix('.txt'), 'w') as f:
		for line in lines:
			f.write("{}\n".format(line))