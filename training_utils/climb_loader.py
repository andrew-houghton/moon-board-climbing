# This function loads all the climbs and converts them to climb objects
import json

# Allow importing of the custom climb types
import os
import sys
base_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_directory + '/types')

from climbset import Climbset
from climb import Climb


def load_all_as_climbset():
    # Get all of the json climbs as a big climbset
    json_data = load_all_as_json()
    all_climbs = json_to_climbset(json_data)
    return all_climbs


def load_all_as_json():
    # Open all json data stored in the data directory.
    with open(base_directory + '/data/json/combined.json') as handle:
        loaded_data = json.load(handle)
    return loaded_data


def json_to_climbset(data):
    # For each climb stored in json format
    # convert it to a climb and then add it to a climbset.

    all_climbs = Climbset()
    for cur_climb_json in data:
        cur_climb = all_climbs.add(Climb('json', cur_climb_json))
    return all_climbs
