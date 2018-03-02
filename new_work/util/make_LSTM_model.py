import os

network_folder = '../networks/char-rnn-tensorflow/'
data_dir = '../data/strings/'
filename = 'all_climbs_nograde.txt'
command = 'python {network}train.py data --data_dir={data}'

os.system(command.format(network=network_folder,data=data_dir+filename))
