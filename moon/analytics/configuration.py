from dataclasses import dataclass
from typing import Any, List, Tuple

import numpy as np
from sklearn.model_selection import train_test_split

from moon.analytics.grade_preprocessor import (
    BasePreprocessor,
    CategoricalPreprocessor,
    FlandersPreprocessor,
    SplitPreprocessor,
)
from moon.analytics.metrics import Metrics
from moon.models import (
    # keras_lstm_grade,
    keras_mlp,
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
            "\nClimbset "
            "Model                "
            "Preprocessing        "
            "Test Accuracy        "
            "Train Accuracy       "
        )

    def report(self):
        col_width = 20
        test_acc = f"{self.test_metrics.accuracy:.3}"
        train_acc = f"{self.train_metrics.accuracy:.3}"
        return (
            f"{self.climbset.year:<9}"
            f"{self.model.name():<{col_width}} {type(self.preprocessing).__name__:<{col_width}} "
            f"{test_acc:<{col_width}} {train_acc:<{col_width}}"
        )


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
    return (load_climbset("2016"), load_climbset("2017"))


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
    test_sample = config.model.sample(config.x_test)
    config.test_metrics.generate_metrics(config.y_test, test_sample)

    train_sample = config.model.sample(config.x_train)
    config.train_metrics.generate_metrics(config.y_train, train_sample)


def random_forest_both_years():
    Configuration.report_headings()
    for year in ("2016", "2017"):
        cfg = Configuration(
            random_forest.Model(), load_climbset(year), FlandersPreprocessor()
        )
        run_configuration(cfg)
        print(cfg.report())

def keras_both_years():
    reports = []
    for year in ("2016", "2017"):
        cfg = Configuration(
            keras_mlp.Model(), load_climbset(year), CategoricalPreprocessor()
        )
        run_configuration(cfg)
        reports.append(cfg.report())

    Configuration.report_headings()
    print("\n".join(reports))

def keras_split():
    reports = []
    for year in ("2016", "2017"):
        cfg = Configuration(
            keras_mlp.Model(), load_climbset(year), SplitPreprocessor(6)
        )
        run_configuration(cfg)
        reports.append(cfg.report())

    Configuration.report_headings()
    print("\n".join(reports))

if __name__ == "__main__":
    keras_split()
