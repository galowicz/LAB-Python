#!/usr/bin/env python3
from pathlib import Path
from PIL import Image
import sys
def jpg2png(file):
	jpg = Image.open(file)
	jpg.save(file+".png")
	return 0

if __name__ == '__main__':
	for i in range(1,len(sys.argv)):
		# if not jpg2png(sys.argv[i]):
		# 	print("failed to convert file:", sys.argv[i])
		jpg2png(sys.argv[i])

