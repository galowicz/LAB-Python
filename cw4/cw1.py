#!/usr/bin/env python3
from pathlib import Path
import sys
import argparse
#import numpy as np
def print_roots(roots : list):
	if roots[0] == roots[1]:
		print("equation has one root at %f"  %roots[0])
		return True
	print("equation has two root points at %f and %f" %(roots[0],roots[1]))


def calc_roots(a : float,b : float,c : float):
	# return 5
	delta = b*b - 4*a*c
	if delta < 0:
		raise ValueError("no real roots")
	x1 = ((-1)*b - delta**(1/2))/(2*a)
	x2 = ((-1)*b + delta**(1/2))/(2*a)
	return [x1,x2]

if __name__ == '__main__':
	
	parser = argparse.ArgumentParser(description="calculate roots of quadratic equation")
	parser.add_argument('a',metavar="a", type=float,help="parameter of quadratic equation",)
	parser.add_argument('b',metavar="b", type=float,help="parameter of quadratic equation",)
	parser.add_argument('c',metavar="c", type=float,help="parameter of quadratic equation",)
	args = parser.parse_args()
	# print(args.a)
	wynik = calc_roots(args.a,args.b, args.c)
	print_roots(wynik)