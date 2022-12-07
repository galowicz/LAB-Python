#!/usr/bin/env python3
# from cw1 import printComplex

import unittest
import sys
import os
sys.path.insert(0, '..')
# sys.path.append('..')
from cw2 import sort_arr
class test_sort(unittest.TestCase):
	def test_int(self):
		arr = [5,1,4,7,2]
		out = sort_arr(arr)
		correct = [1,2,4,5,7]
		self.assertEqual(correct, out)
	def test_float(self):
		arr = [5.1,1.5,4.7,7.3,2.2]
		out = sort_arr(arr)
		correct = [1.5,2.2,4.7,5.1,7.3]
		self.assertEqual(correct, out)
	def test_char(self):
		arr = ['a','d','F','#','2']
		out = sort_arr(arr)
		correct = ['#','2','F','a','d']
		self.assertEqual(correct, out)
	def test_str(self):
		arr = ['str1','str3','str2','str#','str']
		out = sort_arr(arr)
		correct = ['str','str#','str1','str2','str3']
		self.assertEqual(correct, out)
if __name__ == "__main__":
	unittest.main()
