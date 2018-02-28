# This function loads all the climbs and converts them to climb objects

import json
from pathlib import Path
from pprint import pprint

script_parent_directory = Path().resolve().parent
with open(str(script_parent_directory)+'/data/json/combined.json') as handle:
	loaded_data = json.load(handle)

pprint(loaded_data[0])
