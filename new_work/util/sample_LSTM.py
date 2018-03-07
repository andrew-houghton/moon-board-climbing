import os
# surpress tesnsorflow warning
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from pathlib import Path
import sys

# import LSTM model
script_parent_directory = Path().resolve().parent
network_folder = '{}/networks/char-rnn-tensorflow/'.format(script_parent_directory)
sys.path.append(network_folder)
sys.path.append('{}/types/'.format(script_parent_directory))
sys.path.append('{}/explorer/'.format(script_parent_directory))
import climbset
import sample

import layout

def sample_model(grade_mode):
    # Check that function parameters are valid
    if not grade_mode in ['no_grade', 'post_grade', 'pre_grade']:
        raise ValueError(
            'Invalid grade_mode for model training. Use no_grade, post_grade or pre_grade as the grade_mode parameter.')

    # Find directories
    base_save_dir = '{}/data/lstm_files/{}/'.format(script_parent_directory, grade_mode)

    # Start the sample with an the seed_str
    # (ie the network will start generating characters that come after the seed.)
    seed_str = '_'
    # Number of characters in the generated sample
    sample_length = 5000

    return sample.get_sample(base_save_dir, sample_length, seed_str)


def clean_sample(sample):
    terminator_char = climbset.Climbset.get_terminator()
    split_sample = sample.split(terminator_char)
    nn_grade_chars = ['È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö']

    # Clean up items at the end
    if len(split_sample[0]) <= 1:
        # remove first item if it is too short to be a climb
        split_sample.pop(0)
    split_sample.pop(len(split_sample) - 1)

    output_list = []

    # TODO
    # MOVE THE VALIDATION OF CLIMBS IN A SAMPLE INTO THE CLIMB CLASS!

    # Check all the moves have valid characters
    for climb in split_sample:
        if climb[0] in nn_grade_chars:
            # pre grade climb
            climb = climb[1:]
        elif climb[-1] in nn_grade_chars:
            # post grade climb
            climb = climb[:len(climb) - 1]

        if len(climb) % 2 != 0:
            print('Weird climb length error in clean_sample:{}'.format(climb))
            continue

        valid_moves = True
        for i in range(0, len(climb), 2):
            if not is_valid_move(climb[i:i + 2]):
                valid_moves = False
                break

        if valid_moves:
            output_list.append(climb)

    return output_list


def is_valid_move(move_str):
    if len(move_str) == 2:
        if move_str[0] in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']:
            if move_str[1] in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r']:
                return True
    return False

if __name__ == '__main__':
    grade_mode = 'no_grade'
    climbs = clean_sample(sample_model(grade_mode))
    climbset = climbset.Climbset(climbs, 'sample')

    app = layout.ClimbsetNavigator(climbset)
    app.run()