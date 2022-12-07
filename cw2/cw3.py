#!/usr/bin/env python3
from pathlib import Path
from PIL import Image
import sys
import argparse

def jpg2png(file:Path):
	jpg = Image.open(file)
	jpg.save(file.with_suffix(".png"))
	return 0

if __name__ == '__main__':
	# for i in range(1,len(sys.argv)):
	# 	# if not jpg2png(sys.argv[i]):
	# 	# 	print("failed to convert file:", sys.argv[i])
	# 	jpg2png(Path(sys.argv[i]))

	parser = argparse.ArgumentParser(description="Convert jpg file to png")
	parser.add_argument('file',metavar="file", type=str,help="file to convert",nargs='+')

	args = parser.parse_args()
	print(args.file)

	for i in args.file:
		jpg2png(Path(i))