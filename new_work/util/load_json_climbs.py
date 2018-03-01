# This function loads all the climbs and converts them to climb objects

import json
from pathlib import Path
from pprint import pprint

import os, sys
import_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/types'
sys.path.append(import_path)

from climbset import Climbset
from climb import Climb

script_parent_directory = Path().resolve().parent
with open(str(script_parent_directory)+'/data/json/combined.json') as handle:
	loaded_data = json.load(handle)

all_climbs = Climbset()

for cur_climb_json in loaded_data:
	cur_climb = all_climbs.add(Climb('json',cur_climb_json))

print(all_climbs.pre_grade_string())