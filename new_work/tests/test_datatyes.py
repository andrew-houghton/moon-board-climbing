import unittest

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from climb import Hold
import climb

class TestHoldType(unittest.TestCase):

	def test_load_data(self):
		example_hold = Hold('website_format','A12')
		self.assertEqual(example_hold.row,12)
		self.assertEqual(example_hold.col,1)

	def test_climb_utilities(self):
		self.assertEqual(climb._character_to_int('A'),1)
		self.assertEqual(climb._character_to_int('a'),1)
		self.assertEqual(climb._character_to_int('b'),2)
		self.assertEqual(climb._int_to_char(1),'A')
		self.assertEqual(climb._int_to_char(2),'B')

	def test_website_format(self):
		for holdname in ['A12','A1','D8']:
			example_hold = Hold('website_format',holdname)
			self.assertEqual(example_hold.as_website_format(),holdname)

if __name__ == '__main__':
	unittest.main(verbosity = 2)
