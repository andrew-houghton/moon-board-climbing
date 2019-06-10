#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL.PngImagePlugin import PngImageFile

from moon.types.grade import Grade
from moon.types.hold import Hold


class Climb:
    def __init__(self, input_type, input_data):
        # You can either input in json (dictionary) format or in image format.
        # Both of these types can be used to create a new instance.

        if input_type == "json" and type(input_data) == dict:

            # Loop through all the holds in the input and store them as Hold type objects in a list.
            self.holds = []
            for hold_text in input_data["Moves"]:
                next_hold = Hold("website_format", hold_text)
                self.holds.append(next_hold)

            self.rating = input_data["UserRating"]
            self.grade = Grade(input_data["Grade"])  # store the grade as type grade

        elif input_type == "image" and type(input_data) == PngImageFile:
            # Catch invalid image sizes
            if input_data.size != (11, 18):
                print(input_data.size)

            # These fields are not stored with the images so they cannot be restored/initialized.
            self.grade = None
            self.rating = None

            # Loop through every pixel on the image
            # Store all the pixels which are not black as holds
            # Preserver order of moves if possible
            self.holds = []
            pixels = input_data.load()
            for y in range(17, -1, -1):  # loop over rows
                for x in range(11):  # loop over columns (but not columns outside the moon board)
                    if pixels[x, y] != 0:  # select only non black pixels
                        # Add a new hold using the co-ordinates of the pixel
                        next_hold = Hold("tuple", (18 - y, x + 1))
                        self.holds.append(next_hold)
        elif input_type == "sample" and type(input_data) == str and len(input_data) > 1:
            self.rating = None

            # find out if there is a grade character
            nn_grade_chars = [
                "z",
                "x",
                "y",
                "w",
                "u",
                "v",
                "t",
                "s",
                "Z",
                "X",
                "Y",
                "W",
                "U",
                "V",
                "T",
            ]
            if input_data[0] in nn_grade_chars:
                # pre grade climb
                grade_char = input_data[0]
                input_data = input_data[1:]
                self.grade = Grade(grade_char)

            elif input_data[-1] in nn_grade_chars:
                # post grade climb
                grade_char = input_data[-1]
                input_data = input_data[: len(input_data) - 3]
                self.grade = Grade(grade_char)

            else:
                self.grade = None

            # Check that the climb move string is in pairs
            if len(input_data) % 2 != 0:
                raise ValueError("Invalid climb string length, moves should be a pair of holds.")

            self.holds = []

            # Work through the string converting pairs of characters into Holds
            for i in range(0, len(input_data), 2):
                cur_hold = Hold("nn", input_data[i : i + 2])
                self.holds.append(cur_hold)

        else:
            raise ValueError("Invalid input type.")

    def moves_nn_string(self):
        # Turn the moves into a string for use as LSTM input
        return "".join([hold.as_nn_format() for hold in self.holds])

    def as_image(self):
        from PIL import Image

        # Create new blank canvas
        image = Image.new("1", (11, 18))

        im = image.load()

        # Add all the holds to the image
        for hold in self.holds:
            # Subtract 1 to convert row and col to 0 indexed values
            # Subtract from 18 because row 1 is at the bottom
            pixel_y = 18 - (hold.row)
            pixel_x = hold.col - 1
            im[pixel_x, pixel_y] = 1

        # Note: use .save to save the image.
        return image

    def __repr__(self):
        # Create a string representing the class
        return "Moves:{}\nGrade:{}\nRating:{}".format(
            " ".join([i.as_website_format() for i in self.holds]), self.grade, self.rating
        )

    @classmethod
    def valid_input_sample(cls, sample):
        nn_grade_chars = ["z", "x", "y", "w", "u", "v", "t", "s", "Z", "X", "Y", "W", "U", "V", "T"]
        # First check that it is in a valid length range
        if len(sample) < 2:
            return False

        # Remove the grade character from the sample if it exists
        if sample[0] in nn_grade_chars:
            # pre grade climb
            sample = sample[1:]
        elif sample[-1] in nn_grade_chars:
            # post grade climb
            sample = sample[: len(sample) - 1]

        # Check remaining moves/ holds are pairs of characters
        if len(sample) % 2 != 0:
            return False

        for i in range(0, len(sample), 2):
            if not Hold.is_valid_hold(sample[i : i + 2]):
                return False
        return True
