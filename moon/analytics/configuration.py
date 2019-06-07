from dataclasses import dataclass
from typing import List, Tuple

import numpy as np
from sklearn.model_selection import train_test_split

from moon.analytics.grade_preprocessor import (
    BasePreprocessor,
    CategoricalPreprocessor,
)
from moon.analytics.metrics import Metrics
from moon.models import (
    keras_lstm_grade,
    keras_mlp,
    random_forest,
    xgboost_model,
)
from moon.models.base_model import GradingModel
from moon.types.climbset import Climbset
from moon.utils.load_data import load_climbset

Grade = List[bool]  # Various length
Climb = List[bool]  # One hot encoded, 18*11 options


@dataclass
class Configuration:
    model: GradingModel
    climbset: Climbset
    preprocessing: BasePreprocessor
    metrics: Metrics = Metrics()
    data_split: Tuple[
        Tuple[List[Climb], List[Climb]], Tuple[List[Grade], List[Grade]]
    ] = None

    def report(self):
        pass

    def execute(self):
        pass


# Generate configurations here
def get_grading_models() -> Tuple[GradingModel]:
    return (
        keras_lstm_grade.Model(),
        keras_mlp.Model(),
        random_forest.Model(),
        xgboost_model.Model(),
    )


def get_grade_preprocessors() -> Tuple[BasePreprocessor]:
    return (CategoricalPreprocessor(),)


def get_climbsets() -> Tuple[Climbset]:
    return (load_climbset("2016"), load_climbset("2017"))


def generate_configurations() -> List[Configuration]:
    print("Generating configurations.")
    configurations = []
    for model in get_grading_models():
        for climbset in get_climbsets():
            for preprocessing in get_grade_preprocessors():
                configurations.append(
                    Configuration(
                        model=model,
                        climbset=climbset,
                        preprocessing=preprocessing,
                    )
                )
    return configurations


def run_configuration(config: Configuration) -> None:
    # Run grade preprocessing
    grades = [i.grade.grade_number for i in config.climbset.climbs]
    new_grades = config.preprocessing.preprocess(grades)

    # Format climbset
    climbs = np.asarray(
        [np.asarray(climb.as_image()) for climb in config.climbset.climbs]
    )
    climbs = np.reshape(climbs, (len(climbs), 11 * 18)).astype(int)

    # Split test train data
    print(len(grades))
    print(climbs.shape)

    config.data_split = train_test_split(
        climbs,
        grades,
        test_size=0.2,
        random_state=42,
    )

    # Train the model
    # Get test set accuracy
    # Generate metrics
    # Print report


def main():
    configurations = generate_configurations()
    for configuration in configurations:
        print(f"Running configuration {configuration}")
        run_configuration(configuration)
        break
    print("Finished")


if __name__ == "__main__":
    main()
