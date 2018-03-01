# This function loads all the climbs and converts them to climb objects
import json
from pathlib import Path
from pprint import pprint

import os, sys
import_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/types'
sys.path.append(import_path)

from climbset import Climbset
from climb import Climb

def load_all_as_climbset():
	json_data = load_all_as_json()
	all_climbs = json_to_climbset(json_data)
	return all_climbs

def load_all_as_json():
	script_parent_directory = Path().resolve().parent
	with open(str(script_parent_directory)+'/data/json/combined.json') as handle:
		loaded_data = json.load(handle)
	return loaded_data

def json_to_climbset(data):
	all_climbs = Climbset()
	for cur_climb_json in data:
		cur_climb = all_climbs.add(Climb('json',cur_climb_json))
	return all_climbs

if __name__ == '__main__':
	all_climbs=load_all_as_climbset()
	print(all_climbs.pre_grade_string())