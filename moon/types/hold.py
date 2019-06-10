_lower_chr_base = 64
_upper_chr_base = 96
_max_row = 18
_max_col = 11


def _character_to_int(character):
    # Eg;
    # a or A --> 1
    # b or B --> 2
    return ord(character.upper()) - _lower_chr_base


def _int_to_char(integer):
    return chr(integer + _lower_chr_base)


class Hold:
    def __init__(self, input_type, hold_input):
        # Initialize a Hold object
        # Use either the A3 kind of format that the website provides
        # Or use the (row, column) format that comes from image input

        if input_type == "website_format":
            # Check the type/format of the input first
            if not (type(hold_input) == str or type(hold_input) == unicode):
                raise ValueError("Invalid data type. hold_input should be str.")

            self.col = _character_to_int(hold_input[0])
            self.row = int(hold_input[1:])

        elif input_type == "tuple":
            # Check the type/format of the input first
            if type(hold_input) != tuple:
                raise ValueError("Invalid data type. hold_input should be tuple.")
            elif len(hold_input) != 2:
                raise ValueError("Invalid tuple length. hold_input should have length of 2.")

            self.row = int(hold_input[0])
            self.col = int(hold_input[1])
        elif input_type == "nn":
            # Check the type/format of the input first
            if type(hold_input) != str:
                raise ValueError("Invalid data type. hold_input should be str.")
            elif len(hold_input) != 2:
                raise ValueError("Invalid string length. hold_input should have length of 2.")

            self.row = ord(hold_input[1]) - _upper_chr_base
            self.col = ord(hold_input[0]) - _lower_chr_base

        else:
            raise ValueError(
                'Invalid input type. input_type argument should be a value like "website_format"'
            )

        # Check that the row and column number is in a valid range
        if self.row not in range(1, _max_row + 1, 1):
            raise ValueError("Row number {} invalid.".format(self.row))
        if self.col not in range(1, _max_col + 1, 1):
            raise ValueError("Column number {} invalid.".format(self.col))

    def __repr__(self):
        # Use the website format to create human readable string representing the object.
        return self.as_website_format()

    def as_nn_format(self):
        # Convert the hold to 2 characters representing the row and column.
        row_char = chr(_upper_chr_base + self.row)
        col_char = chr(_lower_chr_base + self.col)
        return col_char + row_char

    def as_website_format(self):
        # Output Hold as A12 kind of format
        return _int_to_char(self.col) + str(self.row)

    @classmethod
    def is_valid_hold(cls, move_str):
        if len(move_str) == 2:
            if move_str[0] in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]:
                if move_str[1] in [
                    "a",
                    "b",
                    "c",
                    "d",
                    "e",
                    "f",
                    "g",
                    "h",
                    "i",
                    "j",
                    "k",
                    "l",
                    "m",
                    "n",
                    "o",
                    "p",
                    "q",
                    "r",
                ]:
                    return True
        return False
