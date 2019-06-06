from moon.models.base_model import GradingModel
from moon.types.climbset import Climbset
from moon.analytics.grade_preprocess import BasePreprocessor
from moon.analytics.metrics import Metrics
from typing import Tuple
from moon.util.load_data import load_climbset

from moon.models import keras_lstm_grade, keras_mlp, random_forest, xgboost

Grade=List[bool] # Various length
Climb=List[bool] # One hot encoded, 18*11 options


@dataclass
class Configuration:
    model: GradingModel
    climbset: Climbset
    preprocessing: BasePreprocessor
    metrics: Metrics
    data_split: Tuple[Tuple[List[Climb], List[Climb]], Tuple[List[Grade], List[Grade]]]

    def report(self):
        pass

    def execute(self):
        pass

# Generate configurations here
def get_grading_models() -> Tuple[GradingModel]:
    return (
        keras_lstm_grade.Model(), keras_mlp.Model(), random_forest.Model(), xgboost.Model()
    )

def get_grade_preprocessors() -> Tuple[BasePreprocessor]:
    pass

def get_climbsets() -> Tuple[Climbset]:
    return (
        load_climbset("2016"),
        load_climbset("2017")
    )

def generate_configurations() -> Tuple[Configuration]:
    pass

def run_configuration(config: Configuration) -> None:
    # Run grade preprocessing
    grades = [i.grade.grade_number for i in config.climbset.climbs]
    new_grades = config.preprocessing.preprocess(grades)

    # Format climbset
    climbs = np.asarray([np.asarray(climb.as_image()) for climb in base_climbset.climbs])
    climbs = [np.reshape(climbs, (len(climbs), 11 * 18)).astype(int)]

    # Split test train data
    config.data_split = train_test_split(
            np.reshape(climbs, (len(climbs), 11 * 18)).astype(int),
            grades,
            test_size=0.2,
            random_state=42,
        )

    # Train the model
    # Get test set accuracy
    # Generate metrics
    # Print report
    pass

def main():
    for configuration in generate_configurations():
        run_configuration(configuration)
