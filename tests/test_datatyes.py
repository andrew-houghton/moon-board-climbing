#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import os
import sys
import_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/types'
sys.path.append(import_path)

from hold import Hold
import hold
from PIL import Image


class TestHoldType(unittest.TestCase):

    # This class tests all the functions of the Hold type.
    def test_load_data(self):
        example_hold = Hold('website_format', 'A12')
        self.assertEqual(example_hold.row, 12)
        self.assertEqual(example_hold.col, 1)

    def test_climb_utilities(self):
        self.assertEqual(hold._character_to_int('A'), 1)
        self.assertEqual(hold._character_to_int('a'), 1)
        self.assertEqual(hold._character_to_int('b'), 2)
        self.assertEqual(hold._int_to_char(1), 'A')
        self.assertEqual(hold._int_to_char(2), 'B')

    def test_website_format(self):
        for holdname in ['A12', 'A1', 'D8']:
            example_hold = Hold('website_format', holdname)
            self.assertEqual(example_hold.as_website_format(), holdname)

    def test_nn_format(self):
        hold_input = ['A1', 'A2', 'B1']
        hold_output = ['Aa', 'Ab', 'Ba']

        for holdname, formatted in zip(hold_input, hold_output):
            example_hold = Hold('website_format', holdname)
            self.assertEqual(example_hold.as_nn_format(), formatted)

    def test_invalid_input(self):
        self.assertRaises(ValueError, Hold, 'website_format', 'A0')
        self.assertRaises(ValueError, Hold, 'website_format', 'A99')
        self.assertRaises(ValueError, Hold, 'website_format', 'A')
        self.assertRaises(IndexError, Hold, 'website_format', '')
        self.assertRaises(ValueError, Hold, 'website_format', 1)

from climb import Climb


class TestClimbType(unittest.TestCase):

    # This class tests all the functions of the Climb type.
    def test_load_data(self):
        example_climb_info = {'Grade': '8A', 'UserRating': 0, 'Moves': [
            'G2', 'J7', 'J8', 'D8', 'D10', 'A5', 'A13', 'F6', 'D16', 'C18']}
        example_climb = Climb('json', example_climb_info)
        self.assertEqual(example_climb.grade.as_font_grade(), '8A')
        self.assertEqual(example_climb.rating, 0)

        # Check that the first hold was input properly
        self.assertEqual(example_climb.holds[0].row, 2)
        self.assertEqual(example_climb.holds[0].col, 7)
        self.assertEqual(len(example_climb.holds), 10)

    def test_nn_string(self):
        example_climb_info = {'Grade': '8A', 'UserRating': 0, 'Moves': [
            'G2', 'J7', 'J8', 'D8', 'D10', 'A5', 'A13', 'F6', 'D16', 'C18']}
        example_climb = Climb('json', example_climb_info)
        self.assertEqual(
            example_climb.moves_nn_string(),
            'GbJgJhDhDjAeAmFfDpCr')

    def test_image_creation(self):
        # Bottom row (non symmetrical image test)
        example_climb_info1 = {'Grade': '8A', 'UserRating': 0, 'Moves': ['A1', 'B1', 'C1']}
        example_climb1 = Climb('json', example_climb_info1)
        example_image1 = example_climb1.as_image()

        stored_sample1 = Image.open('test_image1.png')
        self.assertEqual(stored_sample1.tobytes(), example_image1.tobytes())

        # 4 corners test
        example_climb_info2 = {'Grade': '8A', 'UserRating': 0, 'Moves': ['A1', 'K1', 'A18', 'K18']}
        example_climb2 = Climb('json', example_climb_info2)
        example_image2 = example_climb2.as_image()

        stored_sample2 = Image.open('test_image2.png')
        self.assertEqual(stored_sample2.tobytes(), example_image2.tobytes())

    def test_image_loading(self):
        stored_sample1 = Image.open('test_image1.png')
        example_climb1 = Climb('image', stored_sample1)

        self.assertEqual(example_climb1.moves_nn_string(), 'AaBaCa')
        self.assertEqual(example_climb1.grade, None)
        self.assertEqual(example_climb1.rating, None)

        stored_sample2 = Image.open('test_image2.png')
        example_climb2 = Climb('image', stored_sample2)
        self.assertEqual(example_climb2.moves_nn_string(), 'AaKaArKr')

    def test_image_loading_invalid(self):
        # Pixels outside of range in image
        # They should not be loaded and the climb should not have any holds
        stored_sample = Image.open('test_image3.png')
        example_climb = Climb('image', stored_sample)
        self.assertEqual(example_climb.moves_nn_string(), '')


from climbset import Climbset


def new_climbset():
    example_climb_info = {'Grade': '8A', 'UserRating': 0, 'Moves': [
        'G2', 'J7', 'J8', 'D8', 'D10', 'A5', 'A13', 'F6', 'D16', 'C18']}
    example_climb = Climb('json', example_climb_info)
    example_climb_info2 = {'Grade': '7A', 'UserRating': 0, 'Moves': [
        'G3', 'J7', 'J8', 'D8', 'D10', 'A5', 'A13', 'F6', 'D16', 'C18']}
    example_climb2 = Climb('json', example_climb_info2)
    example_climb_info3 = {'Grade': '6C', 'UserRating': 0, 'Moves': [
        'G4', 'J7', 'J8', 'D8', 'D10', 'A5', 'A13', 'F6', 'D16', 'C18']}
    example_climb3 = Climb('json', example_climb_info3)
    example_climb_list = [example_climb, example_climb2, example_climb3]
    return Climbset(example_climb_list)


