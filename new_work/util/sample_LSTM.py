import os
#surpress tesnsorflow warning
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from pathlib import Path
import sys

#import LSTM model
script_parent_directory = Path().resolve().parent
network_folder = '{}/networks/char-rnn-tensorflow/'.format(script_parent_directory)
sys.path.append(network_folder)
sys.path.append('{}/types/'.format(script_parent_directory))
import climbset
import sample

def sample_model(grade_mode):
	# Check that function parameters are valid
	if not grade_mode in ['no_grade','post_grade','pre_grade']:
		raise ValueError('Invalid grade_mode for model training. Use no_grade, post_grade or pre_grade as the grade_mode parameter.')


	# Find directories
	base_save_dir = '{}/data/lstm_files/{}/'.format(script_parent_directory,grade_mode)

	# Start the sample with an the seed_str
	# (ie the network will start generating characters that come after the seed.)
	seed_str='_'
	# Number of characters in the generated sample
	sample_length=500
	
	return sample.get_sample(base_save_dir,sample_length,seed_str)


def clean_sample(sample):
	terminator_char = climbset.Climbset.get_terminator()
	split_sample = sample.split(terminator_char)

	# Clean up items at the end
	if len(split_sample[0])<=1:
		#remove first item if it is too short to be a climb
		split_sample.pop(0)
	split_sample.pop(len(split_sample)-1)

	return split_sample


if __name__ == '__main__':
	grade_mode = 'post_grade'
	print(clean_sample(sample_model(grade_mode)))