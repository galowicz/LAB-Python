#!/usr/bin/env python3
from pathlib import Path
import sys
import argparse
import numpy as np
from cw1 import printComplex
from cw1 import Complex
from parse import parse
def Calc(left:Complex, right:Complex, operation):
	# left = left.split()
	# right = right.split()
	# print(left)
	# print(right)
	# left = Complex(int(left[0]), int(left[2].translate({ord('j'): None})))
	# right = Complex(int(right[0]), int(right[2].translate({ord('j'): None})))
	match (operation):
		case '+':
			return left + right
		case '-':
			return left - right
		case '*':
			return left * right
		case '/':
			return left / right
		case _:
			print("unknown operation")
			return Complex(0,0)

if __name__ == "__main__":
	print("Enter input in the format x + yj")
	string = input("Enter your first value: ")
	res = parse('{}+{}j',string)
	num1 = Complex(float(res[0]), float(res[1]))
	operation = input("Enter operation you want to do: ")
	string = input("Enter your second value: ")
	res = parse('{}+{}j',string)
	num2 = Complex(float(res[0]), float(res[1]))
	printComplex(Calc(num1, num2, operation))