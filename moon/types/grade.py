#!/usr/bin/env python
# -*- coding: utf-8 -*-

_valid_grades = {
    "6A": 0,
    "6A+": 1,
    "6B": 2,
    "6B+": 3,
    "6C": 4,
    "6C+": 5,
    "7A": 6,
    "7A+": 7,
    "7B": 8,
    "7B+": 9,
    "7C": 10,
    "7C+": 11,
    "8A": 12,
    "8A+": 13,
    "8B": 14,
    "8B+": 15,
}

_to_v_grade = {
    0: "V3",
    1: "V3",
    2: "V4",
    3: "V4",
    4: "V5",
    5: "V5",
    6: "V6",
    7: "V7",
    8: "V8",
    9: "V8",
    10: "V9",
    11: "V10",
    12: "V11",
    13: "V12",
    14: "V13",
    15: "V14",
}

_valid_nn_grades = {
    "z": 0,
    "x": 1,
    "y": 2,
    "w": 3,
    "u": 4,
    "v": 5,
    "t": 6,
    "s": 7,
    "Z": 8,
    "X": 9,
    "Y": 10,
    "W": 11,
    "U": 12,
    "V": 13,
    "T": 14,
}

_nn_grades_inverse = ["z", "x", "y", "w", "u", "v", "t", "s", "Z", "X", "Y", "W", "U", "V", "T"]


class Grade:
    def __init__(self, grade):
        # Initialize a new grade object starting with a font format grade.
        if type(grade) == int:
            self.grade_number = grade
        elif grade not in _valid_grades.keys():
            if grade not in _valid_nn_grades.keys():
                raise ValueError(
                    f"Invalid grade: {grade}. Not in grade list. Grade should be something like 7C."
                )
            else:
                self.grade_number = _valid_nn_grades[grade]
        else:
            self.grade_number = _valid_grades[grade]

    def as_v_grade(self):
        # Convert the grade of a climb to V grade format
        return _to_v_grade[self.grade_number]

    def as_font_grade(self):
        for grd in _valid_grades.keys():
            if _valid_grades[grd] == self.grade_number:
                return grd
        raise Exception("Invalid grade number. Font grade not found.")

    def as_nn_grade(self):
        # Convert the grade of the climb to a single ascii character
        # (most grades look like E with an accent or something like that)
        return _nn_grades_inverse[self.grade_number]

    def __repr__(self):
        return self.as_font_grade()
