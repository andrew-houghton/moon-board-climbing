import json
import pickle
from functools import partial
from pprint import pprint
from pathlib import Path

from sklearn.model_selection import train_test_split

from moon.analytics.climb_preprocessor import HoldListPreprocessor
from moon.analytics.configuration import Configuration, run_configuration
from moon.analytics.grade_preprocessor import CategoricalPreprocessor, FlandersPreprocessor
from moon.models import keras_lstm_grade, keras_mlp, random_forest, xgboost_model
from moon.types.grade import Grade
from moon.types.climbset import Climbset
from moon.utils.load_data import local_file_path


def web_json_format(climb):
    return {
        "grade": {"original": climb.grade.as_v_grade()},
        "moves": [hold.as_website_format() for hold in climb.holds],
    }


def model_setups(training_data):
    return [
        (xgboost_model.Model(), training_data, FlandersPreprocessor()),
        (keras_mlp.Model(), training_data, CategoricalPreprocessor()),
        (random_forest.Model(), training_data, CategoricalPreprocessor()),
        (keras_lstm_grade.Model(), training_data, CategoricalPreprocessor()),
    ]


def nums_to_font(nums):
    return [Grade(int(i)).as_v_grade() for i in nums]


def website_json_structure(file_data):
    data = {}
    for name, climbset in file_data.items():
        data[name] = []

        for climb in climbset.climbs:
            climb_dict = {"moves": [hold.as_website_format() for hold in climb.holds], "grade": {}}
            if climb.grade:
                climb_dict["grade"] = {"original": climb.grade.as_v_grade()}
            data[name].append(climb_dict)

    return data


def add_grades(data_to_grade, config, climbs):
    grades = nums_to_font(config.sample(climbs))
    for i in range(len(grades)):
        data_to_grade[i]["grade"][config.model.name()] = grades[i]


def train_model(args):
    model, training_data, preprocessor = args
    # Train classifier on original (graded) data
    if model.name() == "Keras LSTM":
        config = Configuration(model, training_data, preprocessor, HoldListPreprocessor())
    else:
        config = Configuration(model, training_data, preprocessor)
    run_configuration(config)
    return config


def main(year):
    # Load generated climbsets
    file_data = pickle.load(open(local_file_path(__file__, year + ".pickle"), "rb"))

    # Train the models
    trained_models = map(train_model, model_setups(file_data["original"]))

    # Only keep test set for original climbs
    original_climbs = file_data["original"].climbs
    _, test_climbs, _, _ = train_test_split(original_climbs, range(len(original_climbs)), test_size=0.2, random_state=42)
    file_data["original"].climbs = test_climbs[:500]

    # Format the data for the website
    data = website_json_structure(file_data)

    # Add grades to the website data
    for config in trained_models:
        add_grades(data["original"], config, file_data["original"].climbs)
        add_grades(data["lstm"], config, file_data["lstm"].climbs)

    # Save to file'
    repo_base_directory = Path(__file__).resolve().parent.parent.parent
    website_climb_directory = repo_base_directory.joinpath("website-moon", "moon", "climbs")

    with open(website_climb_directory.joinpath(f"{year}.js"), "w") as handle:
        handle.write(f"var climbs_{year} = " + json.dumps(data))


if __name__ == "__main__":
    main("2016")
    main("2017")
