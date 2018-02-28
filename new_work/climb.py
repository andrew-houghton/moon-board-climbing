def _character_to_int(character):
    # Eg;
    # a or A --> 1
    # b or B --> 2
    return ord(character.upper())-64

def _int_to_char(integer):
    return chr(integer+64)

class Hold():
    def __init__(self, input_type, hold_input):
        if input_type == 'website_format':
            self.col=_character_to_int(hold_input[0])
            self.row=int(hold_input[1:])
        else:
            self.col = None
            self.row = None


    def as_nn_format(self):
        return ''

    def as_website_format(self):
        return _int_to_char(self.row) + str(self.col)

    def __repr__(self):
        return self.as_website_format()
