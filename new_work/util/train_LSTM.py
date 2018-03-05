import os
#surpress tesnsorflow warning
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from pathlib import Path
import sys

#import LSTM model
script_parent_directory = Path().resolve().parent
network_folder = '{}/networks/char-rnn-tensorflow/'.format(script_parent_directory)
sys.path.append(network_folder)
import train

def train_model(grade_mode):
	# Check that function parameters are valid
	if not grade_mode in ['no_grade','post_grade','pre_grade']:
		raise ValueError('Invalid grade_mode for model training. Use no_grade, post_grade or pre_grade as the grade_mode parameter.')

	# Find directories
	base_save_dir = '{}/data/lstm_files/{}/'.format(script_parent_directory,grade_mode)

	# Train the model
	train.build_model(base_save_dir)

if __name__ == '__main__':
	grade_mode = 'post_grade'
	train_model(grade_mode)
