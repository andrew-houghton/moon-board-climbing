import json
import os
import pickle

from moon.utils.load_data import load_climbset


def prep_no_grade():
    output_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")
    with open(output_path, "w") as handle:
        handle.write(load_climbset().no_grade_string())
    return output_path


def clean_output_json():
    with open("sample.pickle", "rb") as handle:
        sample = pickle.load(handle)
    hold_lists = [i.holds for i in sample.climbs]
    hold_lists = [[i.as_website_format() for i in j] for j in hold_lists]
    hold_lists = [[(i[0], i[1:]) for i in j] for j in hold_lists]
    with open("sample.json", "w") as handle:
        json.dump(hold_lists, handle)


if __name__ == "__main__":
    clean_output_json()
