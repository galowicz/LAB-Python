#!/usr/bin/env python3
from pathlib import Path
import sys
def del_words(fpath):
	excluded_words = ["i", "oraz", "nigdy", "dlaczego"]
	replace_by = ["oraz1", "i", "prawie nigdy", "czemu"]


	if len(excluded_words) != len(replace_by):
		print("arrays have not equal length")
		exit(False)


	#read text file
	f = open(fpath,'r')
	lines = f.readlines()
	f.close()
	
	for i in range(0,len(excluded_words)):
		newlines = []
		for line in lines:
			newline = ""
			for word in line.split():
					if word == excluded_words[i]:
						newline = newline + " " + replace_by[i]
					else:
						newline = newline + " " + word
			#newline = newline + "\n"
			newlines.append(newline)
		lines = newlines
		
						
	#save to file
	f = open(fpath+"new", 'w')
	for line in lines:
		f.write("{}\n".format(line))
	f.close()



if __name__ == '__main__':
	for i in range(1,len(sys.argv)):
		del_words(sys.argv[i])