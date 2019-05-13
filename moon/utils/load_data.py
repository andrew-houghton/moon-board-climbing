import os
import pickle
import gzip
import json
import shutil
from moon.types.climbset import Climbset
from moon.types.climb import Climb
import numpy as np


def local_file_path(filename):
    scriptpath = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(scriptpath, filename)


def get_or_generate(filename, generator_function):
    filepath = local_file_path(filename)
    if os.path.isfile(filepath):
        generator_function()
    return filepath


def load_numpy():
    path = get_or_generate("numpy.pkl", gen_numpy)
    return pickle.load(open(path, "rb"))


def gen_numpy():
    base_climbset = json_to_climbset(load_json())
    climbs = np.asarray([np.asarray(climb.as_image()) for climb in base_climbset.climbs])
    grades = np.asarray([climb.grade.grade_number for climb in base_climbset.climbs])
    pickle.dump((climbs, grades), open(local_file_path("numpy.pkl"), "wb"))


def load_json():
    path = get_or_generate("combined.json", gen_json)
    return json.load(open(path))


def gen_json():
    with open(local_file_path("combined.json"), "wb") as f_out, gzip.open(
        local_file_path("combined.json.gz"), "rb"
    ) as f_in:
        shutil.copyfileobj(f_in, f_out)


def json_to_climbset(data):
    # For each climb stored in json format
    # convert it to a climb and then add it to a climbset.
    all_climbs = Climbset()
    for cur_climb_json in data:
        cur_climb = all_climbs.add(Climb("json", cur_climb_json))
    return all_climbs


if __name__ == "__main__":
    gen_numpy()
