#!/usr/bin/env python3

import cw1
import sys
import io

class dw1_test:
	old_stdout 
	buffer
	
	def set_stdout(self):
		old_stdout = sys.stdout # Memorize the default stdout stream
		sys.stdout = buffer = io.StringIO()
	def test_printing():
		set_stdout()
		print_hello()
		if (buffer == "hello world"):
			unset_stdout()
			print()
		else:
			return False

if __name__ == '__main__':
# old_stdout = sys.stdout # Memorize the default stdout stream
# sys.stdout = buffer = io.StringIO()

	dw1_test().test_printing()