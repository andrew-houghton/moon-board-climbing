#import LSTM model
import os
from pathlib import Path
script_parent_directory = Path().resolve().parent
import sys
import_path = str(script_parent_directory) + '/networks/char-rnn-tensorflow'
sys.path.append(import_path)
import sample

# def sample_getter(seed_string,lenght):

