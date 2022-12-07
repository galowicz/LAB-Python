#!/usr/bin/env python3
from pathlib import Path
import sys
import argparse
from file_op import read_file,save_file

def compare_words(old:str, new:str):
	punctuation = [',','.','?','!','"',"'",'(',')','\n','\t','/','\\']
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


def replace_words(lines : list, words : dict):

	newlines = []
	for line in lines:
		newline = ""
		for word in line.split():
			replaced = 0
			for excluded,replace in words.items():
				if compare_words(word,excluded):
					newline = newline + " " + replace
					replaced = 1
					break
				else:
					replaced = 0
			if not replaced :
				newline = newline + " " + word	
		newlines.append(newline)

	return newlines
if __name__ == '__main__':
	
	parser = argparse.ArgumentParser(description="remove words from textfile")
	parser.add_argument('file',metavar="file", type=str,help="file to clean",nargs='+')

	args = parser.parse_args()
	#print(args.file)

	for plik in args.file:
		readlines = read_file(Path(plik))
		wynik = replace_words(readlines, {'i':"oraz", "oraz": "i", "nigdy":"prawie nigdy", "dlaczego": "czemu"})
		save_file(Path(plik), wynik)