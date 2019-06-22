import time
from dataclasses import dataclass
from typing import Any, List, Tuple

import numpy as np
from sklearn.model_selection import train_test_split

from moon.analytics.climb_preprocessor import HoldListPreprocessor, OneHotPreprocessor
from moon.analytics.grade_preprocessor import (
    CategoricalPreprocessor,
    FlandersPreprocessor,
    HalfGradePreprocessor,
    SplitPreprocessor,
)
from moon.analytics.metrics import Metrics
from moon.models import keras_lstm_grade, keras_mlp, random_forest, xgboost_model
from moon.types.climbset import Climbset
from moon.utils.load_data import load_climbset

Grade = List[bool]  # Various length
Climb = List[bool]  # One hot encoded, 18*11 options


@dataclass
class Configuration:
    model: Any
    climbset: Climbset
    y_preprocessing: Any
    x_preprocessing: Any = OneHotPreprocessor()
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
            "Climb Preprocessing  "
            "Grade Preprocessing  "
            "Train Acc "
            "Test Acc  "
            "Within 1  "
            "Within 2  "
        )

    def report(self):
        metric_width = 10
        col_width = 20
        test_acc = f"{self.test_metrics.accuracy:.3}"
        train_acc = f"{self.train_metrics.accuracy:.3}"
        within_1 = f"{self.test_metrics.within_1:.3}"
        within_2 = f"{self.test_metrics.within_2:.3}"

        return (
            f"{self.climbset.year:<9} "
            f"{self.model.name():<{col_width}} "
            f"{type(self.x_preprocessing).__name__[:-12]:<{col_width}} "
            f"{type(self.y_preprocessing).__name__[:-12]:<{col_width}} "
            f"{train_acc:<{metric_width}}"
            f"{test_acc:<{metric_width}}"
            f"{within_1:<{metric_width}}"
            f"{within_2:<{metric_width}}"
        )

    def __repr__(self):
        return (
            f"Configuration: {self.model.name():<15} "
            f"Climbset={self.climbset.year} "
            f"X={type(self.y_preprocessing).__name__[:-12]:<13} "
            f"Y={type(self.y_preprocessing).__name__[:-12]:<13} "
        )

    def sample(self, climbset):
        new_climbs = self.x_preprocessing.preprocess(climbset.climbs)
        grades = self.model.sample(new_climbs)
        if type(self.y_preprocessing) == FlandersPreprocessor:
            return grades
        else:
            return [np.argmax(i) for i in grades]


def run_configuration(config: Configuration) -> None:
    print(f"Training {str(config)}", end="", flush=True)
    start = time.time()

    # Run climb preprocessing
    new_climbs = config.x_preprocessing.preprocess(config.climbset.climbs)

    # Run grade preprocessing
    grades = np.asarray([i.grade.grade_number for i in config.climbset.climbs])
    new_grades = config.y_preprocessing.preprocess(grades)

    # Split test train data
    config.x_train, config.x_test, config.y_train, config.y_test = train_test_split(
        new_climbs, new_grades, test_size=0.2, random_state=42
    )

    # Train the model
    config.model.train(config.x_train, config.y_train)

    # Generate metrics
    test_sample = config.model.sample(config.x_test)
    config.test_metrics.generate_metrics(config.y_test, test_sample)

    train_sample = config.model.sample(config.x_train)
    config.train_metrics.generate_metrics(config.y_train, train_sample)

    print(f" Trained in {time.time() - start:.2f}s")


def run_custom_model():
    for year in ("2016", "2017"):
        cfg = Configuration(random_forest.Model(), load_climbset(year), CategoricalPreprocessor())
        run_configuration(cfg)
        Configuration.report_headings()
        print(cfg.report())


def generate_all_valid_configurations():
    configs = []
    for year in ("2016", "2017"):
        # XGBoost
        configs.append(
            Configuration(xgboost_model.Model(), load_climbset(year), FlandersPreprocessor())
        )
        # Random forest flanders proprocessor
        configs.append(
            Configuration(random_forest.Model(), load_climbset(year), FlandersPreprocessor())
        )

        # Loop through categorical grade preprocessors
        for preprocessor in (
            CategoricalPreprocessor(),
            SplitPreprocessor(4),
            HalfGradePreprocessor(),
        ):
            # LSTM
            configs.append(
                Configuration(
                    keras_lstm_grade.Model(),
                    load_climbset(year),
                    preprocessor,
                    HoldListPreprocessor(),
                )
            )
            # MLP
            configs.append(Configuration(keras_mlp.Model(), load_climbset(year), preprocessor))
            # Random forest
            configs.append(Configuration(random_forest.Model(), load_climbset(year), preprocessor))

    print(f"Generated {len(configs)} configruations.")
    return configs


if __name__ == "__main__":
    # run_custom_model()
    program_start = time.time()
    configs = generate_all_valid_configurations()

    reports = []
    for cfg in configs:
        run_configuration(cfg)
        reports.append(cfg.report())

    print(f"Completed training and sampling in {time.time() - program_start:.2f}s")
    Configuration.report_headings()
    print("\n".join(reports))
