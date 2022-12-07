#!/usr/bin/env python3
# from cw1 import printComplex

import unittest
import sys
import os
sys.path.insert(0, '..')
# sys.path.append('..')
from cw1 import calc_roots

class TestComplex(unittest.TestCase):
	def test_root(self):
		out = calc_roots(1,-2, 1)
		correct = [1,1]
		self.assertEqual(correct, out)

	def test_roots(self):
		out = calc_roots(1,-2, 0)
		correct = [0,2]
		self.assertEqual(correct, out)

if __name__ == "__main__":
	unittest.main()
