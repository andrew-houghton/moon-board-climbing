# This function loads all the climbs and converts them to climb objects

import json
from pathlib import Path
from pprint import pprint

import os, sys
import_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/types'
sys.path.append(import_path)

script_parent_directory = Path().resolve().parent
with open(str(script_parent_directory)+'/data/json/combined.json') as handle:
	loaded_data = json.load(handle)

print(loaded_data[0])

grades = set()
for i in loaded_data:
	grades.add(i['Grade'])

print(grades)