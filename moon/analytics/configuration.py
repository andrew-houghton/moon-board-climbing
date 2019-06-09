from dataclasses import dataclass
from typing import Any, List, Tuple

import numpy as np
from sklearn.model_selection import train_test_split

from moon.analytics.grade_preprocessor import (
    BasePreprocessor,
    CategoricalPreprocessor,
    FlandersPreprocessor,
)
from moon.analytics.metrics import Metrics
from moon.models import (
    # keras_lstm_grade,
    # keras_mlp,
    random_forest,
    xgboost_model,
)

from moon.types.climbset import Climbset
from moon.utils.load_data import load_climbset

Grade = List[bool]  # Various length
Climb = List[bool]  # One hot encoded, 18*11 options


@dataclass
class Configuration:
    model: Any
    climbset: Climbset
    preprocessing: BasePreprocessor
    train_metrics: Metrics = Metrics()
    test_metrics: Metrics = Metrics()
    x_train: List[Climb] = None
    x_test: List[Climb] = None
    y_train: List[Grade] = None
    y_test: List[Grade] = None

    @staticmethod
    def report_headings():
        print(
            "Climbset "
            "Model                "
            "Preprocessing        "
            "Test Accuracy        "
            "Train Accuracy       "
        )

    def report(self):
        col_width = 20
        test_acc = f"{self.test_metrics.accuracy:.3}"
        train_acc = f"{self.train_metrics.accuracy:.3}"
        print(
            f"{self.climbset.year:<9}"
            f"{self.model.name():<{col_width}} {type(self.preprocessing).__name__:<{col_width}} "
            f"{test_acc:<{col_width}} {train_acc:<{col_width}}"
        )

    def execute(self):
        pass


# Generate configurations here
def get_grading_models() -> tuple:
    return (
        # keras_lstm_grade.Model(),
        # keras_mlp.Model(),
        random_forest.Model(),
        xgboost_model.Model(),
    )


def get_grade_preprocessors() -> Tuple[BasePreprocessor]:
    return (CategoricalPreprocessor(),)


def get_climbsets() -> Tuple[Climbset]:
    return (load_climbset("2016"),)


def run_configuration(config: Configuration) -> None:
    # Run grade preprocessing
    grades = np.asarray([i.grade.grade_number for i in config.climbset.climbs])
    new_grades = config.preprocessing.preprocess(grades)

    # Format climbset
    climbs = np.asarray(
        [np.asarray(climb.as_image()) for climb in config.climbset.climbs]
    )
    climbs = np.reshape(climbs, (len(climbs), 11 * 18)).astype(int)

    # Split test train data
    config.x_train, config.x_test, config.y_train, config.y_test = train_test_split(
        climbs, new_grades, test_size=0.2, random_state=42
    )

    # Train the model
    config.model.train(config.x_train, config.y_train)

    # Generate metrics
    config.test_metrics.generate_metrics(
        config.y_test, config.model.sample(config.x_test)
    )
    config.train_metrics.generate_metrics(
        config.y_train, config.model.sample(config.x_train)
    )


def main():
    configurations = generate_configurations()
    for configuration in configurations:
        print(f"Running configuration {configuration}")
        run_configuration(configuration)
    print("Finished")


if __name__ == "__main__":
    Configuration.report_headings()
    for year in ("2016", "2017"):
        cfg = Configuration(
            xgboost_model.Model(), load_climbset(year), FlandersPreprocessor()
        )
        run_configuration(cfg)
        cfg.report()

        cfg = Configuration(
            random_forest.Model(), load_climbset(year), FlandersPreprocessor()
        )
        run_configuration(cfg)
        cfg.report()
