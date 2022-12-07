#!/usr/bin/env python3
# from cw1 import printComplex
import unittest
import sys
import os
sys.path.insert(0, '..')
# sys.path.append('..')
from cw1 import Complex

class TestComplex(unittest.TestCase):
	def test_add(self):
		l = Complex(1, 1)
		r = Complex(2, 1)
		out = l + r
		correct = Complex(3, 2)
		self.assertEqual(correct, out)
	def test_subtract(self):
		l = Complex(1, 1)
		r = Complex(2, 1)
		out = l - r
		correct = Complex(-1, 0)
		self.assertEqual(correct, out)
	def test_multiply(self):
		l = Complex(1, 1)
		r = Complex(2, 1)
		out = l * r
		correct = Complex(1, 3)
		self.assertEqual(correct, out)
	def test_division(self):
		l = Complex(1, 1)
		r = Complex(2, 1)
		out = l / r
		correct = Complex(0.6, 0.2)
		self.assertEqual(correct, out)

if __name__ == "__main__":
	unittest.main()
