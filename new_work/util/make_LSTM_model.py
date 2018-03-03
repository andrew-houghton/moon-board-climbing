import os
from pathlib import Path
from shutil import copyfile
import subprocess

script_parent_directory = Path().resolve().parent

# Move file to input folder
filename = 'allclimbs_nograde.txt'
string_folder = '{}/data/strings/'.format(script_parent_directory)
string_fullpath = string_folder + filename
network_folder = '{}/networks/char-rnn-tensorflow/'.format(script_parent_directory)
copyfile(string_fullpath, network_folder + 'data/input.txt')

# Run command to train model
# --log_dir={network}logs --save_dir={network}save'
command = 'python {network}train.py --data_dir={network}data'

subprocess.call(command.format(network=network_folder))

# Save model
model_filename = filename.replace('.txt', '.ckpt')
model_save_path = '{}+/data/models/{}'.format(script_parent_directory, model_filename)
copyfile(network_folder + 'save/model.ckpt', model_filename)
