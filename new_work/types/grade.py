_valid_grades = {
    '6A': 0,
    '6A+': 1,
    '6B+': 2,
    '6C': 3,
    '6C+': 4,
    '7A': 5,
    '7A+': 6,
    '7B': 7,
    '7B+': 8,
    '7C': 9,
    '7C+': 10,
    '8A': 11,
    '8A+': 12,
    '8B': 13,
    '8B+': 14}


class Grade():

    def __init__(self, grade):
        # Initialize a new grade object starting with a font format grade.
        if not grade in _valid_grades.keys():
            raise ValueError('Invalid grade. Not in grade list. Grade should be something like 7C.')
        self.grade_number = _valid_grades[grade]

    def as_v_grade(self):
        # Convert the grade of a climb to V grade format
        return 'Not implemented'

    def as_font_grade(self):
        for grd in _valid_grades.keys():
            if _valid_grades[grd] == self.grade_number:
                return grd
        raise Exception('Invalid grade number. Font grade not found.')

    def as_nn_grade(self):
        # Convert the grade of the climb to a single ascii character
        # (most grades look like E with an accent or something like that)
        
        asci_grade_base_num = 200
        return chr(asci_grade_base_num + self.grade_number)
