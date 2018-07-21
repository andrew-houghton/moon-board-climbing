import gzip
import shutil
from pathlib import Path
import os

script_parent_directory = str(Path().resolve().parent)

if not os.path.exists(script_parent_directory + '/data/json'):
    os.makedirs(script_parent_directory + '/data/json')

with open(script_parent_directory + '/data/json/combined.json', 'wb') as f_out, gzip.open(script_parent_directory + '/data/compressed/combined.json.gz', 'rb') as f_in:
    shutil.copyfileobj(f_in, f_out)
