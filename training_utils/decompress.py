import gzip
import shutil
from pathlib import Path
import os
base_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    if not os.path.exists(base_directory + '/data/json'):
        os.makedirs(base_directory + '/data/json')

    with open(base_directory + '/data/json/combined.json', 'wb') as f_out, gzip.open(base_directory + '/data/compressed/combined.json.gz', 'rb') as f_in:
        shutil.copyfileobj(f_in, f_out)

if __name__ == '__main__':
    main()
