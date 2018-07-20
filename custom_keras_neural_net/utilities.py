
# Encoding constants
padding_character = '_'
climb_seperator = '|'
max_moves = 13
col_char_base = 64
num_base = 96
grade_base = 44

nrows=16
ncols=10


def encode_move(move_str):
    # Turns a move from readable format to LSTM format.
    # EG G2 --> Gb
    return move_str[0] + chr(num_base + int(move_str[1:]))


def encode_grade(grade_str):
    # Turns a grade from readable format to LSTM format.
    return chr(grade_base + int(grade_str))


def decode_move(move_str):
    return move_str[0] + str(ord(move_str[1]) - num_base)


def decode_grade(grade_str):
    return str(ord(grade_str) - grade_base)


def character_represet(climb):
    # turns a climb loaded from a pickle file into LSTM format

    climb_moves = []
    for move in climb['Moves']:
        climb_moves.append(encode_move(move['Description']))

    # create a string from moves
    move_str = ''.join(climb_moves)

    # pad and crop the string
    move_str = move_str[:2 * max_moves].ljust(2 * max_moves, padding_character)

    # create the grade string
    grade_str = encode_grade(climb['Grade'])

    return move_str + grade_str


def character_decode(climb_chars):
    # turns a climb formated for LSTM into a dictionary format
    moves = climb_chars[:max_moves * 2]  # moves section of string
    grade = climb_chars[max_moves * 2]  # last character of string

    move_list = []
    for i in range(0, max_moves * 2, 2):  # go through the string in steps of 2
        # look at a pair of characters (a move)
        current_move = climb_chars[i:i + 2]
        if current_move != '__':  # don't process padding characters
            move_list.append(current_move)
    move_list = [decode_move(i) for i in move_list]

    return {
        'Grade': nn_grade_to_british(grade),
        'Moves': move_list
    }


def nn_grade_to_british(grade):
    # Must write +'s first'
    GradeConv = {
        '9': '8A',
        '8': '7C+',
        '7': '7C',
        '6': '7B+',
        '5': '7B',
        '4': '7A+',
        '3': '7A',
        '2': '6C+',
        '1': '6C',
        '0': '6B+',
    }

    return GradeConv[grade]


def is_valid_climb(climb):
    first_hold = climb['Moves'][0]
    last_hold = climb['Moves'][-1]

    # valid finish hold
    if last_hold[1:] != '18':
        return False
    # valid start hold
    if not first_hold[1:] in ['4', '5', '6']:
        return False
    # that at most 2 holds are in the top row.
    top_row_holds = 0
    for move in climb['Moves']:
        if move[1:] == '18':
            top_row_holds += 1
    if top_row_holds < 1 or top_row_holds > 2:
        return False

    # i don't allow holds under row 4 I think
    for move in climb['Moves']:
        if move[1:] in ['1', '2', '3']:
            return False

    return True

def normalize_XY(hold):
    return (hold[0]/ncols,hold[1]/nrows)