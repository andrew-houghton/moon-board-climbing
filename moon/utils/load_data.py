import json
import os
import pickle
import shutil

import numpy as np

from moon.types.climb import Climb
from moon.types.climbset import Climbset


def local_file_path(script_file, filename):
    scriptpath = os.path.dirname(os.path.realpath(script_file))
    return os.path.join(scriptpath, filename)


def get_or_generate(filename, generator_function, *args):
    filepath = local_file_path(__file__, filename)
    if not os.path.isfile(filepath):
        generator_function(*args)
    return filepath


def load_numpy(year):
    path = get_or_generate(year + ".pkl", gen_numpy, year)
    return pickle.load(open(path, "rb"))


def gen_numpy(year):
    base_climbset = load_climbset(year)
    climbs = np.asarray([np.asarray(climb.as_image()) for climb in base_climbset.climbs])
    grades = np.asarray([climb.grade.grade_number for climb in base_climbset.climbs])
    pickle.dump((climbs, grades), open(local_file_path(__file__, year + ".pkl"), "wb"))


def load_climbset(year):
    climbset = json_to_climbset(load_json(year))
    climbset.year = year
    return climbset


def load_json(year):
    with open(local_file_path(__file__, year + ".json"), "r") as handle:
        return json.load(handle)


def json_to_climbset(data):
    # For each climb stored in json format
    # convert it to a climb and then add it to a climbset.
    all_climbs = Climbset()
    for cur_climb_json in data:
        all_climbs.add(Climb("json", cur_climb_json))
    return all_climbs


if __name__ == "__main__":
    load_numpy()
