import os
# surpress tesnsorflow warning
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import sys

# import LSTM model
base_directory = os.path.abspath(__file__ + "/../../")
network_folder = '{}/models/char-rnn-tensorflow/'.format(base_directory)
sys.path.append(network_folder)
sys.path.append('{}/types/'.format(base_directory))
sys.path.append('{}/climb_viewer/'.format(base_directory))
import climbset
from climb import Climb
import sample

import layout


def sample_model(grade_mode):
    # Check that function parameters are valid
    if not grade_mode in ['no_grade', 'post_grade', 'pre_grade']:
        raise ValueError(
            'Invalid grade_mode for model training. Use no_grade, post_grade or pre_grade as the grade_mode parameter.')

    # Find directories
    base_save_dir = '{}/data/lstm_files/{}/'.format(base_directory, grade_mode)

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

    # Check all the climbs are valid
    for climb_str in split_sample:
        if Climb.valid_input_sample(climb_str):
            output_list.append(climb_str)

    return output_list


if __name__ == '__main__':
    grade_mode = 'no_grade'
    climbs = clean_sample(sample_model(grade_mode))
    climbset = climbset.Climbset(climbs, 'sample')

    app = layout.ClimbsetNavigator(climbset)
    app.run()
