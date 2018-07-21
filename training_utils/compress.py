# compress

import gzip
import shutil
from pathlib import Path

script_parent_directory = str(Path().resolve().parent)

with open(script_parent_directory + '/data/json/combined.json', 'rb') as f_in, gzip.open(script_parent_directory + '/data/compressed/combined.json.gz', 'wb') as f_out:
    shutil.copyfileobj(f_in, f_out)
