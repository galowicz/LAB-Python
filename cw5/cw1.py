#!/usr/bin/env python3
from pathlib import Path
import sys
import argparse
import numpy as np

class Complex:
	def __init__(self, realpart, imaginarypart):
		self.real = realpart
		self.imaginary = imaginarypart

	def conjugate(self):
		self.imaginary = - self.imaginary

	def __add__(self, other):
		return Complex(self.real + other.real, self.imaginary + other.imaginary)

	def __sub__(self, other):
		return Complex(self.real - other.real, self.imaginary - other.imaginary)

	def __mul__(self, other):
		return Complex(
		(self.real * other.real - self.imaginary * other.imaginary),
		(self.real * other.imaginary + self.imaginary * other.real)
				   )
	def __truediv__(self, other):
		divisor = other.real**2 + other.imaginary**2
		return Complex(
		(self.real * other.real + self.imaginary * other.imaginary)/(divisor),
		(self.imaginary * other.real - self.real * other.imaginary)/(divisor)
		)
	def __str__(self):
		if self.imaginary >= 0:
			return "{0} + {1}j".format(self.real, self.imaginary)
		else:
			return "{0} {1}j".format(self.real, self.imaginary)
	def __eq__(self, z2):
		if(self.real == z2.real) and (self.imaginary == z2.imaginary):
			return True
		else:
			return False


def printComplex(complex_number):
	if(complex_number.imaginary >= 0):
		print(complex_number.real, "+", complex_number.imaginary,'j')
	else:
		print(complex_number.real, complex_number.imaginary,'j')

if __name__ == "__main__":
	num1 = Complex(1,1)
	num2 = Complex(2,1)

	add = num1 + num2
	sub = num1 - num2
	mul = num1 * num2
	div = num1 / num2
	printComplex(num1)
	printComplex(num2)
	print('sum:')
	printComplex(add)
	print('sub:')
	printComplex(sub)
	print('mul:')
	printComplex(mul)
	print('div:')
	printComplex(div)