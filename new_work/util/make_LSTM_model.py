import os
from pathlib import Path
script_parent_directory = Path().resolve().parent

#import LSTM model
import sys
import_path = str(script_parent_directory) + '/networks/char-rnn-tensorflow'
sys.path.append(import_path)
import train

# Set up command arguments
data_filename = 'allclimbs_nograde.txt'
data_folder = '{}/data/strings/'.format(script_parent_directory)
network_folder = '{}/networks/char-rnn-tensorflow/'.format(script_parent_directory)
model_filename = data_filename.replace('.txt', '.ckpt')
model_dir = '{}/data/models/{}'.format(script_parent_directory, model_filename)

# Train the model
train.build_model(
	data_folder,
	data_filename,
	model_dir,
	model_filename,
	network_folder,
	)