class TestClimbsetType(unittest.TestCase):

    # This class tests all the functions of the Climbset type.
    def test_load_data(self):
        example_climbset = new_climbset()

        # Check all 3 climbs were imported
        self.assertEqual(len(example_climbset.climbs), 3)

        # Check that the first move of the first climb was imported correctly
        first_move = example_climbset.climbs[0].holds[0].as_website_format()
        self.assertEqual(first_move, 'G2')

        # Check all the grades were input right
        self.assertEqual(example_climbset.climbs[0].grade.as_font_grade(), '8A')
        self.assertEqual(example_climbset.climbs[1].grade.as_font_grade(), '7A')
        self.assertEqual(example_climbset.climbs[2].grade.as_font_grade(), '6C')

    # Test string generatino stuff
    def test_pre_format(self):
        example_climbset = new_climbset()
        self.assertEqual(
            example_climbset.pre_grade_string(),
            'ÓGbJgJhDhDjAeAmFfDpCr_ÍGcJgJhDhDjAeAmFfDpCr_ËGdJgJhDhDjAeAmFfDpCr_')

    def test_post_format(self):
        example_climbset = new_climbset()
        self.assertEqual(
            example_climbset.post_grade_string(),
            'GbJgJhDhDjAeAmFfDpCrÓ_GcJgJhDhDjAeAmFfDpCrÍ_GdJgJhDhDjAeAmFfDpCrË_')

    def test_no_format(self):
        example_climbset = new_climbset()
        self.assertEqual(
            example_climbset.no_grade_string(),
            'GbJgJhDhDjAeAmFfDpCr_GcJgJhDhDjAeAmFfDpCr_GdJgJhDhDjAeAmFfDpCr_')

    def test_post_grade_sample(self):
        example_post_string = ['ChDlHnGjErÊ', 'JbIeDhDjCmEoBrÊ', 'FeHhJhHkEjEmEnIhEoDqErÌ']
        loaded_climbset = Climbset(example_post_string, 'sample')

        # Check all climbs were added
        self.assertEqual(len(loaded_climbset.climbs), 3)

        first_climb = loaded_climbset.climbs[0]

        # Check climb 0 grade
        self.assertEqual(first_climb.grade.as_font_grade(), '6B+')
        # Check climb 0 number of holds
        self.assertEqual(len(first_climb.holds), 5)
        # Check climb 0 holds
        self.assertEqual(first_climb.holds[0].as_nn_format(), 'Ch')
        self.assertEqual(first_climb.holds[1].as_nn_format(), 'Dl')
        self.assertEqual(first_climb.holds[2].as_nn_format(), 'Hn')
        self.assertEqual(first_climb.holds[3].as_nn_format(), 'Gj')
        self.assertEqual(first_climb.holds[4].as_nn_format(), 'Er')

    def test_pre_grade_sample(self):
        example_pre_string = ['ÊChDlHnGjEr', 'ÊJbIeDhDjCmEoBr', 'ÌFeHhJhHkEjEmEnIhEoDqEr']
        loaded_climbset = Climbset(example_pre_string, 'sample')

        # Check all climbs were added
        self.assertEqual(len(loaded_climbset.climbs), 3)

        first_climb = loaded_climbset.climbs[0]

        # Check climb 0 grade
        self.assertEqual(first_climb.grade.as_font_grade(), '6B+')
        # Check climb 0 number of holds
        self.assertEqual(len(first_climb.holds), 5)
        # Check climb 0 holds
        self.assertEqual(first_climb.holds[0].as_nn_format(), 'Ch')
        self.assertEqual(first_climb.holds[1].as_nn_format(), 'Dl')
        self.assertEqual(first_climb.holds[2].as_nn_format(), 'Hn')
        self.assertEqual(first_climb.holds[3].as_nn_format(), 'Gj')
        self.assertEqual(first_climb.holds[4].as_nn_format(), 'Er')

    def test_no_grade_sample(self):
        example_no_string = ['ChDlHnGjEr', 'JbIeDhDjCmEoBr', 'FeHhJhHkEjEmEnIhEoDqEr']
        loaded_climbset = Climbset(example_no_string, 'sample')

        # Check all climbs were added
        self.assertEqual(len(loaded_climbset.climbs), 3)

        first_climb = loaded_climbset.climbs[0]

        # Check climb 0 grade
        self.assertEqual(first_climb.grade, None)

        # Check climb 0 number of holds
        self.assertEqual(len(first_climb.holds), 5)
        # Check climb 0 holds
        self.assertEqual(first_climb.holds[0].as_nn_format(), 'Ch')
        self.assertEqual(first_climb.holds[1].as_nn_format(), 'Dl')
        self.assertEqual(first_climb.holds[2].as_nn_format(), 'Hn')
        self.assertEqual(first_climb.holds[3].as_nn_format(), 'Gj')
        self.assertEqual(first_climb.holds[4].as_nn_format(), 'Er')


from grade import Grade


class TestGradeType(unittest.TestCase):

    def test_grade_input(self):
        grades = ['6A', '6A+', '6B+', '6C', '6C+', '7A', '7A+',
                  '7B', '7B+', '7C', '7C+', '8A', '8A+', '8B', '8B+']
        nn_grade_chars = ['È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö']

        for grd, nn_grd in zip(grades, nn_grade_chars):
            grd_obj = Grade(grd)
            self.assertEqual(grd_obj.as_nn_grade(), nn_grd)

    def test_nn_grade_input(self):
        example_grade = Grade('È')
        self.assertEqual(example_grade.grade_number, 0)

if __name__ == '__main__':
    # unittest.main(verbosity=2)
    unittest.main(verbosity=1)
