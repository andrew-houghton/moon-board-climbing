_lower_chr_base = 64
_upper_chr_base = 96
_max_row = 18
_max_col = 11

def _character_to_int(character):
    # Eg;
    # a or A --> 1
    # b or B --> 2
    return ord(character.upper())-_lower_chr_base

def _int_to_char(integer):
    return chr(integer+_lower_chr_base)

class Hold():
    def __init__(self, input_type, hold_input):
        if input_type == 'website_format':
            if type(hold_input) != str:
                raise ValueError('Invalid data type. hold_input should be str.')
            
            self.col=_character_to_int(hold_input[0])
            self.row=int(hold_input[1:])

        elif input_type == 'tuple':
            if type(hold_input) != tuple:
                raise ValueError('Invalid data type. hold_input should be tuple.')
            elif len(hold_input) != 2:
                raise ValueError('Invalid tuple length. hold_input should have length of 2.')

            self.row = int(hold_input[0])
            self.col = int(hold_input[1])
        else:
            raise ValueError('Invalid input type. input_type argument should be a value like "website_format"')

        # Check that the row and column number is in a valid range
        if not self.row in range(1,_max_row+1,1):
            raise ValueError('Row number invalid.')
        if not self.col in range(1,_max_col+1,1):
            raise ValueError('Column invalid.')

    def __repr__(self):
        return self.as_website_format()
    
    def as_nn_format(self):
        row_char=chr(_upper_chr_base+self.row)
        col_char=chr(_lower_chr_base+self.col)
        return col_char+row_char

    def as_website_format(self):
        return _int_to_char(self.col) + str(self.row)

