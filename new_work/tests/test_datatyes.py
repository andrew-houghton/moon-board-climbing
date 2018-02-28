import unittest

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from hold import Hold
import hold

class TestHoldType(unittest.TestCase):

	def test_load_data(self):
		example_hold = Hold('website_format','A12')
		self.assertEqual(example_hold.row,12)
		self.assertEqual(example_hold.col,1)

	def test_climb_utilities(self):
		self.assertEqual(hold._character_to_int('A'),1)
		self.assertEqual(hold._character_to_int('a'),1)
		self.assertEqual(hold._character_to_int('b'),2)
		self.assertEqual(hold._int_to_char(1),'A')
		self.assertEqual(hold._int_to_char(2),'B')

	def test_website_format(self):
		for holdname in ['A12','A1','D8']:
			example_hold = Hold('website_format',holdname)
			self.assertEqual(example_hold.as_website_format(),holdname)

	def test_nn_format(self):
		hold_input = ['A1','A2','B1']
		hold_output = ['aA','aB','bA']

		for holdname, formatted in zip(hold_input,hold_output):
			example_hold = Hold('website_format',holdname)
			self.assertEqual(example_hold.as_nn_format(),formatted)

	def test_invalid_input(self):
		self.assertRaises(ValueError, Hold, 'website_format','A0')
		self.assertRaises(ValueError, Hold,'website_format','A99')
		self.assertRaises(ValueError, Hold,'website_format','A')
		self.assertRaises(IndexError, Hold,'website_format','')
		self.assertRaises(ValueError, Hold,'website_format',1)

if __name__ == '__main__':
	unittest.main(verbosity = 1)
