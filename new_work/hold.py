_lower_chr_base = 64
_upper_chr_base = 96

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
            self.col=_character_to_int(hold_input[0])
            self.row=int(hold_input[1:])
        else:
            self.col = None
            self.row = None


    def as_nn_format(self):
        row_char=chr(_lower_chr_base+self.row)
        col_char=chr(_upper_chr_base+self.col)
        return col_char+row_char

    def as_website_format(self):
        return _int_to_char(self.col) + str(self.row)

    def __repr__(self):
        return self.as_website_format()
