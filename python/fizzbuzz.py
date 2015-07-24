#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/home/showboat/anaconda3/bin/python
# Uses local anaconda python3 instead of system
# Copyright Jakob Lagerstedt, Swedish University of Agricultural Sciences
#
# Licensed under the MIT license;

import unittest
import smtplib
import sys

class TestFizzBuzz(unittest.TestCase):
	def setUp(self):
		self.correct_sequence = [1, 2, "Fizz", 4, 
		"Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, 
		"Fizz", 13, 14, "Fizz Buzz", 16, 17, "Fizz", 
		19, "Buzz", "Fizz", 22, 23, "Fizz", "Buzz", 
		26, "Fizz", 28, 29, "Fizz Buzz", 31, 32, 
		"Fizz", 34, "Buzz", "Fizz"]
		
	def tearDown(self):
		print("\nRan tests for these outputs \n")
		self.i = 0
		self.new_out = ""
		while (self.i <= len(str(self.correct_sequence))):
			self.new_out += '\t' + str(self.correct_sequence)[self.i:self.i+40] + '\n'
			self.i += 40
		print(self.new_out)

	def test_1_to_36(self):
		for i in range(1, len(self.correct_sequence)):
			self.assertEqual(fizzbuzz(i), self.correct_sequence[i-1])

def fizzbuzz(i):
	if i % 15 == 0.:
		return 'Fizz Buzz'
	elif i % 5 == 0.:
		return 'Buzz'
	elif i % 3 == 0.:
		return 'Fizz'
	else:
		return i

if(__name__ == '__main__'):
	# for i in range(1, 101):
	# 	print(fizzbuzz(i))
	print sys
	print smtplib
	import time
	import datetime
	import ogr
	# Run tests to see if our fizzbuzz is correct
	unittest.main()

