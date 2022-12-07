#!/usr/bin/env python3
from pathlib import Path
import sys
import argparse

def compare_words(old:str, new:str):
	punctuation = [',','.','?','!','"',"'",'(',')']
	tmp = old
	for i in punctuation:
		tmp = tmp.replace(i, '')
	#print(tmp.lower())
	#print('\t' + new + '\n')
	
	if tmp.lower() == new:
		# print('\t\ty')
		return True
	else: 
		# print('\t\tn')
		return False

def read_file(fpath: Path):
	with open(fpath, 'r') as f:
		lines = f.readlines()
	return lines

def save_file(fpath: Path,lines:list):
	with open(fpath.with_suffix('.txt'), 'w') as f:
		for line in lines:
			f.write("{}\n".format(line))

def del_words(lines : list, excluded_words : set):
	
	for excluded in excluded_words:
		newlines = []
		for line in lines:
			newline = ""
			for word in line.split():
					if compare_words(word,excluded):
						continue
					else:
						newline = newline + " " + word
			#newline = newline + "\n"
			newlines.append(newline)
		lines = newlines

	return lines


if __name__ == '__main__':
	# for i in range(1,len(sys.argv)):
	# 	# if not jpg2png(sys.argv[i]):
	# 	# 	print("failed to convert file:", sys.argv[i])
	# 	jpg2png(Path(sys.argv[i]))

	parser = argparse.ArgumentParser(description="remove words from textfile")
	parser.add_argument('file',metavar="file", type=str,help="file to clean",nargs='+')

	args = parser.parse_args()
	print(args.file)

	for i in args.file:
		save_file(Path(i), del_words(read_file(Path(i)),{"się", "oraz", "i", "dlaczego", "nigdy"}))