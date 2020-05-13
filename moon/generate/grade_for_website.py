import json
import pickle
from functools import partial
from pprint import pprint
from pathlib import Path
import time

from sklearn.model_selection import train_test_split
import numpy as np

from moon.analytics.climb_preprocessor import HoldListPreprocessor
from moon.analytics.configuration import Configuration
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
    x_train, y_train = training_data

    # Train classifier on original (graded) data
    if model.name() == "Keras LSTM":
        config = Configuration(model, training_data, preprocessor, HoldListPreprocessor())
    else:
        config = Configuration(model, training_data, preprocessor)

    start = time.time()
    print(f"Training {str(config)}", end="", flush=True)
    config.model.train(
        config.x_preprocessing.preprocess(x_train), config.y_preprocessing.preprocess(y_train)
    )
    print(f" Trained in {time.time() - start:.2f}s")
    return config


def main(year):
    # Load generated climbsets
    file_data = pickle.load(open(local_file_path(__file__, year + ".pickle"), "rb"))

    # Split training and test data
    original_climbs = file_data["original"].climbs
    original_grades = np.asarray([i.grade.grade_number for i in original_climbs])
    x_train, x_test, y_train, _ = Configuration.split_function(original_climbs, original_grades)

    # Only keep a sample of the test set for original climbs
    file_data["original"].climbs = x_test[:500]

    # Train the models
    trained_models = map(train_model, model_setups((x_train, y_train)))

    # Format the data for the website
    data = website_json_structure(file_data)

    # Add grades to the website data
    for config in trained_models:
        add_grades(data["original"], config, file_data["original"].climbs)
        add_grades(data["lstm"], config, file_data["lstm"].climbs)

    # Save to file
    repo_base_directory = Path(__file__).resolve().parent.parent.parent
    website_climb_directory = repo_base_directory.joinpath("website-moon", "moon", "climbs")

    with open(website_climb_directory.joinpath(f"{year}.js"), "w") as handle:
        handle.write(f"var climbs_{year} = " + json.dumps(data))


if __name__ == "__main__":
    main("2016")
    main("2017")
