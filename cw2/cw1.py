#!/usr/bin/env python3
from pathlib import Path
# import os
if __name__ == '__main__':
	# dev = os.listdir("/dev")
	# print(dev.__sizeof__())
	dev = Path('/dev')
	count = 0
	if dev.is_dir():
		for child in dev.iterdir():
			count+=1
		print(count)
	else:
		print("/dev is not a directory")